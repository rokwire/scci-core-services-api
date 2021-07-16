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
import datetime
import logging

from flask import wrappers, request
from bson import ObjectId

import controllers.configs as cfg
import utils.datasetutils as datasetutils
import utils.rest_handlers as rs_handlers
import utils.mongoutils as mongoutils
import utils.otherutils as otherutils
import utils.modelutils as modelutils
import utils.adminutils as adminutils
import utils.jsonutils as jsonutils

from utils import query_params
from models.contribution import Contribution
from models.person import Person
from models.organization import Organization
from models.capabilities.capability import Capability
from models.talents.talent import Talent
from models.reviewer import Reviewer
from pymongo import MongoClient


client_contribution = MongoClient(cfg.MONGO_CONTRIBUTION_URL, connect=False)
db_contribution = client_contribution[cfg.CONTRIBUTION_DB_NAME]
coll_contribution = db_contribution[cfg.CONTRIBUTION_COLL_NAME]
coll_reviewer = db_contribution[cfg.REVIEWER_COLL_NAME]

def post(token_info):
    is_new_install = True
    in_json = None

    # check if name is in there otherwise it is either a first installation
    try:
        in_json = request.get_json()
        name = in_json[cfg.FIELD_NAME]
        # check if the dataset is existing with given name
        dataset = mongoutils.get_contribution_dataset_from_field_no_status(coll_contribution, cfg.FIELD_NAME, name)
        if dataset is not None:
            is_new_install = False
            msg = {
                "reason": "NAME in input json already exists in the database: " + str(name),
                "error": "Bad Request: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Contribution", "POST", msg)
            logging.error("Contribution POST " + json.dumps(msg_json))
            return rs_handlers.bad_request(msg)
    except:
        pass

    if is_new_install:
        # new installation of the app
        currenttime = datetime.datetime.now()
        currenttime = currenttime.strftime("%Y/%m/%dT%H:%M:%S")
        contribution_dataset = Contribution('')
        contribution_dataset, restjson = datasetutils.update_contribution_dataset_from_json(contribution_dataset, in_json)
        contribution_dataset.set_date_created(currenttime)
        contribution_dataset.set_date_modified(currenttime)

        # get contribution admins, if failed it is a bad request
        contribution_admins = in_json['contributionAdmins']

        # get contribution_admins value from the list
        # doing this because connexion's minItems doesn't work, otherwise this is not needed
        if len(contribution_admins) == 0:
            msg = {
                "reason": "Contribution admin list is empty.",
                "error": "Bad Request: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Contribution", "POST", msg)
            logging.error("Contribution POST " + json.dumps(msg_json))
            return rs_handlers.bad_request(msg_json)

        # check if the logged in user's login is included in contribution admin list
        is_admin_user = otherutils.check_login_admin(token_info["login"], contribution_admins)
        if not is_admin_user:
            msg = {
                "reason": "Contribution admin list must contain logged in user",
                "error": "Bad Request: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Contribution", "POST", msg)
            logging.error("Contribution POST " + json.dumps(msg_json))
            return rs_handlers.bad_request(msg_json)

        # set contributors list
        contributors_list = []
        try:
            contributors_json = in_json["contributors"]
            for i in range(len(contributors_json)):
                contributor, rest_contributor_json, msg = modelutils.construct_contributors(contributors_json[i])
                if contributor is None:
                    return rs_handlers.bad_request(msg)
                contributors_list.append(contributor)
            contribution_dataset.set_contributors(contributors_list)
        except:
            pass

        # set capability list
        capability_list = []
        try:
            capability_json = in_json["capabilities"]
            for i in range(len(capability_json)):
                capability, rest_capability_json, msg = modelutils.construct_capability(capability_json[i])
                if capability is None:
                    return rs_handlers.bad_request(msg)

                # following two lines are for creating id. However, it might not needed for now
                # because catalog will create it and send it to endpoint.
                # If not, use following two lines that commented out
                # capability_id = str(uuidlib.uuid4())
                # capability.set_id(capability_id)

                # check if the capability id is in uuid format
                is_uuid = otherutils.check_if_uuid(capability.id)
                if not is_uuid:
                    msg = {
                        "reason": "Capability id is not in uuid format",
                        "error": "Bad Request: " + request.url,
                    }
                    msg_json = jsonutils.create_log_json("Contribution", "POST", msg)
                    logging.error("Contribution POST " + json.dumps(msg_json))
                    return rs_handlers.bad_request(msg)
                capability_list.append(capability)
            contribution_dataset.set_capabilities(capability_list)
        except:
            pass

        # set talent list
        talent_list = []
        try:
            talent_json = in_json["talents"]
            for i in range(len(talent_json)):
                talent, rest_talent_json, msg = modelutils.construct_talent(talent_json[i])
                if talent is None:
                    return rs_handlers.bad_request(msg)

                # following two lines are for creating id. However, it might not needed for now
                # because catalog will create it and send it to endpoint.
                # If not, use following two lines that commented out
                # talent_id = str(uuidlib.uuid4())
                # talent.set_id(talent_id)

                # check if the talent id is in uuid format
                is_uuid = otherutils.check_if_uuid(talent.id)
                if not is_uuid:
                    msg = {
                        "reason": "Talent id is not in uuid format",
                        "error": "Bad Request: " + request.url,
                    }
                    msg_json = jsonutils.create_log_json("Contribution", "POST", msg)
                    logging.error("Contribution POST " + json.dumps(msg_json))
                    return rs_handlers.bad_request(msg)

                # check required capabilities id format
                if talent.requiredCapabilities is not None:
                    required_cap_list = talent.requiredCapabilities
                    for capability_json in required_cap_list:
                        capability, rest_capability_json, msg = modelutils.construct_capability(capability_json)
                        is_uuid = otherutils.check_if_uuid(capability.id)
                        if not is_uuid:
                            msg = {
                                "reason": "Capability id in requiredCapabilities is not in uuid format",
                                "error": "Bad Request: " + request.url,
                            }
                            msg_json = jsonutils.create_log_json("Contribution", "POST", msg)
                            logging.error("Contribution POST " + json.dumps(msg_json))
                            return rs_handlers.bad_request(msg)
                talent_list.append(talent)
            contribution_dataset.set_talents(talent_list)
        except:
            pass

        # insert contribution dataset
        dataset, id = mongoutils.insert_dataset_to_mongodb(coll_contribution, contribution_dataset)
        contribution_name = dataset[cfg.FIELD_NAME]
        contribution_id = str(dataset['_id'])

        # use this if it needs to return actual dataset
        dataset = jsonutils.remove_objectid_from_dataset(dataset)
        # out_json = mongoutils.construct_json_from_query_list(dataset)
        msg = "new contribution has been created: " + str(contribution_name)
        msg_json = jsonutils.create_log_json("Contribution", "POST", {"id": str(contribution_id)})
        logging.info("Contribution POST " + json.dumps(msg_json))

        return rs_handlers.return_id(msg, 'id', contribution_id)

