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

import json
import logging
import controllers.configs as cfg

from bson import ObjectId
from flask import make_response, json
from bson.json_util import dumps
from pymongo import MongoClient, ASCENDING

from models.non_pii_data import NonPiiData
from models.pii_data import PiiData
import utils.jsonutils as jsonutils

client_profile = MongoClient(cfg.MONGO_PROFILE_URL, connect=False)
db_profile = client_profile[cfg.PROFILE_DB_NAME]
db_profile.non_pii_collection = db_profile[cfg.PROFILE_DB_PROFILE_COLL_NAME]
db_profile.non_pii_collection.create_index([("uuid", ASCENDING)], background=True)
client_pii = MongoClient(cfg.MONGO_PII_URL, connect=False)
db_pii = client_pii[cfg.PII_DB_NAME]
db_pii.pii_collection = db_pii[cfg.PII_DB_PII_COLL_NAME]
db_pii.pii_collection.create_index([("pid", ASCENDING)], background=True)
db_pii.pii_collection.create_index([("uin", ASCENDING)], background=True)
db_pii.pii_collection.create_index([("phone", ASCENDING)], background=True)
db_pii.pii_collection.create_index([("uid", ASCENDING)], background=True)

"""
get query output json of PII from query using search arguments
"""
def get_profile_result(query):
    if not query:
        return None

    db_data = db_profile.non_pii_collection.find(query, {'_id': 0})
    data_list = list(db_data)

    if len(data_list) > 0:
        data_dump = dumps(data_list)
        if len(data_list) == 1: # remove blacket in the first and last character location
            data_dump = data_dump[:-1]
            data_dump = data_dump[1:]
        json_load = json.loads(data_dump)

        return json_load
    else:
        return None

"""
get query output json of PII from query using search arguments
"""
def get_pii_result(query):
    if not query:
        return None

    db_data = db_pii.pii_collection.find(query, {'_id': 0})
    data_list = list(db_data)

    if len(data_list) > 0:
        data_dump = dumps(data_list)
        data_dump = data_dump[:-1]
        data_dump = data_dump[1:]
        json_load = json.loads(data_dump)

        return json_load
    else:
        return None

"""
get query output json from field name and query string
"""
def get_pii_http_output_query_result_using_field_string(fld, query_str):
    outjson = get_pii_query_json_from_field(fld, query_str)
    if (outjson is not None) and (len(outjson)) > 0:
        data_dump = dumps(outjson)
        out_json = make_response(data_dump)
        out_json.mimetype = 'application/json'

        msg = "request profile information: " + str(query_str)
        logging.debug(msg)

        return out_json
    else:
        msg = "the dataset does not exist with uuid of : " + str(query_str)
        logging.error(msg)

        return None

"""
query non-pii using objectid and convert result to non-pii object
"""
def get_non_pii_dataset_from_objectid(objectid):
    is_profile_id = check_if_objectid(objectid)
    if is_profile_id:
        id = ObjectId(objectid)
        db_data = query_non_pii_dataset_by_objectid(id)
        data_list = list(db_data)
        if len(data_list) > 0:
            data_dump = dumps(data_list)
            data_dump = data_dump[:-1]
            data_dump = data_dump[1:]
            json_load = json.loads(data_dump)
            dataset = NonPiiData(json_load)

            return dataset
        else:
            return None
    else:
        return None

"""
query non-pii using field name and querystring and convert result to non-pii object
"""
def get_non_pii_dataset_from_field(fld, query_str):
    db_data = query_non_pii_dataset(fld, query_str)
    data_list = list(db_data)
    if len(data_list) == 1:
        data_dump = dumps(data_list)
        data_dump = data_dump[:-1]
        data_dump = data_dump[1:]
        json_load = json.loads(data_dump)
        dataset = NonPiiData(json_load)

        try:
            dataset.set_uuid(json_load[cfg.FIELD_PROFILE_UUID])
        except:
            pass

        return dataset

    elif len(data_list) > 1:
        #TODO create a method to handle this

        return None

    else:
        msg = 'there is no output query result or multiple query result'
        logging.debug(msg)

        return None

"""
query pii using field name and querystring and convert result to non-pii object
"""
def get_pii_dataset_from_field(fld, query_str):
    db_data = query_pii_dataset(fld, query_str)
    data_list = list(db_data)
    if len(data_list) == 1:
        data_dump = dumps(data_list)
        data_dump = data_dump[:-1]
        data_dump = data_dump[1:]
        json_load = json.loads(data_dump)
        dataset = PiiData(json_load)

        try:
            dataset.set_uuid(json_load[cfg.FIELD_PROFILE_UUID])
        except:
            pass

        # this will not be implemented to protect pid get updated from request body
        # try:
        #     dataset.set_pid(json_load[cfg.FIELD_PID])
        # except:
        #     pass

        return dataset

    elif len(data_list) > 1:
        #TODO create a method to handle this

        return None

    else:
        msg = 'there is no output query result or multiple query result'
        logging.debug(msg)

        return None

"""
convert non-pii mongodb query using field result to json
"""
def get_non_pii_query_json_from_field(fld, query_str):
    db_data = query_non_pii_dataset(fld, query_str)
    data_list = list(db_data)
    if len(data_list) > 0:
        data_dump = dumps(data_list)
        data_dump = data_dump[:-1]
        data_dump = data_dump[1:]
        json_load = json.loads(data_dump)

        return json_load
    else:
        return None

