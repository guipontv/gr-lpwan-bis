#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: LECIM DSSS rx
# Author: Kristian Maier
# Generated: Mon Jul 24 16:05:08 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from dsss_fec_dec_fb import dsss_fec_dec_fb  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import lpwan
import numpy as np
import pmt
import sip
from gnuradio import qtgui


class rx(gr.top_block, Qt.QWidget):

    def __init__(self, chiprate=2000000, data_seed_rx=2645625, fec_tailbiting=True, max_freq_hypo=1, ovsf_code_index=0, ovsf_spreading_factor=0, preamble_len=32, preamble_seed_rx=54321, psdu_len=16, roll_off=1, sfd_present=False, spread_factor=2**10, sps=4):
        gr.top_block.__init__(self, "LECIM DSSS rx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("LECIM DSSS rx")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "rx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.chiprate = chiprate
        self.data_seed_rx = data_seed_rx
        self.fec_tailbiting = fec_tailbiting
        self.max_freq_hypo = max_freq_hypo
        self.ovsf_code_index = ovsf_code_index
        self.ovsf_spreading_factor = ovsf_spreading_factor
        self.preamble_len = preamble_len
        self.preamble_seed_rx = preamble_seed_rx
        self.psdu_len = psdu_len
        self.roll_off = roll_off
        self.sfd_present = sfd_present
        self.spread_factor = spread_factor
        self.sps = sps

        ##################################################
        # Variables
        ##################################################
        self.taps_num = taps_num = 64
        self.samp_rate = samp_rate = 4e6
        self.len_tag_var = len_tag_var = "packet_len"
        self.freq_vec = freq_vec = lpwan.dsss_const.gen_freq_hypo_vec(spread_factor, chiprate, max_freq_hypo)
        self.fo = fo = 2000

        ##################################################
        # Blocks
        ##################################################
        self._fo_range = Range(-15000, 15000, 1, 2000, 200)
        self._fo_win = RangeWidget(self._fo_range, self.set_fo, "fo", "counter_slider", float)
        self.top_layout.addWidget(self._fo_win)
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, sps, 1, 1, taps_num))
        self.qtgui_time_sink_x_3_0 = qtgui.time_sink_f(
        	5240000, #size
        	4e6, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_3_0.set_update_time(0.10)
        self.qtgui_time_sink_x_3_0.set_y_axis(-1, 2e6)

        self.qtgui_time_sink_x_3_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_3_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_3_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 3, 40000, 0, "PSDU")
        self.qtgui_time_sink_x_3_0.enable_autoscale(True)
        self.qtgui_time_sink_x_3_0.enable_grid(False)
        self.qtgui_time_sink_x_3_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_3_0.enable_control_panel(True)

        if not True:
          self.qtgui_time_sink_x_3_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_3_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_3_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_3_0_win = sip.wrapinstance(self.qtgui_time_sink_x_3_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_3_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
        	psdu_len*8, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(True)
        self.qtgui_const_sink_x_1.enable_grid(False)
        self.qtgui_const_sink_x_1.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_win)
        self.lpwan_message_counter_0 = lpwan.message_counter(10, 1)
        self.lpwan_dsss_preamble_search_cc_0_0 = lpwan.dsss_preamble_search_cc(spread_factor, preamble_seed_rx, ovsf_code_index, ovsf_spreading_factor, (freq_vec), preamble_len, sfd_present,
                sps, 0, chiprate, "oqpsk", (firdes.root_raised_cosine(1,sps,1,roll_off,taps_num)))

        self.lpwan_dsss_normalize_ff_0 = lpwan.dsss_normalize_ff(len_tag_var)
        self.lpwan_dsss_filter_crc_packets_0 = lpwan.dsss_filter_crc_packets()
        self.lpwan_dsss_diff_decoding_ff_0 = lpwan.dsss_diff_decoding_ff(len_tag_var, True, preamble_len + (8 if sfd_present else 0))
        self.lpwan_dsss_despread_cc_0_0 = lpwan.dsss_despread_cc(spread_factor, data_seed_rx, preamble_seed_rx, ovsf_code_index, ovsf_spreading_factor, sps,
            psdu_len, 1, chiprate, False, False,
            1,0.05, 0.8, 0.25)
        self.lpwan_dsss_deinterleaver_ff_0 = lpwan.dsss_deinterleaver_ff(len_tag_var)
        self.dsss_fec_dec_fb_0 = dsss_fec_dec_fb(
            len_tag_var=len_tag_var,
            tailbiting=fec_tailbiting,
        )
        self.digital_crc32_async_bb_1_0 = digital.crc32_async_bb(False)
        self.digital_crc32_async_bb_1 = digital.crc32_async_bb(True)
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.complex_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.complex_t, 'packet_len')
        self.blocks_null_sink_1_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0, ))
        self.blocks_message_debug_0_0 = blocks.message_debug()
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/media/maier/73083b7c-6150-4a9b-9a6d-38e866ba5fba/mathesis_iq_files/per_messung dachgeschoss cel/PER_Dachgeschoss1024_reference_txgain80.iq', True)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_0_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, fo, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.lpwan_dsss_filter_crc_packets_0, 'in_soft'))
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.digital_crc32_async_bb_1_0, 'in'))
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.lpwan_message_counter_0, 'in'))
        self.msg_connect((self.digital_crc32_async_bb_1_0, 'out'), (self.lpwan_dsss_filter_crc_packets_0, 'in_hard_crc_ok'))
        self.msg_connect((self.dsss_fec_dec_fb_0, 'out'), (self.digital_crc32_async_bb_1, 'in'))
        self.msg_connect((self.dsss_fec_dec_fb_0, 'out'), (self.lpwan_dsss_filter_crc_packets_0, 'in_hard'))
        self.msg_connect((self.lpwan_dsss_filter_crc_packets_0, 'out_soft'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.qtgui_time_sink_x_3_0, 0))
        self.connect((self.blocks_complex_to_mag_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.lpwan_dsss_deinterleaver_ff_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_3_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.qtgui_const_sink_x_1, 0))
        self.connect((self.lpwan_dsss_deinterleaver_ff_0, 0), (self.lpwan_dsss_normalize_ff_0, 0))
        self.connect((self.lpwan_dsss_despread_cc_0_0, 0), (self.lpwan_dsss_diff_decoding_ff_0, 0))
        self.connect((self.lpwan_dsss_diff_decoding_ff_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.lpwan_dsss_diff_decoding_ff_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))
        self.connect((self.lpwan_dsss_normalize_ff_0, 0), (self.dsss_fec_dec_fb_0, 0))
        self.connect((self.lpwan_dsss_preamble_search_cc_0_0, 1), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.lpwan_dsss_preamble_search_cc_0_0, 0), (self.blocks_complex_to_mag_0_0, 0))
        self.connect((self.lpwan_dsss_preamble_search_cc_0_0, 1), (self.blocks_null_sink_1_0, 0))
        self.connect((self.lpwan_dsss_preamble_search_cc_0_0, 0), (self.lpwan_dsss_despread_cc_0_0, 0))
        self.connect((self.lpwan_message_counter_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.lpwan_dsss_preamble_search_cc_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_chiprate(self):
        return self.chiprate

    def set_chiprate(self, chiprate):
        self.chiprate = chiprate
        self.set_freq_vec(lpwan.dsss_const.gen_freq_hypo_vec(self.spread_factor, self.chiprate, self.max_freq_hypo))

    def get_data_seed_rx(self):
        return self.data_seed_rx

    def set_data_seed_rx(self, data_seed_rx):
        self.data_seed_rx = data_seed_rx

    def get_fec_tailbiting(self):
        return self.fec_tailbiting

    def set_fec_tailbiting(self, fec_tailbiting):
        self.fec_tailbiting = fec_tailbiting
        self.dsss_fec_dec_fb_0.set_tailbiting(self.fec_tailbiting)

    def get_max_freq_hypo(self):
        return self.max_freq_hypo

    def set_max_freq_hypo(self, max_freq_hypo):
        self.max_freq_hypo = max_freq_hypo
        self.set_freq_vec(lpwan.dsss_const.gen_freq_hypo_vec(self.spread_factor, self.chiprate, self.max_freq_hypo))

    def get_ovsf_code_index(self):
        return self.ovsf_code_index

    def set_ovsf_code_index(self, ovsf_code_index):
        self.ovsf_code_index = ovsf_code_index

    def get_ovsf_spreading_factor(self):
        return self.ovsf_spreading_factor

    def set_ovsf_spreading_factor(self, ovsf_spreading_factor):
        self.ovsf_spreading_factor = ovsf_spreading_factor

    def get_preamble_len(self):
        return self.preamble_len

    def set_preamble_len(self, preamble_len):
        self.preamble_len = preamble_len

    def get_preamble_seed_rx(self):
        return self.preamble_seed_rx

    def set_preamble_seed_rx(self, preamble_seed_rx):
        self.preamble_seed_rx = preamble_seed_rx

    def get_psdu_len(self):
        return self.psdu_len

    def set_psdu_len(self, psdu_len):
        self.psdu_len = psdu_len

    def get_roll_off(self):
        return self.roll_off

    def set_roll_off(self, roll_off):
        self.roll_off = roll_off

    def get_sfd_present(self):
        return self.sfd_present

    def set_sfd_present(self, sfd_present):
        self.sfd_present = sfd_present

    def get_spread_factor(self):
        return self.spread_factor

    def set_spread_factor(self, spread_factor):
        self.spread_factor = spread_factor
        self.set_freq_vec(lpwan.dsss_const.gen_freq_hypo_vec(self.spread_factor, self.chiprate, self.max_freq_hypo))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.sps, 1, 1, self.taps_num))

    def get_taps_num(self):
        return self.taps_num

    def set_taps_num(self, taps_num):
        self.taps_num = taps_num
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.sps, 1, 1, self.taps_num))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_len_tag_var(self):
        return self.len_tag_var

    def set_len_tag_var(self, len_tag_var):
        self.len_tag_var = len_tag_var
        self.dsss_fec_dec_fb_0.set_len_tag_var(self.len_tag_var)

    def get_freq_vec(self):
        return self.freq_vec

    def set_freq_vec(self, freq_vec):
        self.freq_vec = freq_vec

    def get_fo(self):
        return self.fo

    def set_fo(self, fo):
        self.fo = fo
        self.analog_sig_source_x_0.set_frequency(self.fo)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--chiprate", dest="chiprate", type="intx", default=2000000,
        help="Set Chiprate [default=%default]")
    parser.add_option(
        "", "--data-seed-rx", dest="data_seed_rx", type="intx", default=2645625,
        help="Set RX Data Goldcode Seed [default=%default]")
    parser.add_option(
        "", "--max-freq-hypo", dest="max_freq_hypo", type="intx", default=1,
        help="Set Max. frequency deviation (Hz) [default=%default]")
    parser.add_option(
        "", "--ovsf-code-index", dest="ovsf_code_index", type="intx", default=0,
        help="Set OVSF Code Index [default=%default]")
    parser.add_option(
        "", "--ovsf-spreading-factor", dest="ovsf_spreading_factor", type="intx", default=0,
        help="Set OVSF Log Spreading Factor [default=%default]")
    parser.add_option(
        "", "--preamble-len", dest="preamble_len", type="intx", default=32,
        help="Set Preamble Length [default=%default]")
    parser.add_option(
        "", "--preamble-seed-rx", dest="preamble_seed_rx", type="intx", default=54321,
        help="Set RX Preamble Goldcode Seed [default=%default]")
    parser.add_option(
        "", "--psdu-len", dest="psdu_len", type="intx", default=16,
        help="Set PSDU Length [default=%default]")
    parser.add_option(
        "", "--roll-off", dest="roll_off", type="eng_float", default=eng_notation.num_to_str(1),
        help="Set RRC Roll Off [default=%default]")
    parser.add_option(
        "", "--spread-factor", dest="spread_factor", type="intx", default=2**10,
        help="Set Spreading Faktor [default=%default]")
    parser.add_option(
        "", "--sps", dest="sps", type="intx", default=4,
        help="Set Samples Per Symbol [default=%default]")
    return parser


def main(top_block_cls=rx, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(chiprate=options.chiprate, data_seed_rx=options.data_seed_rx, max_freq_hypo=options.max_freq_hypo, ovsf_code_index=options.ovsf_code_index, ovsf_spreading_factor=options.ovsf_spreading_factor, preamble_len=options.preamble_len, preamble_seed_rx=options.preamble_seed_rx, psdu_len=options.psdu_len, roll_off=options.roll_off, spread_factor=options.spread_factor, sps=options.sps)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
