cmake_minimum_required(VERSION 3.0.0)
project(catch2-test VERSION 0.1.0 LANGUAGES C CXX)

include(CTest)
enable_testing()

Include(FetchContent)

FetchContent_Declare(
  Catch2
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git
  GIT_TAG        v3.4.0 # or a later release
)

FetchContent_MakeAvailable(Catch2)

add_executable(catch2-test ./src/main.cpp ./src/testfuncs.cpp)
target_link_libraries(catch2-test PRIVATE Catch2::Catch2)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