def search(token_info=None, name=None):
    # args = request.args
    is_list = False
    query = dict()

    login_id, is_login = otherutils.get_login(token_info)

    # building query parematers
    query = query_params.format_query_status_login(query, login_id, is_login)

    # if there is no query word, it is simply requesting list of all records
    if name is None:
        is_list = True

    if is_list:
        # return the list of all records
        out_json = mongoutils.get_result(coll_contribution, query)
    else:
        try:
            query = query_params.format_query_contribution(name, query)
        except Exception as ex:
            msg = {
                "reason": "The query is wrong or bad argument",
                "error": "Bad Request: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Contribution", "SEARCH", msg)
            logging.error("Contribution SEARCH " + json.dumps(msg_json))
            return rs_handlers.bad_request(msg_json)

        try:
            # get result using query
            out_json = mongoutils.get_result(coll_contribution, query)
        except Exception as ex:
            msg = {
                "reason": "The query is wrong or bad argument",
                "error": "Bad Request: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Contribution", "SEARCH", msg)
            logging.error("Contribution SEARCH " + json.dumps(msg_json))
            return rs_handlers.bad_request(msg_json)

    if out_json is None:
        out_json = []

    msg = {
        "search": "Contribution search performed with : " + str(name)
    }
    msg_json = jsonutils.create_log_json("Contribution", "SEARCH", msg)
    logging.info("Contribution SEARCH " + json.dumps(msg))

    return out_json

