import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from icecream import ic
from matplotlib.colors import BoundaryNorm, ListedColormap


FileName = 'Dane_do_heatmapy'
ColorMaps = ['viridis','plasma','inferno','magma','cividis',
             'rocket','icefire','coolwarm',
             'hsv','tab20','tab20b','tab20c']
 
df = pd.read_csv(FileName+'.csv',sep=';',index_col=0)
df = df.dropna(axis=1)

FigureWidth, FigureHeight = 10,5
Scale = 1.0

Splits = [np.arange(0,0.05,.01),
          np.arange(0.05,0.1,.025),
          np.arange(0.1,0.5,0.1),
          np.arange(0.5,2.5,0.5),
          np.arange(2.5,15,2.5),
          np.arange(15,90,15)]

bounds  = []
for spl in Splits:
    bounds = np.append(bounds,spl)

for ColorMap in ColorMaps:
    nColorMap = plt.colormaps[ColorMap]
    Colors = nColorMap(np.linspace(0, 1, len(bounds)-1))
    uColorMap = ListedColormap(Colors)
    Norm = BoundaryNorm(bounds, ncolors=len(Colors))

    fig, ax = plt.subplots(figsize=(FigureWidth*Scale,FigureHeight*Scale)) 
    sns.heatmap(df.T,
                cmap=uColorMap,
                norm=Norm,
                ax = ax,
                robust=False,
                square=True,
                annot=False
                )
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    fig.tight_layout()
    fig.savefig(FileName+'-'+ColorMap+'.png',bbox_inches='tight',dpi=200)
    fig.savefig(FileName+'-'+ColorMap+'.pdf',bbox_inches='tight',dpi=200)