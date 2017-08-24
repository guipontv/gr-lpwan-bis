#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: LECIM DSSS tx
# Author: Kristian Maier
# Generated: Mon Jul 24 15:58:18 2017
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
from dsss_fec_enc_b import dsss_fec_enc_b  # grc-generated hier_block
from dsss_oqpsk_mod import dsss_oqpsk_mod  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import lpwan
import numpy as np
import pmt
from gnuradio import qtgui


class tx(gr.top_block, Qt.QWidget):

    def __init__(self, chiprate=2000000, data_seed_tx=2645625, fec_tailbiting=True, ovsf_code_index=0, ovsf_spreading_factor=0, preamble_len=32, preamble_seed_tx=54321, psdu_len=16, roll_off=1, sfd_present=False, spread_factor=2**10, sps=4):
        gr.top_block.__init__(self, "LECIM DSSS tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("LECIM DSSS tx")
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

        self.settings = Qt.QSettings("GNU Radio", "tx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.chiprate = chiprate
        self.data_seed_tx = data_seed_tx
        self.fec_tailbiting = fec_tailbiting
        self.ovsf_code_index = ovsf_code_index
        self.ovsf_spreading_factor = ovsf_spreading_factor
        self.preamble_len = preamble_len
        self.preamble_seed_tx = preamble_seed_tx
        self.psdu_len = psdu_len
        self.roll_off = roll_off
        self.sfd_present = sfd_present
        self.spread_factor = spread_factor
        self.sps = sps

        ##################################################
        # Variables
        ##################################################
        self.sfd = sfd = lpwan.dsss_const.sfd32 if preamble_len == 32 else lpwan.dsss_const.sfd16
        self.preamble = preamble = lpwan.dsss_const.preamble32 if preamble_len == 32 else lpwan.dsss_const.preamble16
        self.taps_num = taps_num = 32
        self.shr = shr = np.append(preamble, sfd) if sfd_present else preamble
        self.len_tag_var = len_tag_var = "packet_len"

        ##################################################
        # Blocks
        ##################################################
        self.lpwan_dsss_spreading_bb_0_0 = lpwan.dsss_spreading_bb(len_tag_var, spread_factor, preamble_seed_tx, True, ovsf_code_index, ovsf_spreading_factor)
        self.lpwan_dsss_spreading_bb_0 = lpwan.dsss_spreading_bb(len_tag_var, spread_factor, data_seed_tx, False, ovsf_code_index, ovsf_spreading_factor)
        self.lpwan_dsss_interleaver_bb_0 = lpwan.dsss_interleaver_bb(len_tag_var)
        self.lpwan_dsss_diff_coding_bb_0_0 = lpwan.dsss_diff_coding_bb(len_tag_var)
        self.lpwan_dsss_diff_coding_bb_0 = lpwan.dsss_diff_coding_bb(len_tag_var)
        self.dsss_oqpsk_mod_0_0 = dsss_oqpsk_mod(
            burst_tag="burst",
            num_of_taps=taps_num,
            packet_length=(psdu_len*8*2+len(shr))*spread_factor,
            roll_off=roll_off,
            sps=sps,
        )
        self.dsss_fec_enc_b_0_0 = dsss_fec_enc_b(
            len_tag_var=len_tag_var,
            tailbiting=fec_tailbiting,
        )
        self.digital_crc32_async_bb_0 = digital.crc32_async_bb(False)
        self.blocks_vector_source_x_0_0 = blocks.vector_source_b(shr.tolist(), True, 1, [gr.tag_utils.python_to_tag((0, pmt.intern(len_tag_var), pmt.from_long(len(shr))))])
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_char*1, (len(shr)*spread_factor, psdu_len*2*8*spread_factor))
        self.blocks_random_pdu_0 = blocks.random_pdu(psdu_len-4, psdu_len-4, chr(0xFF), 1)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("generate"), 50)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/Users/victorguipont/Developpement-informatique/GNU-radio/sf1024', False)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.blocks_random_pdu_0, 'generate'))
        self.msg_connect((self.blocks_random_pdu_0, 'pdus'), (self.digital_crc32_async_bb_0, 'in'))
        self.msg_connect((self.digital_crc32_async_bb_0, 'out'), (self.dsss_fec_enc_b_0_0, 'in'))
        self.connect((self.blocks_stream_mux_0, 0), (self.dsss_oqpsk_mod_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.lpwan_dsss_diff_coding_bb_0_0, 0))
        self.connect((self.dsss_fec_enc_b_0_0, 0), (self.lpwan_dsss_interleaver_bb_0, 0))
        self.connect((self.dsss_oqpsk_mod_0_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.lpwan_dsss_diff_coding_bb_0, 0), (self.lpwan_dsss_spreading_bb_0, 0))
        self.connect((self.lpwan_dsss_diff_coding_bb_0_0, 0), (self.lpwan_dsss_spreading_bb_0_0, 0))
        self.connect((self.lpwan_dsss_interleaver_bb_0, 0), (self.lpwan_dsss_diff_coding_bb_0, 0))
        self.connect((self.lpwan_dsss_spreading_bb_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.lpwan_dsss_spreading_bb_0_0, 0), (self.blocks_stream_mux_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_chiprate(self):
        return self.chiprate

    def set_chiprate(self, chiprate):
        self.chiprate = chiprate

    def get_data_seed_tx(self):
        return self.data_seed_tx

    def set_data_seed_tx(self, data_seed_tx):
        self.data_seed_tx = data_seed_tx

    def get_fec_tailbiting(self):
        return self.fec_tailbiting

    def set_fec_tailbiting(self, fec_tailbiting):
        self.fec_tailbiting = fec_tailbiting
        self.dsss_fec_enc_b_0_0.set_tailbiting(self.fec_tailbiting)

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
        self.set_sfd(lpwan.dsss_const.sfd32 if self.preamble_len == 32 else lpwan.dsss_const.sfd16)
        self.set_preamble(lpwan.dsss_const.preamble32 if self.preamble_len == 32 else lpwan.dsss_const.preamble16)

    def get_preamble_seed_tx(self):
        return self.preamble_seed_tx

    def set_preamble_seed_tx(self, preamble_seed_tx):
        self.preamble_seed_tx = preamble_seed_tx

    def get_psdu_len(self):
        return self.psdu_len

    def set_psdu_len(self, psdu_len):
        self.psdu_len = psdu_len
        self.dsss_oqpsk_mod_0_0.set_packet_length((self.psdu_len*8*2+len(self.shr))*self.spread_factor)

    def get_roll_off(self):
        return self.roll_off

    def set_roll_off(self, roll_off):
        self.roll_off = roll_off
        self.dsss_oqpsk_mod_0_0.set_roll_off(self.roll_off)

    def get_sfd_present(self):
        return self.sfd_present

    def set_sfd_present(self, sfd_present):
        self.sfd_present = sfd_present
        self.set_shr(np.append(self.preamble, self.sfd) if self.sfd_present else self.preamble)

    def get_spread_factor(self):
        return self.spread_factor

    def set_spread_factor(self, spread_factor):
        self.spread_factor = spread_factor
        self.dsss_oqpsk_mod_0_0.set_packet_length((self.psdu_len*8*2+len(self.shr))*self.spread_factor)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.dsss_oqpsk_mod_0_0.set_sps(self.sps)

    def get_sfd(self):
        return self.sfd

    def set_sfd(self, sfd):
        self.sfd = sfd
        self.set_shr(np.append(self.preamble, self.sfd) if self.sfd_present else self.preamble)

    def get_preamble(self):
        return self.preamble

    def set_preamble(self, preamble):
        self.preamble = preamble
        self.set_shr(np.append(self.preamble, self.sfd) if self.sfd_present else self.preamble)

    def get_taps_num(self):
        return self.taps_num

    def set_taps_num(self, taps_num):
        self.taps_num = taps_num
        self.dsss_oqpsk_mod_0_0.set_num_of_taps(self.taps_num)

    def get_shr(self):
        return self.shr

    def set_shr(self, shr):
        self.shr = shr
        self.dsss_oqpsk_mod_0_0.set_packet_length((self.psdu_len*8*2+len(self.shr))*self.spread_factor)
        self.blocks_vector_source_x_0_0.set_data(shr.tolist(), [gr.tag_utils.python_to_tag((0, pmt.intern(self.len_tag_var), pmt.from_long(len(self.shr))))])

    def get_len_tag_var(self):
        return self.len_tag_var

    def set_len_tag_var(self, len_tag_var):
        self.len_tag_var = len_tag_var
        self.dsss_fec_enc_b_0_0.set_len_tag_var(self.len_tag_var)
        self.blocks_vector_source_x_0_0.set_data(shr.tolist(), [gr.tag_utils.python_to_tag((0, pmt.intern(self.len_tag_var), pmt.from_long(len(self.shr))))])


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--chiprate", dest="chiprate", type="intx", default=2000000,
        help="Set Chiprate [default=%default]")
    parser.add_option(
        "", "--data-seed-tx", dest="data_seed_tx", type="intx", default=2645625,
        help="Set TX Data Goldcode Seed [default=%default]")
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
        "", "--preamble-seed-tx", dest="preamble_seed_tx", type="intx", default=54321,
        help="Set TX Preamble Goldcode Seed [default=%default]")
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


def main(top_block_cls=tx, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(chiprate=options.chiprate, data_seed_tx=options.data_seed_tx, ovsf_code_index=options.ovsf_code_index, ovsf_spreading_factor=options.ovsf_spreading_factor, preamble_len=options.preamble_len, preamble_seed_tx=options.preamble_seed_tx, psdu_len=options.psdu_len, roll_off=options.roll_off, spread_factor=options.spread_factor, sps=options.sps)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
