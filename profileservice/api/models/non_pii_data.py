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

import utils.datasetutils as datasetutils

class NonPiiData():
    def __init__(self, injson):
        self.uuid = None
        self.interests = None
        self.favorites = None
        self.over13 = None
        self.positiveInterestTags = None
        self.negativeInterestTags = None
        self.privacySettings = None
        self.creationDate = None
        self.lastModifiedDate = None

        self, restjson = datasetutils.update_non_pii_dataset_from_json(self, injson)

    def set_uuid(self, uuid):
        self.uuid = uuid

    def get_uuid(self):
        return self.uuid

    def set_over13(self, over13):
        self.over13 = over13

    def get_over13(self):
        return self.over13

    def add_interests(self, interest):
        if (interest is not None):
            self.get_interests().append(interest)

    def set_interests(self, interests):
        self.interests = interests

    def get_interests(self):
        return self.interests

    def set_favorites(self, favorites):
        self.favorites = favorites

    def get_favorites(self):
        return self.favorites

    def add_positiveInterestTags(self, positiveInterestTag):
        if (positiveInterestTag is not None):
            self.get_positiveInterestTags().append(positiveInterestTag)

    def set_positiveInterestTags(self, positiveInterestTags):
        self.positiveInterestTags = positiveInterestTags

    def get_positiveInterestTags(self):
        return self.positiveInterestTags

    def add_negativeInterestTags(self, negativeInterestTag):
        if (negativeInterestTag is not None):
            self.get_negativeInterestTags().append(negativeInterestTag)

    def set_negativeInterestTags(self, negativeInterestTags):
        self.negativeInterestTags = negativeInterestTags

    def get_negativeInterestTags(self):
        return self.negativeInterestTags

    def set_privacy_settings(self, privacySettings):
        self.privacySettings = privacySettings

    def get_privacy_settings(self):
        return self.privacySettings

    def set_creation_date(self, creationDate):
        self.creationDate = creationDate

    def get_creation_date(self):
        return self.creationDate

    def set_last_modified_date(self, lastModifiedDate):
        self.lastModifiedDate = lastModifiedDate

    def get_last_modified_date(self):
        return self.lastModifiedDate