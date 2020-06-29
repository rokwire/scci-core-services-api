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

import re

from connexion import Resolver


class RokwireResolver(Resolver):
    """
    Resolves endpoint functions using REST semantics (unless overridden by specifying operationId)
    """

    def __init__(self, default_module_name, collection_endpoint_name='search'):
        """
        :param default_module_name: Default module name for operations
        :type default_module_name: str
        """
        Resolver.__init__(self)
        self.default_module_name = default_module_name
        self.collection_endpoint_name = collection_endpoint_name

    def resolve_operation_id(self, operation):
        """
        Resolves the operationId using REST semantics unless explicitly configured in the spec

        :type operation: connexion.operations.AbstractOperation
        """
        if operation.operation_id:
            return Resolver.resolve_operation_id(self, operation)

        return self.resolve_operation_id_using_rest_semantics(operation)

    def resolve_operation_id_using_rest_semantics(self, operation):
        """
        Resolves the operationId using REST semantics

        :type operation: connexion.operations.AbstractOperation
        """

        elements = operation.path.split('/')[1:]

        # prefix part of the function name (i.e. file on disk)
        if operation.router_controller:
            name = operation.router_controller
        else:
            name = self.default_module_name

            # append all other paths using _ names, except parameters
            for path in elements:
                if '{' not in path:
                    if name.count('.') < 2:
                        name += '.' + path.replace('-', '_')
                    else:
                        name += '_' + path.replace('-', '_')
                # TODO if there is a conflict in naming convention,
                #  following lines could be helpful
                # else:
                #     if name.count('.') < 2:
                #         name += '.var'
                #     else:
                #         name += '_var'

        # append method
        method = operation.method.lower()
        if method == 'get' and '{' not in elements[-1]:
            method = self.collection_endpoint_name
        print(name + "_" + method)

        if name.count('.') < 2:
            return name + '.' + method
        else:
            return name + '-' + method
