import streamlit as st
# adding the selectbox in the sidebar
add_selectbox = st.sidebar.selectbox(
    "What Language do you prefer",
    ("Java", "Python", "C++")
)
# adding the radio button in the sidebar
st.sidebar.radio('Where do you work',('Amazon','Microsoft','Google'))
'''#importing library
import time
import streamlit as st
# here we are taking an element an overwriting it 
with st.empty():
    for seconds in range(60):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
st.write("✔️ 1 minute over!")'''