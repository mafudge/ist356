import streamlit as st

# initialize
if 'total' not in st.session_state:
    st.session_state.total = 0.0
if 'history' not in st.session_state:
    st.session_state.history = []

st.title('Order Total and History')
amount = st.number_input("Amount:")
btn_add = st.button('Add to Total')
btn_clear = st.button('Clear')

if btn_add:
    st.session_state.history.append(amount)
    st.session_state.total = sum(st.session_state.history)
    st.write(f"TOTAL: {st.session_state.total}")
    st.write("HISTORY:")
    for h in st.session_state.history:
        st.write(h)

if btn_clear:
    st.session_state.history = []
    st.session_state.total = 0.0
