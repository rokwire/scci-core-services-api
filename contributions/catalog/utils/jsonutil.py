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
from bson import ObjectId
from flask import session

'''
add contributionAdmins element in the contribution json
'''
def add_contribution_admins(in_json):
    login_user = session['username']
    admin_input = in_json['contributionAdmins']

    contribution_admins = []
    # if the form input is not empty, then we want to filter out those names from there
    if admin_input:
        contribution_admins = [admin_name for admin_name in admin_input.split(',') if admin_name]

    updated_json = {"contributionAdmins": [login_user] + contribution_admins}
    in_json.update(updated_json)
    return in_json

"""
convert object id from json to regular json element
"""
def convert_obejctid_from_dataset_json(dataset):
    if "_id" in dataset:
        # check if _id is object ID
        if isinstance(dataset["_id"], ObjectId):
            dataset["id"] = str(dataset["_id"])
            dataset = remove_objectid_from_dataset(dataset)
        else:
            if "$oid" in dataset["_id"]:
                dataset["id"] = dataset["_id"]["$oid"]
            else:
                dataset["id"] = str(dataset["_id"])
            dataset = remove_objectid_from_dataset(dataset)

    return dataset

"""
convert object id from json list to regular json element
"""
def convert_obejctid_from_dataset_json_list(json_list):
    out_json_list = []
    for dataset in json_list:
        dataset = convert_obejctid_from_dataset_json(dataset)
        out_json_list.append(dataset)

    return out_json_list

"""
remove object id from dataset json
"""
def remove_objectid_from_dataset(dataset):
    if "_id" in dataset:
        del dataset["_id"]

    return dataset

