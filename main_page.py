import streamlit as st
from PIL import Image
import base64


def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Set up the page config
logo_path = 'UC_logo.png'  # Confirm this path is correct
logo = Image.open(logo_path)
logo_base64 = get_image_base64(logo_path)
st.set_page_config(page_title="Enhancing Decision-Making in Human Agent Team", page_icon=logo, layout='wide')

# Import the modules for different pages
from _farm_page import page_farm
from _finance_page import page_finance
from _digital_page import page_digital_security
from _health_page import page_dietary_health

# Initialize navigation state if not already done
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'main'  # Default to main page

def main():
    # Navigation header with logo
    cols = st.columns([1, 1, 1])
    with cols[1]:
        st.markdown(
            f"<img src='data:image/png;base64,{logo_base64}' style='margin-left: 90px; width: 120px;'/>",
            unsafe_allow_html=True
        )
        st.write("""
            <h1 style='text-align: left; margin-left: -30px;'>Human Agent Team</h1>
        """, unsafe_allow_html=True)

    # Display navigation buttons
    page_options = {
        "🏠 Home": 'main',  # Using the house emoji as the Home icon
        "🚜 Irrigation Practices for Dairy Farms": 'farm',
        "🏦 Financial Literacy Decisions": 'finance',
        "🥦 Dietary Health Decisions": 'health',
        "🔒 Digital Security": 'security'
    }

    for page_name, page_key in page_options.items():
        if st.button(page_name):
            st.session_state['current_page'] = page_key

    # Adding a horizontal line after navigation
    st.markdown("<hr>", unsafe_allow_html=True)
    # Conditional rendering based on the navigation state
    if st.session_state['current_page'] == 'main':
        pass
    elif st.session_state['current_page'] == 'farm':
        page_farm()
    elif st.session_state['current_page'] == 'finance':
        page_finance()
    elif st.session_state['current_page'] == 'health':
        page_dietary_health()
    elif st.session_state['current_page'] == 'security':
        page_digital_security()


if __name__ == "__main__":
    main()
