import streamlit as st

from figures import *

output = df6.melt(id_vars=['COLA'], 
                  value_vars=['COLB', 'COLC'],
                  var_name='department',
                  value_name='amount')

st.write(output)
#, var_name='variable', value_name='value'