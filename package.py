name = "jpeg"

version = "9.c"

authors = [
    "Independent JPEG Group"
]

description = \
    """
    libjpeg is a free library with functions for handling the JPEG image data format. It implements a JPEG codec
    alongside various utilities for handling JPEG data.
    """

requires = [
    "cmake-3+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "cjpeg",
    "djpeg",
    "jpegtran",
    "rdjpgcom",
    "wrjpgcom"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "jpeg-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    # Helper environment variables.
    env.JPEG_BINARY_PATH.set("{root}/bin")
    env.JPEG_INCLUDE_PATH.set("{root}/include")
    env.JPEG_LIBRARY_PATH.set("{root}/lib")
