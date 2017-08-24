#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: LECIM DSSS TxRx BER test
# Author: Kristian Maier
# Generated: Sat Jun 24 12:17:38 2017
##################################################
import threading

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import lpwan
import numpy
import numpy as np
import random as rnd
import sip
import sys
from gnuradio import qtgui


class dsss_sim_perfekt_sync_fg(gr.top_block, Qt.QWidget):

    def __init__(self, ebn0_db=3.3, spread_factor=2**10, tailbiting=True):
        gr.top_block.__init__(self, "LECIM DSSS TxRx BER test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("LECIM DSSS TxRx BER test")
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

        self.settings = Qt.QSettings("GNU Radio", "dsss_sim_perfekt_sync_fg")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        self._lock = threading.RLock()

        ##################################################
        # Parameters
        ##################################################
        self.ebn0_db = ebn0_db
        self.spread_factor = spread_factor
        self.tailbiting = tailbiting

        ##################################################
        # Variables
        ##################################################
        self.cc_poly = cc_poly = [121,91]
        self.pdu_size = pdu_size = 32
        self.noise = noise = (np.sqrt(1*spread_factor/10**(ebn0_db/10.0))*1.0)
        self.len_tag_var = len_tag_var = "packet_len"


        self.cc_encoder_terminated = cc_encoder_terminated = map( (lambda a: fec.cc_encoder_make(32*8, 7, 2, (cc_poly), 0, fec.CC_TERMINATED, True)), range(0,1) );


        self.cc_encoder_tailbiting = cc_encoder_tailbiting = map( (lambda a: fec.cc_encoder_make(32*8, 7, 2, (cc_poly), 0, fec.CC_TAILBITING, False)), range(0,1) );


        self.cc_decoder_terminated = cc_decoder_terminated = map( (lambda a: fec.cc_decoder.make(32*8, 7, 2, (cc_poly), 0, -1, fec.CC_TERMINATED, True)), range(0,1) );


        self.cc_decoder_tailbiting = cc_decoder_tailbiting = map( (lambda a: fec.cc_decoder.make(32*8, 7, 2, (cc_poly), 0, -1, fec.CC_TAILBITING, False)), range(0,1) );

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("BER")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_win)
        self.probe_ber_running = blocks.probe_signal_f()
        self.lpwan_dsss_spreading_bb_0 = lpwan.dsss_spreading_bb(len_tag_var, spread_factor, 123456, False, 0, 0)
        self.lpwan_dsss_normalize_ff_0 = lpwan.dsss_normalize_ff(len_tag_var)
        self.lpwan_dsss_interleaver_bb_0 = lpwan.dsss_interleaver_bb(len_tag_var)
        self.lpwan_dsss_diff_decoding_ff_0 = lpwan.dsss_diff_decoding_ff(len_tag_var, False, 0)
        self.lpwan_dsss_diff_coding_bb_0 = lpwan.dsss_diff_coding_bb(len_tag_var)
        self.lpwan_dsss_despread_simple_cc_0 = lpwan.dsss_despread_simple_cc(len_tag_var, spread_factor, 123456, False, 0, 0)
        self.lpwan_dsss_deinterleaver_ff_0 = lpwan.dsss_deinterleaver_ff(len_tag_var)
        self.fec_extended_tagged_encoder_0 = fec.extended_tagged_encoder(encoder_obj_list=cc_encoder_tailbiting if tailbiting else cc_encoder_terminated, puncpat='11', lentagname=len_tag_var, mtu=32)
        self.fec_extended_tagged_decoder_0 = self.fec_extended_tagged_decoder_0 = fec_extended_tagged_decoder_0 = fec.extended_tagged_decoder(decoder_obj_list=cc_decoder_tailbiting if tailbiting else cc_decoder_terminated, ann=None, puncpat='11', integration_period=10000, lentagname=len_tag_var, mtu=32)
        self.fec_ber_running = fec.ber_bf(False, 100, -7.0)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(([-1,1]), 1)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, pdu_size, len_tag_var)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(1, 8, len_tag_var, False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 1, len_tag_var, False, gr.GR_LSB_FIRST)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        (self.blocks_add_xx_0).set_min_output_buffer(2097152)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 10000000)), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise, rnd.randint(0,10000))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.lpwan_dsss_despread_simple_cc_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.lpwan_dsss_deinterleaver_ff_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.fec_extended_tagged_encoder_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.fec_ber_running, 1))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.fec_ber_running, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.fec_ber_running, 0), (self.probe_ber_running, 0))
        self.connect((self.fec_ber_running, 0), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.fec_extended_tagged_decoder_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0, 0), (self.lpwan_dsss_interleaver_bb_0, 0))
        self.connect((self.lpwan_dsss_deinterleaver_ff_0, 0), (self.lpwan_dsss_normalize_ff_0, 0))
        self.connect((self.lpwan_dsss_despread_simple_cc_0, 0), (self.lpwan_dsss_diff_decoding_ff_0, 0))
        self.connect((self.lpwan_dsss_diff_coding_bb_0, 0), (self.lpwan_dsss_spreading_bb_0, 0))
        self.connect((self.lpwan_dsss_diff_decoding_ff_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.lpwan_dsss_interleaver_bb_0, 0), (self.lpwan_dsss_diff_coding_bb_0, 0))
        self.connect((self.lpwan_dsss_normalize_ff_0, 0), (self.fec_extended_tagged_decoder_0, 0))
        self.connect((self.lpwan_dsss_spreading_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "dsss_sim_perfekt_sync_fg")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_ebn0_db(self):
        return self.ebn0_db

    def set_ebn0_db(self, ebn0_db):
        with self._lock:
            self.ebn0_db = ebn0_db
            self.set_noise((np.sqrt(1*self.spread_factor/10**(self.ebn0_db/10.0))*1.0))

    def get_spread_factor(self):
        return self.spread_factor

    def set_spread_factor(self, spread_factor):
        with self._lock:
            self.spread_factor = spread_factor
            self.set_noise((np.sqrt(1*self.spread_factor/10**(self.ebn0_db/10.0))*1.0))

    def get_tailbiting(self):
        return self.tailbiting

    def set_tailbiting(self, tailbiting):
        with self._lock:
            self.tailbiting = tailbiting

    def get_cc_poly(self):
        return self.cc_poly

    def set_cc_poly(self, cc_poly):
        with self._lock:
            self.cc_poly = cc_poly

    def get_pdu_size(self):
        return self.pdu_size

    def set_pdu_size(self, pdu_size):
        with self._lock:
            self.pdu_size = pdu_size
            self.blocks_stream_to_tagged_stream_0.set_packet_len(self.pdu_size)
            self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.pdu_size)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        with self._lock:
            self.noise = noise
            self.analog_noise_source_x_0.set_amplitude(self.noise)

    def get_len_tag_var(self):
        return self.len_tag_var

    def set_len_tag_var(self, len_tag_var):
        with self._lock:
            self.len_tag_var = len_tag_var

    def get_cc_encoder_terminated(self):
        return self.cc_encoder_terminated

    def set_cc_encoder_terminated(self, cc_encoder_terminated):
        with self._lock:
            self.cc_encoder_terminated = cc_encoder_terminated

    def get_cc_encoder_tailbiting(self):
        return self.cc_encoder_tailbiting

    def set_cc_encoder_tailbiting(self, cc_encoder_tailbiting):
        with self._lock:
            self.cc_encoder_tailbiting = cc_encoder_tailbiting

    def get_cc_decoder_terminated(self):
        return self.cc_decoder_terminated

    def set_cc_decoder_terminated(self, cc_decoder_terminated):
        with self._lock:
            self.cc_decoder_terminated = cc_decoder_terminated

    def get_cc_decoder_tailbiting(self):
        return self.cc_decoder_tailbiting

    def set_cc_decoder_tailbiting(self, cc_decoder_tailbiting):
        with self._lock:
            self.cc_decoder_tailbiting = cc_decoder_tailbiting


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--ebn0-db", dest="ebn0_db", type="eng_float", default=eng_notation.num_to_str(3.3),
        help="Set ebn0_db [default=%default]")
    parser.add_option(
        "", "--spread-factor", dest="spread_factor", type="intx", default=2**10,
        help="Set spread_factor [default=%default]")
    return parser


def main(top_block_cls=dsss_sim_perfekt_sync_fg, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(ebn0_db=options.ebn0_db, spread_factor=options.spread_factor)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
