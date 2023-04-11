import streamlit as st
from streamlit_option_menu import option_menu
import SnipRead.Summary_page as sp
import QueryPal.Question_page as qp
from home import homeWork as hW

st.set_page_config(layout="wide",page_title="AI Professor",page_icon="balloon")

#if you want a sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="SpeedBar",
        options = ["Home",
                   "SnipRead",
                   "QueryPal"],
        menu_icon=["lightning"],
        icons= ["house","scissors","robot"],
        default_index= 0,
    )

# If you want it in middle of the page, uncomment down!
    
# selected = option_menu(
#         # menu_title="SpeedBar",
#         menu_title=None,
#         options = ["Home",
#                    "SnipRead",
#                    "QueryPal"],
#         # menu_icon=["lightning"],
#         icons= ["house","scissors","robot"],
#         default_index= 0,
#         orientation= "horizontal"
#     )

if selected == "Home":
    hW()
if selected == "SnipRead":
    sp.Snip()
if selected == "QueryPal":
    qp.Query()