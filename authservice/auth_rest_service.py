import os
import jwt
import schema
import pprint
import socket
import logging
import requests
import connexion

from datetime import datetime
from flask import request, abort

logger = logging.getLogger(__name__)


def is_digits(x):
    return x.isdigit()


ISDIGITS_SCHEMA = schema.Schema(
    is_digits,
    name="should be numeric",
)


def initiate_verification():
    addl_schema = schema.Schema(
        {'phoneNumber': ISDIGITS_SCHEMA},
        ignore_extra_keys=True,
    )
    body_dict = request.get_json(force=True)
    try:
        addl_schema.validate(body_dict)
    except schema.SchemaError as se:
        abort(400, str(se))

    twilio_resp = requests.post(
        'https://verify.twilio.com/v2/Services/%s/Verifications' % (
            os.getenv('TWILIO_VERIFY_SERVICE_ID')
        ),
        auth=(
            os.getenv('TWILIO_ACCT_SID'),
            os.getenv('TWILIO_AUTH_TOKEN'),
        ),
        data={
            'To': '+1' + body_dict['phoneNumber'],
            'Channel': body_dict['channel'],
        },
    )
    twil_dict = twilio_resp.json()
    if twilio_resp.status_code != 201:
        logger.error("Error posting to twilio. data = %s" % pprint.pformat(twil_dict))
    twilio_resp.raise_for_status()
    return None, 201


def verification_check():
    addl_schema = schema.Schema({
        'phoneNumber': ISDIGITS_SCHEMA,
        'code': ISDIGITS_SCHEMA,
    })
    body_dict = request.get_json(force=True)
    try:
        addl_schema.validate(body_dict)
    except schema.SchemaError as se:
        abort(400, str(se))
    twilio_resp = requests.post(
        'https://verify.twilio.com/v2/Services/%s/VerificationCheck' % (
            os.getenv('TWILIO_VERIFY_SERVICE_ID')
        ),
        auth=(
            os.getenv('TWILIO_ACCT_SID'),
            os.getenv('TWILIO_AUTH_TOKEN'),
        ),
        data={
            'To': '+1' + body_dict['phoneNumber'],
            'Code': body_dict['code'],
        },
    )
    twil_dict = twilio_resp.json()
    if twilio_resp.status_code != 200:
        logger.error("Error posting to twilio on verification check. data = %s" % pprint.pformat(twil_dict))
        return {'success': False}
    twilio_resp.raise_for_status()
    if not twil_dict['valid'] or twil_dict['status'] != 'approved':
        return {'success': False}
    id_token = jwt.encode(
        {
            'phoneNumber': body_dict['phoneNumber'],
            'iat': datetime.utcnow(),  # issued at
            'aud': os.getenv('PHONE_VERIFY_AUDIENCE'),
            'iss': socket.gethostname(),
        },
        os.getenv('PHONE_VERIFY_SECRET'),
        headers={'phone': True},
    ).decode('utf-8')
    print("id_token = %s" % id_token)
    return {
        'success': True,
        'id_token': id_token,
    }


def ping():
    return {
        'message': "if you beat me at ping pong, I'll just play ping ponger",
    }


app = connexion.FlaskApp(__name__, debug=True)

# create the bindings, if you use demo2.yaml you will need to use ApiResolver
app.add_api(
    'openapi.yaml',
    arguments={'title': 'rokwire-auth'},
    # resolver=connexion.RestyResolver('auth_rest_service'),
    resolver_error=501,
)


# @app.app.before_request
# def before_request():
#     user_agent = request.headers.get('User-Agent')
#     if user_agent == 'ELB-HealthChecker/2.0':
#         return
#     print("full path = %s, user_agent = %s" % (
#         request.full_path,
#         user_agent,
#     ), flush=True)


if __name__ == '__main__':
    # start the application, in debug mode this will auto reload.
    app.run(port=5000, host=None, server='flask', debug=True)