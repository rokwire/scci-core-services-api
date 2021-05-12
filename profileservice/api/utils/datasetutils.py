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

import copy

from models.interest import Interest
from models.favorites import Favorites
from models.privacysettings import PrivacySettings
from models.testresultsconsent import TestResultsConsent

"""
set non pii dataset
"""
def update_non_pii_dataset_from_json(dataset, injson):
    outjson = copy.copy(injson)
    try:
        dataset.set_file_descriptors(injson['fileDescriptors'])
        del outjson['fileDescriptors']
    except:
        pass
    try:
        dataset.set_over13(injson['over13'])
        del outjson['over13']
    except:
        pass
    try:
        # check if it is a first interests
        if dataset.get_interests() is not None:
            for i in range(len(injson["interests"])):
                interest = Interest()
                category = injson["interests"][i]["category"]
                interest.set_category(category)

                try:
                    subcategory_list = injson["interests"][i]["subcategories"]
                    interest.subcategories = []
                    for j in range(len(subcategory_list)):
                        subcategory = injson["interests"][i]["subcategories"][j]
                        interest.add_subcategories(subcategory)
                except:
                    pass
                dataset.add_interests(interest)
        else:
            dataset.interests = []
        del outjson["interests"]
    except Exception as e:
        pass
    try:
        favorites = Favorites()
        favorites.set_eventIds(injson["favorites"]["eventIds"])
        favorites.set_placeIds(injson["favorites"]["placeIds"])
        favorites.set_diningPlaceIds(injson["favorites"]["diningPlaceIds"])
        favorites.set_laundryPlaceIds(injson["favorites"]["laundryPlaceIds"])
        favorites.set_athleticEventIds(injson["favorites"]["athleticEventIds"])
        dataset.set_favorites(favorites)
        del outjson["favorites"]
    except Exception as e:
        pass
    try:
        dataset.set_positiveInterestTags(injson["positiveInterestTags"])
        del outjson["positiveInterestTags"]
    except:
        pass
    try:
        dataset.set_negativeInterestTags(injson["negativeInterestTags"])
        del outjson["negativeInterestTags"]
    except:
        pass
    try:
        privacySettings = PrivacySettings()
        level = injson["privacySettings"]["level"]
        date_modified = injson["privacySettings"]["dateModified"]
        privacySettings.set_level(level)
        privacySettings.set_date_modified(date_modified)

        dataset.set_privacy_settings(privacySettings)
    except Exception as e:
        pass
    try:
        dataset.set_creation_date(injson["creationDate"])
    except Exception as e:
        pass
    try:
        dataset.set_last_modified_date(injson["lastModifiedDate"])
    except Exception as e:
        pass
    try:
        del outjson["creationDate"]
        del outjson["lastModifiedDate"]
        del outjson["uuid"]
    except:
        pass

    return dataset, outjson

"""
set pii dataset
"""
def update_pii_dataset_from_json(dataset, injson):
    try:
        dataset.set_pid(injson['pid'])
    except Exception as e:
        pass
    try:
        dataset.set_lastname(injson['lastname'])
    except Exception as e:
        pass
    try:
        dataset.set_firstname(injson['firstname'])
    except Exception as e:
        pass
    try:
        dataset.set_middlename(injson['middlename'])
    except Exception as e:
        pass
    try:
        dataset.set_phone(injson['phone'])
    except Exception as e:
        pass
    try:
        dataset.set_uid(injson['uid'])
    except Exception as e:
        pass
    try:
        dataset.set_email(injson['email'])
    except Exception as e:
        pass
    try:
        dataset.set_username(injson['username'])
    except Exception as e:
        pass
    try:
        dataset.set_uin(injson['uin'])
    except Exception as e:
        pass
    try:
        dataset.set_netid(injson['netid'])
    except Exception as e:
        pass
    try:
        dataset.set_birth_year(injson['birthYear'])
    except Exception as e:
        pass
    try:
        dataset.set_address(injson['address'])
    except Exception as e:
        pass
    try:
        dataset.set_zip_code(injson['zipCode'])
    except Exception as e:
        pass
    try:
        dataset.set_home_county(injson['homeCounty'])
    except Exception as e:
        pass
    try:
        dataset.set_work_county(injson['workCounty'])
    except Exception as e:
        pass
    try:
        dataset.set_state(injson['state'])
    except Exception as e:
        pass
    try:
        dataset.set_country(injson['country'])
    except Exception as e:
        pass
    try:
        dataset.set_healthcare_provider_ids(injson['healthcareProviderIDs'])
    except Exception as e:
        pass
    try:
        testresultsconsent = TestResultsConsent()
        testresultsconsent.set_consent_provided(injson["testResultsConsent"]["consentProvided"])
        dataset.set_test_results_consent(injson['testResultsConsent'])
    except Exception as e:
        pass
    try:
        dataset.set_document_type(injson['documentType'])
    except Exception as e:
        pass
    try:
        dataset.set_photo_image_base64(injson['photoImageBase64'])
    except Exception as e:
        pass
    try:
        dataset.set_creation_date(injson["creationDate"])
    except Exception as e:
        pass
    try:
        dataset.set_last_modified_date(injson["lastModifiedDate"])
    except Exception as e:
        pass

    return dataset
