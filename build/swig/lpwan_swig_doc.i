
/*
 * This file was automatically generated using swig_doc.py.
 *
 * Any changes to it will be lost next time it is regenerated.
 */




%feature("docstring") gr::lpwan::conj_multiply_delay_ccc "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::conj_multiply_delay_ccc.

To avoid accidental use of raw pointers, lpwan::conj_multiply_delay_ccc's constructor is in a private implementation class. lpwan::conj_multiply_delay_ccc::make is the public interface for creating new instances.

Args:
    delay : "

%feature("docstring") gr::lpwan::conj_multiply_delay_ccc::make "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::conj_multiply_delay_ccc.

To avoid accidental use of raw pointers, lpwan::conj_multiply_delay_ccc's constructor is in a private implementation class. lpwan::conj_multiply_delay_ccc::make is the public interface for creating new instances.

Args:
    delay : "

%feature("docstring") gr::lpwan::dsss_deinterleaver_ff "Deinterleaver block for LECIM DSSS Phy.

Deinterleaves the tagged input stream with soft decision floats. The length has to be 256, 384, or 512. Std. 23.2.4

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_deinterleaver_ff.

Args:
    len_tag : length tag key"

%feature("docstring") gr::lpwan::dsss_deinterleaver_ff::make "Deinterleaver block for LECIM DSSS Phy.

Deinterleaves the tagged input stream with soft decision floats. The length has to be 256, 384, or 512. Std. 23.2.4

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_deinterleaver_ff.

Args:
    len_tag : length tag key"

%feature("docstring") gr::lpwan::dsss_despread_cc "Despreading of already timesynced LECIM DSSS packets.

This block despreads packets marked with a stream tag in the input stream. The tag has to be on the first chip of the payload, with the tag key \"sop\" and an estimation of the frequency offset as float value. It is possible to despread overlapping packets.

The output is a tagged stream with one despreaded payload packet per tagged block.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_despread_cc.

Args:
    sf : gold code spreading factor
    seed : seed of the cold gode generator for the data payload
    preamble_seed : seed of the cold gode generator for the preamble, assumed reset_per_symbol = true
    ovsf_code_index : ovsf code index [0, 2^ovsf_log_sf-1]
    ovsf_log_sf : ovsf spreading factor [0, 8]
    sps : samples per symbol, interpolation factor
    psdu_len : length of the psdu payload (16, 24, 32)
    modulation : OQPSK or BPSK
    chiprate : absolute chiprate, for frequency synchronisation
    reset_per_symbol : reset gold code after each symbol / after sf chips
    dll_active : true if the dll should be used
    dll_delta : sample delay of early late to prompt
    dll_gain : loop gain of dll
    dll_error_reset : single gain multiplier after sample error detection
    dll_cmp : cmp value for dll"

%feature("docstring") gr::lpwan::dsss_despread_cc::make "Despreading of already timesynced LECIM DSSS packets.

This block despreads packets marked with a stream tag in the input stream. The tag has to be on the first chip of the payload, with the tag key \"sop\" and an estimation of the frequency offset as float value. It is possible to despread overlapping packets.

The output is a tagged stream with one despreaded payload packet per tagged block.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_despread_cc.

Args:
    sf : gold code spreading factor
    seed : seed of the cold gode generator for the data payload
    preamble_seed : seed of the cold gode generator for the preamble, assumed reset_per_symbol = true
    ovsf_code_index : ovsf code index [0, 2^ovsf_log_sf-1]
    ovsf_log_sf : ovsf spreading factor [0, 8]
    sps : samples per symbol, interpolation factor
    psdu_len : length of the psdu payload (16, 24, 32)
    modulation : OQPSK or BPSK
    chiprate : absolute chiprate, for frequency synchronisation
    reset_per_symbol : reset gold code after each symbol / after sf chips
    dll_active : true if the dll should be used
    dll_delta : sample delay of early late to prompt
    dll_gain : loop gain of dll
    dll_error_reset : single gain multiplier after sample error detection
    dll_cmp : cmp value for dll"

