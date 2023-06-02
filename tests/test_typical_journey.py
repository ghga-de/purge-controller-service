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

"""Tests typical user journeys"""

import json

import pytest
from fastapi import status
from ghga_event_schemas import pydantic_ as event_schemas
from hexkit.providers.akafka.testutils import ExpectedEvent

from tests.fixtures.joint import JointFixture, joint_fixture  # noqa: F401


@pytest.mark.asyncio
async def test_happy_journey(joint_fixture: JointFixture):  # noqa: F811
    """Simulates a typical, successful API journey."""
    file_id = "test_id"

    non_staged_requested_event = event_schemas.FileDeletionRequested(file_id=file_id)
    async with joint_fixture.kafka.expect_events(
        events=[
            ExpectedEvent(
                payload=json.loads(non_staged_requested_event.json()),
                type_=joint_fixture.config.files_to_delete_type,
            )
        ],
        in_topic=joint_fixture.config.files_to_delete_topic,
    ):
        response = await joint_fixture.rest_client.get(f"/files/{file_id}", timeout=5)
    assert response.status_code == status.HTTP_202_ACCEPTED
