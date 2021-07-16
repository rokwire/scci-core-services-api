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

import os

from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Config(object):
    OAUTHLIB_INSECURE_TRANSPORT = bool(os.getenv('OAUTHLIB_INSECURE_TRANSPORT', 'False') == 'True')
    CONTRIBUTION_BUILDING_BLOCK_URL = os.getenv("CONTRIBUTION_BUILDING_BLOCK_URL",
                                                "http://localhost:5000/contributions")
    MONGO_URL = os.getenv('MONGO_URL', 'mongodb://localhost:27017')
    DB_NAME = os.getenv("MONGO_DATABASE", "contribution")
    DB_COLLECTION = os.getenv("MONGO_DATABASE", "catalog")
    URL_PREFIX = os.getenv("URL_PREFIX", "")
    DBTYPE = 'mongoDB'
    SECRET_KEY = os.getenv("SECRET_KEY", "SECRET_KEY")
    AUTHENTICATION_TOKEN = os.getenv("AUTHENTICATION_TOKEN", "...")
    ROKWIRE_API_KEY = os.getenv("ROKWIRE_API_KEY", "...")
    DEBUG = bool(os.getenv('DEBUG', 'False') == 'True')
    GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID", "NO ID")
    GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET", "NO SECRET")
    AUTHORIZATION_BASE_URL = os.getenv("AUTHORIZATION_BASE_URL", 'https://github.com/login/oauth/authorize')
    TOKEN_URL = os.getenv("TOKEN_URL", 'https://github.com/login/oauth/access_token')
    CORS_ENABLED = bool(os.getenv('CORS_ENABLED', 'False') == 'True')
    ADMIN_USERS = os.getenv('ADMIN_USERS', [])