%feature("docstring") gr::lpwan::dsss_despread_simple_cc "Despreads succeeding LECIM DSSS packets.

This tagged stream block despreads timesynced succeeding spreaded payload data. Useful for simulations.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_despread_simple_cc.

!

Args:
    len_tag : length tag key
    spread_factor : gold code spreading factor
    seed : seed of the cold gode generator for the data payload
    reset_per_symbol : 
    ovsf_code_index : ovsf code index [0, 2^ovsf_log_sf-1]
    ovsf_log2_spread_factor : ovsf spreading factor [0, 8]"

%feature("docstring") gr::lpwan::dsss_despread_simple_cc::make "Despreads succeeding LECIM DSSS packets.

This tagged stream block despreads timesynced succeeding spreaded payload data. Useful for simulations.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_despread_simple_cc.

!

Args:
    len_tag : length tag key
    spread_factor : gold code spreading factor
    seed : seed of the cold gode generator for the data payload
    reset_per_symbol : 
    ovsf_code_index : ovsf code index [0, 2^ovsf_log_sf-1]
    ovsf_log2_spread_factor : ovsf spreading factor [0, 8]"

%feature("docstring") gr::lpwan::dsss_diff_coding_bb "Differential Coding for LECIM DSSS Phy.

This tagged stream block performs differential coding described in Std 23.2.5. Input and output are unpacked bytes.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_diff_coding_bb.

Args:
    len_tag : length tag key"

%feature("docstring") gr::lpwan::dsss_diff_coding_bb::make "Differential Coding for LECIM DSSS Phy.

This tagged stream block performs differential coding described in Std 23.2.5. Input and output are unpacked bytes.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_diff_coding_bb.

Args:
    len_tag : length tag key"

%feature("docstring") gr::lpwan::dsss_diff_decoding_ff "Differential Decoding for LECIM DSSS Phy.

This tagged stream block performs differential decoding described in Std 23.2.5.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_diff_decoding_ff.

Args:
    len_tag : length tag key
    phase_ref : additional phase reference symbol from preamble is in input stream
    shr_len : length of the SHR, not needed if phase_ref == false"

%feature("docstring") gr::lpwan::dsss_diff_decoding_ff::make "Differential Decoding for LECIM DSSS Phy.

This tagged stream block performs differential decoding described in Std 23.2.5.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_diff_decoding_ff.

Args:
    len_tag : length tag key
    phase_ref : additional phase reference symbol from preamble is in input stream
    shr_len : length of the SHR, not needed if phase_ref == false"

%feature("docstring") gr::lpwan::dsss_filter_crc_packets "Filters out packets with unsuccessful CRC check.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_filter_crc_packets."

%feature("docstring") gr::lpwan::dsss_filter_crc_packets::make "Filters out packets with unsuccessful CRC check.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_filter_crc_packets."

%feature("docstring") gr::lpwan::dsss_fragmentation "Fragmentation Layer Std. 23.3.

Takes a MAC frame and divides them into smaller fragments, which are tranmitted and acked as a seperate unit.

For now the destination address is fixed and not extracted from the MAC packet. This could be relevant in a testbed with more than two participants, where the coordinator wants to send to different transceivers. As a workaround it should be possible to use multiple fragmentation blocks.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_fragmentation.

Args:
    psdu_size : in bytes
    frak_policy_tx : only policy 1 supported so far
    frak_tx_timeout_ms : (frak policy 1) timeout for sending a frak and retransmission of fscd packet and fscd-ack
    frak_rx_timeout_ms : for receiving a frak, tx-abortion after timeout
    frame_max_retry : is the maximum number of retries of the same fragment/fraks until abortion
    fics_size_tx : fics = crc length, 2 or 4 bytes
    device_addr_short : address of this device, only short address (16bit) supported
    is_coordinator : true if pan coordinator, (FOR NOW NO EFFEKT )
    psdu_tx_dur : duration of one psdu on air, so fragments don't flood phy queue
    dest_addr_short : address of the destination (coordinator)
    verbose : print some (debug) info"

