# Install script for directory: /Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc

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

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_conj_multiply_delay_ccc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_deinterleaver_ff.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_despread_cc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_despread_simple_cc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_diff_coding_bb.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_diff_decoding_ff.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_filter_crc_packets.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_fragmentation.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_interleaver_bb.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_normalize_ff.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_preamble_demod_cc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_preamble_detector_cc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_preamble_search_cc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_snr_estimator.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_spreading_bb.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_dsss_tx_gain_sweep.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_SFD_corr_bb.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_corr_est_cc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_correlator_ccc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_deinterleaver.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_demodulator_cb.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_despreading_bb.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_detector_cb.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_detector_cc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_freq_offset_est_cc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_interleaver.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_modulator_fc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_normalize_fcc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_phr_parser.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_phr_pdu_demux.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_spreading_bb.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_synchronizer_cc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_time_synchronizer_cc.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_whitening_bb.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_fsk_lecim_zero_depadding_bb.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_message_counter.xml"
    "/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/grc/lpwan_sync.xml"
    )
endif()