"""
convert pii mongodb query using field result to json
"""
def get_pii_query_json_from_field(fld, query_str):
    db_data = query_pii_dataset(fld, query_str)
    data_list = list(db_data)

    # remove fileDescriptors from db_data
    data_list = jsonutils.remove_file_descriptor_from_data_list(data_list)

    if len(data_list) > 0:
        data_dump = dumps(data_list)
        data_dump = data_dump[:-1]
        data_dump = data_dump[1:]
        json_load = json.loads(data_dump)

        return json_load
    else:
        return None

"""
check if the query string is objectid
"""
def check_if_objectid(query_str):
    is_objectid = True
    try:
        id = ObjectId(query_str)
    except:
        is_objectid = False

    return is_objectid

"""
query non pii dataset using object id
"""
def query_non_pii_dataset_by_objectid(objectid):
    return db_profile.non_pii_collection.find({'_id': objectid})

"""
qyery non pii dataset using field
"""
def query_non_pii_dataset(fld, query_str):
    return db_profile.non_pii_collection.find({fld: query_str}, {'_id': False})

"""
query PII dataset using object id
"""
def query_pii_dataset_by_objectid(objectid):
    return db_pii.pii_collection.find({'_id': objectid})

"""
qyery pii dataset using field
"""
def query_pii_dataset(fld, query_str):
    return db_pii.pii_collection.find({fld: query_str}, {'_id': False})

"""
construct json from mongo query
"""
def construct_json_from_query_list(data_list):
    data_dump = dumps(data_list)
    out_json = make_response(data_dump)
    out_json.mimetype = 'application/json'

    return out_json

"""
insert non pii dataset to mognodb
"""
def insert_non_pii_dataset_to_mongodb(indataset):
    dataset = json.dumps(indataset, default=lambda x: x.__dict__)
    dataset = json.loads(dataset)

    id = db_profile.non_pii_collection.insert(dataset)

    return dataset, id

"""
insert pii dataset to mognodb
"""
def insert_pii_dataset_to_mongodb(indataset):
    dataset = json.dumps(indataset, default=lambda x: x.__dict__)
    dataset = json.loads(dataset)

    id = db_pii.pii_collection.insert(dataset)

    return dataset

"""
update non pii dataset in mongodb by objectid
"""
def update_non_pii_dataset_in_mongo_by_objectid(objectid, datasetobj):
    dataset = json.dumps(datasetobj, default=lambda x: x.__dict__)
    dataset = json.loads(dataset)
    id = ObjectId(objectid)
    result = db_profile.non_pii_collection.update_one({'_id': id}, {"$set": dataset}, upsert=False)

    return result.acknowledged, dataset

"""
update non pii dataset in mongodb by field
"""
def update_non_pii_dataset_in_mongo_by_field(fld, query_str, datasetobj):
    dataset = json.dumps(datasetobj, default=lambda x: x.__dict__)
    dataset = json.loads(dataset)
    result = db_profile.non_pii_collection.update_one({fld: query_str}, {"$set": dataset}, upsert=False)

    return result.acknowledged, dataset

"""
update json that doesn't belong to data schema
"""
def update_json_with_no_schema(fld, query_str, datasetobj, restjson):
    dataset = db_profile.non_pii_collection.find({fld: query_str}, {'_id': False})
    dataset = json.dumps(datasetobj, default=lambda x: x.__dict__)
    dataset = json.loads(dataset)
    for dictkey, dictelement in restjson.items():
        tmpDict = {dictkey: dictelement}
        dataset.update(tmpDict)
        result = db_profile.non_pii_collection.update_one({fld: query_str}, {"$set": tmpDict}, upsert=False)

    return result.acknowledged, dataset

"""
update pii dataset in mongodb by objectid
"""
def update_pii_dataset_in_mongo_by_objectid(objectid, datasetobj):
    dataset = json.dumps(datasetobj, default=lambda x: x.__dict__)
    dataset = json.loads(dataset)
    id = ObjectId(objectid)
    result = db_pii.pii_collection.update_one({'_id': id}, {"$set": dataset}, upsert=False)

    return result.acknowledged, dataset

"""
update pii dataset in mongodb by field
"""
def update_pii_dataset_in_mongo_by_field(fld, query_str, datasetobj):
    dataset = json.dumps(datasetobj, default=lambda x: x.__dict__)
    dataset = json.loads(dataset)
    result = db_pii.pii_collection.update_one({fld: query_str}, {"$set": dataset}, upsert=False)

    return result.acknowledged, dataset

"""
index non pii collection
"""
def index_non_pii_data():
    db_profile.non_pii_collection.create_index([('uuid', ASCENDING)], background=True)

"""
index non pii collection
"""
def index_pii_data():
    db_pii.pii_collection.create_index([('pid', ASCENDING)], background=True)
    db_pii.pii_collection.create_index([('uin', ASCENDING)], background=True)
    db_pii.pii_collection.create_index([('phone', ASCENDING)], background=True)
    db_pii.pii_collection.create_index([("uid", ASCENDING)], background=True)