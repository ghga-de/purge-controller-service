# Copyright 2021 - 2023 Universität Tübingen, DKFZ, EMBL, and Universität zu Köln
# for the German Human Genome-Phenome Archive (GHGA)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""A collection of http exceptions."""


from ghga_service_commons.httpyexpect.server import HttpCustomExceptionBase


class HttpAuthorizationFailedError(HttpCustomExceptionBase):
    """Raised when bearer token cannot be validated"""

    exception_id = "authorizationFailedError"

    def __init__(self, *, status_code: int = 403):
        """Construct message and init the exception."""
        super().__init__(
            status_code=status_code,
            description="Endpoint file ID did not match file ID announced in work order token.",
            data={},
        )
