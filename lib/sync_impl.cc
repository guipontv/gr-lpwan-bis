/* -*- c++ -*- */
/* 
 * Copyright 2017 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <volk/volk.h>
#include <gnuradio/io_signature.h>
#include "sync_impl.h"

namespace gr {
  namespace lpwan {

    sync::sptr
    sync::make(int len_est)
    {
      return gnuradio::get_initial_sptr
        (new sync_impl(len_est));
    }

    /*
     * The private constructor
     */
    sync_impl::sync_impl(int len_est)
      : gr::sync_block("sync",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(gr_complex))),
      d_len_est(len_est)
    {
      set_output_multiple(d_len_est);
    }

    /*
     * Our virtual destructor.
     */
    sync_impl::~sync_impl()
    {
    }

    int
    sync_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex *) input_items[0];
      gr_complex *out = (gr_complex *) output_items[0];
      gr_complex *in0 = (gr_complex *) in;
      // Do <+signal processing+>
      uint16_t index_local_max;
      volk_32fc_index_max_16u(&index_local_max, in0, noutput_items);
      volk_32fc_s32fc_multiply_32fc(out, in0, 1/abs(in[index_local_max]), noutput_items);
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace lpwan */
} /* namespace gr */

