cmake_minimum_required(VERSION 3.22.0)

project(
    {{project_name}}
    VERSION 0.1.0
    DESCRIPTION "{{description}}"
    HOMEPAGE_URL "{{url}}"
    LANGUAGES CXX
)

{% set PREFIX = project_short_name | uppersnakecase %}
cmake_path(SET {{PREFIX}}_PROJECT_DIR ${CMAKE_CURRENT_SOURCE_DIR})
cmake_path(SET {{PREFIX}}_BUILD_DIR ${CMAKE_CURRENT_BINARY_DIR})
cmake_path(APPEND {{PREFIX}}_PROJECT_DIR "{{source_folder}}" OUTPUT_VARIABLE {{PREFIX}}_SOURCE_DIR)
cmake_path(APPEND {{PREFIX}}_PROJECT_DIR "{{bin_folder}}" OUTPUT_VARIABLE {{PREFIX}}_BIN_DIR)

option({{PREFIX}}_USE_CONAN "Use conan package manager. For more details https://conan.io/" ON)
option({{PREFIX}}_AUTODETECT_EXECUTABLES "Consider all Main*.cpp files as executables and install them to {{'${' + PREFIX}}_BIN_DIR}." ON)

file(GLOB_RECURSE {{PREFIX}}_LIB_HEADERS CONFIGURE_DEPENDS "{{'${' + PREFIX}}_SOURCE_DIR}/*.h" "{{'${' + PREFIX}}_SOURCE_DIR}/*.hpp")
file(GLOB_RECURSE {{PREFIX}}_LIB_SOURCES CONFIGURE_DEPENDS "{{'${' + PREFIX}}_SOURCE_DIR}/*.cpp")
list(FILTER {{PREFIX}}_LIB_SOURCES EXCLUDE REGEX "Main.*.cpp")

# {{project_short_name}}lib target can not be created if there are not *.h and *.cpp files in ./srs/{{project_short_name}} folder.
# This is why dummy files are created.
if(NOT {{PREFIX}}_LIB_HEADERS)
    cmake_path(APPEND_STRING {{PREFIX}}_BUILD_DIR "/__dummy_file.h" OUTPUT_VARIABLE {{PREFIX}}_DUMMY_HEADER_FILE)
    file(WRITE {{'${' + PREFIX}}_DUMMY_HEADER_FILE} "")
    list(APPEND {{PREFIX}}_LIB_HEADERS {{'${' + PREFIX}}_DUMMY_HEADER_FILE})
endif()

if(NOT {{PREFIX}}_LIB_SOURCES)
    cmake_path(APPEND_STRING {{PREFIX}}_BUILD_DIR "/__dummy_file.cpp" OUTPUT_VARIABLE {{PREFIX}}_DUMMY_SOURCE_FILE)
    file(WRITE {{'${' + PREFIX}}_DUMMY_SOURCE_FILE} "")
    list(APPEND {{PREFIX}}_LIB_SOURCES {{'${' + PREFIX}}_DUMMY_SOURCE_FILE})
endif()

add_library({{project_short_name}}lib {{'${' + PREFIX}}_LIB_HEADERS} {{'${' + PREFIX}}_LIB_SOURCES})
target_include_directories({{project_short_name}}lib PUBLIC {{'${' + PREFIX}}_SOURCE_DIR})


if({{PREFIX}}_USE_CONAN)
    cmake_path(APPEND_STRING {{PREFIX}}_BUILD_DIR "/conanbuildinfo.cmake" OUTPUT_VARIABLE {{PREFIX}}_CONAN_BUILD_INFO_FILE)

    if(NOT EXISTS {{'${' + PREFIX}}_CONAN_BUILD_INFO_FILE})
        message(FATAL_ERROR "Conan's required dependencies are not built. Try to run:\nconan install . -if {{'${' + PREFIX}}_BUILD_DIR}")
    endif()

    include({{'${' + PREFIX}}_CONAN_BUILD_INFO_FILE})
    conan_basic_setup()

    list(APPEND {{PREFIX}}_EXTRA_LIBS ${CONAN_LIBS})

endif()


if({{PREFIX}}_AUTODETECT_EXECUTABLES)
    file(GLOB_RECURSE {{PREFIX}}_EXECUTABLES "{{'${' + PREFIX}}_SOURCE_DIR}/Main*.cpp")
    message("Detect executable files: {{'${' + PREFIX}}_EXECUTABLES}")

    foreach(executable_file {{'${' + PREFIX}}_EXECUTABLES})
        string(REGEX MATCH ".*/Main(.+)\.cpp" _ ${executable_file})
        string(TOLOWER ${CMAKE_MATCH_1} executable_name)

        add_executable(${executable_name} ${executable_file})
        target_link_libraries(${executable_name} PRIVATE {{project_short_name}}lib {{'${' + PREFIX}}_EXTRA_LIBS})

        list(APPEND executables ${executable_name})
    endforeach()

    message("Create executables: ${executables}")

    install(
        TARGETS ${executables}
        DESTINATION {{'${' + PREFIX}}_BIN_DIR}
    )

endif()
