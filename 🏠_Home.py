import streamlit as st
from streamlit_card import card

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
        


# main function call
if __name__ == '__main__':
    main()