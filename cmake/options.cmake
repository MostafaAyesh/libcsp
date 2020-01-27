set(LIBCSP_VERSION 1.5)
set(GIT_REV \"1\") # Change this to reflect git rev
include(CMakeDependentOption)

CMAKE_DEPENDENT_OPTION(CSP_POSIX "Build CSP for POSIX" ON "NOT CSP_FREERTOS;NOT CSP_WINDOWS;NOT CSP_MACOSX" OFF)
option(CSP_FREERTOS "Build CSP for FreeRTOS" OFF)
option(CSP_WINDOWS "Build CSP for Windows" OFF)
option(CSP_MACOSX "Build CSP for macOS" OFF)
option(CSP_DEBUG "Enable CSP debugging" ON)
option(CSP_INSTALL "Installs CSP headers and lib" OFF)

option(CSP_USE_RDP "Enable RDP support" OFF)
option(CSP_USE_CRC32 "Enable CRC32 support" OFF)
option(CSP_USE_HMAC "Enable HMAC-SHA1 support" OFF)
option(CSP_USE_XTEA "Enable XTEA support" OFF)
option(CSP_USE_PROMISC "Enable promiscuous mode support" OFF)
option(CSP_USE_QOS "Enable Quality of Service support" OFF)
option(CSP_USE_DEDUP "Enable packet deduplicator" OFF)
option(CSP_USE_INIT_SHUTDOWN "Use init system commands for shutdown/reboot" OFF)

option(ENABLE_IF_CAN "Enable CAN interface" OFF)
option(ENABLE_IF_I2C "Enable I2C interface" OFF)
option(ENABLE_IF_KISS "Enable KISS/RS.232 interface" OFF)
option(ENABLE_IF_ZMQHUB "Enable ZMQHUB interface" OFF)

option(SOCKETCAN_DRIVER "Build SocketCAN driver" OFF)
set(USART_DRIVER "none" CACHE STRING "Build USART driver. [windows, linux, none]")

set(CSP_CONN_MAX 10 CACHE STRING "Set maximum number of concurrent connections")
set(CSP_CONN_QUEUE_LENGTH 100 CACHE STRING "Set maximum number of packets in queue for a connection")
set(CSP_FIFO_INPUT 10 CACHE STRING "Set maximum number of packets to be queued at the input of the router")
set(CSP_MAX_BIND_PORT 31 CACHE STRING "Set maximum bindable port")
set(CSP_RDP_MAX_WINDOW 20 CACHE STRING "Set maximum window size for RDP")
set(CSP_PADDING_BYTES 8 CACHE STRING "Set padding bytes before packet length field")
set(CSP_CONNECTION_SO 0x0000 CACHE STRING "Set outgoing connection socket options, see csp.h for valid values")
set(CSP_BUFFER_ALIGN 0 CACHE STRING "Set buffer alignment")
set(CSP_RTABLE "STATIC" CACHE STRING "Set routing table type")

set(USER_INCLUDES "" CACHE STRING "Add additional include paths. Separate with semicolon")
set(INSTALL_PATH ${CMAKE_CURRENT_BINARY_DIR}/lib CACHE STRING "Add additional include paths. Separate with semicolon")

option(ENABLE_EXAMPLES "Enable examples" OFF)


# Endianness check
include (TestBigEndian)
test_big_endian(IS_BIG_ENDIAN)
if(IS_BIG_ENDIAN)
 message(STATUS "TARGET IS BIG_ENDIAN")
 set(CSP_BIG_ENDIAN ON)
else()
 message(STATUS "TARGET LITTLE_ENDIAN")
 set(CSP_LITTLE_ENDIAN ON)
endif()

configure_file(csp_autoconfig.h.in csp/csp_autoconfig.h @ONLY)
