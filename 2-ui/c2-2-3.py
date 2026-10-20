import streamlit as st

st.title("Order Processor")

# initialize variables
total = 0.0
count = 0

# input
file = st.file_uploader("Upload Text File:", 
                        type=["txt"])
# process
if file is not None:
    for line in file:
        try:
            amount = float(line.strip())
            total += amount
            count += 1
        except ValueError:
            st.error(f"Invalid amount: {line.strip()}") 

# output
st.write(f"Total Amount: ${total}")
st.write(f"Total Orders: {count}")