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

from utils import requestutil
from controllers.config import Config as cfg

"""
check if the logged in user is a superuser
"""
def check_if_superuser(login_id):
    sp_list = cfg.ADMIN_USERS.split(",")

    if login_id in sp_list:
        return True
    else:
        return False

"""
check if the logged in user is a reviewer
"""
def check_if_reviewer(login_id, headers):
    # check if the logged in id is admin user
    is_superuser = check_if_superuser(login_id)

    if is_superuser:
        return True

    # check if the logged in id is in reviewers database
    # otherwise it will give 401
    result = requestutil.request_reviewers(headers)

    # if you can get this result, the user is a reviewer
    if result.status_code == 200:
        return True

    return False


