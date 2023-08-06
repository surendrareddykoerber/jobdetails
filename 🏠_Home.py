import streamlit as st
from streamlit_card import card
from streamlit_star_rating import st_star_rating
from streamlit_marquee import streamlit_marquee
import pygwalker as pyg
import pandas as pd
from st_chat_message import message

# Header template
html_temp = """
    <body style="background-color:red;">
    <div style="background-color:tomato;padding:10px">
    <h3 style="color:white;text-align:center;"> Job Opening Details</h3>
    </div>
    </body>
"""
# Hide Styles
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
# Page Config details
st.set_page_config(
        page_title = 'jobopenings',
        page_icon = "✍",
        layout = "wide",
        initial_sidebar_state = "expanded"
    )

def main():
    """
    This function contains the streamlit code details
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    card(
        title="",
        text="",
        image="https://resourseas.com/wp-content/uploads/2021/01/Job-Openings-we-are-hiring-1.jpg",
        url="",
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🚀 Cloud Architect",
    "🚀 Cloud Engineer",
    "🚀 Cloud Tester",
    "🚀 IAM Developer",
    "🚀 Kafka Developer"
    ])

    with tab1:
        st.subheader("Positions: 1")
        st.write("Job Description")
        st.write("Self Review checklist")

    df = pd.read_csv('./openings.csv')
    pyg.walk(df, env='Streamlit')

    

    # message("Hello world!", is_user=True)
    # message("Hi")

    # st_star_rating(label = "Rate you experience", maxValue = 5, defaultValue = 3, key = "rating", emoticons = True )
    # streamlit_marquee(**{
    # # the marquee container background color
    # 'background': "#ff0000",
    # # the marquee text size
    # 'fontSize': '12px',
    # # the marquee text color
    # "color": "#ffffff",
    # # the marquee text content
    # 'content': 'here is custom marquee component~',
    # # the marquee container width
    # 'width': '600px',
    # # the marquee container line height
    # 'lineHeight': "35px",
    # # the marquee duration
    # 'animationDuration': '5s',
    # })
        


# main function call
if __name__ == '__main__':
    main()