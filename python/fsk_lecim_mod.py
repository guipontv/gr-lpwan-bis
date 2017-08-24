import numpy as np
import fsk_lecim_const as cst
import fsk_lecim_phy

from math import floor
from cmath import exp, pi, phase

class fsk_lecim_modulator(fsk_lecim_phy.physical_layer):
    def modulate_random(self, n):
        self.phyPacketSize = n
        self.PHR = self.gen_PHR()
        PDU = np.random.randint(0, 2, size=(n * 8,))
        return self.modulate(PDU)

    def modulate(self, data_in):
        PHR = self.fec_encoder(self.PHR)
        PHR = self.interleaver(PHR, True)
        PHR = self.interleaver(PHR, True)
        PHR = self.spreading(PHR)
        PDU = self.zero_padding(data_in)
        PDU = self.fec_encoder(PDU)
        PDU = self.interleaver(PDU)
        PDU = self.data_whitening(PDU)
        PDU = self.interleaver(PDU)
        PDU = self.spreading(PDU)
        PSDU = self.mux(self.SHR, PHR, PDU)
        PSDU = self.mapper(PSDU)
        PSDU = self.modulator(PSDU)
        return [data_in, PSDU]

    #PDU length in bytes
    def pdu_len(self, data_in):
        pdu_len = len(data_in)
        if((pdu_len%8)!= 0):
            print 'PDU length is not a multiple of 8, padding zero to compensate'
            data_in = np.concatenate((data_in, np.zeros((8-(pdu_len%8), ), dtype=int)))
        return len(data_in)/8

    #zero padding
    def zero_padding(self, data_in):
        nPad = self.nPad
        data_out = np.concatenate((data_in, np.zeros((nPad, ), dtype=int)))
        return data_out

    #FEC : G0(x) = 1 + x^2 + x^3 + x^5 + x^6, G1(x) = 1 + x + x^2 + x^3 + x^6  
    def fec_encoder(self, data_in):
        poly = np.zeros((6, ), dtype = int)
        data_in = np.concatenate((data_in, np.zeros((6, ), dtype=int)))
        data_out = np.zeros((2*len(data_in)), dtype=int)
        for i in range(len(data_in)):
            data_out[2*i] = data_in[i]^poly[1]^poly[2]^poly[4]^poly[5]
            data_out[2*i+1] = data_in[i]^poly[0]^poly[1]^poly[2]^poly[5]
            poly = np.insert(poly, 0, data_in[i])
            poly = np.delete(poly, 6)
        return data_out

    #interleave K : compute the index to permute with   
    def interleave_k(self, k, nDepth, lambda_):
        a = int((((nDepth-1-k)%lambda_)*nDepth/float(lambda_))+floor((nDepth-1-k)/(float(lambda_))))
        return a    

    #interleaver 
    def interleaver(self, data_in, phr = False):
        data_out = np.zeros((len(data_in), ), dtype=int)
        if(phr):
            for i in range(self.nPhr):
                data_out[self.interleave_k(i,self.nPhr,self.lambdaPhr)] = data_in[i]
        else:
            for m in range(self.nBlock):
                for k in range(self.nPsdu):
                    data_out[m*self.nPsdu+self.interleave_k(k,self.nPsdu,self.lambdaPsdu)] = data_in[m*self.nPsdu+k]
        return data_out

    #Data whitening
    def data_whitening(self, data_in):
        if self.dataWhitening:
            data_out = np.zeros((len(data_in), ), dtype=int)
            PN9 = np.ones((9, ), dtype=int)
            for i in range(len(data_in)):
                PN9n = PN9[3]^PN9[8]
                poly = np.insert(PN9, 0, PN9n)
                poly = np.delete(poly, 9)
                data_out[i] = data_in[i]^PN9[0]
            return data_out
        else:
            return data_in

    #Spreading fundtion
    def spreading(self, data_in):
        if self.phyLecimFskSpreading:
            data_out = np.array([], dtype=int)
            if self.phyLecimFskSpreadingAlternating:
                for i in range(len(data_in)):
                    if data_in[i]==0:
                        data_out = np.concatenate((data_out, np.tile(cst.spreadingAlternating_0,self.phyLecimFskSpreadingFactor/2)))
                    else:
                        data_out = np.concatenate((data_out, np.tile(cst.spreadingAlternating_1,self.phyLecimFskSpreadingFactor/2)))
            else:
                if self.phyLecimFskSpreadingFactor <= 4:
                    for i in range(len(data_in)):
                        if data_in[i]==0:
                            data_out = np.concatenate((data_out, np.tile(cst.spreadingAlternating_1,self.phyLecimFskSpreadingFactor/2)))
                        else:
                            data_out = np.concatenate((data_out, np.tile(cst.spreadingAlternating_0,self.phyLecimFskSpreadingFactor/2)))
                if self.phyLecimFskSpreadingFactor == 8:
                    for i in range(len(data_in)):
                        if data_in[i]==0:
                            data_out = np.concatenate((data_out, cst.spreadingNonAlternating8_0))
                        else:
                            data_out = np.concatenate((data_out, cst.spreadingNonAlternating8_1))
                if self.phyLecimFskSpreadingFactor == 16:
                    for i in range(len(data_in)):
                        if data_in[i]==0:
                            data_out = np.concatenate((data_out, cst.spreadingNonAlternating16_0))
                        else:
                            data_out = np.concatenate((data_out,cst.spreadingNonAlternating16_1))
            return data_out
        else:
            return data_in

    #MUX
    def mux(self, shr, phr, psdu):
        return np.concatenate((shr, phr, psdu))
 
    #mapper
    def mapper(self, data_in):
        data_out = np.zeros((len(data_in), ), dtype=int)
        if self.pfsk:
            for i in range(int(floor(len(data_in)/2.0))):
                if data_in[2*i] == 0 and data_in[2*i+1] == 0:
                    data_out[2*i] = -1
                    data_out[2*i+1]  = 0
                if data_in[2*i] == 0 and data_in[2*i+1] == 1:
                    data_out[2*i] = 0
                    data_out[2*i+1] = -1
                if data_in[2*i] == 1 and data_in[2*i+1] == 0:
                    data_out[2*i] = 1
                    data_out[2*i+1] = 0
                if data_in[2*i] == 1 and data_in[2*i+1] == 1:
                    data_out[2*i] = 0
                    data_out[2*i+1] = 1
        else:
            for i in range(len(data_in)):
                if data_in[i]:
                    data_out[i] = 1
                else:
                    data_out[i] = -1
        return data_out

    #modulator
    def modulator(self, data_in):
        data_out = np.zeros((len(data_in)*self.sps, ), dtype=complex)
        for i in range(len(data_in)):
            for k in range(self.sps):
                data_out[self.sps*i+k] = abs(data_in[i])*exp(1j*2*pi*data_in[i]*self.freq_dev*(self.sps*i+k)/(self.sps*self.symbol_rate))
        return data_out

    #channel 
    def rayleigh_fading(self, PSDU, fading_factor = -1, noise_power = 1, delay = 0):
        if delay == 0:
            padding = 0
        else:
            padding = self.sps - (delay % self.sps)
        if fading_factor != -1:
            fading = np.random.normal(size=int(len(PSDU)/float(self.sps)), scale=np.sqrt(fading_factor)/2.0) + 1j * np.random.normal(size=int(len(PSDU)/float(self.sps)), scale=np.sqrt(fading_factor)/2.0)
            fading_interpolation = np.zeros(delay)
            for i in range(len(fading)):
                a = np.tile(fading[i], self.sps)
                fading_interpolation = np.concatenate([fading_interpolation, a/abs(fading[i])])
            fading_interpolation = np.concatenate([fading_interpolation, np.zeros(padding)])
        else:
            fading_interpolation = 1  
        noise = (np.random.normal(size=len(PSDU)+delay+padding, scale=np.sqrt(noise_power)/2.0) + 1j * np.random.normal(size=len(PSDU)+delay+padding, scale=np.sqrt(noise_power)/2.0))
        PSDU = np.concatenate([np.zeros(delay), PSDU, np.zeros(padding)])
        return PSDU, fading_interpolation, noise