def get(token_info=None, id=None):
    login_id, is_login = otherutils.get_login(token_info)

    data_list, is_objectid, is_error, resp = otherutils.get_data_list(id, login_id, is_login, coll_contribution)

    # if getting data process failed, that is is_error is true, return error reponse
    if is_error:
        return resp
    jsonutils.convert_obejctid_from_dataset_json(data_list[0])
    out_json = mongoutils.construct_json_from_query_list(data_list[0])
    msg_json = jsonutils.create_log_json("Contribution", "GET", {"id": str(id)})
    logging.info("Contribution GET " + json.dumps(jsonutils.remove_objectid_from_dataset(msg_json)))

    return out_json

def put(token_info, id):
    try:
        in_json = request.get_json()
    except Exception as ex:
        msg = {
            "reason": "Json format error: " + str(id),
            "error": "Bad Request: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Contribution", "PUT", msg)
        logging.error("Contribution PUT " + json.dumps(msg_json))
        return rs_handlers.bad_request(msg_json)
    # check if the given id exists
    contribution_dataset = mongoutils.get_contribution_dataset_from_objectid_no_status(coll_contribution, id)

    if contribution_dataset is None:
        msg = {
            "reason": "There is no contribution dataset with given id: " + str(id),
            "error": "Not Found: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Contribution", "PUT", msg)
        logging.error("Contribution PUT " + json.dumps(msg_json))
        return rs_handlers.not_found(msg_json)

    # check contribution admins
    contribution_admins = contribution_dataset.contributionAdmins

    # check if the logged in user's login is included in contribution admin list
    is_admin_user = otherutils.check_login_admin(token_info["login"], contribution_admins)
    if not is_admin_user:
        msg = {
            "reason": "Contribution admin list must contain logged in user",
            "error": "Not Authorized: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Contribution", "POST", msg)
        logging.error("Contribution POST " + json.dumps(msg_json))
        return rs_handlers.not_authorized(msg_json)

    date_created = contribution_dataset.dateCreated
    contribution_dataset, restjson = datasetutils.update_contribution_dataset_from_json(contribution_dataset, in_json)
    currenttime = datetime.datetime.now()
    currenttime = currenttime.strftime("%Y/%m/%dT%H:%M:%S")
    contribution_dataset.set_date_modified(currenttime)
    contribution_dataset.set_date_created(date_created)

    # set capability list
    capability_list = []
    try:
        capability_json = in_json["capabilities"]
        for i in range(len(capability_json)):
            capability, rest_capability_json, msg = modelutils.construct_capability(capability_json[i])
            if capability is None:
                return rs_handlers.bad_request(msg)
            # check if the capability id is in uuid format
            is_uuid = otherutils.check_if_uuid(capability.id)
            if not is_uuid:
                msg = {
                    "reason": "Capability id is not in uuid format",
                    "error": "Bad Request: " + request.url,
                }
                msg_json = jsonutils.create_log_json("Contribution", "POST", msg)
                logging.error("Contribution POST " + json.dumps(msg_json))
                return rs_handlers.bad_request(msg)
            capability_list.append(capability)
        contribution_dataset.set_capabilities(capability_list)
    except:
        pass

    # set talent list
    talent_list = []
    try:
        talent_json = in_json["talents"]
        for i in range(len(talent_json)):
            talent, rest_talent_json, msg = modelutils.construct_talent(talent_json[i])
            if talent is None:
                return rs_handlers.bad_request(msg)
            # check if the talent id is in uuid format
            is_uuid = otherutils.check_if_uuid(talent.id)
            if not is_uuid:
                msg = {
                    "reason": "Talent id is not in uuid format",
                    "error": "Bad Request: " + request.url,
                }
                msg_json = jsonutils.create_log_json("Contribution", "POST", msg)
                logging.error("Contribution POST " + json.dumps(msg_json))
                return rs_handlers.bad_request(msg)

            # check required capabilities id format
            if talent.requiredCapabilities is not None:
                required_cap_list = talent.requiredCapabilities
                for capability_json in required_cap_list:
                    capability, rest_capability_json, msg = modelutils.construct_capability(capability_json)
                    is_uuid = otherutils.check_if_uuid(capability.id)
                    if not is_uuid:
                        msg = {
                            "reason": "Capability id in requiredCapabilities is not in uuid format",
                            "error": "Bad Request: " + request.url,
                        }
                        msg_json = jsonutils.create_log_json("Contribution", "POST", msg)
                        logging.error("Contribution POST " + json.dumps(msg_json))
                        return rs_handlers.bad_request(msg)

            talent_list.append(talent)
        contribution_dataset.set_talents(talent_list)
    except:
        pass

    result, contribution_dataset = mongoutils.update_dataset_in_mongo_by_objectid(coll_contribution, id, contribution_dataset)

    if result is None:
        msg = {
            "reason": "Failed to update contribution dataset: " + str(id),
            "error": "Not Implemented: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Contribution", "PUT", msg)
        logging.error("Contribution PUT " + json.dumps(msg_json))
        return rs_handlers.not_implemented(msg_json)

    out_json = contribution_dataset
    msg_json = jsonutils.create_log_json("Contribution", "PUT", {"id": str(id)})
    logging.info("Contribution PUT " + json.dumps(msg_json))
    out_json = mongoutils.construct_json_from_query_list(out_json)

    return out_json

