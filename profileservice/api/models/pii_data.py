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

class PiiData:
    def __init__(self, injson):
        self.pid = None
        self.lastname = None
        self.firstname = None
        self.middlename = None
        self.phone = None
        self.email = None
        self.username = None
        self.uin = None
        self.uid = None
        self.netid = None
        self.birthYear = None
        self.address = None
        self.zipCode = None
        self.homeCounty = None
        self.workCounty = None
        self.state = None
        self.country = None
        self.healthcareProviderIDs = None
        self.testResultsConsent = None
        self.documentType = None
        self.photoImageBase64 = None
        self.imageUrl = None
        self.fileDescriptors = None
        self.creationDate = None
        self.lastModifiedDate = None

        self = datasetutils.update_pii_dataset_from_json(self, injson)

    def set_pid(self, pid):
        self.pid = pid

    def get_pid(self):
        return self.pid

    def set_lastname(self, lastname):
        self.lastname = lastname

    def get_lastname(self):
        return self.lastname

    def set_firstname(self, firstname):
        self.firstname = firstname

    def get_firstname(self):
        return self.firstname

    def set_middlename(self, middlename):
        self.middlename = middlename

    def get_middlename(self):
        return self.middlename

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_uin(self, uin):
        self.uin = uin

    def get_uin(self):
        return self.uin

    def set_uid(self, uid):
        self.uid = uid

    def get_uid(self):
        return self.uid

    def set_netid(self, netid):
        self.netid = netid

    def get_netid(self):
        return self.netid

    def add_uuid(self, uuid):
        if (uuid != None):
            self.get_uuid().append(uuid)

    def set_uuid(self, uuid):
        self.uuid = uuid

    def get_uuid(self):
        return self.uuid

    def set_birth_year(self, birthYear):
        self.birthYear = birthYear

    def get_birth_year(self):
        return self.birthYear

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_zip_code(self, zipCode):
        self.zipCode = zipCode

    def get_zip_code(self):
        return self.zipCode

    def set_home_county(self, homeCounty):
        self.homeCounty = homeCounty

    def get_home_county(self):
        return self.homeCounty

    def set_work_county(self, workCounty):
        self.workCounty = workCounty

    def get_work_county(self):
        return self.workCounty

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_country(self, country):
        self.country = country

    def get_country(self):
        return self.country

    def set_healthcare_provider_ids(self, healthcareProviderIDs):
        self.healthcareProviderIDs = healthcareProviderIDs

    def get_healthcare_provider_ids(self):
        return self.healthcareProviderIDs

    def set_test_results_consent(self, testResultsConsent):
        self.testResultsConsent = testResultsConsent

    def get_test_results_consent(self):
        return self.testResultsConsent

    def set_document_type(self, documentType):
        self.documentType = documentType

    def get_document_type(self):
        return self.documentType

    def set_photo_image_base64(self, photoImageBase64):
        self.photoImageBase64 = photoImageBase64

    def get_photo_image_base64(self):
        return self.photoImageBase64

    def add_file_descriptor(self, fileDescriptor):
        if (fileDescriptor is not None):
            self.get_file_descriptors().append(fileDescriptor)

    def set_file_descriptors(self, fileDescriptors):
        self.fileDescriptors = fileDescriptors

    def get_file_descriptors(self):
        return self.fileDescriptors

    def set_image_url(self, imageUrl):
        self.imageUrl = imageUrl

    def get_image_url(self):
        return self.imageUrl

    def set_creation_date(self, creationDate):
        self.creationDate = creationDate

    def get_creation_date(self):
        return self.creationDate

    def set_last_modified_date(self, lastModifiedDate):
        self.lastModifiedDate = lastModifiedDate

    def get_last_modified_date(self):
        return self.lastModifiedDate