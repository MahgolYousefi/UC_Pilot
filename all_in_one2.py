
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

       "Q29": "What advanced techniques enhance irrigation efficiency?",

       "Q30": "What are the important end-of-season maintenance actions for irrigation systems?"

}


farm_options = {
   "Q1": {"a": ("Use data from soil moisture sensors to determine irrigation needs", "Q4", +2),

          "b": ("Irrigate based on current soil moisture data obtained through manual testing", "Q3", +1),

          "c": ("Seek personalized advice from local irrigation experts based on current soil data", "Q2", -1)},

   "Q2": {"a": ("Estimate soil moisture from visual inspections", "Q3", -1),

          "b": ("Analyze plant stress indicators", "Q5", +2),

          "c": ("Use historical weather patterns to predict irrigation needs", "Q4", +1)},

   "Q3": {"a": ("System that meets your minimum functional requirements at the lowest cost", "Q7", +2),

          "b": ("Systems with automation and weather tracking for long-term efficiency", "Q4", -1),

          "c": ("Ease of maintenance and operation to minimize future service costs", "Q6", +1)},

   "Q4": {"a": ("Adjust irrigation systems to use water more effectively based on soil capacity", "Q10", +2),

          "b": ("Maintain a fixed irrigation routine regardless of soil type", "Q5", -1),

          "c": ("Tailor water usage predictions to seasonal variations and soil characteristics", "Q8", +1)},

   "Q5": {"a": ("Schedule regular preventive maintenance to optimize system performance", "Q11", +2),

          "b": ("Perform reactive maintenance by addressing system failures as they occur", "Q6", -1),

          "c": ("Update software systems and conduct basic inspections annually", "Q9", +1)},

   "Q6": {"a": ("Maintain a consistent irrigation schedule based on historical averages", "Q7", -1),

          "b": ("Adjust dynamically based on soil moisture and plant stress data", "Q11", +2),

          "c": ("Incorporate weather forecast adjustments along with a baseline irrigation schedule", "Q8", +1)},

   "Q7": {"a": ("Utilize subsurface drip irrigation for precise water delivery to plant root zones", "Q12", +2),

          "b": ("Employ overhead sprinklers with even water distribution across the field", "Q10", +1),

          "c": ("Implement furrow irrigation for efficient water delivery along furrows", "Q8", -1)},

   "Q8": {"a": ("Increase in runoff and reduced water infiltration, wasting water and potential nutrient leaching", "Q9", -1),

          "b": ("Waterlogging of the root zone, leading to reduced oxygen availability and potential root damage", "Q13", +2),

          "c": ("Inefficient use of water resources, potentially leading to unnecessary irrigation expenses", "Q12", +1)},

   "Q9": {"a": ("Ensure uniform and efficient water distribution across various pressure settings", "Q15", +2),

          "b": ("Reduce the frequency and cost of maintenance by operating reliably under varying conditions", "Q14", +1),

          "c": ("Rely on generic pumps that may not be optimized for specific irrigation needs", "Q10", -1)},

   "Q10": {"a": ("Disregard rainfall forecasts and continue with preset irrigation schedules", "Q11", -1),

           "b": ("Use rainfall forecasts to adjust irrigation volumes and timings to prevent overwatering", "Q17", +2),

           "c": ("Modify irrigation strategies based on recent rainfall events and soil moisture data", "Q16", +1)},

   "Q11": {"a": ("Failing to account for variations in water pressure and flow requirements across different zones", "Q18", +1),

           "b": ("Neglecting to consider soil type variability, leading to uneven water distribution", "Q12", -1),

           "c": ("Not adjusting nozzle types and spacing based on crop type and growth stage requirements", "Q19", +2)},

   "Q12": {"a": ("Enhanced energy efficiency by adjusting motor speed to demand, reducing power use", "Q20", +2),

           "b": ("Continue with fixed-speed pumps, which often offer less flexibility and efficiency", "Q13", -1),

           "c": ("Allow for precise control of water flow, adapting to changes in irrigation needs", "Q10", +1)},

   "Q13": {"a": ("Adjust irrigation frequency and volume to match increased water loss from plants and soil", "Q22", +2),

           "b": ("Continue with a regular irrigation timetable without adjusting for climatic changes", "Q14", -1),

           "c": ("Incorporate real-time evapotranspiration rates into irrigation planning to optimize water use", "Q21", +1)},

   "Q14": {"a": ("Perform preventative maintenance after significant weather events to ensure system functionality", "Q23", +1),

           "b": ("To detect and rectify issues early, preventing costly downtime and repairs", "Q24", +2),

           "c": ("Inspect systems only in response to evident issues, risking the escalation of undetected problems", "Q15", -1)},

   "Q15": {"a": ("Evaluate local water resources and compliance with water usage regulations", "Q26", +2),

           "b": ("Prioritize the initial cost of the system before considering efficiency or suitability", "Q16", -1),

           "c": ("Plan for the system’s future expansion and integration with new irrigation technologies", "Q25", +1)},

   "Q16": {"a": ("Sprinkler systems distribute water over large areas while; drip systems provide more controlled and consistent delivery directly to plant root zones", "Q27", +2),

           "b": ("All systems are equally effective regardless of design", "Q17", -1),

           "c": ("Examine technological enhancements in systems that improve precision in water delivery, adjusting to field and crop needs", "Q26", +1)},

   "Q17": {"a": ("Adjust settings based on soil composition and permeability", "Q29", +2),

           "b": ("Set a uniform irrigation schedule for all soil types", "Q18", -1),

           "c": ("Monitor soil moisture levels closely to avoid over-irrigation", "Q28", +1)},

   "Q18": {"a": ("Implement rain sensors to halt irrigation during downpours", +2),

           "b": ("Continue irrigation during rain to ensure schedule adherence", "Q19", -1),

           "c": ("Use drought-resistant plants to reduce water needs", "Q30", +1)},

   "Q19": {"a": ("Collect runoff water for reuse in irrigation", +1),

           "b": ("Increase irrigation rates to promote deeper root growth", "Q20", -1),

           "c": ("Integrate drip irrigation systems to reduce runoff", +2)},

   "Q20": {"a": ("Use a single pressure setting for simplicity", "Q21", -1),

           "b": ("Ensure that irrigation pressures are optimized for each crop type", +2),

           "c": ("Regularly test system pressure to detect any discrepancies", +1)},

   "Q21": {"a": ("Soil temperature is a non-significant factor", "Q22", -1),

           "b": ("Higher soil temperatures increase evaporation and plant transpiration rates, requiring more frequent irrigation", +1),

           "c": ("Soil temperature variations affect water uptake by roots, necessitating adjustments in irrigation timing and volume for optimal growth", +2)},

   "Q22": {"a": ("Reduce irrigation frequency during wet seasons", +1),

           "b": ("Enhance soil drainage systems to cope with excess water", +2),

           "c": ("Maintain a steady irrigation routine throughout the year", "Q23", -1)},

   "Q23": {"a": ("Optimize schedules to water during the cooler parts of the day", +2),

           "b": ("Stick to a fixed watering schedule to simplify management", "Q24", -1),

           "c": ("Increase watering during hot periods to reduce plant stress", +1)},

   "Q24": {"a": ("Optimize equipment setup seasonally to adapt to changing crop needs and environmental conditions", +2),

           "b": ("Keep the irrigation setup consistent year-round", "Q25", -1),

           "c": ("Regularly review and tweak equipment settings for efficiency", +1)},

   "Q25": {"a": ("Choose early morning hours to minimize evaporation losses", +2),

           "b": ("Irrigate at noon to coincide with peak sun and heat", "Q26", -1),

           "c": ("Alternate irrigation times weekly to test different efficiencies", +1)},

   "Q26": {"a": ("Customize irrigation based on specific crop water needs", +2),

           "b": ("Apply the same amount of water regardless of the crop type", "Q27", -1),

           "c": ("Consider crop profitability to ensure economic sustainability while meeting basic water needs", +1)},

   "Q27": {"a": ("Excessive minimization of irrigation could stress plants, forcing roots to extend deeper, which might not always be beneficial", +2),

           "b": ("Consistent over-irrigation leads to soil saturation, reducing aeration and potentially causing root rot and nutrient leaching", "Q28", -1),

           "c": ("Adjusting water application based on indicators like soil moisture and plant health can maintain optimal soil conditions", +1)},

   "Q28": {"a": ("Adjust irrigation frequency based on the plant growth stages", +2),

           "b": ("Disregard the varying needs for water during different plant growth stages", "Q29", -1),

           "c": ("Use generic irrigation schedules regardless of plant growth", -1)},

   "Q29": {"a": ("Employ evapotranspiration models to adjust irrigation based on climatic conditions and plant water requirements", +2),

           "b": ("Use irrigation schedules without adapting to changes in weather or crop stages", -1),

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

     "Q3": "How should an investor adjust his/her portfolio in response to a major stock market correction?",

     "Q4": "What critical factor should be considered before investing in high-yield bonds?",

     "Q5": "What is a wise approach to managing significant credit card debt?",

     "Q6": "How should personal investments be adjusted in anticipation of rising inflation?",

     "Q7": "As a university student managing your finances, what is the most beneficial strategy for saving for future educational expenses?",

     "Q8": "What should be prioritized when creating a long-term financial plan?",

     "Q9": "How can one optimize their investment portfolio for tax efficiency?",

     "Q10": "What is a key consideration when selecting a life insurance policy?",

     "Q11": "What strategy can young adults adopt to manage their assets and minimize future tax liabilities?",

     "Q12": "How can one ensure adequate diversification in their investment portfolio?",

     "Q13": "What is the best way to approach debt consolidation?",

     "Q14": "How should one decide between investing in a Roth IRA versus a traditional IRA?",

     "Q15": "What are the risks associated with investing in emerging markets?",

     "Q16": "What factors should be considered when planning to buy versus rent a home?",

     "Q17": "What is an effective strategy for managing a personal budget?",

     "Q18": "How should one evaluate the decision to refinance a mortgage?",

     "Q19": "What strategy should be prioritized when launching a new business to mitigate initial risks?",

     "Q20": "How does one determine the right amount of emergency savings?",

     "Q21": "What steps should be taken to protect one's financial information online?",

     "Q22": "How should one assess the impact of economic recession on personal finances?",

     "Q23": "Which approach can significantly enhance the efficiency of paying off student loans?",

     "Q24": "What are effective strategies for leveraging real estate to build wealth?",

     "Q25": "What factors should influence the asset allocation in a retirement portfolio?",

     "Q26": "As a young professional, how should you revise your financial goals following significant life changes, such as a new job or moving to a new city?",

     "Q27": "What should be factored into retirement planning to effectively manage future healthcare costs?",

     "Q28": "When is it okay to accept higher investment fees?",

     "Q29": "What is the most effective way to utilize credit scores for securing low-interest loans?",

     "Q30": "What key step should not be overlooked in a financial risk management plan?",

 }


finance_options = {
     "Q1": {"a": ("Maximize contributions to tax-deferred accounts", "Q4", +2),

            "b": ("Invest in a diverse portfolio of stocks", "Q3", +1),

            "c": ("Purchase annuities for guaranteed income", "Q2", -1)},

     "Q2": {"a": ("Invest entirely in a diversified stock portfolio", "Q3", -1),

            "b": ("Allocate to an emergency fund, then invest the rest", "Q5", +2),

            "c": ("Pay off existing debt, then save the remainder", "Q4", +1)},

     "Q3": {"a": ("Rebalance to maintain original asset allocation and risk profile", "Q7", +2),

            "b": ("Shift a portion to more conservative investments, such as bonds, to mitigate risk", "Q4", -1),

            "c": ("Identify and invest in stocks that may now be undervalued", "Q6", +1)},

     "Q4": {"a": ("Assess the credit risk and maturity period", "Q10", +2),

            "b": ("Focus on the potential returns not risks", "Q5", -1),

            "c": ("Choose bonds with the highest yield", "Q8", +1)},

     "Q5": {"a": ("Consolidate debt through a personal loan", "Q11", +2),

            "b": ("Only make minimum payments to manage cash flow", "Q6", -1),

            "c": ("Transfer balances to a zero-interest card", "Q9", +1)},

     "Q6": {"a": ("Increase allocations to inflation-resistant assets like real estate and commodities", "Q11", +2),

            "b": ("Convert a portion of investments to cash to manage potential market downturns", "Q7", -1),

            "c": ("Adjust investment ratios subtly while monitoring economic indicators closely", "Q8", +1)},

     "Q7": {"a": ("Utilize a savings plan like a 529 that provides tax advantages and educational expense flexibility", "Q12", +2),

            "b": ("Allocate a portion of investments into mutual funds specifically designated for educational purposes", "Q10", +1),

            "c": ("Plan on leveraging scholarships and student loans to cover educational costs", "Q8", -1)},

     "Q8": {"a": ("Focus on accumulating assets ignoring liabilities", "Q9", -1),

            "b": ("Balance between saving, investing, and debt repayment", "Q13", +2),

            "c": ("Prioritize high-risk, high-return investments", "Q12", +1)},

     "Q9": {"a": ("Invest in tax-exempt municipal bonds", "Q15", +2),

            "b": ("Maximize contributions to retirement accounts", "Q14", +1),

            "c": ("Avoid selling assets to reduce capital gains", "Q10", -1)},

     "Q10": {"a": ("Opt for the policy offering the most affordable premiums", "Q16", +1),

             "b": ("Assess policies based on coverage depth, terms, and insurer reliability", "Q17", +2),

             "c": ("Choose a policy recommended by trusted family or financial advisors", "Q11", -1)},

     "Q11": {"a": ("Establish a trust to protect assets and minimize taxes", "Q18", +2),

             "b": ("Distribute assets equally among heirs without tax planning", "Q12", -1),

             "c": ("Incorporate life insurance to manage future tax burdens on assets", "Q18", +1)},

     "Q12": {"a": ("Invest in a mix of domestic and international funds", "Q20", +2),

             "b": ("Focus solely on high-growth tech stocks", "Q13", -1),

             "c": ("Keep all investments in bonds for safety", "Q19", +1)},

     "Q13": {"a": ("Combine all debts into one low-interest loan", "Q22", +2),

             "b": ("Pay off each debt separately to track progress", "Q21", +1),

             "c": ("Take out a home equity loan to pay off credit card debt", "Q14", -1)},

     "Q14": {"a": ("Invest based on tax implications now and expected income at retirement", "Q24", +2),

             "b": ("Choose based on the advice of a financial advisor", "Q23", +1),

             "c": ("Opt for traditional IRA for immediate tax relief", "Q15", -1)},

     "Q15": {"a": ("Evaluate political and economic stability before investing", "Q26", +2),

            "b": ("Invest small amounts regardless of market conditions", "Q16", -1),

             "c": ("Focus on sectors with potential for quick growth", "Q25", +1)},

     "Q16": {"a": ("Consider long-term financial goals and real estate market trends", "Q27", +2),

             "b": ("Always prefer to rent for financial flexibility", "Q17", -1),

             "c": ("Buy a home when the mortgage is less than rent", "Q26", +1)},

     "Q17": {"a": ("Track income and expenses strictly and adjust as needed", "Q29", +2),

             "b": ("Set a fixed budget and stick to it regardless of changes in income", "Q28", +1),

             "c": ("Prioritize expenses based on immediate needs only", "Q18", -1)},

     "Q18": {"a": ("Refinance only when it leads to substantial immediate monthly savings", "Q19", -1),

             "b": ("Consider refinancing when there's a significant decrease in interest rates", "Q30", +1),

             "c": ("Evaluate the benefits of a longer-term loan regardless of immediate market fluctuations", +2)},

     "Q19": {"a": ("Thoroughly analyse market demand and scalability prospects", +1),

             "b": ("Begin with a lean startup approach, minimising initial costs and expanding gradually", +2),

             "c": ("Target a niche market, minimizing the impact of competitors", "Q20", -1)},

     "Q20": {"a": ("Set aside 6-12 months of expenses depending on job stability", +2),

             "b": ("Save a flat rate monthly regardless of overall expenses", "Q21", -1),

             "c": ("Adjust savings based on current economic conditions", +1)},

     "Q21": {"a": ("Use unique passwords and two-factor authentication for all financial accounts", +2),

             "b": ("Regularly monitor financial statements for unauthorized transactions", +1),

             "c": ("Rely on bank security measures and fraud protection services", "Q22", -1)},

     "Q22": {"a": ("Focus on enhancing liquidity through increased cash holdings and similar assets", +1),

             "b": ("Seize the opportunity to buy undervalued assets while continuing regular investment activities", +2),

             "c": ("Shift investments towards sectors typically resistant to economic downturns, such as utilities and consumer staples", "Q23", -1)},

     "Q23": {"a": ("Focus on eliminating loans with the highest interest rates first to minimize overall interest costs", +2),

             "b": ("Opt for income-based repayment plans that adjust payments according to your financial situation", +1),

             "c": ("Consolidate multiple student loans into a single payment for better management and potentially lower rates", "Q24", -1)},

     "Q24": {"a": ("Acquire residential properties in urban areas for long-term rental income", +1),

             "b": ("Invest in vacation homes that can be rented out on a short-term basis", +2),

             "c": ("Engage in house flipping, targeting properties that can be quickly renovated and sold at a profit", "Q25", -1)},

     "Q25": {"a": ("Shift more towards bonds and stable investments as retirement approaches", +2),

             "b": ("Maintain a high proportion of stocks for growth", +1),

             "c": ("Invest heavily in emerging markets for potentially high returns", "Q26", -1)},

     "Q26": {"a": ("Assess and realign your savings and investment strategies to better suit your updated life circumstances", +2),

             "b": ("Continue with your existing financial strategies to avoid disruption", "Q27", -1),

             "c": ("Prioritize immediate financial needs and adjust long-term aspirations as your situation stabilises", +1)},

     "Q27": {"a": ("Secure long-term care insurance and explore the benefits of health savings accounts", +2),

             "b": ("Rely on governmental support like Medicare to handle healthcare needs", "Q28", -1),

             "c": ("Establish a dedicated savings fund for unforeseen medical expenses", +1)},

     "Q28": {"a": ("If the fund consistently beats the market, fees included", +1),

             "b": ("If the fund is managed by highly successful managers", "Q29", -1),

             "c": ("If the returns after fees meet your investment goals", +2)},

     "Q29": {"a": ("Regularly review and optimise credit reports for accuracy", +2),

             "b": ("Focus on high credit utilisation to demonstrate creditworthiness", "Q30", -1),

             "c": ("Apply for multiple credit lines to increase available credit", +1)},

     "Q30": {"a": ("Expand your portfolio across different types of investments for risk spread", +1),

             "b": ("Invest in opportunities that promise high returns despite the higher risk", -1),

             "c": ("Ensure adequate insurance coverage to protect against unforeseen financial losses", +2)}

 }


#######################################################################################################################

## Health

#######################################################################################################################
health_questions = {

 "Q1": "Considering the varied nature of obesity, what is often the most influential factor in the occurance of excess weight across diverse populations?",

 "Q2": "In the evaluation of obesity and associated health risks, which metric provides the most widely used assessment of excess weight?",

 "Q3": "What minimal percentage of weight loss significantly reduces health risks?",

 "Q4": "Considering the multifactorial nature of obesity, which factor significantly complicates individual efforts towards weight management?",

 "Q5": "Which macronutrient is crucial for numerous bodily functions but should be moderated in dietary intake due to its high caloric density?",

 "Q6": "Which pervasive environmental change in modern society most significantly contributes to increasing obesity rates?",

 "Q7": "Which approach is least effective for long-term weight management?",

 "Q8": "Which initial action best aligns with an effective strategy for weight management?",

 "Q9": "In what ways do psychological elements contribute to fluctuations in body weight?",

 "Q10": "To what extent do genetics contribute to an individual's risk of developing obesity?",

 "Q11": "Which type of physical activity is recommended for effective weight loss?",

 "Q12": "How does optimal water consumption vary in a diet plan aimed at weight loss, considering individual physiological differences?",

 "Q13": "What is the best practice for incorporating proteins into a balanced diet?",

 "Q14": "What is the optimal strategy for integrating fats into a diet to support cardiovascular health and overall wellness?",

 "Q15": "What is the primary benefit of incorporating dietary fiber into a weight loss regimen?",

 "Q16":  "How can increased feelings of fullness contribute to a sustainable weight management plan?",

 "Q17": "What is a common but misleading perception about the effectiveness of dieting for weight loss?",

 "Q18": "Which meal planning strategy best supports sustainable weight management and balanced nutrition?",

 "Q19": "When considering fats in a weight loss diet, which characteristic is most beneficial for long-term health?",

 "Q20": "Which psychological strategy is most effective for maintaining long-term weight loss?",

 "Q21": "What is the least helpful method to achieve and maintain a healthy weight?",

 "Q22": "Which strategy is most recommended for a beginner to start losing weight?",

 "Q23": "What is the recommended timing for surgical interventions in the treatment of obesity?",

 "Q24": "What is the best initial dietary change to make when starting a weight loss plan?",

 "Q25": "What common dietary advice is now considered outdated?",

 "Q26": "In what ways can modern technology facilitate effective weight management?",

 "Q27":  "What is an essential factor to consider when selecting medications for weight loss?",

 "Q28": "Which lifestyle change provides the most sustainable impact on weight loss?",

 "Q29": "What nutritional misconception could lead to ineffective dieting?",

 "Q30":  "Which approach is most effective in sustaining long-term weight management?",

}


health_options = {
 "Q1": {"a": ("Biological predispositions that affect metabolic rates", "Q3", +1),

        "b": ("Changes in lifestyle patterns that reduce physical activity", "Q2", -1),

        "c": ("Patterns of food consumption and overall calorie management", "Q4", +2)},

 "Q2": {"a": ("Body Mass Index (BMI), a common standard for categorizing weight relative to height", "Q7", +2),

        "b": ("Waist-to-hip ratio, which assesses fat distribution and potential risk", "Q3", -1),

        "c": ("Body fat percentage, a direct measure of body composition", "Q6", +1)},

 "Q3": {"a": ("5% of total body weight", "Q4", -1),

        "b": ("10% of total body weight", "Q7", +2),

        "c": ("15% of total body weight", "Q6", +1)},

 "Q4": {"a": ("Personal discipline issues, including consistency in diet and exercise", "Q5", -1),

        "b": ("Genetic predispositions that influence metabolic rate and fat storage", "Q10", +2),

        "c": ("Environmental factors, such as availability of and access to healthy food options", "Q8", +1)},

 "Q5": {"a": ("Proteins, which are vital for muscle repair and growth", "Q6", -1),

        "b": ("Fats, necessary for hormone production and nutrient absorption", "Q11", +2),

        "c": ("Carbohydrates, main source of energy for daily activities", "Q9", +1)},

 "Q6": {"a": ("Increased food availability", "Q11", +2),

        "b": ("Economic factors", "Q7", -1),

        "c": ("Technological advancements", "Q8", +1)},

 "Q7": {"a": ("Following fad diets", "Q12", +2),

        "b": ("Caloric restriction", "Q8", -1),

        "c": ("Sustainable lifestyle changes", "Q10", +1)},

 "Q8": {"a": ("Setting realistic goals", "Q13", +2),

        "b": ("Seeking professional advice", "Q12", +1),

        "c": ("Committing to a fitness facility", "Q9", -1)},

 "Q9": {"a": ("Emotional overeating", "Q15", +2),

        "b": ("Sleep deprivation", "Q10", -1),

        "c": ("Interpersonal tensions", "Q14", +1)},

 "Q10": {"a": ("70% genetic influence", "Q11", -1),

         "b": ("50% genetic influence", "Q16", +1),

         "c": ("30% genetic influence", "Q17", +2)},

 "Q11": {"a": ("High-intensity steady-state cardio", "Q18", +1),

         "b": ("High-intensity interval training", "Q19", +2),

         "c": ("Weight training", "Q12", -1)},

 "Q12": {"a": ("Maintain a baseline of at least 2 liters per day, potentially increasing based on factors like physical activity and overall health", "Q20", +2),

         "b": ("Recommend a flexible approach, starting at 1 liter per day and adjusting according to personal health advice and bodily responses", "Q13", -1),

         "c": ("Tailor water intake to personal hydration cues and adjust according to specific dietary and exercise regimes", "Q19", +1)},

 "Q13": {"a": ("Focus primarily on animal-based proteins, which are complete sources of all essential amino acids", "Q14", -1),

         "b": ("Mix of plant-based and animal-based proteins for nutritional diversity", "Q22", +2),

         "c": ("Include plant-based proteins predominantly, supplementing with animal-based proteins as needed", "Q21", +1)},

 "Q14": {"a": ("Focus primarily on increasing the intake of omega-9 monounsaturated fats, such as those found in olive oil", "Q15", -1),

         "b": ("Limit all forms of dietary fats significantly to reduce calorie intake and prevent fat accumulation", "Q23", +1),

         "c": ("Balance the intake of omega-3 and omega-6 polyunsaturated fats, ensuring a higher proportion of omega-3s from sources like fish and flaxseed", "Q24", +2)},

 "Q15": {"a": ("It accelerates the metabolism, leading to rapid weight loss", "Q25", +1),

         "b": ("It supports digestive health, promoting satiety and regular bowel movements", "Q26", +2),

         "c": ("It enhances nutrient absorption, ensuring efficient use of consumed calories", "Q16", -1)},

 "Q16": {"a": ("By reducing overall caloric intake", "Q27", +2),

         "b": ("By increasing energy expenditure", "Q26", +1),

         "c": ("By improving metabolic flexibility", "Q17", -1)},

 "Q17": {"a": ("Emphasizing the quality of food consumed is more important than the quantity for sustainable weight loss", "Q18", -1),

         "b": ("Effective dieting primarily revolves around strict calorie restriction regardless of nutritional value", "Q28", +2),

         "c": ("Short-term dieting approaches can lead to long-term weight management success", "Q28", +1)},

 "Q18": {"a": ("Adopting a fixed calorie limit", "Q19", -1),

         "b": ("Integrating a balance of macronutrients and permit occasional indulgences", "Q30", +2),

         "c": ("Focusing primarily on high-protein, low-carb meals to maximise fat loss", "Q29", +1)},

 "Q19": {"a": ("High levels of medium-chain triglycerides (MCTs) for quick energy", "Q20", -1),

         "b": ("High in monounsaturated fats which support heart health", +2),

         "c": ("Rich in saturated fats to increase satiety and reduce hunger", +1)},

 "Q20": {"a": ("Creating a system of small, frequent rewards to maintain motivation", "Q21", -1),

         "b": ("Establishing a reliable support network for encouragement and accountability", +2),

         "c": ("Regularly setting and reassessing short-term, achievable goals", +1)},

 "Q21": {"a": ("Adopting a very low-calorie diet", "Q22", -1),

         "b": ("Incorporating moderate physical activity", +1),

         "c": ("Making gradual dietary adjustments", +2)},

 "Q22": {"a": ("Joining a weight loss clinic", "Q23", -1),

         "b": ("Starting with light exercise", +2),

         "c": ("Starting with cutting all sugars", +1)},

 "Q23": {"a": ("They are preferred as an initial treatment option", "Q24", -1),

         "b": ("They are considered after lifestyle and pharmacological interventions have been attempted", +2),

         "c": ("They are avoided in favor of non-invasive methods", +1)},

 "Q24": {"a": ("Increasing protein intake", +1),

         "b": ("Eliminating all fats", "Q25", -1),

         "c": ("Reducing processed foods", +2)},

 "Q25": {"a": ("Eating multiple small meals is necessary", "Q26", -1),

         "b": ("Calorie counting is the only way to lose weight", +1),

         "c": ("Balanced macronutrients are key", +2)},

 "Q26": {"a": ("Integrating comprehensive dietary tracking applications with personalised feedback systems", +2),

         "b": ("Minimising screen time and digital device usage to focus on physical activities", "Q27", -1),

         "c": ("Utilising wearable devices exclusively to monitor physical activity levels without considering dietary intake", +1)},

 "Q27": {"a": ("They should be used without medical consultation", "Q28", -1),

         "b": ("They are typically for individuals with a BMI exceeding 30", +2),

         "c": ("They can serve as a substitute for dietary modifications", +1)},

 "Q28": {"a": ("Switching to a vegetarian diet", +1),

         "b": ("Gradual increase in physical activity", +2),

         "c": ("Frequent fasting periods", "Q29", -1)},

 "Q29": {"a": ("Fats are the main dietary enemy", "Q30", -1),

         "b": ("All carbs must be eliminated", +1),

         "c": ("Protein should be the focus of the diet", +2)},

 "Q30": {"a": ("Regularly switching diet plans to prevent metabolic adaptation", +1),

         "b": ( "Adhering to consistent, healthy eating habits", +2),

         "c": ("Avoiding all social situations involving food to control intake", -1)}

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
            "c": ("Sharing work without proper attribution", "Q1", +1)}
}


#######################################################################################################################

## Main

#######################################################################################################################

def reset_state():
    # Reset all session state variables necessary for starting a new task
    st.session_state['current_question'] = 'Q1'
    st.session_state['user_responses'] = {}
    st.session_state['selected_option'] = None
    st.session_state['total_score'] = 0
    st.session_state['path_length'] = 0
    st.session_state['endpoint_reached'] = False


# Define a function that resets the state and switches to a new task
def load_task(task_key):
    reset_state()
    st.session_state['current_page'] = task_key
    st.rerun()


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
        "🏦 Financial Decisions": 'finance',
        "🥦 Health Decisions": 'health'
        # "🔒 Mock Example": 'security'
    }

    # Render task selection buttons
    for page_name, page_key in page_options.items():
        if st.button(page_name):
            load_task(page_key)

    # for page_name, page_key in page_options.items():
    #     if st.button(page_name):
    #         st.session_state['current_page'] = page_key

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
    # elif st.session_state['current_page'] == 'security':
    #     page_farm(digital_questions, digital_options, page_name='security')


if __name__ == "__main__":
    main()
