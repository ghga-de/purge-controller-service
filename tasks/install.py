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

"""Installation tasks."""

from invoke import Context, call, task


@task
def install(context: Context, all_extras: bool = False, edit_mode: bool = False):
    """Install the main package."""

    args = " -e " if edit_mode else ""
    extras = "[all]" if all_extras else ""
    context.run(f"pip install {args} .{extras}")


@task(call(install, all_extras=True, edit_mode=True))
def dev_install(context: Context):
    """Install the main package along with development dependencies."""

    context.run("pip install -r requirements-dev.txt")
