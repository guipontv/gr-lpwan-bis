#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 Victor Guipont>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy as np
from cmath import exp, pi
from gnuradio import gr

class fsk_lecim_modulator_fc(gr.interp_block):
    """
    This block modulates the symbols.
    """
    def __init__(self, sps, freq_dev, symbol_rate):
        self.sps = sps
        self.freq_dev = freq_dev
        self.symbol_rate = symbol_rate
        gr.interp_block.__init__(self,
            name="fsk_lecim_modulator_fc",
            in_sig=[np.float32],
            out_sig=[np.complex64], interp = self.sps)

    def work(self, input_items, output_items):
        self.set_tag_propagation_policy(0)
        in0 = input_items[0]
        out = output_items[0]
        iterable = ( abs(in0[k/self.sps]) * exp(1j*2*pi*in0[k/self.sps]
                    *self.freq_dev*k/(self.sps*self.symbol_rate)) 
                    for k in range(len(out)) )        
        mod = np.fromiter(iterable, np.complex64)
        out[:] = mod 
        return len(output_items[0])

