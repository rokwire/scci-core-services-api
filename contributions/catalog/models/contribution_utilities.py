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

from .capability_utilities import to_capability
from .talent_utilities import to_talent


def init_contribution():
    d = {
        "name": '',
        "shortDescription": '',
        "longDescription": '',
        'contributionAdmins': [],
        "contributors": [],
        "capabilities": [],
        "talents": []
    }
    return d


def init_person():
    return {
        "firstName": "",
        "middleName": "",
        "lastName": "",
        "email": "",
        "phone": "",
        "affiliation": {
            "name": "",
            "address": "",
            "email": "",
            "phone": ""
        }
    }


def init_organization():
    return {
        "name": "",
        "address": "",
        "email": "",
        "phone": ""
    }


def to_contributor(d):
    if not d: return {}
    person_list = []
    org_list = []

    if 'org_name' in d:
        if isinstance(d['org_name'], str):
            org_list.append(init_organization())
        else:
            for _ in range(len(d['org_name'])):
                org_list.append(init_organization())

    if 'person_firstName' in d:
        if isinstance(d['person_firstName'], str):
            person_list.append(init_person())
        else:
            for _ in range(len(d['person_firstName'])):
                person_list.append(init_person())

    for i, e in enumerate(person_list):
        for k, v in d.items():
            if "affiliation_" in k.lower():
                # print(k,v)
                name = k.split("affiliation_")[-1]
                person_list[i]["affiliation"][name] = v[i]
            if "person_" in k.lower():
                name = k.split("person_")[-1]
                person_list[i][name] = v[i]
    # print(person_list)

    for i, e in enumerate(org_list):
        for k, v in d.items():
            if "org_" in k:
                name = k.split("org_")[-1]
                org_list[i][name] = v[i]

    if not person_list or len(person_list) == 0: return org_list
    if not org_list or len(person_list) == 0: return person_list
    return person_list + org_list


def to_contribution(d):
    if not d: return {}
    res = init_contribution()
    capability = to_capability(d)
    if len(capability) >= 1 and capability[0]["name"]:
        res["capabilities"] = capability
    # print(res["capabilities"])
    talent = to_talent(d)
    if len(talent) >= 1 and talent[0]["name"]:
        res["talents"] = talent
    contributor = to_contributor(d)
    res["contributors"] = contributor

    for k, v in d.items():
        if "contribution_" in k:
            name = k.split("contribution_")[-1]
            res[name] = v[0]
    return res
