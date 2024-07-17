import streamlit as st
import random
from save_results import save_results


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

# st.title("Optimising Irrigation Practices for Dairy Farms: A Decision-Making Guide")

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
    "Q1": {"a": ("Use real-time data from soil moisture sensors to determine irrigation needs", "Q2", +2),
           "b": ("Irrigate based on current soil moisture data obtained through manual testing", "Q3", +1),
           "c": ("Seek personalized advice from local agricultural experts based on current soil data", "Q4", -1),
           "d": ("Initiate irrigation based on historical calendar dates commonly used in the region", "Q5", -1)},
    "Q2": {"a": ("Estimate soil moisture from visual inspections", "Q7", -1),
           "b": ("Deploy soil moisture sensors for real-time data", "Q6", +2),
           "c": ("Use historical weather patterns to predict needs", "Q8", +1),
           "d": ("Follow a predetermined irrigation schedule", "Q9", -1)},
    "Q3": {"a": ("Prioritize systems from reputable local suppliers for faster initial support", "Q13", -1),
           "b": ("Consider systems with automation and weather tracking for long-term efficiency", "Q11", +1),
           "c": ("Evaluate ease of maintenance and operation to minimize future service costs", "Q12", +1),
           "d": ("Choose the system that meets your minimum functional requirements at the lowest cost", "Q10", +2)},
    "Q4": {"a": ("Assume a pre-defined average water holding capacity for your crop type", "Q15", -1),
           "b": ("Optimize irrigation based on real-time soil moisture data and historical water holding capacity", "Q14", +2),
           "c": ("Follow regulatory guidelines for water usage, adjusting for local conditions if allowed", "Q16", +1)},
    "Q5": {"a": ("Schedule regular preventive maintenance to optimize system performance", "Q17", +2),
           "b": ("Perform reactive maintenance by addressing system failures as they occur", "Q18", -1),
           "c": ("Update software systems and conduct basic inspections annually", "Q19", +1)},
    "Q6": {"a": ("Maintain a consistent irrigation schedule based on historical averages", "Q21", -1),
           "b": ("Adjust irrigation frequency dynamically based on real-time soil moisture and plant stress data", "Q20", +2),
           "c": ("Incorporate weather forecast adjustments along with a baseline irrigation schedule", "Q22", +1)},
    "Q7": {"a": ("Utilize subsurface drip irrigation for precise water delivery to plant root zones", "Q23", +2),
           "b": ("Employ overhead sprinklers with even water distribution across the field", "Q24", +1),
           "c": ("Implement furrow irrigation for efficient water delivery along furrows", "Q25", -1)},
     "Q8": {"a":("Disregard risks and follow standard irrigation volume", "Q27", -1),
           "b": ("Address risks of over-watering and waterlogging", "Q26", +2),
           "c": ("Optimize based on recent field capacity measurements", "Q28", +1)},
    "Q9": {"a": ("To ensure efficient delivery at varied pressures", "Q29", +2),
           "b": ("To minimize system maintenance needs", "Q30", +1),
           "c": ("Use standard pumps without custom settings", -1)},
    "Q10": {"a": ("Ignore weather forecasts and rely on set schedules", -1),
            "b": ("Incorporate rainfall predictions into planning", +2),
            "c": ("Adjust plans based on soil saturation levels", +1)},
    "Q11": {"a": ("Reviewing local irrigation guidelines and adapting as necessary", "Q12", +1),
            "b": ("Ignoring variations in soil types across fields", "Q13", -1),
            "c": ("Analyzing historical crop response data to refine practices", "Q14", +2),
            "d": ("Consulting with a water management specialist", "Q15", +1)},
    "Q12": {"a": ("Upgrade to variable speed drive pumps for better energy efficiency", "Q16", +2),
            "b": ("Continue using older, less efficient pump technology", "Q17", -1),
            "c": ("Implement automated water flow sensors to adjust rates", "Q18", +1)},
    "Q13": {"a": ("Increase watering frequency during periods of high heat", "Q19", +2),
            "b": ("Maintain a constant irrigation schedule regardless of weather", "Q20", -1),
            "c": ("Use evapotranspiration data to guide irrigation timing", "Q21", +1)},
    "Q14": {"a": ("Schedule inspections after any significant weather events", "Q22", +1),
            "b": ("Check irrigation equipment regularly to prevent failures", "Q23", +2),
            "c": ("Only check systems when visible problems occur", "Q24", -1)},
    "Q15": {"a": ("Assess the water availability and regulatory constraints first", "Q25", +2),
            "b": ("Choose an irrigation system based on lowest cost", "Q26", -1),
            "c": ("Consider future scalability and potential technological upgrades", "Q27", +1)},
    "Q16": {"a": ("Evaluate the uniformity of water distribution in current systems", "Q28", +2),
            "b": ("Assume all systems are equally effective regardless of design", "Q29", -1),
            "c": ("Research new irrigation technologies for potential implementation", "Q30", +1)},
    "Q17": {"a": ("Adjust settings based on soil composition and permeability", +2),
            "b": ("Set a uniform irrigation schedule for all soil types", -1),
            "c": ("Monitor soil moisture levels closely to avoid over-irrigation", +1)},
    "Q18": {"a": ("Implement rain sensors to halt irrigation during downpours", +2),
            "b": ("Continue irrigation during rain to ensure schedule adherence", -1),
            "c": ("Use drought-resistant plants to reduce water needs", +1)},
    "Q19": {"a": ("Collect runoff water for reuse in irrigation", +1),
            "b": ("Increase irrigation rates to promote deeper root growth", -1),
            "c": ("Integrate drip irrigation systems to reduce runoff", +2)},
    "Q20": {"a": ("Use a single pressure setting for simplicity", -1),
            "b": ("Ensure that irrigation pressures are optimized for each crop type", +2),
            "c": ("Regularly test system pressure to detect any discrepancies", +1)},
    "Q21": {"a": ("Disregard soil temperature as a non-significant factor", -1),
            "b": ("Consider adjusting irrigation based on daily temperature fluctuations", +1),
            "c": ("Calibrate irrigation systems to respond automatically to temperature sensors", +2)},
    "Q22": {"a": ("Reduce irrigation frequency during wet seasons", +1),
            "b": ("Enhance soil drainage systems to cope with excess water", +2),
            "c": ("Maintain a steady irrigation routine throughout the year", -1)},
    "Q23": {"a": ("Optimize schedules to water during the cooler parts of the day", +2),
            "b": ("Stick to a fixed watering schedule to simplify management", -1),
            "c": ("Increase watering during hot periods to reduce plant stress", +1)},
    "Q24": {"a": ("Adjust the irrigation equipment setup based on seasonal observations", +2),
            "b": ("Keep the irrigation setup consistent year-round", -1),
            "c": ("Periodically review and tweak equipment settings for efficiency", +1)},
    "Q25": {"a": ("Choose early morning hours to minimize evaporation losses", +2),
            "b": ("Irrigate at noon to coincide with peak sun and heat", "Q26", -1),
            "c": ("Alternate irrigation times weekly to test different efficiencies", "Q27", +1)},
    "Q26": {"a": ("Customize irrigation based on specific crop water needs", "Q28", +2),
            "b": ("Apply the same amount of water regardless of the crop type", "Q29", -1),
            "c": ("Focus on the most economically feasible option", "Q30", +1)},
    "Q27": {"a": ("Minimize irrigation to encourage deeper root systems", +2),
            "b": ("Over-irrigate to ensure soil is always saturated", -1),
            "c": ("Balance water application based on soil health indicators", +1)},
    "Q28": {"a": ("Plan irrigation frequency based on the plant growth stages", +2),
            "b": ("Ignore plant growth stages in scheduling irrigation", -1),
            "c": ("Use generic irrigation schedules regardless of plant growth", -1)},
    "Q29": {"a": ("Implement soil moisture sensors to automate irrigation", +2),
            "b": ("Depend solely on manual checking for soil moisture", -1),
            "c": ("Use timed irrigation without soil moisture checks", -1)},
    "Q30": {"a": ("Conduct thorough cleaning and maintenance at season's end", +2),
            "b": ("Perform minimal maintenance and prepare for unexpected repairs", -1),
            "c": ("Delay all maintenance until operational issues occur", -1)}
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
        # st.markdown(
        #     f"**You've reached the end of the survey with a final score of: {st.session_state['total_score']}**")
        # st.markdown(
        #     f"**You've reached the end of the survey with a total path length of: {st.session_state['path_length']}**")

        if st.button('Submit Results'):
            results_data = (
                f"You've reached the end of the survey with a final score of: {st.session_state['total_score']}\n"
                f"You've reached the end of the survey with a total path length of: {st.session_state['path_length']}")
            result_message = save_results(results_data, file_prefix="user")
            st.success(result_message)


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
        # if st.button("Get AI Recommendation", key=f'{current_question}_recommendation'):
        #     # Determine AI's recommendation based on the maximum score
        #     max_score_option = max(options[current_question].items(), key=lambda item: item[1][-1])[0]
        #     recommended_option = options[current_question][max_score_option][0]
        #     st.write(f"I recommend: {recommended_option}")
        st.markdown("""
        <style>
        .guidance {
            font-size: 20px;
            font-weight: bold;
            color: green;
            padding: 10px;
            background-color: lightgray;
        }
        </style>
        <div class="guidance">Ask AI for Guidance</div>
        """, unsafe_allow_html=True)

        if selected:
            st.session_state['selected_option'] = selected[1]

        if st.button("Next", key=f'{current_question}_next', on_click=navigate_questions):
            pass

    if st.session_state.get('endpoint_reached', False):
        # # Display the final score in a bold format
        # st.markdown(
        #     f"**You've reached the end of the survey with a final score of: {st.session_state['total_score']}**")
        # st.markdown(
        #     f"**You've reached the end of the survey with a total path length of: {st.session_state['path_length']}**")
        if st.button('Submit Results'):
            results_data = (
                f"You've reached the end of the survey with a final score of: {st.session_state['total_score']}\n"
                f"You've reached the end of the survey with a total path length of: {st.session_state['path_length']}")
            result_message = save_results(results_data, file_prefix="user_agent")
            st.success(result_message)


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

        # if st.button("Get Consultant Recommendation", key=f'{current_question}_consultant_recommendation'):
        #     if current_question in consultant_available_questions:
        #         max_score_option = max(options[current_question].items(), key=lambda item: item[1][-1])[0]
        #         recommended_option = options[current_question][max_score_option][0]
        #         st.write(f"Consultant recommends: {recommended_option}")
        #     else:
        #         st.write("Consultant recommendation is not available for this question.")
        st.markdown("""
               <style>
               .guidance {
                   font-size: 20px;
                   font-weight: bold;
                   color: green;
                   padding: 10px;
                   background-color: lightgray;
               }
               </style>
               <div class="guidance">Ask Consultant for Guidance</div>
               """, unsafe_allow_html=True)

        if selected:
            st.session_state['selected_option'] = selected[1]

        if st.button("Next", key=f'{current_question}_next', on_click=navigate_questions):
            pass

    if st.session_state.get('endpoint_reached', False):
        # st.markdown(
        #     f"**You've reached the end of the survey with a final score of: {st.session_state['total_score']}**")
        # st.markdown(
        #     f"**You've reached the end of the survey with a total path length of: {st.session_state['path_length']}**")
        if st.button('Submit Results'):
            results_data = (
                f"You've reached the end of the survey with a final score of: {st.session_state['total_score']}\n"
                f"You've reached the end of the survey with a total path length of: {st.session_state['path_length']}")
            result_message = save_results(results_data, file_prefix="user_consultant")
            st.success(result_message)