%feature("docstring") gr::lpwan::dsss_fragmentation::make "Fragmentation Layer Std. 23.3.

Takes a MAC frame and divides them into smaller fragments, which are tranmitted and acked as a seperate unit.

For now the destination address is fixed and not extracted from the MAC packet. This could be relevant in a testbed with more than two participants, where the coordinator wants to send to different transceivers. As a workaround it should be possible to use multiple fragmentation blocks.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_fragmentation.

Args:
    psdu_size : in bytes
    frak_policy_tx : only policy 1 supported so far
    frak_tx_timeout_ms : (frak policy 1) timeout for sending a frak and retransmission of fscd packet and fscd-ack
    frak_rx_timeout_ms : for receiving a frak, tx-abortion after timeout
    frame_max_retry : is the maximum number of retries of the same fragment/fraks until abortion
    fics_size_tx : fics = crc length, 2 or 4 bytes
    device_addr_short : address of this device, only short address (16bit) supported
    is_coordinator : true if pan coordinator, (FOR NOW NO EFFEKT )
    psdu_tx_dur : duration of one psdu on air, so fragments don't flood phy queue
    dest_addr_short : address of the destination (coordinator)
    verbose : print some (debug) info"

%feature("docstring") gr::lpwan::dsss_interleaver_bb "Interleaver block for LECIM DSSS Phy.

Interleaves the tagged input stream (unpacked bytes). The length has to be 256, 384, or 512. Std. 23.2.4

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_interleaver_bb.

Args:
    len_tag : length tag key"

%feature("docstring") gr::lpwan::dsss_interleaver_bb::make "Interleaver block for LECIM DSSS Phy.

Interleaves the tagged input stream (unpacked bytes). The length has to be 256, 384, or 512. Std. 23.2.4

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_interleaver_bb.

Args:
    len_tag : length tag key"

%feature("docstring") gr::lpwan::dsss_normalize_ff "Normalizes one tagged stream block with length N.

out = in / (Sum_N_x(abs(in[x])) / N)

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_normalize_ff.

Args:
    len_tag : length tag key"

%feature("docstring") gr::lpwan::dsss_normalize_ff::make "Normalizes one tagged stream block with length N.

out = in / (Sum_N_x(abs(in[x])) / N)

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_normalize_ff.

Args:
    len_tag : length tag key"

%feature("docstring") gr::lpwan::dsss_preamble_demod_cc "Preamble Demodulation/Correlation.

out[n] = Sum_N_i(in(n+i*sf*sps) * preamble(i))

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_preamble_demod_cc.

Args:
    sf : spreading factor of shr
    sps : samples per symbol
    preamble_length : length of the preamble in bits
    sfd_present : "

%feature("docstring") gr::lpwan::dsss_preamble_demod_cc::make "Preamble Demodulation/Correlation.

out[n] = Sum_N_i(in(n+i*sf*sps) * preamble(i))

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_preamble_demod_cc.

Args:
    sf : spreading factor of shr
    sps : samples per symbol
    preamble_length : length of the preamble in bits
    sfd_present : "

%feature("docstring") gr::lpwan::dsss_preamble_detector_cc "Detects the preamble.

