# Copyright 2008-2011 Nokia Networks
# Copyright 2011-2016 Ryan Tomac, Ed Manlove and contributors
# Copyright 2016-     Robot Framework Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class SeleniumLibraryException(Exception):
    ROBOT_SUPPRESS_NAME = True


class ElementNotFound(SeleniumLibraryException):
    pass


class WindowNotFound(SeleniumLibraryException):
    pass


class CookieNotFound(SeleniumLibraryException):
    pass


class NoOpenBrowser(SeleniumLibraryException):
    pass


class PluginError(SeleniumLibraryException):
    pass


class UnkownExpectedCondition(SeleniumLibraryException):
    pass