from inputUtils import input
from Constants import *
from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy
import matplotlib.pyplot as plt
from utils import *
import types
import os
import plotsetting


class visualize:
    def __init__(self, input_config):
        self.input_config = input_config



    def _getFileConfFunc(self, key):
        func_name = FUNC_SET_PREFIX + key
        func = getattr(self.input_config.file_configure, func_name)
        return func

    def testPlot(self):
        plt.plot([1, 2, 3])
        plt.title("TITLE")
        plt.xlabel("XLABEL")
        plt.ylabel("YLABEL")
        plt.savefig('/Users/yes/saved_pic')

    # animation
    def contourGif(self):
        duration = 6
        size = len(time_array)
        fig = plt.figure()

        # DRAW A FIGURE WITH MATPLOTLIB
        def make_frame(t):
            plt.clf()

            im = plt.contourf(data[int(t * size / duration)])
            plt.clim(-60, 40)
            plt.colorbar()

            def setvisible(self, vis):
                for c in self.collections: c.set_visible(vis)

            im.set_visible = types.MethodType(setvisible, im)
            im.axes = plt.gca()

            # plt.title(self.plot_title)
            return mplfig_to_npimage(fig)

        data = []
        for time in time_array:
            d = self.input_config.inputSpiralWave(time)
            data.append(d)
        # ANIMATE WITH MOVIEPY (UPDATE THE CURVE FOR EACH t). MAKE A GIF.
        animation = mpy.VideoClip(make_frame, duration=duration)
        # plt.title(self.plot_title)
        self._checkDirExists()
        animation.write_gif(os.path.join(self.input_config.visual_direct, u'%s.gif' % self.input_config.spec), fps=20)

    def plotSpiralWaves(self, listoftime=time_array):
        filter_array = listoftime[-25:]  # filter(lambda x:int(x)>4500,time_array)    
        for t in filter_array:
            data = self.input_config.inputSpiralWave(t)
            plt.clf()
            plt.contourf(data)
            plt.xlabel('Network Column Index')
            plt.ylabel('Network Row Index')
            plt.clim(-60, 40)
            cbar = plt.colorbar()
            checkDirExists(self.input_config.visual_direct)
            plt.savefig(os.path.join(self.input_config.visual_direct, u'%s_t=%.5f.png' % (self.input_config.spec_out, t)))
            del cbar

    def plotHeterFiringRate(self, key, value, xlabel=""):
        plt.clf()
        func = self._getFileConfFunc(key)
        quant = []
        for i, val in enumerate(value):
            func(val)
            data = self.input_config.inputAverISI()
            quant.append(1000.0 * np.mean(np.reciprocal(data)))
        plt.plot(value, quant, label=r'$g_s =$ $%.2f$' % gc_ce)
        #        plt.title('(a)')
        plt.legend(loc='best')

        if (xlabel == ""):
            plt.xlabel(xlabel)
        else:
            plt.xlabel(u'Percentage of Type I Neurons(%)')
        plt.ylabel(u'Population Firing Rate(Hz)')
        # plt.xlabel(r'$p ( \% ) $')
        # plt.ylabel(r'$f$')
        # self._checkDirExists()
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, midname, u'_Heter_FiringRate'))

        data = listTupleToArray(value, quant)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, midname, u'_Heter_FiringRate.txt'),
                   data)
