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

from datetime import date
import uuid

def init_talent():
    d = {
        'id': '',
        "name": '',
        "shortDescription": '',
        "longDescription": '',
        "requiredCapabilities": [],
        "requiredBuildingBlocks": [],
        "minUserPrivacyLevel": 1,
        "minEndUserRoles": [],
        "startDate": date.today().strftime("%d/%m/%Y"),
        "endDate": date.today().strftime("%d/%m/%Y"),
        "dataDescription": '',
        "selfCertification": {
            "dataDeletionUponRequest": '',
            "respectingUserPrivacySetting": '',
            "discloseAds": '',
            "discloseSponsors": '',
            "discloseImageRights": ''
        }
    }
    return d


def to_talent(d):
    if not d: return {}
    talent_list = []

    if isinstance(d['talent_name'], str):
        talent_list.append(init_talent())
    else:
        for _ in range(len(d['talent_name'])):
            talent_list.append(init_talent())

    for i, talent in enumerate(talent_list):
        tal_id = str(uuid.uuid4())
        talent['id'] = tal_id

        for k, v in d.items():
            print(k, v)
            if "minUserPrivacyLevel" in k:
                if len(v[i]) > 0:
                    talent_list[i]["minUserPrivacyLevel"] = int(v[i])
                d[k][i] = talent_list[i]["minUserPrivacyLevel"]
            if "talent_" in k:
                name = k.split("talent_")[-1]
                if name in talent_list[i] and isinstance(talent_list[i][name], list) and len(v[i]) > 0:
                    talent_list[i][name].append(v[i])
                elif name in talent_list[i] and isinstance(talent_list[i][name], list) and len(v[i]) == 0:
                    talent_list[i][name] = []
                else:
                    talent_list[i][name] = v[i]
    return talent_list
