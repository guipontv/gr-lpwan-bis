#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: LECIM DSSS Loopback Test
# Author: Kristian Maier
# Description: Simple Loopback Test for the DSSS Phy
# Generated: Mon Jul 17 10:00:21 2017
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
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from lpwan_dsss_oqpsk_phy import lpwan_dsss_oqpsk_phy  # grc-generated hier_block
from optparse import OptionParser
import pmt
from gnuradio import qtgui


class loopback_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "LECIM DSSS Loopback Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("LECIM DSSS Loopback Test")
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

        self.settings = Qt.QSettings("GNU Radio", "loopback_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Blocks
        ##################################################
        self.lpwan_dsss_oqpsk_phy_0 = lpwan_dsss_oqpsk_phy(
            burst_tag="burst",
            chiprate=2000000,
            data_seed_rx=2345432,
            data_seed_tx=2345432,
            fec_tailbiting=True,
            max_freq_hypo=2000,
            ovsf_code_index=0,
            ovsf_spreading_factor=0,
            preamble_len=32,
            preamble_seed_rx=54321,
            preamble_seed_tx=54321,
            psdu_len=32,
            roll_off=1,
            sfd_present=False,
            spread_factor=2**8,
            sps=4,
        )
        self.digital_crc32_async_bb_0_0 = digital.crc32_async_bb(True)
        self.digital_crc32_async_bb_0 = digital.crc32_async_bb(False)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=2,
        	frequency_offset=0.0001,
        	epsilon=1.0,
        	taps=(1.0 + 1.0j, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_random_pdu_0 = blocks.random_pdu(28, 28, chr(0xFF), 1)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("generate"), 140)
        self.blocks_message_debug_0 = blocks.message_debug()

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.blocks_random_pdu_0, 'generate'))
        self.msg_connect((self.blocks_random_pdu_0, 'pdus'), (self.digital_crc32_async_bb_0, 'in'))
        self.msg_connect((self.digital_crc32_async_bb_0, 'out'), (self.lpwan_dsss_oqpsk_phy_0, 'in_tx'))
        self.msg_connect((self.digital_crc32_async_bb_0_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.lpwan_dsss_oqpsk_phy_0, 'out_rx'), (self.digital_crc32_async_bb_0_0, 'in'))
        self.connect((self.channels_channel_model_0, 0), (self.lpwan_dsss_oqpsk_phy_0, 0))
        self.connect((self.lpwan_dsss_oqpsk_phy_0, 0), (self.channels_channel_model_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "loopback_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


def main(top_block_cls=loopback_test, options=None):

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
