import ctypes
import numpy as np
import numpy.ctypeslib as ctl

from photonpy import Context


class DSplineMethods:
    def __init__(self, ctx:Context):
        self.lib = ctx.smlm.lib

        #void DSpline_LLWeightsGradient(Vector3f* emitterPos, const float* emitterIntensities,
    	#int emitterCount, int roisize, Int3& splineDims, 
    	#const float* weights, float* weightsGradient, float* partialWeightGradients, const float* pixels, 
        #const float* pixelBackgrounds, const float* expval, bool cuda)

        self._DSpline_LLWeightsGradient = self.lib.DSpline_LLWeightsGradient
        self._DSpline_LLWeightsGradient.argtypes = [
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # pos
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # intensities
            ctypes.c_int32,  # count
            ctypes.c_int32,  # roisize
            ctl.ndpointer(np.int32, flags="aligned, c_contiguous"),  # splinedims
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # weightsgradient
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # pwg
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # pixels
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # bg
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # expval
            ctypes.c_bool  # cuda
        ]

        #void DSpline_Eval(Vector3f* pos, int count, int roisize, const Int3& splineDims, 
            #float* weights, float* output)
        self._DSpline_Eval = self.lib.DSpline_Eval
        self._DSpline_Eval.argtypes = [
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # pos
            ctypes.c_int32,  # count
            ctypes.c_int32,  # roisize
            ctl.ndpointer(np.int32, flags="aligned, c_contiguous"),  # splinedims
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # weights
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # output
        ]

    def Eval(self, pos, roisize, weights):
        pos = np.ascontiguousarray(pos,dtype=np.float32)
        assert pos.shape[1] == 3
        splinedims = np.array(weights.shape,dtype=np.int32)
        weights = np.ascontiguousarray(weights, dtype=np.float32)
        output = np.zeros((len(pos),roisize,roisize),dtype=np.float32)
        self._DSpline_Eval(pos, len(pos), roisize, splinedims, weights, output)
        return output

    def ComputeWeightsGradient(pos, intensities, roisize, splineWeights, pixels, pixelBg):
        ...

if __name__ == "__main__":
    with Context() as ctx:
        dsm = DSplineMethods(ctx)
        
        roisize = 10
        D = 4
        pos = [[roisize*0.5,roisize*0.5,D*0.5]]
        
        weights = np.zeros((D,W,W,8),dtype=np.float32)
        
        output = dsm.Eval(pos, roisize, weights)


