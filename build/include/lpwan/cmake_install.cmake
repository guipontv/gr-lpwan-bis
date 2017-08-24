# Install script for directory: /Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "lpwan_devel" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/lpwan/gnuradio/lpwan" TYPE FILE FILES
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_interleaver_bb.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_codes.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_diff_coding_bb.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_spreading_bb.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_deinterleaver_ff.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_diff_decoding_ff.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_despread_simple_cc.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_preamble_demod_cc.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/conj_multiply_delay_ccc.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_preamble_detector_cc.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_despread_cc.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_normalize_ff.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_snr_estimator.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_fragmentation.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/mac_format.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/mac_field.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/mac_field_frame_ctrl.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/mac_field_frag_header.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/mac_field_frag_status.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/mac_field_frame.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/mac_crc.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/mac_field_header_ie.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/mac_field_ie_fscd.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/mac_field_fragment.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/mac_field_frak.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/dsss_filter_crc_packets.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/fsk_lecim_interleaver.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/fsk_lecim_deinterleaver.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/fsk_lecim_phr_pdu_demux.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/fsk_lecim_corr_est_cc.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/fsk_lecim_phr_parser.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/fsk_lecim_normalize_fcc.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/fsk_lecim_synchronizer_cc.h"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/include/lpwan/sync.h"
    )
endif()