def delete(token_info, id):
    login_id, is_login = otherutils.get_login(token_info)
    data_list, is_objectid, is_error, resp = otherutils.get_data_list(id, login_id, is_login, coll_contribution)

    if is_error:
        return resp

    contribution_admins = data_list[0]['contributionAdmins']

    # check if the logged in user's login is included in contribution admin list
    is_admin_user = otherutils.check_login_admin(token_info["login"], contribution_admins)
    if not is_admin_user:
        msg = {
            "reason": "Contribution admin list must contain logged in user",
            "error": "Bad Request: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Contribution", "POST", msg)
        logging.error("Contribution POST " + json.dumps(msg_json))
        return rs_handlers.bad_request(msg_json)

    if (is_objectid):
        coll_contribution.delete_one({cfg.FIELD_OBJECTID: ObjectId(id)})
        msg = {"id": str(id)}
        msg_json = jsonutils.create_log_json("Contribution", "DELETE", msg)
        logging.info("Contribution DELETE " + json.dumps(msg_json))
        return rs_handlers.entry_deleted('ID', id)

    # ToDo: use following line to delete using the other field than ObjectId
    # try:
    #     coll_contribution.delete_one({fld: id})
    #     msg = {fld: str(id)}
    #     msg_json = jsonutils.create_log_json("Contribution", "DELETE", msg)
    #     logging.info("DELETE " + json.dumps(msg_json))
    #     return rs_handlers.entry_deleted('name', id)
    # except:
    #     msg = {
    #         "reason": "Failed to delete. The dataset does not exist: " + str(id),
    #         "error": "Not Found: " + request.url,
    #     }
    #     msg_json = jsonutils.create_log_json("Contribution", "DELETE", msg)
    #     logging.error("DELETE " + json.dumps(msg_json))
    #     return rs_handlers.not_found(msg_json)

