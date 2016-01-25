import matplotlib as mpl
#For Spatial Patterns
# axes.titlesize = 30
# axes.labelsize = 25
# xtick.labelsize = 25
# ytick.labelsize = 25
# subplots_adjust(left = 0.15,bottom = 0.14,right = 0.9,top = 0.9)
paramsForSpatialPattern={
    'axes.titlesize':30,
    'axes.labelsize':25,
    'xtick.labelsize':25,
    'ytick.labelsize':25
}

#For Indicator
# axes.titlesize = 25
# axes.labelsize = 20
# xtick.labelsize = 20
# ytick.labelsize = 20
# subplots_adjust(left = 0.15,bottom = 0.14,right = 0.9,top = 0.9)
paramsForIndicator={
    'axes.titlesize':25,
    'axes.labelsize':20,
    'xtick.labelsize':20,
    'ytick.labelsize':20,
    'legend.fontsize':20,
    'legend.frameon':False
}


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
mpl.rcParams['axes.labelsize']=20#'large'use 18


#ticks
#xticks
mpl.rcParams['xtick.major.size']=5
mpl.rcParams['xtick.minor.size']=2
mpl.rcParams['xtick.major.width']=1.5
mpl.rcParams['xtick.minor.width']=0.5
mpl.rcParams['xtick.labelsize']=20

#yticks
mpl.rcParams['ytick.major.size']=5
mpl.rcParams['ytick.minor.size']=2
mpl.rcParams['ytick.major.width']=1.5
mpl.rcParams['ytick.minor.width']=0.5
mpl.rcParams['ytick.labelsize']=20


#legend
mpl.rcParams['legend.fontsize']=20
mpl.rcParams['legend.frameon']=False

#saving figures
mpl.rcParams['savefig.dpi']=100
mpl.rcParams['savefig.facecolor']='white'
#mpl.rcParams['savefig.format']='tiff'

mpl.rcParams.update(paramsForIndicator)




