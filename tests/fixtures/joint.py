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
#
"""Join the functionality of all fixtures for API-level integration testing."""

from dataclasses import dataclass
from typing import AsyncGenerator

import httpx
import pytest_asyncio
from ghga_service_commons.api.testing import AsyncTestClient
from hexkit.providers.akafka.testutils import KafkaFixture, kafka_fixture  # noqa: F401

from pcs.config import Config
from pcs.container import Container
from pcs.main import get_configured_container, get_rest_api
from tests.fixtures.config import get_config


@dataclass
class JointFixture:
    """Returned by the `joint_fixture`."""

    config: Config
    container: Container
    rest_client: httpx.AsyncClient
    kafka: KafkaFixture


@pytest_asyncio.fixture
async def joint_fixture(
    kafka_fixture: KafkaFixture,  # noqa: F811
) -> AsyncGenerator[JointFixture, None]:
    """A fixture that embeds all other fixtures for API-level integration testing"""

    config = get_config(
        sources=[
            kafka_fixture.config,
        ]
    )

    # create a DI container instance:translators
    async with get_configured_container(config=config) as container:
        container.wire(
            modules=[
                "dcs.adapters.inbound.fastapi_.routes",
            ]
        )

        api = get_rest_api(config=config)
        # setup an API test client:
        async with AsyncTestClient(app=api) as rest_client:
            yield JointFixture(
                config=config,
                container=container,
                kafka=kafka_fixture,
                rest_client=rest_client,
            )
