#  Copyright 2020 Board of Trustees of the University of Illinois.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import controllers.configs as cfg


def get_id_info_from_token(in_token):
    # in_token = convert_str_to_dict(in_token)
    tk_id = None
    issuer = in_token.get("iss")
    phoneNumber = in_token.get('phoneNumber')
    if issuer == cfg.AUTH_ISSUER:
        tk_id = in_token.get('uid')

    # Will be later replaced by issuer for rokwire phone auth
    elif phoneNumber is not None:
        tk_id = phoneNumber

    # OIDC Auth or Shibboleth
    else:
        tk_id = in_token.get('uiucedu_uin')

    return tk_id


def convert_str_to_dict(in_token):
    while True:
        try:
            converted_dict = eval(in_token)
        except NameError as e:
            key = e.message.split("'")[1]
            in_token = in_token.replace(key, "'{}'".format(key))
        else:
            return converted_dict


def get_data_from_token(in_token):
    tk_uid = tk_name = tk_email = tk_phone = tk_auth = None
    issuer = in_token.get("iss")
    phoneNumber = in_token.get('phoneNumber')
    if issuer == cfg.AUTH_ISSUER:
        tk_uid = in_token.get('uid')
        tk_name = in_token.get('name')
        tk_email = in_token.get('email')
        tk_phone = in_token.get('phone')
        tk_auth = in_token.get('auth')

    # Will be later replaced by issuer for rokwire phone auth
    elif phoneNumber is not None:
        tk_uid = phoneNumber
        tk_phone = phoneNumber
        tk_auth = 'rokwire_phone'

    # OIDC Auth or Shibboleth
    else:
        tk_uid = in_token.get('uiucedu_uin')
        tk_name = in_token.get('given_name', '') + ' ' + \
            in_token.get('family_name', '')
        tk_email = in_token.get('email')
        tk_auth = "oidc"

    return tk_uid, tk_name, tk_email, tk_phone, tk_auth
