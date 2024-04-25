import streamlit as st
import random

def set_custom_css():
    custom_css = """
    <style>
        /* Targeting the generic HTML elements used by Streamlit for radios */
        div[data-testid="stRadio"] label {
            font-size: 20px !important;  /* Larger font size for readability */
            font-weight: bold !important; /* Adding bold for better visibility */
        }
        /* Applying styles to all paragraph text */
        p {
            font-size: 18px !important; /* Larger font size for regular text */
        }
        /* Customizing the main page title font size */
        .main .block-container > h1 {
            font-size: 30px !important; /* Smaller font size for the main page title */
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Apply the custom CSS as soon as possible in your app's execution
set_custom_css()

st.title("Optimising Irrigation Practices for Dairy Farms: A Decision-Making Guide")

questions = {
    "Q1": "What is the primary consideration for starting spring irrigation on a dairy farm?",
    "Q2": "What is the most accurate method to assess soil moisture before initiating irrigation?",
    "Q3": "What key factor influences the choice of an irrigation system for dairy farming?",
    "Q4": "Why is it important to understand the water holding capacity (WHC) of your soil?",
    "Q5": "What routine maintenance is essential for maintaining irrigation efficiency?",
    "Q6": "How should irrigation frequency be adjusted throughout the growing season?",
    "Q7": "Which irrigation method minimizes water loss in sandy soils?",
    "Q8": "What are the risks of irrigating when the soil is at field capacity?",
    "Q9": "What role does an efficient pump play in an irrigation system?",
    "Q10": "How should rainfall data integrate into irrigation planning?",
    "Q11": "What common installation error should be avoided with irrigation nozzles?",
    "Q12": "What is a major benefit of variable speed drives on irrigation pumps?",
    "Q13": "What is the best strategy for irrigation during periods of high evapotranspiration?",
    "Q14": "Why should irrigation systems be checked regularly?",
    "Q15": "What should be considered first when installing a new irrigation system?",
    "Q16": "How does the type of irrigation system affect water distribution uniformity?",
    "Q17": "Why should irrigation settings be adjusted according to soil type?",
    "Q18": "How can water wastage be effectively reduced during irrigation?",
    "Q19": "What technique helps prevent nutrient leaching during irrigation?",
    "Q20": "Why is it crucial to maintain correct irrigation pressure?",
    "Q21": "What effect does soil temperature have on irrigation needs?",
    "Q22": "What adjustments are necessary for irrigation during rainy periods?",
    "Q23": "How can irrigation schedules be adjusted to minimize plant stress?",
    "Q24": "How does irrigation equipment configuration affect its effectiveness?",
    "Q25": "What are the best practices for choosing irrigation times to maximize efficiency?",
    "Q26": "How does the choice of crops affect irrigation strategies?",
    "Q27": "What impact does improper irrigation have on soil health?",
    "Q28": "How do return periods affect plant growth in irrigation settings?",
    "Q29": "What role do soil moisture sensors play in efficient irrigation?",
    "Q30": "What are the important end-of-season maintenance actions for irrigation systems?"
}


options = {
    "Q1": {"a": ("Check soil temperature at 10cm depth", "Q2", +2),
           "b": ("Start when other farmers do", "Q3", -1),
           "c": ("Base on the previous year's schedule", "Q4", +1)},
    "Q2": {"a": ("Following a fixed calendar date", "Q5", +1),
           "b": ("Using a soil moisture sensor", "Q6", +2),
           "c": ("Estimating based on appearance", "Q7", -1)},
    "Q3": {"a": ("Ease of operation and maintenance", "Q8", +1),
           "b": ("System's capacity to match peak ET rates", "Q9", +2),
           "c": ("Lowest cost system available", "Q10", -1)},
    "Q4": {"a": ("Water holding capacity is irrelevant", "Q11", -1),
           "b": ("For regulatory compliance", "Q12", +1),
           "c": ("To prevent water logging and nutrient leaching", "Q13", +2)},
    "Q5": {"a": ("Annual system overhaul only", "Q14", +1),
           "b": ("As-needed repairs based on system failures", "Q15", -1),
           "c": ("Regular leak checks and pressure adjustments", "Q16", +2)},
    "Q6": {"a": ("Keep a constant schedule regardless of conditions", "Q17", -1),
           "b": ("Adjust based on evapotranspiration rates", "Q18", +2),
           "c": ("Reduce frequency to save water", "Q19", +1)},
    "Q7": {"a": ("Increasing watering duration", "Q20", -1),
           "b": ("Watering at night to reduce evaporation", "Q21", +1),
           "c": ("Implementing sub-surface drip irrigation", "Q22", +2)},
    "Q8": {"a": ("Leads to under-watering of plants", "Q23", +1),
           "b": ("Has no impact on plant growth", "Q24", -1),
           "c": ("Prevents over-saturation and promotes root oxygenation", "Q25", +2)},
    "Q9": {"a": ("To filter out impurities from water", "Q26", -1),
           "b": ("Pumps are not necessary for modern systems", "Q27", +1),
           "c": ("To deliver water at correct pressure and flow rate", "Q28", +2)},
    "Q10": {"a": ("Use rainfall forecasts only, not historical data", "Q29", +1),
            "b": ("To adjust irrigation based on actual moisture availability", "Q30", +2),
            "c": ("Rainfall should not influence irrigation planning", "Q1", -1)},
    "Q11": {"a": ("Over-tightening, causing damage to threads", +1),
            "b": ("Ignoring nozzle maintenance", -1),
            "c": ("Choosing a mismatched nozzle size", +2)},
    "Q12": {"a": ("Increased system complexity", +1),
            "b": ("No significant benefits", -1),
            "c": ("Energy savings and better water control", +2)},
    "Q13": {"a": ("Maintain usual watering schedule", -1),
            "b": ("Increase irrigation frequency", +2),
            "c": ("Decrease watering frequency to conserve water", +1)},
    "Q14": {"a": ("Only necessary after system failures", -1),
            "b": ("Maintenance is the responsibility of the equipment provider", +1),
            "c": ("To prevent minor issues from becoming major failures", +2)},
    "Q15": {"a": ("Select the cheapest system available", -1),
            "b": ("Evaluate water source and soil type compatibility", +2),
            "c": ("Base decision solely on technology features", +1)},
    "Q16": {"a": ("All systems are essentially the same", -1),
            "b": ("System type does not matter if managed well", +1),
            "c": ("Different systems offer varying levels of water distribution uniformity", +2)},
    "Q17": {"a": ("Soil type only affects the amount of water needed", +1),
            "b": ("Different soils have different irrigation needs", +2),
            "c": ("All soils should be treated the same", -1)},
    "Q18": {"a": ("Water at fixed intervals regardless of need", -1),
            "b": ("Use manual checking to decide when to water", +1),
            "c": ("Implement automated moisture sensors", +2)},
    "Q19": {"a": ("Increase irrigation frequency to promote growth", +1),
            "b": ("Ignore soil saturation levels", -1),
            "c": ("Schedule irrigation to minimize runoff", +2)},
    "Q20": {"a": ("Low pressure can be compensated by longer irrigation times", -1),
            "b": ("High pressure ensures deeper water penetration", +1),
            "c": ("Ensures efficient system operation and reduces wear", +2)},
    "Q21": {"a": ("Higher soil temperatures always require more water", +1),
            "b": ("Colder soil can delay plant growth, requiring adjusted irrigation", +2),
            "c": ("Soil temperature has no significant effect on irrigation needs", -1)},
    "Q22": {"a": ("Increase irrigation to counteract cooling soil temperatures", +1),
            "b": ("Reduce irrigation following significant rainfall", +2),
            "c": ("Continue regular irrigation regardless of rainfall", -1)},
    "Q23": {"a": ("Keep a consistent schedule to simplify management", -1),
            "b": ("Water more frequently to prevent any potential stress", +1),
            "c": ("Adjust schedules to provide water during peak demand times", +2)},
    "Q24": {"a": ("Equipment setup has minimal impact if water is applied", +1),
            "b": ("Advanced features compensate for poor setup", -1),
            "c": ("Proper setup and maintenance ensure maximum efficiency", +2)},
    "Q25": {"a": ("Time of day does not affect irrigation efficiency", -1),
            "b": ("Evening irrigation is most effective for growth", +1),
            "c": ("Early morning irrigation reduces evaporation losses", +2)},
    "Q26": {"a": ("Watering more boosts crop productivity regardless of type", +1),
            "b": ("All crops have similar water requirements", -1),
            "c": ("Crop-specific water needs dictate irrigation frequency and amount", +2)},
    "Q27": {"a": ("Frequent light watering is always best for soil health", +1),
            "b": ("Soil health is unaffected by irrigation methods", -1),
            "c": ("Improper irrigation can lead to soil degradation and salinity issues", +2)},
    "Q28": {"a": ("Minimal irrigation promotes deeper root systems", -1),
            "b": ("Frequent irrigation is necessary regardless of return period", +1),
            "c": ("Longer return periods require careful water management to avoid stress", +2)},
    "Q29": {"a": ("Sensors are unnecessary with modern irrigation systems", -1),
            "b": ("They provide precise data for optimizing irrigation schedules", +2),
            "c": ("Can be used to supplement manual checks", +1)},
    "Q30": {"a": ("Store all equipment fully assembled", -1),
            "b": ("Leave maintenance until next season", +1),
            "c": ("Inspect and repair equipment", +2)}
}

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state['current_question'] = 'Q1'
    st.session_state['user_responses'] = {}
    st.session_state['selected_option'] = None
    st.session_state['total_score'] = 0  # Initialize score
    st.session_state['path_length'] = 0


def navigate_questions():
    # Retrieve the user's selected option
    option_selected = st.session_state.get('selected_option')

    if option_selected is None:
        # If no option is selected, do nothing and prompt the user to select an option
        st.warning('Please select an option before moving to the next question.')
        return  # Return early to avoid processing further

    # Get the tuple associated with the selected option
    option_data = options[st.session_state['current_question']].get(option_selected)

    if option_data is None:
        # Handle unexpected cases where the selected_option does not correspond to a valid choice
        st.error('Selected option is invalid. Please select a valid option.')
        return

    # Extract the next question or endpoint indicator and score change
    if len(option_data) == 2:  # Assuming the endpoint tuples only contain score change and no next question
        score_change = option_data[1]
        next_q = None  # Indicates the endpoint
    elif len(option_data) == 3:
        next_q, score_change = option_data[1], option_data[2]
    else:
        st.error("Invalid option configuration.")
        return

    # Update responses and score
    st.session_state['user_responses'][st.session_state['current_question']] = option_selected
    st.session_state['total_score'] += score_change  # Update score
    st.session_state['path_length'] += 1  # Increment path length by 1 for each navigation

    # Check if it's an endpoint
    if next_q is None:
        st.session_state['current_question'] = None
        st.session_state['endpoint_reached'] = True
    else:
        st.session_state['current_question'] = next_q  # Move to the next question
        st.session_state['selected_option'] = None  # Reset for the next question


def user_page():
    # Check if the page has been manually selected for a reset
    if st.session_state.page == '👤 User Only' and st.session_state.get('reset', False):
        st.session_state['current_question'] = 'Q1'
        st.session_state['total_score'] = 0
        st.session_state['user_responses'] = {}
        st.session_state['endpoint_reached'] = False
        st.session_state['selected_option'] = None
        st.session_state['reset'] = False  # Reset the reset flag

    current_question = st.session_state['current_question']
    if current_question:
        options_list = [(f"{k}: {v[0]}", k) for k, v in options[current_question].items()]
        selected = st.radio(f"{current_question}) {questions[current_question]}", options_list,
                            format_func=lambda x: x[0], index=None, key=f'{current_question}_radio')

        if selected:
            st.session_state['selected_option'] = selected[1]

        if st.button("Next", key=f'{current_question}_next', on_click=navigate_questions):
            pass

    if st.session_state.get('endpoint_reached', False):
        # Display the final score in a bold format
        st.markdown(f"**You've reached the end of the survey with a final score of: {st.session_state['total_score']}**")
        st.markdown(
            f"**You've reached the end of the survey with a total path length of: {st.session_state['path_length']}**")


def user_agent_page():
    st.write("This page is for interaction between the user and an AI agent.")
    current_question = st.session_state['current_question']
    if current_question:
        # List all options for the current question
        options_list = [(f"{k}: {v[0]}", k) for k, v in options[current_question].items()]

        # Display radio buttons for options
        selected = st.radio(f"{current_question}) {questions[current_question]}", options_list,
                            format_func=lambda x: x[0], index=None, key=f'{current_question}_radio')

        # Button to get AI's recommendation
        if st.button("Get AI Recommendation", key=f'{current_question}_recommendation'):
            # Determine AI's recommendation based on the maximum score
            max_score_option = max(options[current_question].items(), key=lambda item: item[1][-1])[0]
            recommended_option = options[current_question][max_score_option][0]
            st.write(f"I recommend: {recommended_option}")

        if selected:
            st.session_state['selected_option'] = selected[1]

        if st.button("Next", key=f'{current_question}_next', on_click=navigate_questions):
            pass

    if st.session_state.get('endpoint_reached', False):
        # Display the final score in a bold format
        st.markdown(
            f"**You've reached the end of the survey with a final score of: {st.session_state['total_score']}**")
        st.markdown(
            f"**You've reached the end of the survey with a total path length of: {st.session_state['path_length']}**")


def initialize_consultant_availability(questions, percentage=0.8):
    question_keys = list(questions.keys())
    num_available = int(len(question_keys) * percentage)
    available_questions = random.sample(question_keys, num_available)
    return set(available_questions)  # Using a set for fast membership testing


# Use this function to initialize which questions will have consultant availability
consultant_available_questions = initialize_consultant_availability(questions)


def user_consultant_page():
    st.write("This page is for interaction between the User and a human consultant.")
    current_question = st.session_state['current_question']
    if current_question:
        options_list = [(f"{k}: {v[0]}", k) for k, v in options[current_question].items()]
        selected = st.radio(f"{current_question}) {questions[current_question]}", options_list,
                            format_func=lambda x: x[0], index=None, key=f'{current_question}_radio')

        if st.button("Get Consultant Recommendation", key=f'{current_question}_consultant_recommendation'):
            if current_question in consultant_available_questions:
                max_score_option = max(options[current_question].items(), key=lambda item: item[1][-1])[0]
                recommended_option = options[current_question][max_score_option][0]
                st.write(f"Consultant recommends: {recommended_option}")
            else:
                st.write("Consultant recommendation is not available for this question.")

        if selected:
            st.session_state['selected_option'] = selected[1]

        if st.button("Next", key=f'{current_question}_next', on_click=navigate_questions):
            pass

    if st.session_state.get('endpoint_reached', False):
        st.markdown(
            f"**You've reached the end of the survey with a final score of: {st.session_state['total_score']}**")
        st.markdown(
            f"**You've reached the end of the survey with a total path length of: {st.session_state['path_length']}**")


def user_agent_consultant_page():
    st.write("This page allows interaction between the user, an AI agent, and a human consultant.")
    current_question = st.session_state['current_question']
    if current_question:
        # List all options for the current question
        options_list = [(f"{k}: {v[0]}", k) for k, v in options[current_question].items()]

        # Display radio buttons for options
        selected = st.radio(f"{current_question}) {questions[current_question]}", options_list, format_func=lambda x: x[0], index=None, key=f'{current_question}_radio')

        # Button to get Consultant's recommendation
        if st.button("Get Consultant Recommendation", key=f'{current_question}_consultant_recommendation'):
            if current_question in consultant_available_questions:
                max_score_option = max(options[current_question].items(), key=lambda item: item[1][-1])[0]
                recommended_option = options[current_question][max_score_option][0]
                st.write(f"Consultant recommends: {recommended_option}")
            else:
                st.write("Consultant recommendation is not available for this question.")

        # Button to get AI's recommendation
        if st.button("Get AI Recommendation", key=f'{current_question}_ai_recommendation'):
            # Determine AI's recommendation based on the maximum score
            max_score_option = max(options[current_question].items(), key=lambda item: item[1][-1])[0]
            recommended_option = options[current_question][max_score_option][0]
            st.write(f"AI recommends: {recommended_option}")

        if selected:
            st.session_state['selected_option'] = selected[1]

        if st.button("Next", key=f'{current_question}_next', on_click=navigate_questions):
            pass

    if st.session_state.get('endpoint_reached', False):
        # Display the final score in a bold format
        st.markdown(f"**You've reached the end of the survey with a final score of: {st.session_state['total_score']}**")
        st.markdown(
            f"**You've reached the end of the survey with a total path length of: {st.session_state['path_length']}**")



# Initialize session state for page navigation if it's not already set
if 'page' not in st.session_state:
    st.session_state.page = '👤 User Only'

# Check and initialize session state values if not already present
def ensure_session_state():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 'Q1'
    if 'user_responses' not in st.session_state:
        st.session_state.user_responses = {}
    if 'selected_option' not in st.session_state:
        st.session_state.selected_option = None
    if 'total_score' not in st.session_state:
        st.session_state.total_score = 0
    if 'endpoint_reached' not in st.session_state:
        st.session_state.endpoint_reached = False
    if 'page' not in st.session_state:
        st.session_state.page = '👤 User Only'
    if 'initial_load' not in st.session_state:
        st.session_state.initial_load = True

# Call this function at the start of your script to ensure all session state variables are initialized
ensure_session_state()

# Define your navigation and page display functions...

# Define a function to reset the state relevant for the navigation
def reset_navigation_state():
    st.session_state['current_question'] = 'Q1'  # Reset to the first question
    st.session_state['total_score'] = 0
    st.session_state['path_length'] = 0
    st.session_state['user_responses'] = {}
    st.session_state['selected_option'] = None
    st.session_state['endpoint_reached'] = False

# Sidebar navigation setup
st.sidebar.title("Human-Agent Team (HAT)")
menu_items = {
    "👤 User Only": user_page,
    "👤💼 User-Consultant Interaction": user_consultant_page,
    "👤🤖 User-AI Interaction": user_agent_page,
    "🤝 User-AI-Consultant Interaction": user_agent_consultant_page
}

# Create navigation links in the sidebar
for item, func in menu_items.items():
    if st.sidebar.button(item):
        # Reset the survey state when the different page is selected
        if item != st.session_state.page:
            reset_navigation_state()
        st.session_state.page = item

# Call the function associated with the selected page to render it
menu_items[st.session_state.page]()
