cmake_minimum_required(VERSION 3.1)
project(quant LANGUAGES CXX C)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Use the project root to find includes
include_directories(${PROJECT_SOURCE_DIR})

add_executable(hello-repeater run.cc)
install(TARGETS hello-repeater DESTINATION bin)
