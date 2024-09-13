import streamlit as st

from io import StringIO # required to convert binary to text

st.title("Order File Processing")
text_file_data = st.file_uploader("Upload the order file", type=["txt"])

if text_file_data:
    binary_contents = text_file_data.getvalue()
    # Convert binary to text
    text_contents = StringIO(binary_contents.decode("utf-8")).read() 
    total = 0
    count = 0
    for line in text_contents.split("\n"):
        try:
            order = float(line)
            total = total + order
            count = count + 1
        except ValueError:
            continue 
    st.info(f"Number of orders: {count}", icon="➕")
    st.info(f"Total amount: ${total:.2f}", icon="💵")