def allcapabilitiessearch(token_info=None, name=None):
    query = dict()
    is_list = False

    login_id, is_login = otherutils.get_login(token_info)

    query = query_params.format_query_status_login(query, login_id, is_login)

    if name is None:
        is_list = True

    if is_list:
        out_json = mongoutils.get_result(coll_contribution, query)
    else:
        try:
            query = query_params.format_query_capability(name, query)
        except Exception as ex:
            msg = {
                "reason": "The query is wrong or bad argument",
                "error": "Bad Request: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Capability", "SEARCH", msg)
            logging.error("Capability SEARCH " + json.dumps(msg_json))
            return rs_handlers.bad_request(msg_json)

        try:
            out_json = mongoutils.get_result(coll_contribution, query)
        except Exception as ex:
            msg = {
                "reason": "The query is wrong or bad argument",
                "error": "Bad Request: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Capability", "SEARCH", msg)
            logging.error("Capability SEARCH " + json.dumps(msg_json))
            return rs_handlers.bad_request(msg_json)

    return_json = []
    if out_json is None:
        return_json = []
    else:
        if is_list:  # list all
            if isinstance(out_json, list):
                for in_json in out_json:
                    contribution_id = in_json["id"]
                    if in_json['capabilities'] is not None:
                        for capability in in_json['capabilities']:
                            capability["contributionId"] = contribution_id
                            return_json.append(capability)
            else:
                contribution_id = out_json["id"]
                capability = out_json['capabilities']
                capability["contributionId"] = contribution_id
                return_json.append(capability)
        else:   # extract out capabilities with the given name
            if isinstance(out_json, list):
                for tmp_json in out_json:
                    capabilities_json = tmp_json["capabilities"]
                    contribution_id = tmp_json["id"]
                    # TODO this is the case of only 1 args that is name.
                    #  If there are more args this should be updated
                    for tmp_capability_json in capabilities_json:
                        capability_json = None
                        if tmp_capability_json["name"] == name:
                            capability_json = tmp_capability_json
                            capability_json["contributionId"] = contribution_id
                            return_json.append(capability_json)
            else:
                capabilities_json = out_json["capabilities"]
                contribution_id = out_json["id"]
                # TODO this is the case of only 1 args that is name.
                #  If there are more args this should be updated
                for tmp_capability_json in capabilities_json:
                    capability_json = None
                    if tmp_capability_json["name"] == name:
                        capability_json = tmp_capability_json
                        capability_json["contributionId"] = contribution_id
                        return_json.append(capability_json)
    if is_list:
        msg = {
            "GET": "Capabilities list"
        }
        msg_json = jsonutils.create_log_json("Capabilities", "GET", msg)
        logging.info("Capabilities GET " + json.dumps(msg_json))
    else:
        msg = {
            "search": "Capability search performed with " + str(name)
        }
        msg_json = jsonutils.create_log_json("Capability", "SEARCH", msg)
        logging.info("Capability SEARCH " + json.dumps(msg_json))

    return return_json

def capabilities_search(token_info=None, id=None):
    login_id, is_login = otherutils.get_login(token_info)

    contribution_dataset, status_code = mongoutils.get_contribution_dataset_from_objectid(
        coll_contribution, id, login_id, is_login)
    if status_code == '200':
        if contribution_dataset is not None:
            capability_dataset = contribution_dataset.get_capabilities()
        else:
            msg = {
                "reason": "There is no contribution dataset with given id, "
                          "or you don't have privilege to view this: " + str(id),
                "error": "Not Authorized: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Capability", "SEARCH", msg)
            logging.error("Capability SEARCH " + json.dumps(msg_json))
            return rs_handlers.not_authorized(msg_json)
    else:
        if status_code == "401":
            msg = {
                "reason": "Not authorized to view the contribution dataset with given id: " + str(id),
                "error": "Not Authorized: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Capability", "SEARCH", msg)
            logging.error("Capability SEARCH " + json.dumps(msg_json))
            return rs_handlers.not_authorized(msg_json)
        elif status_code == '404':
            msg = {
                "reason": "There is no contribution dataset with given id: " + str(id),
                "error": "Not Found: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Capability", "SEARCH", msg)
            logging.error("Capability SEARCH " + json.dumps(msg_json))
            return rs_handlers.not_found(msg_json)
        else:
            msg = {
                "reason": "The query was not successfully performed: " + str(id),
                "error": "Bad Request: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Capability", "SEARCH", msg)
            logging.error("Capability SEARCH " + json.dumps(msg_json))
            return rs_handlers.bad_request(msg_json)

    if capability_dataset is None:
        msg = {
            "reason": "There is no capability with given contribution id: " + str(id),
            "error": "Not Found: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Capability", "GET", msg)
        logging.error("Capability SEARCH " + json.dumps(msg_json))
        return rs_handlers.not_found(msg_json)

    msg = {
        "search": "Capability data in the contirubion dataset with given id : " + str(id)
    }
    msg_json = jsonutils.create_log_json("Capability", "GET", msg)
    logging.info("Capability GET " + json.dumps(msg))

    return capability_dataset

