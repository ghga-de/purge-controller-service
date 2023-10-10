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

"""Utils to customize openAPI script"""
from typing import Any

from fastapi.openapi.utils import get_openapi

from pcs import __version__
from pcs.config import Config

config = Config()  # type: ignore [call-arg]


def get_openapi_schema(api) -> dict[str, Any]:
    """Generates a custom openapi schema for the service"""
    return get_openapi(
        title="Purge Controller Service",
        version=__version__,
        description="A service exposing an external API to commission file deletions"
        + "from the wholefile backend.",
        servers=[{"url": config.api_root_path}],
        tags=[{"name": "PurgeControllerService"}],
        routes=api.routes,
    )
