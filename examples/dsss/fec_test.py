#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: LECIM DSSS FEC Test
# Author: Kristian Maier
# Description: Simple Test of the DSSS FEC Blocks
# Generated: Thu Jun  8 11:57:46 2017
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
from dsss_fec_enc_b import dsss_fec_enc_b  # grc-generated hier_block
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
import numpy as np
import pmt
import sip
from gnuradio import qtgui


class fec_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "LECIM DSSS FEC Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("LECIM DSSS FEC Test")
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

        self.settings = Qt.QSettings("GNU Radio", "fec_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.len_tag_var = len_tag_var = "len_tag"
        self.ebn0_db = ebn0_db = 3

        ##################################################
        # Blocks
        ##################################################
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
            self.qtgui_number_sink_0.set_min(i, -1)
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
        self.lpwan_dsss_normalize_ff_0 = lpwan.dsss_normalize_ff(len_tag_var)
        self.lpwan_dsss_interleaver_bb_0 = lpwan.dsss_interleaver_bb(len_tag_var)
        self.lpwan_dsss_deinterleaver_ff_0 = lpwan.dsss_deinterleaver_ff(len_tag_var)
        self.fec_ber_bf_0 = fec.ber_bf(False, 100, -7.0)
        self.dsss_fec_enc_b_0 = dsss_fec_enc_b(
            len_tag_var="len_tag",
            tailbiting=True,
        )
        self.dsss_fec_dec_fb_0 = dsss_fec_dec_fb(
            len_tag_var=len_tag_var,
            tailbiting=True,
        )
        self.digital_map_bb_0_1 = digital.map_bb(([-1, 1]))
        self.blocks_random_pdu_0 = blocks.random_pdu(32, 32, chr(0xFF), 1)
        self.blocks_pdu_to_tagged_stream_0_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0.001, ))
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("generate"), 10)
        self.blocks_char_to_float_1_2 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, np.sqrt(10**(-ebn0_db/10.0)), 4)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.blocks_random_pdu_0, 'generate'))
        self.msg_connect((self.blocks_random_pdu_0, 'pdus'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.blocks_random_pdu_0, 'pdus'), (self.dsss_fec_enc_b_0, 'in'))
        self.msg_connect((self.dsss_fec_dec_fb_0, 'out'), (self.blocks_pdu_to_tagged_stream_0_0, 'pdus'))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_char_to_float_1_2, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.lpwan_dsss_deinterleaver_ff_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.fec_ber_bf_0, 1))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0, 0), (self.fec_ber_bf_0, 0))
        self.connect((self.digital_map_bb_0_1, 0), (self.blocks_char_to_float_1_2, 0))
        self.connect((self.dsss_fec_enc_b_0, 0), (self.lpwan_dsss_interleaver_bb_0, 0))
        self.connect((self.fec_ber_bf_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.lpwan_dsss_deinterleaver_ff_0, 0), (self.lpwan_dsss_normalize_ff_0, 0))
        self.connect((self.lpwan_dsss_interleaver_bb_0, 0), (self.digital_map_bb_0_1, 0))
        self.connect((self.lpwan_dsss_normalize_ff_0, 0), (self.dsss_fec_dec_fb_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fec_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_len_tag_var(self):
        return self.len_tag_var

    def set_len_tag_var(self, len_tag_var):
        self.len_tag_var = len_tag_var
        self.dsss_fec_dec_fb_0.set_len_tag_var(self.len_tag_var)

    def get_ebn0_db(self):
        return self.ebn0_db

    def set_ebn0_db(self, ebn0_db):
        self.ebn0_db = ebn0_db
        self.analog_noise_source_x_0.set_amplitude(np.sqrt(10**(-self.ebn0_db/10.0)))


def main(top_block_cls=fec_test, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
