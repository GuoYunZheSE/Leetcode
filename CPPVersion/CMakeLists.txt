cmake_minimum_required(VERSION 3.15)
project(CPPVersion)

set(CMAKE_CXX_STANDARD 11)

include_directories(${PROJECT_SOURCE_DIR}/googletest-release-1.10.0/googletest/include/)
add_subdirectory(./googletest-release-1.10.0)
set(3RD_LIBS gtest pthread)
add_executable(
        CPPVersion
        984/984.h 984/984.cpp
        199/199.h 199/199.cpp
        962/962.h
        731/731.h
        441/441.h
        409/409.h
        905/905.h
        345/345.h
        349/349.h
        1110/1110.h
        65/65.h
        1144/1144.h
        1175/1175.h
        20/20.h
        1323/1323.h
        922/922.h
        34/34.h
        1/1.h
        542/542.h
        1010/1010.h
        547/547.h
        1041/1041.h
        605/605.h
        1300/1300.h
        121/121.h
        1014/1014.h
        3/3.h
        1248/1248.h
        583/583.h
        42/42.h
        226/226.h
        206/206.h
        141/141.h
        92/92.h
        448/448.h
        324/324.h
        14/14.h
        179/179.h
        46/46.h
        31/31.h
        1356/1356.h
        1357/1357.h
        1358/1358.h
        47/47.h
        996/996.h
        209/209.h
        862/862.h
        916/916.h
        904/904.h
        1287/1287.h
        1372/1372.h
        189/189.h
        225/225.h 700/700.h 107/107.h
        1491/1491.h 1492/1492.h 1493/1493.h 2/2.h 43/43.h 67/67.h 415/415.h 5/5.h 11/11.h 8/8.h 79/79.h
        239/239.h
        84/84.h
        91/91.h
        101/101.h 110/110.h
        105/105.h
        106/106.h
        122/122.h
        123/123.h
        127/127.h UTILS.h
        131/131.h
        131/131.cpp
        139/139.h
)
target_link_libraries(${PROJECT_NAME} ${3RD_LIBS})
enable_testing()