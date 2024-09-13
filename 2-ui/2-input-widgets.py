import streamlit as st
from  datetime import datetime 
st.title('Streamlit Input Widgets!')

st.markdown("## Text Inputs")
txt = st.text_input('Enter your name:', value='John Doe')
st.text(f"OUTPUT: {txt}, type: {type(txt)}")
pw = st.text_input('Enter your password:', type="password")
st.text(f"OUTPUT: {pw}, type: {type(pw)}")
txta = st.text_area('Leave a comment:', value='Type here...')
st.text(f"OUTPUT: {txta}, type: {type(txta)}")
st.divider()

st.markdown("## Binary Widgets")
chk = st.checkbox('I agree to the terms and conditions', value=False)
st.text(f"OUTPUT: {chk}, type: {type(chk)}")
tog = st.toggle('Enable notifications', value=False)
st.text(f"OUTPUT: {tog}, type: {type(tog)}")
st.divider()

st.markdown("## Date / Time Widgets")
dt =st.date_input('Select a date:')
st.text(f"OUTPUT: {dt}, type: {type(dt)}")
tm = st.time_input('Select a time:')
st.text(f"OUTPUT: {tm}, type: {type(tm)}")
st.divider()

st.markdown("## Number Widgtets")
numi = st.number_input('Enter Hourly Wage:', value=7.25, max_value=20.0, min_value=5.25, step=0.25)
st.text(f"OUTPUT: {numi}, type: {type(numi)}")
nums = st.slider('Pick a number between 1 and 20:', min_value=1, max_value=20, value=10, step=1)
st.text(f"OUTPUT: {nums}, type: {type(nums)}")
st.divider()

st.markdown("## Selection Widgets")
selbox = st.selectbox('Choose one shipping method:', ['Jiffy Express', ' You Pee Es', 'FedUp Express'])
st.text(f"OUTPUT: {selbox}, type: {type(selbox)}")
mulselbox = st.multiselect('Select all your favorite colors:', ['Red', 'Green', 'Blue', 'Yellow', 'White'])
st.text(f"OUTPUT: {mulselbox}, type: {type(mulselbox)}")
selslider = st.select_slider('Rate us:', options=['1=Poor','2=ok','3=good','4=great','5=excellent'], value = '3=good')
st.text(f"OUTPUT: {selslider}, type: {type(selslider)}")
radio = st.radio('Rate us:', ['1=Poor','2=ok','3=good','4=great','5=excellent'], index=2, horizontal=True)
st.text(f"OUTPUT: {radio}, type: {type(radio)}")
st.divider()


st.markdown("## 'Other' Widgets")
feed = st.feedback('faces')
st.text(f"OUTPUT: {feed}, type: {type(feed)}")
color = st.color_picker('Pick a color:', value='#00f900')
st.text(f"OUTPUT: {color}, type: {type(color)}")
file = st.file_uploader('Upload a file:')
st.text(f"OUTPUT: {file}, type: {type(file)}")
pic = st.camera_input('Take a selfie:')
st.text(f"OUTPUT: {pic}, type: {type(pic)}")
st.divider()