def alltalentssearch(token_info=None, name=None):
    query = dict()
    is_list = False

    login_id, is_login = otherutils.get_login(token_info)

    query = query_params.format_query_status_login(query, login_id, is_login)

    if name is None:
        is_list = True

    if is_list:
        out_json = mongoutils.get_result(coll_contribution, query)
    else:
        try:
            query = query_params.format_query_talent(name, query)
        except Exception as ex:
            msg = {
                "reason": "The query is wrong or bad argument",
                "error": "Bad Request: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Talent", "SEARCH", msg)
            logging.error("Talent SEARCH " + json.dumps(msg_json))
            return rs_handlers.bad_request(msg_json)

        try:
            out_json = mongoutils.get_result(coll_contribution, query)
        except Exception as ex:
            msg = {
                "reason": "The query is wrong or bad argument",
                "error": "Bad Request: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Talent", "SEARCH", msg)
            logging.error("Talent SEARCH " + json.dumps(msg_json))
            return rs_handlers.bad_request(msg_json)

    return_json = []
    if out_json is None:
        return_json = []
    else:
        if is_list:  # list all
            if isinstance(out_json, list):
                for in_json in out_json:
                    contribution_id = in_json["id"]
                    if in_json['talents'] is not None:
                        for talent in in_json['talents']:
                            talent["contributionId"] = contribution_id
                            return_json.append(talent)
            else:
                contribution_id = out_json["id"]
                talent = out_json['talents']
                talent["contributionId"] = contribution_id
                return_json.append(talent)
        else:   # extract out talent with the given name
            if isinstance(out_json, list):
                for tmp_json in out_json:
                    contribution_id = tmp_json["id"]
                    talents_json = tmp_json["talents"]
                    # TODO this is the case of only 1 args that is name.
                    #  If there are more args this should be updated
                    for tmp_talent_json in talents_json:
                        talent_json = None
                        if tmp_talent_json["name"] == name:
                            talent_json = tmp_talent_json
                            talent_json["contributionId"] = contribution_id
                            return_json.append(talent_json)
            else:
                talents_json = out_json["talents"]
                contribution_id = out_json["id"]
                # TODO this is the case of only 1 args that is name.
                #  If there are more args this should be updated
                for tmp_talent_json in talents_json:
                    talent_json = None
                    if tmp_talent_json["name"] == name:
                        talent_json = tmp_talent_json
                        talent_json["contributionId"] = contribution_id
                        return_json.append(talent_json)
    if is_list:
        msg = {
            "GET": "Talent list"
        }
        msg_json = jsonutils.create_log_json("Talent", "GET", msg)
        logging.info("Talent GET " + json.dumps(msg_json))
    else:
        msg = {
            "search": "Talent search performed with " + str(name)
        }
        msg_json = jsonutils.create_log_json("Talent", "SEARCH", msg)
        logging.info("Talent SEARCH " + json.dumps(msg_json))

    return return_json

