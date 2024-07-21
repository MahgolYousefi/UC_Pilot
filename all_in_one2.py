
import os
import datetime
import streamlit as st
from PIL import Image
import base64

def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


# def save_results(data, file_prefix):
#     folder_path = 'C:/HAT_Results'
#     # Ensure the folder exists
#     folder_path = ensure_folder_exists(folder_path)
#
#     # Get current datetime to use as a filename
#     current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     filename = f"{file_prefix}_{current_time}.txt"
#     file_path = os.path.join(folder_path, filename)
#
#     # Write data to the file
#     with open(file_path, 'w') as file:
#         file.write(data)
#
#     return f"Results sent successfully."

def save_results(data, file_prefix):
    # Get current datetime to use as a filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{file_prefix}_{current_time}.txt"

    # Convert data to bytes
    b64 = base64.b64encode(data.encode()).decode()  # Convert to base64

    # Create download link
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">Download results</a>'
    return href

#######################################################################################################################

## Farm

#######################################################################################################################
farm_questions = {
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

farm_options = {
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
               "d": (
               "Choose the system that meets your minimum functional requirements at the lowest cost", "Q10", +2)},
        "Q4": {"a": ("Assume a pre-defined average water holding capacity for your crop type", "Q15", -1),
               "b": (
               "Optimize irrigation based on real-time soil moisture data and historical water holding capacity", "Q14",
               +2),
               "c": (
               "Follow regulatory guidelines for water usage, adjusting for local conditions if allowed", "Q16", +1)},
        "Q5": {"a": ("Schedule regular preventive maintenance to optimize system performance", "Q17", +2),
               "b": ("Perform reactive maintenance by addressing system failures as they occur", "Q18", -1),
               "c": ("Update software systems and conduct basic inspections annually", "Q19", +1)},
        "Q6": {"a": ("Maintain a consistent irrigation schedule based on historical averages", "Q21", -1),
               "b": (
               "Adjust irrigation frequency dynamically based on real-time soil moisture and plant stress data", "Q20",
               +2),
               "c": ("Incorporate weather forecast adjustments along with a baseline irrigation schedule", "Q22", +1)},
        "Q7": {"a": ("Utilize subsurface drip irrigation for precise water delivery to plant root zones", "Q23", +2),
               "b": ("Employ overhead sprinklers with even water distribution across the field", "Q24", +1),
               "c": ("Implement furrow irrigation for efficient water delivery along furrows", "Q25", -1)},
        "Q8": {"a": ("Disregard risks and follow standard irrigation volume", "Q27", -1),
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


def page_farm(questions, options, page_name):
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

    # st.title("Optimising Irrigation Practices for Dairy Farms: A Decision-Making Guide")

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
                # result_message = save_results(results_data, file_prefix=page_name)
                # st.success(result_message)
                download_link = save_results(results_data, file_prefix=f"U_{page_name}")
                st.markdown(download_link, unsafe_allow_html=True)

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
                # result_message = save_results(results_data, file_prefix="user_agent")
                # st.success(result_message)
                download_link = save_results(results_data, file_prefix=f"UA_{page_name}")
                st.markdown(download_link, unsafe_allow_html=True)

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
                # result_message = save_results(results_data, file_prefix="user_consultant")
                # st.success(result_message)
                download_link = save_results(results_data, file_prefix=f"UH_{page_name}")
                st.markdown(download_link, unsafe_allow_html=True)

    def user_agent_consultant_page():
        st.write("This page allows interaction between the user, an AI agent, and a human consultant.")
        current_question = st.session_state['current_question']
        if current_question:
            # List all options for the current question
            options_list = [(f"{k}: {v[0]}", k) for k, v in options[current_question].items()]

            # Display radio buttons for options
            selected = st.radio(f"{current_question}) {questions[current_question]}", options_list,
                                format_func=lambda x: x[0], index=None, key=f'{current_question}_radio')

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
                # result_message = save_results(results_data, file_prefix="user_agent_consultant")
                # st.success(result_message)
                download_link = save_results(results_data, file_prefix=f"UAH_{page_name}")
                st.markdown(download_link, unsafe_allow_html=True)

    # Initialize session state for page navigation if it's not already set
    if 'page' not in st.session_state:
        st.session_state.page = '1'

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

    # main one
    st.sidebar.title("")
    menu_items = {
        "1": user_page,
        "2": user_consultant_page,
        "3": user_agent_page,
        "4": user_agent_consultant_page
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


#######################################################################################################################

## Finance

#######################################################################################################################
finance_questions = {
        "Q1": "What is the primary factor to consider when planning for retirement savings?",
        "Q2": "What is the best strategy to manage a financial windfall, such as an inheritance?",
        "Q3": "How should an investor adjust their portfolio in response to a major stock market correction?",
        "Q4": "What critical factor should be considered before investing in high-yield bonds?",
        "Q5": "What is a prudent approach to managing significant credit card debt?",
        "Q6": "How should personal investments be adjusted in anticipation of rising inflation?",
        "Q7": "Which strategy is most effective for saving for a child’s college education?",
        "Q8": "What should be prioritized when creating a long-term financial plan?",
        "Q9": "How can one optimize their investment portfolio for tax efficiency?",
        "Q10": "What is a key consideration when selecting a life insurance policy?",
        "Q11": "What approach should be taken for estate planning to minimize taxes?",
        "Q12": "How can one ensure adequate diversification in their investment portfolio?",
        "Q13": "What is the best way to approach debt consolidation?",
        "Q14": "How should one decide between investing in a Roth IRA versus a traditional IRA?",
        "Q15": "What are the risks associated with investing in emerging markets?",
        "Q16": "What factors should be considered when planning to buy versus rent a home?",
        "Q17": "What is an effective strategy for managing a personal budget?",
        "Q18": "How should one evaluate the decision to refinance a mortgage?",
        "Q19": "What considerations are important when deciding to start a new business?",
        "Q20": "How does one determine the right amount of emergency savings?",
        "Q21": "What steps should be taken to protect one's financial information online?",
        "Q22": "How should one assess the impact of economic recession on personal finances?",
        "Q23": "What is the best strategy to pay off student loans efficiently?",
        "Q24": "How can one use real estate as a tool for wealth building?",
        "Q25": "What factors should influence the asset allocation in a retirement portfolio?",
        "Q26": "How should financial goals be adjusted after a major life event?",
        "Q27": "What are the key elements to consider when planning for healthcare costs in retirement?",
        "Q28": "What methods can be employed to minimize investment fees and expenses?",
        "Q29": "What is the most effective way to utilize credit scores for securing low-interest loans?",
        "Q30": "What are the essential elements of a solid financial risk management plan?"
    }

finance_options = {
        "Q1": {"a": ("Maximize contributions to tax-deferred accounts", "Q2", +2),
               "b": ("Invest in a diverse portfolio of stocks", "Q3", +1),
               "c": ("Purchase annuities for guaranteed income", -1)},
        "Q2": {"a": ("Invest entirely in a diversified stock portfolio", -1),
               "b": ("Allocate to an emergency fund, then invest the rest", "Q5", +2),
               "c": ("Pay off existing debt, then save the remainder", "Q7", +1)},
        "Q3": {"a": ("Shift to conservative investments like bonds", -1),
               "b": ("Rebalance to maintain original asset allocation", "Q9", +2),
               "c": ("Invest more in undervalued stocks", "Q10", +1)},
        "Q4": {"a": ("Focus on the potential returns ignoring risks", -1),
               "b": ("Assess the credit risk and maturity period", "Q12", +2),
               "c": ("Choose bonds with the highest yield", "Q13", +1)},
        "Q5": {"a": ("Transfer balances to a zero-interest card", "Q14", +1),
               "b": ("Consolidate debt through a personal loan", "Q15", +2),
               "c": ("Only make minimum payments to manage cash flow", -1)},
        "Q6": {"a": ("Increase investments in real estate and commodities", "Q17", +2),
               "b": ("Hold cash to avoid market volatility", "", -1),
               "c": ("Continue usual investments without changes", "Q19", +1)},
        "Q7": {"a": ("Use a 529 savings plan with tax benefits", "Q20", +2),
               "b": ("Invest in mutual funds earmarked for education", "Q21", +1),
               "c": ("Rely on scholarships and student loans", "", -1)},
        "Q8": {"a": ("Focus on accumulating assets ignoring liabilities", -1),
               "b": ("Balance between saving, investing, and debt repayment", "Q24", +2),
               "c": ("Prioritize high-risk, high-return investments", "Q25", +1)},
        "Q9": {"a": ("Invest in tax-exempt municipal bonds", "Q26", +2),
               "b": ("Maximize contributions to retirement accounts", "Q27", +1),
               "c": ("Avoid selling assets to reduce capital gains", -1)},
        "Q10": {"a": ("Choose the policy with the lowest premium", -1),
                "b": ("Evaluate based on coverage, terms, and company stability", "Q30", +2),
                "c": ("Select based solely on recommendations", +1)},
        "Q11": {"a": ("Establish a trust to protect assets and minimize taxes", "Q12", +2),
                "b": ("Distribute assets equally among heirs without tax planning", -1),
                "c": ("Use life insurance to cover potential estate taxes", "Q14", +1)},
        "Q12": {"a": ("Invest in a mix of domestic and international funds", "Q15", +2),
                "b": ("Focus solely on high-growth tech stocks", -1),
                "c": ("Keep all investments in bonds for safety", "Q17", +1)},
        "Q13": {"a": ("Combine all debts into one low-interest loan", "Q18", +2),
                "b": ("Pay off each debt separately to track progress", "Q19", +1),
                "c": ("Take out a home equity loan to pay off credit card debt", -1)},
        "Q14": {"a": ("Invest based on tax implications now and expected income at retirement", "Q21", +2),
                "b": ("Choose based on the advice of a financial advisor", "Q22", +1),
                "c": ("Opt for traditional IRA for immediate tax relief", -1)},
        "Q15": {"a": ("Evaluate political and economic stability before investing", "Q24", +2),
                "b": ("Invest small amounts regardless of market conditions", -1),
                "c": ("Focus on sectors with potential for quick growth", "Q25", +1)},
        "Q16": {"a": ("Consider long-term financial goals and real estate market trends", "Q27", +2),
                "b": ("Always prefer to rent for financial flexibility", -1),
                "c": ("Buy a home when the mortgage is less than rent", "Q29", +1)},
        "Q17": {"a": ("Track income and expenses meticulously and adjust as needed", +2),
                "b": ("Set a fixed budget and stick to it regardless of changes in income", +1),
                "c": ("Prioritize expenses based on immediate needs only", -1)},
        "Q18": {"a": ("Analyze current interest rates and the potential for rate decreases", +2),
                "b": ("Refinance only if monthly savings are immediate", +1),
                "c": ("Ignore market conditions and refinance for a longer-term loan", -1)},
        "Q19": {"a": ("Assess market demand and potential for scalability before starting", +2),
                "b": ("Start with minimal investment and grow organically", +1),
                "c": ("Focus on a niche market regardless of competition", -1)},
        "Q20": {"a": ("Set aside 6-12 months of expenses depending on job stability", +2),
                "b": ("Save a flat rate monthly regardless of overall expenses", -1),
                "c": ("Adjust savings based on current economic conditions", +1)},
        "Q21": {"a": ("Use strong, unique passwords and two-factor authentication for all financial accounts", +2),
                "b": ("Regularly monitor financial statements for unauthorized transactions", +1),
                "c": ("Rely on bank security measures and fraud protection services", -1)},
        "Q22": {"a": ("Increase liquidity by holding more cash and cash equivalents", +2),
                "b": ("Continue investing aggressively to take advantage of lower prices", -1),
                "c": ("Diversify into recession-proof sectors like utilities and consumer staples", +1)},
        "Q23": {"a": ("Prioritize paying off high-interest loans first to reduce total interest paid", +2),
                "b": ("Enroll in income-driven repayment plans if eligible", +1),
                "c": ("Consolidate loans to simplify monthly payments", -1)},
        "Q24": {"a": ("Invest in rental properties in high-demand areas", +2),
                "b": ("Purchase vacation properties for short-term rental", -1),
                "c": ("Flip houses as a form of active real estate investment", +1)},
        "Q25": {"a": ("Shift more towards bonds and stable investments as retirement approaches", +2),
                "b": ("Maintain a high proportion of stocks for growth", +1),
                "c": ("Invest heavily in emerging markets for potential high returns", -1)},
        "Q26": {"a": ("Reevaluate financial objectives and adjust investments and savings", +2),
                "b": ("Keep financial plans unchanged to maintain course", -1),
                "c": ("Focus on short-term financial needs before updating long-term goals", +1)},
        "Q27": {"a": ("Plan for long-term care insurance and consider health savings accounts", +2),
                "b": ("Assume Medicare will cover all healthcare costs", -1),
                "c": ("Save separately for unexpected medical expenses", +1)},
        "Q28": {"a": ("Choose low-cost index funds and ETFs to minimize fees", +2),
                "b": ("Opt for actively managed funds with potential for higher returns", -1),
                "c": ("Ignore fees as long as returns are satisfactory", +1)},
        "Q29": {"a": ("Regularly review and optimize credit reports for accuracy", +2),
                "b": ("Focus on high credit utilization to demonstrate creditworthiness", -1),
                "c": ("Apply for multiple credit lines to increase available credit", +1)},
        "Q30": {"a": ("Diversify investments to spread risk across various assets", +2),
                "b": ("Focus on high-return, high-risk investments to maximize potential gains", -1),
                "c": ("Purchase insurance to cover potential financial losses", +1)}
    }


#######################################################################################################################

## Health

#######################################################################################################################
health_questions = {
    "Q1": "What is the primary reason some people gain excess weight?",
    "Q2": "Which measurement is most critical for assessing excess weight?",
    "Q3": "What minimal percentage of weight loss significantly reduces health risks?",
    "Q4": "What is a major factor that complicates the process of losing weight?",
    "Q5": "Which dietary component is essential but should be consumed in moderation due to high calories?",
    "Q6": "What modern lifestyle aspect most contributes to excess weight?",
    "Q7": "Which approach is least effective for long-term weight management?",
    "Q8": "What is a crucial first step when beginning a weight loss journey?",
    "Q9": "How do emotional factors affect weight gain?",
    "Q10": "What role does genetics play in a person's susceptibility to obesity?",
    "Q11": "Which type of physical activity is recommended for effective weight loss?",
    "Q12": "How important is water consumption in a weight loss diet?",
    "Q13": "What is the role of proteins in a healthy diet?",
    "Q14": "What impact does consuming fats have on a diet?",
    "Q15": "Why is fiber an important part of a diet to lose weight?",
    "Q16": "What misconception about weight loss medications is most common?",
    "Q17": "What is the most misleading perception about dieting for weight loss?",
    "Q18": "How does meal planning contribute to effective weight management?",
    "Q19": "Which type of fats is considered healthier for a weight loss diet?",
    "Q20": "What psychological approach helps in managing and sustaining weight loss?",
    "Q21": "What is the least helpful method to achieve and maintain a healthy weight?",
    "Q22": "Which strategy is most recommended for a beginner to start losing weight?",
    "Q23": "How significant is the role of surgery in weight loss?",
    "Q24": "What is the best initial dietary change to make when starting a weight loss plan?",
    "Q25": "What common dietary advice is now considered outdated?",
    "Q26": "How can technology aid in weight loss?",
    "Q27": "What is a critical consideration when choosing weight loss medication?",
    "Q28": "Which lifestyle change provides the most sustainable impact on weight loss?",
    "Q29": "What nutritional misconception could lead to ineffective dieting?",
    "Q30": "What is the most effective strategy for avoiding weight regain?"
}

health_options = {
    "Q1": {"a": ("Genetics influencing metabolism", "Q2", +1),
           "b": ("Modern sedentary lifestyles", "Q3", +2),
           "c": ("Dietary habits and caloric intake", "Q4", +2)},
    "Q2": {"a": ("Body Mass Index (BMI)", "Q5", +2),
           "b": ("Waist-to-hip ratio", "Q6", +1),
           "c": ("Body fat percentage", "Q7", +1)},
    "Q3": {"a": ("5% of total body weight", "Q8", -1),
           "b": ("10% of total body weight", "Q9", +2),
           "c": ("15% of total body weight", "Q10", +1)},
    "Q4": {"a": ("Lack of willpower", "Q11", -1),
           "b": ("Biological and genetic factors", "Q12", +2),
           "c": ("Poor access to healthy foods", "Q13", +1)},
    "Q5": {"a": ("Proteins", "Q14", -1),
           "b": ("Fats", "Q15", +2),
           "c": ("Carbohydrates", "Q16", +1)},
    "Q6": {"a": ("Increased food availability", "Q17", +2),
           "b": ("Economic factors", "Q18", -1),
           "c": ("Technological advancements", "Q19", +1)},
    "Q7": {"a": ("Following fad diets", "Q20", +1),
           "b": ("Caloric restriction", "Q21", -1),
           "c": ("Sustainable lifestyle changes", "Q22", +2)},
    "Q8": {"a": ("Setting realistic goals", "Q23", -1),
           "b": ("Seeking professional advice", "Q24", +2),
           "c": ("Purchasing a gym membership", "Q25", +1)},
    "Q9": {"a": ("Stress eating", "Q26", +1),
           "b": ("Lack of sleep", "Q27", -1),
           "c": ("Personal or family issues", "Q28", +2)},
    "Q10": {"a": ("70% genetic influence", "Q29", +1),
            "b": ("50% genetic influence", "Q30", +1),
            "c": ("30% genetic influence", "Q25", +2)},
    "Q11": {"a": ("Low-intensity steady-state cardio", "Q12", +1),
            "b": ("High-intensity interval training", "Q13", +2),
            "c": ("Weight training", +1)},
    "Q12": {"a": ("At least 2 liters per day", "Q14", +2),
            "b": ("1 liter per day", "Q15", -1),
            "c": ("Depending on thirst", +1)},
    "Q13": {"a": ("Mainly from animal sources", "Q16", -1),
            "b": ("Balanced between plant and animal sources", "Q17", +2),
            "c": ("Mostly from supplements", +1)},
    "Q14": {"a": ("Saturated fats are healthier", "Q18", -1),
            "b": ("Trans fats should be minimized", "Q19", +1),
            "c": ("Unsaturated fats are beneficial", "Q20", +2)},
    "Q15": {"a": ("It helps in rapid weight loss", "Q21", +1),
            "b": ("It aids in digestive health", "Q22", +2),
            "c": ("It increases calorie absorption", +1)},
    "Q16": {"a": ("They work independently of diet and exercise", "Q23", -1),
            "b": ("They are effective as part of a lifestyle change", "Q24", +2),
            "c": ("They cause rapid weight loss without side effects", +1)},
    "Q17": {"a": ("Dieting is mainly about strict calorie control", "Q25", -1),
            "b": ("Dieting should focus on food quality, not just quantity", +2),
            "c": ("Short-term diets are effective for permanent weight loss", +1)},
    "Q18": {"a": ("It's unnecessary for successful weight loss", "Q26", -1),
            "b": ("It is crucial for controlling portion sizes", "Q27", +2),
            "c": ("It should be highly restrictive to be effective", +1)},
    "Q19": {"a": ("Butter and lard", "Q28", -1),
            "b": ("Olive oil and avocado oil", "Q29", +2),
            "c": ("Coconut oil and palm oil", "Q30", +1)},
    "Q20": {"a": ("Using rewards such as food", "Q12", -1),
            "b": ("Developing a support network", "Q13", +2),
            "c": ("Setting highly ambitious goals", +1)},
    "Q21": {"a": ("Adopting a very low-calorie diet", "Q14", -1),
            "b": ("Incorporating moderate physical activity", "Q15", +1),
            "c": ("Making gradual dietary adjustments", +2)},
    "Q22": {"a": ("Joining a weight loss clinic", "Q16", -1),
            "b": ("Starting with light exercise", "Q17", +1),
            "c": ("Cutting all sugars abruptly", +2)},
    "Q23": {"a": ("It should be a last resort", "Q18", +2),
            "b": ("It's the most effective method", -1),
            "c": ("It guarantees long-term success", +1)},
    "Q24": {"a": ("Increasing protein intake", "Q19", +1),
            "b": ("Eliminating all fats", -1),
            "c": ("Reducing processed foods", "Q20", +2)},
    "Q25": {"a": ("Eating multiple small meals is necessary", -1),
            "b": ("Calorie counting is the only way to lose weight", +1),
            "c": ("Balanced macronutrients are key", +2)},
    "Q26": {"a": ("Using apps to track dietary intake", +2),
            "b": ("Avoiding the use of any digital devices", -1),
            "c": ("Relying solely on physical activity trackers", +1)},
    "Q27": {"a": ("They should be used without consultation", -1),
            "b": ("They are only for those with a BMI over 30", +2),
            "c": ("They can replace dietary changes", +1)},
    "Q28": {"a": ("Switching to a vegetarian diet", +1),
            "b": ("Gradual increase in physical activity", +2),
            "c": ("Frequent fasting periods", -1)},
    "Q29": {"a": ("Fats are the main dietary enemy", -1),
            "b": ("All carbs must be eliminated", +1),
            "c": ("Protein should be the focus of the diet", +2)},
    "Q30": {"a": ("Constantly changing diet plans", +1),
            "b": ("Maintaining dietary consistency", +2),
            "c": ("Avoiding all social eating occasions", -1)}
}
#######################################################################################################################

## Digital

#######################################################################################################################
digital_questions = {
    "Q1": "Which of the following is not typically associated with compromising network security?",
    "Q2": "Which of the following set of actions is not applicable in mitigating the risk of identity theft in the digital environment?",
    "Q3": "What are the common ways AI tools can be used to breach personal data security?",
    "Q4": "What are effective methods for verifying the authenticity of digital content?",
    "Q5": "Why is cautious sharing on social media crucial for personal security?",
    "Q6": "What techniques do cybercriminals use, like phishing, that leverage AI to create more convincing scams?",
    "Q7": "Which security practices are essential for protecting online accounts from unauthorized access?",
    "Q8": "How does the management of complex passwords safeguard against AI-driven hacking attempts?",
    "Q9": "What is encryption and how does it contribute to safeguarding personal data online?",
    "Q10": "Why is two-factor authentication (2FA) vital for enhancing account security?",
    "Q11": "How can one identify and avoid falling victim to AI-generated scam emails?",
    "Q12": "What are the benefits of regularly updating software and applications in terms of security?",
    "Q13": "What precautions should students take when interacting on AI-driven social platforms?",
    "Q14": "What steps should be followed if a student suspects they have encountered a deepfake video?",
    "Q15": "How can students use AI tools responsibly to avoid compromising their privacy?",
    "Q16": "What are the implications of using public Wi-Fi on personal security, and how can students protect themselves?",
    "Q17": "How can understanding the settings and permissions of apps improve personal digital security?",
    "Q18": "What strategies can students use to manage their digital footprint effectively?",
    "Q19": "What should students know about the legal aspects of digital content and user agreements?",
    "Q20": "How can building a personal brand online affect privacy and security?",
    "Q21": "What measures should be taken if personal information is compromised online?",
    "Q22": "How does artificial intelligence influence user privacy on platforms used by students?",
    "Q23": "What are the ethical considerations of using and developing AI technology?",
    "Q24": "How can students contribute to a safer digital community?",
    "Q25": "What are the long-term consequences of digital security breaches for individuals?",
    "Q26": "How do digital rights and responsibilities vary across different countries?",
    "Q27": "What is the role of anonymity in digital interactions, and what are its pros and cons?",
    "Q28": "How can students detect and protect themselves from malware and ransomware?",
    "Q29": "What are the signs of a secure website that students should look for when browsing?",
    "Q30": "How can students ensure the integrity of their digital work and creative outputs?"
}

digital_options = {
    "Q1": {"a": ("Encrypting all personal data", "Q3", +2),
           "b": ("Using antivirus software", "Q2", +1),
           "c": ("Installing unverified apps", -1)},
    "Q2": {"a": ("Regularly updating passwords", "Q5", +2),
           "b": ("Clicking on unsolicited email links", -1),
           "c": ("Using multi-factor authentication", "Q7", +1)},
    "Q3": {"a": ("Data phishing through fake profiles", "Q8", +2),
           "b": ("Secure browsing with HTTPS", "Q9", +1),
           "c": ("Installing security software from reliable sources", -1)},
    "Q4": {"a": ("Checking digital certificates", "Q11", +2),
           "b": ("Ignoring security warnings", -1),
           "c": ("Verifying through third-party services", "Q13", +1)},
    "Q5": {"a": ("Avoiding oversharing personal information", "Q14", +2),
           "b": ("Sharing location check-ins", -1),
           "c": ("Using privacy filters on posts", "Q16", +1)},
    "Q6": {"a": ("AI-generated phishing emails", "Q17", +2),
           "b": ("General awareness about phishing", "Q18", +1),
           "c": ("Attending cybersecurity webinars", -1)},
    "Q7": {"a": ("Regular security audits", "Q20", +2),
           "b": ("Ignoring software updates", -1),
           "c": ("Using a single password for all accounts", "Q22", +1)},
    "Q8": {"a": ("Employing password managers", "Q23", +2),
           "b": ("Writing down passwords", -1),
           "c": ("Using biometric security", "Q25", +1)},
    "Q9": {"a": ("Encrypting sensitive files", "Q26", +2),
           "b": ("Storing passwords in browsers", -1),
           "c": ("Using public Wi-Fi for transactions", "Q28", +1)},
    "Q10": {"a": ("Adding a verification step with mobile devices", "Q29", +2),
            "b": ("Ignoring unfamiliar login attempts", -1),
            "c": ("Using email verification only", "Q1", +1)},
    "Q11": {"a": ("Analyzing the email header for origin", "Q2", +2),
            "b": ("Opening attachments for verification", -1),
            "c": ("Consulting with cybersecurity experts", "Q4", +1)},
    "Q12": {"a": ("Protecting against new vulnerabilities", "Q5", +2),
            "b": ("Assuming no risk with old software", -1),
            "c": ("Depending solely on antivirus", "Q7", +1)},
    "Q13": {"a": ("Being skeptical of unknown links", "Q8", +2),
            "b": ("Accepting all friend requests", -1),
            "c": ("Limiting time on social platforms", "Q10", +1)},
    "Q14": {"a": ("Reporting suspicious activities", "Q11", +2),
            "b": ("Sharing questionable content", -1),
            "c": ("Ignoring the content", "Q13", +1)},
    "Q15": {"a": ("Being transparent about data usage", "Q14", +2),
            "b": ("Using AI without understanding", -1),
            "c": ("Relying on default settings", "Q16", +1)},
    "Q16": {"a": ("Using a VPN", "Q17", +2),
            "b": ("Connecting to any available network", -1),
            "c": ("Checking network security manually", "Q19", +1)},
    "Q17": {"a": ("Reviewing app permissions regularly", "Q20", +2),
            "b": ("Allowing all apps to access location", -1),
            "c": ("Disabling security notifications", "Q22", +1)},
    "Q18": {"a": ("Curating digital content shared online", "Q23", +2),
            "b": ("Assuming privacy settings are adequate", -1),
            "c": ("Frequently changing social media profiles", "Q25", +1)},
    "Q19": {"a": ("Understanding the terms of service agreements", "Q26", +2),
            "b": ("Skipping the reading of user agreements", -1),
            "c": ("Assuming digital content is free to use", "Q28", +1)},
    "Q20": {"a": ("Being mindful of personal branding", "Q29", +2),
            "b": ("Oversharing for popularity", -1),
            "c": ("Ignoring the impact of online posts", "Q1", +1)},
    "Q21": {"a": ("Securing accounts and monitoring for breaches", "Q2", +2),
            "b": ("Waiting for companies to act first", -1),
            "c": ("Informing friends and family only", "Q4", +1)},
    "Q22": {"a": ("Evaluating AI's role in privacy erosion", "Q5", +2),
            "b": ("Ignoring AI's impact on data privacy", -1),
            "c": ("Focusing only on AI benefits", "Q7", +1)},
    "Q23": {"a": ("Considering ethical implications of AI", "Q8", +2),
            "b": ("Disregarding AI's influence on decision-making", -1),
            "c": ("Emphasizing AI's efficiency only", "Q10", +1)},
    "Q24": {"a": ("Promoting responsible digital citizenship", "Q11", +2),
            "b": ("Assuming secure online environments", -1),
            "c": ("Relying on platforms to ensure safety", "Q13", +1)},
    "Q25": {"a": ("Understanding the impact of data breaches", "Q14", +2),
            "b": ("Minimizing the significance of personal data leaks", -1),
            "c": ("Assuming breaches are quickly resolved", +1)},
    "Q26": {"a": ("Adapting to different digital laws", "Q17", +2),
            "b": ("Ignoring international regulations", -1),
            "c": ("Assuming uniform digital rights globally", "Q19", +1)},
    "Q27": {"a": ("Balancing anonymity with accountability", "Q20", +2),
            "b": ("Using anonymity to avoid responsibility", -1),
            "c": ("Overvaluing anonymity over transparency", "Q22", +1)},
    "Q28": {"a": ("Implementing robust anti-malware measures", "Q23", +2),
            "b": ("Assuming antivirus is infallible", -1),
            "c": ("Underestimating malware threats", "Q25", +1)},
    "Q29": {"a": ("Checking for secure connection indicators", "Q26", +2),
            "b": ("Assuming all websites are secure", -1),
            "c": ("Ignoring browser security warnings", "Q28", +1)},
    "Q30": {"a": ("Using digital signatures and copyrights", +2),
            "b": ("Neglecting copyright laws", -1),
            "c": ("Sharing work without proper attribution", "Q1", +1)}}


#######################################################################################################################

## Main

#######################################################################################################################


def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Set up the page config
logo_path = 'UC_logo.png'  # Confirm this path is correct
logo = Image.open(logo_path)
logo_base64 = get_image_base64(logo_path)
st.set_page_config(page_title="Enhancing Decision-Making in Human Agent Team", page_icon=logo, layout='wide')


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
        page_farm(farm_questions, farm_options, page_name='irrigation')
    elif st.session_state['current_page'] == 'finance':
        page_farm(finance_questions, finance_options, page_name='finance')
    elif st.session_state['current_page'] == 'health':
        page_farm(health_questions, health_options, page_name='health')
    elif st.session_state['current_page'] == 'security':
        page_farm(digital_questions, digital_options, page_name='security')


if __name__ == "__main__":
    main()
