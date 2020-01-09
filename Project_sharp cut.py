# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:12:56 2019

@author: stae
"""

# usual packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

COSMOS = pd.read_csv('match_COSMOS_99_without_err.csv')
COSMOS_rv = COSMOS.replace(to_replace = -99, value = None)
COSMOS_rv = COSMOS_rv.replace(to_replace = -99.900000, value = None)
COSMOS_rv = COSMOS_rv.replace(to_replace = -99.0, value = None)
COSMOS_rv = COSMOS_rv.replace(to_replace = -9.9999, value = None)
print(COSMOS_rv)


################################
def HISTO(x,bn=10,df=COSMOS_rv):
    #Return the figure object with the histogram of x 
    #where x is the keywords from the pandas dataframe df. 
    #You can add features outside the function 
    #to the current instance of the figure, e.g. plt.xlim() or plt.title()
    fig = plt.figure(figsize=(10,8))
    #plt.hist(df[x],bins=bn,histtype='step',lw=3)
    #plt.hist(df[x],bins='auto', range = (-1, 5))
    plt.hist(df[x],bins='auto')
    plt.xlabel(x,fontsize=25)
    plt.ylabel('counts',fontsize=25)
    plt.xlim(20, 25)
    plt.savefig(x)
    return fig 



#HISTO('B_MAG_APER2')
#HISTO('H_MAG_APER2')
#HISTO('Hw_MAG_APER2')
#HISTO('IA484_MAG_APER2')
#HISTO('IA527_MAG_APER2')
#HISTO('IA624_MAG_APER2')
#HISTO('IA679_MAG_APER2')
#HISTO('IA738_MAG_APER2')
HISTO('IA767_MAG_APER2')
HISTO('IB709_MAG_APER2')
HISTO('IB827_MAG_APER2')
HISTO('NB711_MAG_APER2')
HISTO('NB816_MAG_APER2')
HISTO('Y_MAG_APER2')
HISTO('ip_MAG_APER2')
HISTO('zpp_MAG_APER2')
HISTO('Z_MINCHI2')
HISTO('zspec')




plt.show()

