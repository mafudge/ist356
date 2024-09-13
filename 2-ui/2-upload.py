import streamlit as st
from io import StringIO # required to convert binary to text


st.title("File Upload Example")
st.markdown('''
This example demonstrates how to process and uploaded file. 
            
- The first example can process and file-like (image, video, data for a dataframe, etc)
- The second example shows how to process text explicitly.
            
''')
bin_file_data = st.file_uploader("Upload an image/photo file", type=["png", "jpeg", "jpg", "gif"])
text_file_data = st.file_uploader("Upload a text file", type=["txt", "csv", "md"])

if bin_file_data:
    st.markdown(f"### {bin_file_data.name}")
    st.image(bin_file_data)

if text_file_data:
    st.markdown(f"### {text_file_data.name}")
    binary_contents = text_file_data.getvalue()
    # Convert binary to text
    text_contents = StringIO(binary_contents.decode("utf-8")).read() 
    st.text(text_contents)

print(text_file_data)