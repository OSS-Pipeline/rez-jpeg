CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# We split the jpeg version string in multiple ones.
string(REPLACE "." ";" JPEG_VERSION_LIST ${REZ_BUILD_PROJECT_VERSION})
list(GET JPEG_VERSION_LIST 0 JPEG_VERSION_MAJOR)
list(GET JPEG_VERSION_LIST 1 JPEG_VERSION_MINOR)

# We create a version of jpeg to make it match with the one in the archive name.
set(JPEG_ARCHIVE_VERSION "${JPEG_VERSION_MAJOR}${JPEG_VERSION_MINOR}")

# jpeg
rez_set_archive(
    JPEG_URL jpeg/jpegsrc.v${JPEG_ARCHIVE_VERSION}.tar.gz
    https://www.ijg.org/files/jpegsrc.v${JPEG_ARCHIVE_VERSION}.tar.gz
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/jpeg/${REZ_BUILD_PROJECT_VERSION})
set(BUILD_DIR ${EXTRACT_DIR}/build)

# We configure/build/install jpeg through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_JPEG
    URL ${JPEG_URL}
    PREFIX jpeg
    SOURCE_DIR ${EXTRACT_DIR}
    PATCH_COMMAND ""
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND bash ${CMAKE_SOURCE_DIR}/configure.sh ${EXTRACT_DIR} ${BUILD_DIR}
    BUILD_COMMAND bash ${CMAKE_SOURCE_DIR}/build.sh ${BUILD_DIR}
    INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${BUILD_DIR}
)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] jpeg-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