def talents_search(token_info=None, id=None):
    login_id, is_login = otherutils.get_login(token_info)

    contribution_dataset, status_code = mongoutils.get_contribution_dataset_from_objectid(
        coll_contribution, id, login_id, is_login)

    if status_code == '200':
        if contribution_dataset is not None:
            talent_dataset = contribution_dataset.get_talents()
        else:
            msg = {
                "reason": "There is no contribution dataset with given id, "
                          "or you don't have privilege to view this: " + str(id),
                "error": "Not Authorized: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Talent", "SEARCH", msg)
            logging.error("Talent SEARCH " + json.dumps(msg_json))
            return rs_handlers.not_authorized(msg_json)
    else:
        if status_code == "401":
            msg = {
                "reason": "Not authorized to view the contribution dataset with given id: " + str(id),
                "error": "Not Authorized: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Talent", "SEARCH", msg)
            logging.error("Talent SEARCH " + json.dumps(msg_json))
            return rs_handlers.not_authorized(msg_json)
        elif status_code == '404':
            msg = {
                "reason": "There is no contribution dataset with given id: " + str(id),
                "error": "Not Found: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Talent", "SEARCH", msg)
            logging.error("Talent SEARCH " + json.dumps(msg_json))
            return rs_handlers.not_found(msg_json)
        else:
            msg = {
                "reason": "The query was not successfully performed: " + str(id),
                "error": "Bad Request: " + request.url,
            }
            msg_json = jsonutils.create_log_json("Talent", "SEARCH", msg)
            logging.error("Talent SEARCH " + json.dumps(msg_json))
            return rs_handlers.bad_request(msg_json)

    if talent_dataset is None:
        msg = {
            "reason": "There is no Talent with given contribution id: " + str(id),
            "error": "Not Found: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Talent", "GET", msg)
        logging.error("Talent SEARCH " + json.dumps(msg_json))
        return rs_handlers.not_found(msg_json)

    msg = {
        "search": "Talent data in the contirubion dataset with given id : " + str(id)
    }
    msg_json = jsonutils.create_log_json("Talent", "GET", msg)
    logging.info("Talent GET " + json.dumps(msg))

    return talent_dataset

def capabilities_get(token_info=None, id=None, capability_id=None):
    capability_datasets = capabilities_search(token_info, id)

    # when the capablity_datasets is an error response
    if isinstance(capability_datasets, wrappers.Response):
        return capability_datasets

    # otherwise it means that the capability_datasets contains the correct content.

    # search capability that is the correct id
    capability_index = 0
    capability = None

    # there shouldn't be empty list of capability_datasets
    # since it has to be filtered in capabilities_search() already
    for capability_dataset in capability_datasets:
        # this will make an error if there is no id field in capability dataset
        # however, this shouldn't be happen because it is required in connexion
        if capability_dataset["id"] == capability_id:
            capability = capability_dataset
            capability_index += 1

    if capability_index > 1:
        msg = {
            "reason": "There is more than one Capabilities with given capability id: "
                      + str(capability_id),
            "error": "Bad Request: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Capability", "GET", msg)
        logging.error("Capability GET " + json.dumps(msg_json))
        return rs_handlers.bad_request(msg_json)
    elif capability_index == 0:
        msg = {
            "reason": "There is no Capability with given capability id: "
                      + str(capability_id),
            "error": "Not Found: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Capability", "GET", msg)
        logging.error("Capability GET " + json.dumps(msg_json))
        return rs_handlers.not_found(msg_json)
    else:
        return capability

def talents_get(token_info=None, id=None, talent_id=None):
    talent_datasets = talents_search(token_info, id)

    # when the capablity_datasets is an error response
    if isinstance(talent_datasets, wrappers.Response):
        return talent_datasets

    # otherwise it means that the talent_datasets contains the correct content.

    # search talent that is the correct id
    talent_index = 0
    talent = None

    # there shouldn't be empty list of talent_datasets
    # since it has to be filtered in talents_search() already
    for talent_dataset in talent_datasets:
        # this will make an error if there is no id field in talent dataset
        # however, this shouldn't be happen because it is required in connexion
        if talent_dataset["id"] == talent_id:
            talent = talent_dataset
            talent_index += 1

    if talent_index > 1:
        msg = {
            "reason": "There is more than one Capabilities with given talent id: "
                      + str(talent_id),
            "error": "Bad Request: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Talent", "GET", msg)
        logging.error("Talent GET " + json.dumps(msg_json))
        return rs_handlers.bad_request(msg_json)
    elif talent_index == 0:
        msg = {
            "reason": "There is no Capability with given capability id: "
                      + str(talent_id),
            "error": "Not Found: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Capability", "GET", msg)
        logging.error("Capability GET " + json.dumps(msg_json))
        return rs_handlers.not_found(msg_json)
    else:
        return talent

