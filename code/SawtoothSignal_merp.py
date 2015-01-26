# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 17:10:31 2015

@author: casey
"""
import thinkdsp 

class SawtoothSignal_v2(thinkdsp.Sinusoid):
    "This class takes a signal and outputs a float wave array" 
    
    
    def evaluate(self, ts): 
        A = self.period
        ys  = 2*((ts/A) - numpy.floor(0.5 + (ts/A)))
        return ys
        
    def evaluate_v3(self, ts): 
        A = self.amp
        for k in range(0, 2):
            ys = A/2 - (numpy.sin(2*math.pi*self.freq*ts*k))/k
        return ys
        
    def evaluate_v1(self, ts):
        """Evaluates the ys for all ts"""
        """Because it is a sawtooth signal, we know the ys will be -1, 1, 1...and repeat. """ 

        ##first, decide on the number of sawtooth waves you need by dividing the lenof (ts) by the frequency. 
        points_for_one_wave = int(math.floor(len(ts)/self.freq))
        points_for_left_side_wave = points_for_one_wave - 1
        #points_for_left_side_wave = add(points_for_one_wave, -1)
        points_for_right_side_wave = 1
        y_spacing_for_each_point = 2/points_for_left_side_wave
        
        ys = numpy.array([])
        for k in range(0, self.freq): 
        
            ys_left = numpy.array([])
            ys_right = numpy.array([])
             
            for i in range(0, points_for_left_side_wave): 
                ys_left = numpy.append(ys_left, (-1 + y_spacing_for_each_point*i))
            #for j in range(0, points_for_right_side_wave): 
             #   ys_right = 1 - y_spacing_for_each_point*j
            ys_right = -1
            ys_one = numpy.append(ys_left, ys_right)
            ys = (ys, ys_one)
        return ys
        
    def evaluate_v2(self, ts): 
        
        print(ts)
#        ys_l = numpy.array([])
#        ys_r = numpy.array([])
#        points_for_one_wave = math.floor(len(ts)/self.freq)
#        points_for_left_side_wave = points_for_one_wave - 1.0
#        points_for_right_side_wave = 1
#                points_for_one_wave = math        points_for_one_wave = math.floor(len(ts)/self.freq)
        points_for_left_side_wave = points_for_one_wave - 1.0
        points_for_right_side_wave = 1
        #.floor(len(ts)/self.freq)
        points_for_left_side_wave = points_for_one_wave - 1.0
        points_for_right_side_wave = 1
        
        ts = ts*(99999999999999999999999999999999)
        fractional, integers = numpy.modf(ts)
#        for i in range(0, points_for_left_side_wave):
#            this = math.fmod(ts[i], points_for_left_side_wave)
#            ys_l = numpy.append(ys_l, this)
#        for j in range(0, points_for_right_side_wave): 
#            this2 =  math.fmod(ts[j], 1)
#            ys_r = numpy.append(ys_r,this2) 
            
        return fractional
        
        #modulo divider for floats pmodulo divider for floats python ython 
        
        