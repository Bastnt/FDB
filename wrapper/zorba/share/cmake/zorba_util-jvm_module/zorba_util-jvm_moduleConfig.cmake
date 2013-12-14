# Copyright 2006-2010 The FLWOR Foundation.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

IF (WIN32)
  SET (PATH_SEP ",")
ELSE (WIN32)
  SET (PATH_SEP ":")
ENDIF (WIN32)

# Probably should have separate URI and LIB paths here someday; will
# require testdriver to accept --uri-path and --lib-path args
# Note that this path is meaningless if the module is installed; see
# bug 966999.
SET (DEPENDENCY_MODULE_PATH 
  "${DEPENDENCY_MODULE_PATH}${PATH_SEP}D:/ZORBA/release/3.0/zorba/build/zorba_modules/zorba_util-jvm_module/URI_PATH/${PATH_SEP}${DEPENDENCY_LIB_PATH}${PATH_SEP}D:/ZORBA/release/3.0/zorba/build/zorba_modules/zorba_util-jvm_module/LIB_PATH/")

# Dynamic libraries created by this project to link against
SET (zorba_util-jvm_module_LIBRARIES D:/ZORBA/release/3.0/zorba/build/dist/lib/util-jvm.dll )

# Include directories exported by this project
SET (zorba_util-jvm_module_INCLUDE_DIRS D:/ZORBA/release/3.0/zorba/build/dist/include)

# Offer a "use file" to the user of this module. For most module
# packages, this is unnecessary. However it can be utilized by
# advanced packages which wish to, for example, export a C++ header
# file to dependent packages. As above, note that this currently is
# non-functional if this module package is installed; this will only
# work from a project build directory.
SET (zorba_util-jvm_module_USE_FILE "D:/ZORBA/release/3.0/zorba/build/dist/share/cmake/zorba_util-jvm_module/UtilJavaUse.cmake")
