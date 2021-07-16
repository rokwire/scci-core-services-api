import json
import logging
import traceback

import requests
import functools
from flask import (
    Blueprint, render_template, request, session, redirect, url_for
)
from requests_oauthlib import OAuth2Session
from .auth import login_required
from controllers.config import Config as cfg
from models.contribution_utilities import to_contribution
from utils import jsonutil

bp = Blueprint('contribute', __name__, url_prefix='/contribute')


@bp.route('/', methods=['GET', 'POST'])
def home():
    print("homepage.")
    if request.method == 'POST' and request.validate_on_submit():
        result = request.form.to_dict(flat=False)
    if "name" in session:
        return render_template('contribute/home.html', user=session["name"], token=session['oauth_token']['access_token'])
    else:
        return render_template('contribute/home.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Step 1: Get the user identify for authentication.
    """
    # print("Step 1: User Authorization")
    github = OAuth2Session(cfg.GITHUB_CLIENT_ID)
    authorization_url, state = github.authorization_url(cfg.AUTHORIZATION_BASE_URL)

    # State is used to prevent CSRF.
    session['oauth_state'] = state
    return redirect(authorization_url)


@bp.route('/logout')
def logout():
    session.clear()
    return render_template('contribute/home.html')


@bp.route('/results', methods=['POST', 'GET'])
@login_required
def result():
    if request.method == 'POST':
        # result = request.form
        result = request.form.to_dict()
        query = result['search']
        search(query)
        return render_template("contribute/results.html", user=session["name"],  token=session['oauth_token']['access_token'], result=result)



@bp.route('details/<contribution_id>', methods=['GET'])
def contribution_details(contribution_id):
    the_json_res = get_contribution(contribution_id)
    return render_template("contribute/contribution_details.html", post=the_json_res, user=session["name"])

@bp.route('details/<contribution_id>/capabilities/<id>', methods=['GET'])
def capability_details(contribution_id, id):
    the_json_res = get_capability(contribution_id, id)
    return render_template("contribute/capability_details.html", post=the_json_res, user=session["name"])

@bp.route('details/<contribution_id>/talents/<id>', methods=['GET'])
def talent_details(contribution_id, id):
    the_json_res = get_talent(contribution_id, id)
    return render_template("contribute/talent_details.html", post=the_json_res, user=session["name"])


# @bp.route('/edit/<contribution_id>', methods=('GET', 'POST'))
# def edit(contribution_id):
#     #todo: need to implement the edit form page
#     return render_template("contribute/contribution_details.html", contribution_json=the_json_res)

@bp.route('/create', methods=['GET', "POST"])
@login_required
def create():
    if request.method == 'POST':
        result = request.form.to_dict(flat=False)
        # result = dict((key, request.form.getlist(key) if len(request.form.getlist(key)) > 1 else request.form.getlist(key)[0]) for key in request.form.keys())

        contribution = to_contribution(result)
        # add contributionAdmins to the json_contiubtion
        contribution = jsonutil.add_contribution_admins(contribution)
        json_contribution = json.dumps(contribution, indent=4)
        response, s = post(json_contribution)

        if response:
            if "name" in session:
                return render_template('contribute/submitted.html', user=session["name"],  token=session['oauth_token']['access_token'])
            else:
                return render_template('contribute/submitted.html')
        elif not response:
            if "name" in session:
                return render_template('contribute/error.html', user=session["name"],  token=session['oauth_token']['access_token'], error_msg=s)
            else:
                return render_template('contribute/error.html', error_msg=s)
    return render_template('contribute/contribute.html', user=session["name"],  token=session['oauth_token']['access_token'])


@bp.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('contribute/submitted.html', user=session["name"],  token=session['oauth_token']['access_token'])


@bp.route('/submitted', methods=['GET', 'POST'])
@login_required
def submitted():
    return render_template('contribute/submitted.html', user=session["name"],  token=session['oauth_token']['access_token'])


@bp.route('/results')
@login_required
def search_results(search):
    return render_template('results.html', results=results, user=session["name"],  token=session['oauth_token']['access_token'])


# post a json_data in a http request
def post(json_data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + session['oauth_token']['access_token']
    }
    try:
        # Setting up post request
        result = requests.post(cfg.CONTRIBUTION_BUILDING_BLOCK_URL,
                               headers=headers,
                               data=json_data)

        if result.status_code != 200:
            err_json = parse_response_error(result)
            logging.error("Contribution POST " + json.dumps(err_json))
            return False, str("post method fails with error: ") + str(result.status_code) \
                   + ": " + str(err_json['reason'])
        else:
            logging.info("posted ok.".format(json_data))
            return True, str("post success!")

    except Exception:
        traceback.print_exc()
        var = traceback.format_exc()
        return False, var


def get_contribution(contribution_id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + session['oauth_token']['access_token']
    }

    try:
        if contribution_id:
            result = requests.get(cfg.CONTRIBUTION_BUILDING_BLOCK_URL + "/" + str(contribution_id),
                                  headers=headers)

        if result.status_code != 200:
            err_json = parse_response_error(result)
            logging.error("Contribution GET " + json.dumps(err_json))
            return {}
        else:
            print("GET ok.".format(contribution_id))

    except Exception:
        # traceback.print_exc()
        return False
    return result.json()

def get_capability(contribution_id, cid):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + session['oauth_token']['access_token']
    }

    try:
        if contribution_id and cid:
            result = requests.get(cfg.CONTRIBUTION_BUILDING_BLOCK_URL +'/' + str(contribution_id) + "/capabilities/" + str(cid),
                                  headers=headers)
        if result.status_code != 200:
            err_json = parse_response_error(result)
            logging.error("Capability GET " + json.dumps(err_json))
            return {}
        else:
            print("GET ok.".format(id))

    except Exception:
        # traceback.print_exc()
        return False
    return result.json()

def get_talent(contribution_id, tid):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + session['oauth_token']['access_token']
    }

    try:
        if id:
            result = requests.get(cfg.CONTRIBUTION_BUILDING_BLOCK_URL +'/' + str(contribution_id) + "/talents/" + str(tid),
                                  headers=headers)

        if result.status_code != 200:
            err_json = parse_response_error(result)
            logging.error("Talent GET " + json.dumps(err_json))
            return {}
        else:
            print("GET ok.".format(id))

    except Exception:
        # traceback.print_exc()
        return False
    return result.json()

# post a json_data in a http request
def search(input_data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + cfg.AUTHENTICATION_TOKEN
    }

    try:
        # Setting up post request
        if not input_data or len(input_data) == 0:
            result = requests.get(cfg.CONTRIBUTION_BUILDING_BLOCK_URL + "/",
                                  headers=headers)
        else:
            result = requests.get(cfg.CONTRIBUTION_BUILDING_BLOCK_URL + "/" + str(input_data),
                                  headers=headers)

        if result.status_code != 200:
            err_json = parse_response_error(result)
            logging.error("Search " + json.dumps(err_json))
            return False
        else:
            print("posted ok.".format(input_data))
            return True

    except Exception:
        # traceback.print_exc()
        return False

"""
parse error response and convert to json object
"""
def parse_response_error(response):
    err_content = response.content.decode("utf-8").replace('\n', '')
    err_json = json.loads(err_content)

    return err_json