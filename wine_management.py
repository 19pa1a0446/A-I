# -*- coding: utf-8 -*-
"""Wine Management

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vUwXB_hbPUCpIo-jaOnb9wAriZk_bTaG

# **Description**
OUR DATA IS ABOUT *WINE* *MANAGEMENT*

**COUNTRY**     :Name of the country

**DESCRIPTION** :Type of wine

**DESIGNATION** :Action of choosing wine to hold 

**POINTS**      :Points gained by wine

**PRICE**       :Price of wine

**PROVINCE**    :Principal administrative division of a country 

**REGION1**     :Region of manufacture

**REGION2**     :Region of manufacture

**VARIETY**     :Quality of wine

**WINERY**      :An establishment where wine is made
"""

#import pandas 
import pandas as pd
wine= pd.read_csv('/content/winemag-data_first150k.csv')
print(wine)