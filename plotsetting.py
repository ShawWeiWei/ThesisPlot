import matplotlib.pyplot as plt
import matplotlib as mpl

#line
mpl.rcParams['lines.linewidth']=2
mpl.rcParams['lines.style']='-'
mpl.rcParams['lines.color']='black'


#text
mpl.rcParams['text.color']='black'


#axes
mpl.rcParams['axes.linewidth']=1.0
mpl.rcParams['axes.titlesize']='large'
mpl.rcParams['axes.labelsize']='large'


#ticks
#xticks
mpl.rcParams['xtick.major.size']=4
mpl.rcParams['xtick.minor.size']=2
mpl.rcParams['xtick.major.width']=0.5
mpl.rcParams['xtick.minor.width']=0.5

#yticks
mpl.rcParams['ytick.major.size']=4
mpl.rcParams['ytick.minor.size']=2
mpl.rcParams['ytick.major.width']=0.5
mpl.rcParams['ytick.minor.width']=0.5


#saving figures
mpl.rcParams['savefig.dpi']=400
mpl.rcParams['savefig.facecolor']='white'
mpl.rcParams['savefig.format']='tiff'


