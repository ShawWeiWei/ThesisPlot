import matplotlib as mpl

#line
mpl.rcParams['lines.linewidth']=2
#mpl.rcParams['lines.style']='-'
mpl.rcParams['axes.color_cycle']='black'

plotCharacter=['k-','k--','k-.','k:','k*-']

#text
mpl.rcParams['text.color']='black'


#axes
mpl.rcParams['axes.linewidth']=1.5
mpl.rcParams['axes.titlesize']=25#'large'
mpl.rcParams['axes.labelsize']=18#'large'


#ticks
#xticks
mpl.rcParams['xtick.major.size']=5
mpl.rcParams['xtick.minor.size']=2
mpl.rcParams['xtick.major.width']=1.5
mpl.rcParams['xtick.minor.width']=0.5
mpl.rcParams['xtick.labelsize']=14

#yticks
mpl.rcParams['ytick.major.size']=5
mpl.rcParams['ytick.minor.size']=2
mpl.rcParams['ytick.major.width']=1.5
mpl.rcParams['ytick.minor.width']=0.5
mpl.rcParams['ytick.labelsize']=14



#saving figures
mpl.rcParams['savefig.dpi']=100
mpl.rcParams['savefig.facecolor']='white'
#mpl.rcParams['savefig.format']='tiff'




