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

"""Module hosting the dependency injection container."""

from hexkit.inject import ContainerBase, get_configurator, get_constructor
from hexkit.providers.akafka import KafkaEventPublisher

from pcs.adapters.outbound.event_pub import EventPubTranslator
from pcs.config import Config
from pcs.core.file_deletion import FileDeletion


class Container(ContainerBase):
    """DI Container"""

    config = get_configurator(Config)

    # outbound providers:
    event_pub_provider = get_constructor(KafkaEventPublisher, config=config)

    # outbound translators:
    event_publisher = get_constructor(
        EventPubTranslator, config=config, provider=event_pub_provider
    )

    # domain/core components:
    file_deletion = get_constructor(
        FileDeletion,
        event_publisher=event_publisher,
        config=config,
    )