def ok_search():
    return rs_handlers.return_200("okay")

def admin_reviewers_post(token_info):
    # this is for adding reviewers to the database
    # only superuser can add the reviewer
    
    # check if the logged in user is in the administrator
    is_admin = adminutils.check_if_superuser(token_info["login"])

    if not is_admin:
        msg = {
            "reason": "The logged in user should be a superuser",
            "error": "Not Authorized: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Contribution Admin ", "GET", msg)
        logging.error("Contribution Admin GET " + json.dumps(msg_json))
        return rs_handlers.not_authorized(msg_json)

    in_json = request.get_json()
    name = in_json["name"]
    username = in_json["githubUsername"]

    # check if the dataset is existing with given github username
    dataset = mongoutils.get_dataset_from_field(coll_reviewer, "githubUsername", username)
    if dataset is not None:
        msg = {
            "reason": "Github Username in input json already exists in the database: " + str(username),
            "error": "Bad Request: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Contribution Admin", "POST", msg)
        logging.error("Contribution Admin POST " + json.dumps(msg_json))
        return rs_handlers.bad_request(msg)

    currenttime = datetime.datetime.now()
    currenttime = currenttime.strftime("%Y/%m/%dT%H:%M:%S")
    reviewer_dataset = Reviewer('')
    reviewer_dataset, restjson = datasetutils.update_reviwer_dataset_from_json(reviewer_dataset, in_json)
    reviewer_dataset.set_date_created(currenttime)

    dataset, id = mongoutils.insert_dataset_to_mongodb(coll_reviewer, reviewer_dataset)

    msg = "new reviewer has been added: " + str(username)
    msg_json = jsonutils.create_log_json("Contribution Admin ", "POST", {"id": str(id)})
    logging.info("Contribution Admin POST " + json.dumps(msg_json))

    reviewer_id = str(dataset['_id'])

    return rs_handlers.return_id(msg, 'id', reviewer_id)

def admin_reviewers_search(token_info):
    reviewers = []

    # check if the logged in user is a administrator
    is_admin = adminutils.check_if_superuser(token_info["login"])

    if not is_admin:
        msg = {
            "reason": "The logged-in user should be an administrator",
            "error": "Not Authorized: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Contribution Admin ", "GET", msg)
        logging.error("Contribution Admin GET " + json.dumps(msg_json))
        return rs_handlers.not_authorized(msg_json)

    list_reviewers = mongoutils.list_reviewers()

    if list_reviewers is not None:
        reviewers = list_reviewers

    return reviewers

def admin_reviewers_delete(token_info, id):
    # check if the logged in user is in the reviewers db
    is_reviewer = adminutils.check_if_superuser(token_info["login"])

    if not is_reviewer:
        msg = {
            "reason": "The logged0in user should be an administrator",
            "error": "Not Authorized: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Contribution Admin ", "GET", msg)
        logging.error("Contribution Admin GET " + json.dumps(msg_json))
        return rs_handlers.not_authorized(msg_json)

    resp = coll_reviewer.delete_one({cfg.FIELD_OBJECTID: ObjectId(id)})
    if resp.deleted_count > 0:
        msg = {"id": str(id)}
        msg_json = jsonutils.create_log_json("Contribution Admin ", "DELETE", msg)
        logging.info("Contribution Admin DELETE " + json.dumps(msg_json))
        return rs_handlers.entry_deleted('ID', id)
    else:
        msg = {
            "reason": "There is no reviewer with given id: " + str(id),
            "error": "Not Found: " + request.url,
        }
        msg_json = jsonutils.create_log_json("Contribution Admin ", "DELETE", msg)
        logging.info("Contribution Admin DELETE " + json.dumps(msg_json))
        return rs_handlers.not_found(msg_json)
