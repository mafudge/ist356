import streamlit as st

st.title('Streamlit Output Widgets!')

st.markdown("## Text Output")
st.text("Plain text.\nObeys newlines.")

st.markdown("## Markdown Output")
st.markdown('''
### Heading 3
- this
- is a
- list
            
Learn markdown here: [https://www.markdownguide.org/getting-started/](https://www.markdownguide.org/getting-started/)
''')

st.markdown("## Code Output")
st.code('''
name = input("Enter your name:")
print(f"Hello, {name}")
''', language="python", line_numbers=True)

st.markdown("## Image Output")
st.image("https://ist256.com/images/logo.png",caption="IST256 logo")
st.image("https://images.unsplash.com/photo-1552728089-57bdde30beb3?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8YmlyZHxlbnwwfHwwfHx8MA%3D%3D",
         width=200)
st.markdown("## Metric / Card Ouput")
st.metric(label="Temperature", 
          value="70 °F", 
          delta="- 1.2 °F")
st.metric(label="Mike Fudge", value="B+", delta="-5 pts")
st.metric(label="MSFT", value="$36.00", delta="-0.15")

st.markdown("## Video Output")
st.video("https://youtu.be/soVItkifdms?si=eNNbRXnAg4efcJGi")

st.markdown("## Audio Output")
st.audio("https://file-examples.com/storage/fe6993554766e3161a375a5/2017/11/file_example_MP3_700KB.mp3")

st.markdown("## Toast Output")
if st.button("Click to show toast"):
    st.toast("Congrats! You clicked it!", 
             icon=":material/block:")

st.markdown("## Column Layouts")
col1, col2, col3 = st.columns(3)
col1.markdown("Hello")
col2.text("There")
col2.text("Mike")
with col3:
    st.warning("Warning!")
    st.error("Error!")
    st.success("Success!")

st.markdown("## Tab Layouts")
col1, col2, col3 = st.tabs(["Tab A","Tab B","Tab C"])
col1.markdown("Hello")
with col2:
    st.text("There")
    st.text("Mike")
with col3:
    st.warning("Warning!")
    st.error("Error!")
    st.success("Success!")

st.markdown("## Expander Output")
with st.expander("See a map"):
    st.write('Here is a map for you!')
    st.map(latitude=76,longitude=-43, zoom=13)