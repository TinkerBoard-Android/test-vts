#
# Copyright (C) 2017 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from vts.utils.python.android import api


def IsVndkRuntimeEnforced(dut):
    """Returns whether VNDK runtime should be enabled on the device.

    VNDK runtime is optional in O-MR1 (API 27); enforced after O-MR1. If it is
    enabled, the device has the property of vndk_version.
    The usage of this function is to decide whether to skip VNDK test cases.

    Args:
        dut: The AndroidDevice under test.

    Returns:
        A boolean, whether VNDK runtime should be enabled.
    """
    return bool(int(dut.first_api_level) > api.PLATFORM_API_LEVEL_O_MR1 or
                dut.vndk_version)


def FormatVndkPath(pattern, bitness, version=""):
    """Formats a VNDK path.

    Args:
        pattern: The path pattern containing {LIB} and {VER}.
        bitness: A string or an integer, 32 or 64.
        version: A string, the VNDK version.

    Returns:
        A string, the formatted path.
    """
    return pattern.format(
        LIB=("lib64" if str(bitness) == "64" else "lib"),
        VER=("-" + version if version and version != "current" else ""))


def GetVndkCoreDirectory(bitness, version):
    """Returns the path to VNDK-core directory on device.

    Args:
        bitness: A string or an integer, 32 or 64.
        version: A string, the VNDK version.

    Returns:
        A string, the path to VNDK-core directory.
    """
    return FormatVndkPath("/system/{LIB}/vndk{VER}", bitness, version)


def GetVndkSpDirectory(bitness, version):
    """Returns the path to VNDK-SP directory on device.

    Args:
        bitness: A string or an integer, 32 or 64.
        version: A string, the VNDK version.

    Returns:
        A string, the path to VNDK-SP directory.
    """
    return FormatVndkPath("/system/{LIB}/vndk-sp{VER}", bitness, version)


def GetVndkSpExtDirectories(bitness):
    """Returns the paths to VNDK-SP extension directories on device.

    Args:
        bitness: A string or an integer, 32 or 64.

    Returns:
        A list of strings, the paths to VNDK-SP extension directories.
    """
    return [FormatVndkPath("/odm/{LIB}/vndk-sp", bitness),
            FormatVndkPath("/vendor/{LIB}/vndk-sp", bitness)]
