# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LS0o-8qO6Qm_ocYM6G9j_aTkn_eRMnQI
"""

https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv

import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

df.head()

df.tail()

df_agrupado_por_dia = df.groupby('day', sort=False).agg({'total_bill':np.sum}).reset_index()

df_agrupado_por_dia

px.bar(df_agrupado_por_dia, x='day', y='total_bill')

df_agrupado_por_dia_e_sexo = df.groupby(['day','sex'], sort=False).agg({'total_bill':np.sum}).reset_index()

df_agrupado_por_dia_e_sexo

px.bar(df_agrupado_por_dia_e_sexo, x= 'day' , y='total_bill' , color ='sex', barmode='group')

px.bar(df_agrupado_por_dia_e_sexo, y= 'day' , x='total_bill' , color ='sex', barmode='group', orientation='h')

px.scatter(df, x='total_bill', y='tip', color='day' , hover_name='time')

qtd_pedidos_dia = df['day'].value_counts()

qtd_pedidos_dia.index

qtd_pedidos_dia.values

px.pie(names=qtd_pedidos_dia.index ,values=qtd_pedidos_dia.values )