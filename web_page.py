import streamlit as st  # Importing the Streamlit library for building the app
import langchain_support as LC  # Importing a custom module for LangChain support
import os  # Importing os module to work with file paths


# Function to resolve the absolute path for a given relative path
def resolve_path(path):
    return os.path.abspath(os.path.join(os.getcwd(), path))


# Page Configurations
# Setting up the basic configurations for the Streamlit app
st.set_page_config(
    page_title="Book Content Maker",  # Title of the page
    page_icon="📚",  # Icon displayed in the browser tab
    layout="centered",  # Layout style of the app
    initial_sidebar_state="collapsed"  # Sidebar initially collapsed
)

# Page Title
# Displaying the main title of the app
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>📚 Book Content Maker</h1>",  # Title in HTML with inline styling
    unsafe_allow_html=True  # Allowing HTML in markdown
)

# Subtitle
# Displaying a subtitle for additional context
st.markdown(
    "<p style='text-align: center; color: #6c757d;'>Generate chapters and content effortlessly for your books!</p>",
    # Subtitle in HTML
    unsafe_allow_html=True
)

# Input Section
# Prompting the user to input a book name
st.markdown("### Enter the Book Name Below:")  # Header for input section
Book_name = st.text_input("", placeholder="Type the book name here...")  # Text input field with a placeholder

# Generate Content Button
# Checking if the user has entered a book name
if Book_name:
    # Displaying a spinner while processing the request
    with st.spinner("Generating content... Please wait!"):
        try:
            # Using the LangChain module to generate content for the entered book name
            content = LC.get_paagraph_content(Book_name)['output']

            # Displaying the generated content
            st.markdown("### Generated Content:")
            st.markdown(
                f"<p style='color: blue; font-size: 16px;'>{content}</p>",  # Displaying content with styling
                unsafe_allow_html=True
            )
        except Exception as e:
            # Handling any errors during the content generation process
            st.error(f"An error occurred: {e}")
else:
    # Prompting the user to enter a book name if none is provided
    st.info("Please enter a book name to get started.")

# Footer
# Adding a footer with attribution and a link to Streamlit
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: small; color: #6c757d;'>
    Built with ❤️ using <a href='https://streamlit.io/' target='_blank' style='text-decoration: none; color: #007bff;'>Streamlit</a>
    </p>
    """,
    unsafe_allow_html=True  # Allowing HTML in the footer
)
