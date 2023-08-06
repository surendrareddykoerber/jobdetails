import streamlit as st

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

    #st.header("📘Azure Resource Naming Tool")
    st.write('\n')


# main function call
if __name__ == '__main__':
    main()