def user_agent_consultant_page():
    st.write("This page allows interaction between the user, an AI agent, and a human consultant.")
    current_question = st.session_state['current_question']
    if current_question:
        # List all options for the current question
        options_list = [(f"{k}: {v[0]}", k) for k, v in options[current_question].items()]

        # Display radio buttons for options
        selected = st.radio(f"{current_question}) {questions[current_question]}", options_list, format_func=lambda x: x[0], index=None, key=f'{current_question}_radio')

        # # Button to get Consultant's recommendation
        # if st.button("Get Consultant Recommendation", key=f'{current_question}_consultant_recommendation'):
        #     if current_question in consultant_available_questions:
        #         max_score_option = max(options[current_question].items(), key=lambda item: item[1][-1])[0]
        #         recommended_option = options[current_question][max_score_option][0]
        #         st.write(f"Consultant recommends: {recommended_option}")
        #     else:
        #         st.write("Consultant recommendation is not available for this question.")

        # # Button to get AI's recommendation
        # if st.button("Get AI Recommendation", key=f'{current_question}_ai_recommendation'):
        #     # Determine AI's recommendation based on the maximum score
        #     max_score_option = max(options[current_question].items(), key=lambda item: item[1][-1])[0]
        #     recommended_option = options[current_question][max_score_option][0]
        #     st.write(f"AI recommends: {recommended_option}")
        st.markdown("""
               <style>
               .guidance {
                   font-size: 20px;
                   font-weight: bold;
                   color: green;
                   padding: 10px;
                   background-color: lightgray;
               }
               </style>
               <div class="guidance">Ask Consultant And/Or AI for Guidance</div>
               """, unsafe_allow_html=True)

        if selected:
            st.session_state['selected_option'] = selected[1]

        if st.button("Next", key=f'{current_question}_next', on_click=navigate_questions):
            pass

    if st.session_state.get('endpoint_reached', False):
        # Display the final score in a bold format
        # st.markdown(f"**You've reached the end of the survey with a final score of: {st.session_state['total_score']}**")
        # st.markdown(
        #     f"**You've reached the end of the survey with a total path length of: {st.session_state['path_length']}**")
        if st.button('Submit Results'):
            results_data = (
                f"You've reached the end of the survey with a final score of: {st.session_state['total_score']}\n"
                f"You've reached the end of the survey with a total path length of: {st.session_state['path_length']}")
            result_message = save_results(results_data, file_prefix="user_agent_consultant")
            st.success(result_message)


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


def page_digital_security():
    # Sidebar navigation setup
    st.sidebar.title("Digital Security")
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
