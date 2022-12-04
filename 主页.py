# coding=utf-8
# pip install pandas -i https://mirrors.aliyun.com/pypi/simple
# pip install -U requests[security]
""" my_wx: windforyou_ """
import numpy
import pandas

run_url = 'http://192.168.43.240:8501'

import streamlit as st

# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )
#
# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

left_column, right_column, bb = st.columns(3)
# You can use a column just like st.sidebar:
if left_column.button('Press me!'):
    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")
    with bb:
        '133'