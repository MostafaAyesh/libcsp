cmake_minimum_required(VERSION 3.15)

project(csp VERSION 1.5 LANGUAGES C)

include(cmake/options.cmake)
include(CheckSymbolExists)

# Setup CFlags
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Os -Wall -g -std=gnu99")

# LibCSP Include Dirs
set(CSP_INCLUDES
    "include"
    "src"
)

# Add default files
file(GLOB CSP_SRCS "src/*.c" "src/interfaces/csp_if_lo.c" "src/transport/csp_udp.c")

# OS sources
if(CSP_POSIX)
    file(GLOB OS_SRCS "src/arch/posix/*.c")
    list(APPEND CSP_SRCS ${OS_SRCS})
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -pthread -lrt -lutil")
elseif(CSP_FREERTOS)
    file(GLOB OS_SRCS "src/arch/freertos/*.c")
    list(APPEND CSP_SRCS ${OS_SRCS})
elseif(CSP_WINDOWS)
    file(GLOB OS_SRCS "src/arch/windows/*.c")
    list(APPEND CSP_SRCS ${OS_SRCS})
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -D_WIN32_WINNT=0x0600")
elseif(CSP_MACOSX)
    file(GLOB OS_SRCS "src/arch/macosx/*.c")
    list(APPEND CSP_SRCS ${OS_SRCS})
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -pthread")
endif()

# Add CAN driver
if(SOCKETCAN_DRIVER)
    list(APPEND CSP_SRCS "src/drivers/can/can_socketcan.c")
endif()

# Add USART driver
if(USART_DRIVER MATCHES "^(linux|windows)$" )
    list(APPEND CSP_SRCS "src/drivers/usart/usart_${USART_DRIVER}.c")    
endif()

# Interfaces
if(ENABLE_IF_CAN)
    list(APPEND CSP_SRCS "src/interfaces/csp_if_can.c")
endif()
if(ENABLE_IF_I2C)
    list(APPEND CSP_SRCS "src/interfaces/csp_if_i2c.c")
endif()
if(ENABLE_IF_KISS)
    list(APPEND CSP_SRCS "src/interfaces/csp_if_kiss.c")
endif()
# TODO: Add ZMQHub
if(ENABLE_IF_ZMQHUB)
endif()

# CRC32
if(CSP_USE_CRC32)
    list(APPEND CSP_SRCS "src/csp_crc32.c")
endif()

# Crypto sources
if(CSP_USE_HMAC)
    list(APPEND CSP_SRCS 
                "src/crypto/csp_hmac.c" 
                "src/crypto/csp_sha1.c")
endif()

if(CSP_USE_XTEA)
    list(APPEND CSP_SRCS 
                "src/crypto/csp_xtea.c" 
                "src/crypto/csp_sha1.c")
endif()

# Rtable sources
if(CSP_RTABLE STREQUAL "STATIC")
    list(APPEND CSP_SRCS
        "src/rtable/csp_rtable_static.c")
elseif(CSP_RTABLE STREQUAL "CIDR")
    list(APPEND CSP_SRCS
        "src/rtable/csp_rtable_cidr.c")
endif()

# Transport sources
if(CSP_USE_RDP)
    list(APPEND CSP_SRCS "src/transport/csp_rdp.c")
endif()

# Remove duplicate sources
list(REMOVE_DUPLICATES CSP_SRCS)

include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CSP_INCLUDES}
    ${USER_INCLUDES}
)

add_library(${PROJECT_NAME} STATIC ${CSP_SRCS})

if(ENABLE_EXAMPLES)
    add_executable(simple examples/simple.c)
    target_link_libraries(simple ${PROJECT_NAME})
    if(ENABLE_IF_KISS)
        add_executable(kiss examples/kiss.c)
        target_link_libraries(kiss ${PROJECT_NAME})
    endif()
    if(CSP_POSIX)
        add_executable(fifo examples/csp_if_fifo.c)
        target_link_libraries(fifo ${PROJECT_NAME})
    endif()
    if(CSP_WINDOWS)
        add_executable(fifo examples/csp_if_fifo_windows.c)
        target_link_libraries(fifo ${PROJECT_NAME})
    endif()
endif()

