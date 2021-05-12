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

import os

from dotenv import load_dotenv

# Load .env file
load_dotenv()

# this has to be have the file path to the folder for saving image files and other necessary files from rest service
PROFILE_REST_STORAGE = os.getenv('REST_STORAGE', '/usr/src/app/rest')
MONGO_PROFILE_URL = os.getenv('MONGO_PROFILE_URL', 'localhost:27017')
MONGO_PII_URL = os.getenv('MONGO_PII_URL', 'localhost:27017')
FLASK_APP = os.getenv('FLASK_APP', 'profile_rest_service')
FLASK_ENV = os.getenv('FLASK_ENV', 'production')
API_LOC = os.getenv('API_LOC', '../')
PROFILE_URL_PREFIX = os.getenv('PROFILE_URL_PREFIX', '')
SHIB_HOST = os.getenv('SHIBBOLETH_HOST', '')
AUTH_ISSUER = os.getenv('AUTH_ISSUER', '')
DEBUG = bool(os.getenv('DEBUG', 'False') == 'True')

PROFILE_DB_NAME = os.getenv('PROFILE_DB_NAME', 'profiledb')
PII_DB_NAME = os.getenv('PII_DB_NAME', 'piidb')
PROFILE_DB_PROFILE_COLL_NAME = 'NonPiiDataset'
PII_DB_PII_COLL_NAME = 'PiiDataset'
FIELD_OBJECTID = '_id'
FIELD_PROFILE_UUID = 'uuid'
FIELD_PID = 'pid'