This block is basically a peak detector. It tags the raw rx filtered input data with the detected peak positions (key: \"sop\"), an estimation for the frequency offset and an estimation of the SNR. It works together with the despreading block.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_preamble_detector_cc.

Args:
    freqs : vector with the frequency hypothesis
    shr_len : length of the shr in bits
    sf : preamble spreading factor
    sps : samples per symbol
    chiprate : absolute chiprate
    filter_taps : filter taps of the Matched Filter, needed for SNR estimation"

%feature("docstring") gr::lpwan::dsss_preamble_detector_cc::make "Detects the preamble.

This block is basically a peak detector. It tags the raw rx filtered input data with the detected peak positions (key: \"sop\"), an estimation for the frequency offset and an estimation of the SNR. It works together with the despreading block.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_preamble_detector_cc.

Args:
    freqs : vector with the frequency hypothesis
    shr_len : length of the shr in bits
    sf : preamble spreading factor
    sps : samples per symbol
    chiprate : absolute chiprate
    filter_taps : filter taps of the Matched Filter, needed for SNR estimation"

%feature("docstring") gr::lpwan::dsss_snr_estimator "Estimates the SNR of received packets. It discards CRC-failed packets and operates only on packets with correct CRC checks. The estimation is based on comparison of the remodulated data (convolutional encoding) and the soft demodulated rx data (before convolutional decoding).

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_snr_estimator.

Args:
    psdu_size : size of the psdu in bytes (16,24,32)
    sf : spreading factor"

%feature("docstring") gr::lpwan::dsss_snr_estimator::make "Estimates the SNR of received packets. It discards CRC-failed packets and operates only on packets with correct CRC checks. The estimation is based on comparison of the remodulated data (convolutional encoding) and the soft demodulated rx data (before convolutional decoding).

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_snr_estimator.

Args:
    psdu_size : size of the psdu in bytes (16,24,32)
    sf : spreading factor"

%feature("docstring") gr::lpwan::dsss_spreading_bb "Spreads the already upsampled/repeated data with the goldcode.

Input and output as unpacked bytes.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_spreading_bb.

Spreads the incoming samples with the configured code. This block behaves like a tagged stream block, although it is an interpolator, because the output size of one packet could be very big. (big buffer, latency)

Args:
    len_tag : length tag key
    spread_factor : spreading factor
    seed : goldcode seed
    reset_per_symbol : reset the goldcode after each symbol / after spread_factor input samples
    ovsf_code_index : 
    ovsf_log_spread_factor : "

%feature("docstring") gr::lpwan::dsss_spreading_bb::make "Spreads the already upsampled/repeated data with the goldcode.

Input and output as unpacked bytes.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::dsss_spreading_bb.

Spreads the incoming samples with the configured code. This block behaves like a tagged stream block, although it is an interpolator, because the output size of one packet could be very big. (big buffer, latency)

Args:
    len_tag : length tag key
    spread_factor : spreading factor
    seed : goldcode seed
    reset_per_symbol : reset the goldcode after each symbol / after spread_factor input samples
    ovsf_code_index : 
    ovsf_log_spread_factor : "

%feature("docstring") gr::lpwan::fsk_lecim_corr_est_cc "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_corr_est_cc.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_corr_est_cc's constructor is in a private implementation class. lpwan::fsk_lecim_corr_est_cc::make is the public interface for creating new instances.

Args:
    symbols : 
    sps : 
    mark_delay : 
    threshold : "

%feature("docstring") gr::lpwan::fsk_lecim_corr_est_cc::make "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_corr_est_cc.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_corr_est_cc's constructor is in a private implementation class. lpwan::fsk_lecim_corr_est_cc::make is the public interface for creating new instances.

Args:
    symbols : 
    sps : 
    mark_delay : 
    threshold : "

%feature("docstring") gr::lpwan::fsk_lecim_deinterleaver "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_deinterleaver.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_deinterleaver's constructor is in a private implementation class. lpwan::fsk_lecim_deinterleaver::make is the public interface for creating new instances.

Args:
    phr : 
    nBlock : 
    len_tag : "

%feature("docstring") gr::lpwan::fsk_lecim_deinterleaver::make "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_deinterleaver.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_deinterleaver's constructor is in a private implementation class. lpwan::fsk_lecim_deinterleaver::make is the public interface for creating new instances.

Args:
    phr : 
    nBlock : 
    len_tag : "

%feature("docstring") gr::lpwan::fsk_lecim_interleaver "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_interleaver.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_interleaver's constructor is in a private implementation class. lpwan::fsk_lecim_interleaver::make is the public interface for creating new instances.

Args:
    phr : 
    nBlock : 
    len_tag : "

%feature("docstring") gr::lpwan::fsk_lecim_interleaver::make "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_interleaver.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_interleaver's constructor is in a private implementation class. lpwan::fsk_lecim_interleaver::make is the public interface for creating new instances.

Args:
    phr : 
    nBlock : 
    len_tag : "

%feature("docstring") gr::lpwan::fsk_lecim_normalize_fcc "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_normalize_fcc.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_normalize_fcc's constructor is in a private implementation class. lpwan::fsk_lecim_normalize_fcc::make is the public interface for creating new instances."

%feature("docstring") gr::lpwan::fsk_lecim_normalize_fcc::make "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_normalize_fcc.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_normalize_fcc's constructor is in a private implementation class. lpwan::fsk_lecim_normalize_fcc::make is the public interface for creating new instances."

%feature("docstring") gr::lpwan::fsk_lecim_phr_parser "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_phr_parser.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_phr_parser's constructor is in a private implementation class. lpwan::fsk_lecim_phr_parser::make is the public interface for creating new instances.

Args:
    len_tag_key : "

%feature("docstring") gr::lpwan::fsk_lecim_phr_parser::make "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_phr_parser.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_phr_parser's constructor is in a private implementation class. lpwan::fsk_lecim_phr_parser::make is the public interface for creating new instances.

Args:
    len_tag_key : "

%feature("docstring") gr::lpwan::fsk_lecim_phr_pdu_demux "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_phr_pdu_demux.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_phr_pdu_demux's constructor is in a private implementation class. lpwan::fsk_lecim_phr_pdu_demux::make is the public interface for creating new instances.

Args:
    sps : 
    symbol_rate : 
    sf : 
    output_symbols : "

%feature("docstring") gr::lpwan::fsk_lecim_phr_pdu_demux::make "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_phr_pdu_demux.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_phr_pdu_demux's constructor is in a private implementation class. lpwan::fsk_lecim_phr_pdu_demux::make is the public interface for creating new instances.

Args:
    sps : 
    symbol_rate : 
    sf : 
    output_symbols : "

%feature("docstring") gr::lpwan::fsk_lecim_synchronizer_cc "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_synchronizer_cc.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_synchronizer_cc's constructor is in a private implementation class. lpwan::fsk_lecim_synchronizer_cc::make is the public interface for creating new instances.

Args:
    preamble : 
    sps : 
    threshold : "

%feature("docstring") gr::lpwan::fsk_lecim_synchronizer_cc::make "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::fsk_lecim_synchronizer_cc.

To avoid accidental use of raw pointers, lpwan::fsk_lecim_synchronizer_cc's constructor is in a private implementation class. lpwan::fsk_lecim_synchronizer_cc::make is the public interface for creating new instances.

Args:
    preamble : 
    sps : 
    threshold : "

%feature("docstring") gr::lpwan::sync "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::sync.

To avoid accidental use of raw pointers, lpwan::sync's constructor is in a private implementation class. lpwan::sync::make is the public interface for creating new instances.

Args:
    len_est : "

%feature("docstring") gr::lpwan::sync::make "<+description of block+>

Constructor Specific Documentation:

Return a shared_ptr to a new instance of lpwan::sync.

To avoid accidental use of raw pointers, lpwan::sync's constructor is in a private implementation class. lpwan::sync::make is the public interface for creating new instances.

Args:
    len_est : "

%feature("docstring") gr::lpwan::dsss_codes "generates the codes needed in PHY"





















%feature("docstring") gr::lpwan::mac_crc "calculation of CRC"















%feature("docstring") gr::lpwan::mac_field "base class for fragmentation bitfields"







%feature("docstring") gr::lpwan::mac_field_frag_header "fragmentation packet header"

















%feature("docstring") gr::lpwan::mac_field_frag_status "frak packet status field"























%feature("docstring") gr::lpwan::mac_field_fragment "fragment packet"





























%feature("docstring") gr::lpwan::mac_field_frak "frak packet"























%feature("docstring") gr::lpwan::mac_field_frame "mac frame"











































%feature("docstring") gr::lpwan::mac_field_frame_ctrl "frame control field"

















































%feature("docstring") gr::lpwan::mac_field_header_ie "header ie base class"





















%feature("docstring") gr::lpwan::mac_field_ie_fscd "fscd header ie"













































