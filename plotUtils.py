from inputUtils import input

class visualize:
    def __init__(self, input ):
        self.inputconfig = input

    #animation
    def contourGif(self):
 #       time_array=np.linspace(2020,4980,149)
 #       if self.pML1>95:
 #           time_array=np.linspace(5020,7980,149)
        duration=6
        size=len(time_array)
        fig=plt.figure()
        # DRAW A FIGURE WITH MATPLOTLIB
        def make_frame(t):
            plt.clf()


            im = plt.contourf(data[int(t*size/duration)])
            plt.clim(-60,40)
            plt.colorbar()
            def setvisible(self,vis):
                for c in self.collections: c.set_visible(vis)
            im.set_visible = types.MethodType(setvisible,im)
            im.axes = plt.gca()


            plt.title(self.plot_title)
            return mplfig_to_npimage(fig)

        data=[]
        for time in time_array:
            d=self.inputconfig.inputSpiralWave(time)
            data.append(d)
        # ANIMATE WITH MOVIEPY (UPDATE THE CURVE FOR EACH t). MAKE A GIF.
        animation =mpy.VideoClip(make_frame, duration=duration)
        plt.title(self.plot_title)
        checkDirExists(self.Visualdirect)

        animation.write_gif(os.path.join(self.Visualdirect,u'%s.gif'%(self.coupleAndNoise)), fps=20)