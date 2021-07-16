#  Copyright 2021 Board of Trustees of the University of Illinois.
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

import requests
from controllers.config import Config as cfg

""""
create a request header for endpoint using session
"""
def get_header_using_session(session):
    header = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + session['oauth_token']['access_token']
    }

    return header

"""
create header using auth token
"""
def get_header_using_auth_token(auth_token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }

""""
reuqest capability using capability id
"""
def request_capability(headers, contribution_id, cid):
    result = requests.get(cfg.CONTRIBUTION_BUILDING_BLOCK_URL +'/' + str(contribution_id) + "/capabilities/" + str(cid),
                          headers=headers)

    return result

"""
request talent using talent id
"""
def request_talent(headers, contribution_id, tid):
    result = requests.get(cfg.CONTRIBUTION_BUILDING_BLOCK_URL +'/' + str(contribution_id) + "/talents/" + str(tid),
                          headers=headers)

    return result

"""
request reviewer
"""
def request_reviewers(headers):
    result = requests.get(cfg.CONTRIBUTION_BUILDING_BLOCK_URL +'/admin/reviewers', headers=headers)

    return result
