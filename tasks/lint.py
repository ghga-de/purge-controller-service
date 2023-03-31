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

"""Linting tasks."""

from invoke import Context, task

from .install import dev_install
from .utils import REPO_ROOT_DIR, main_src_dir


@task(dev_install)
def pylint(context: Context):
    """Run all tests."""

    context.run(f'pylint "{main_src_dir}"')


@task(dev_install)
def flake8(context: Context):
    """Run all tests."""

    context.run(f'flake8 --config "{REPO_ROOT_DIR / ".flake8"}"')


@task(dev_install)
def mypy(context: Context):
    """Run all tests."""

    context.run("mypy .")


@task(pylint, flake8, mypy)
def all_(context: Context):
    """Run all tests."""

    context.run("mypy .")
