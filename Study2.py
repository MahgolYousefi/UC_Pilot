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



background_info = """
**Background on Good Irrigation Practices for Dairy Farms**

The DairyNZ Guide to Good Irrigation is designed to assist dairy farmers in refining their irrigation practices. It is essential for farm staff and managers to understand how factors such as soil and plant types, climate, and the capabilities of various irrigation systems impact the farm’s irrigation needs. The guide emphasizes the importance of timely and appropriate water application, considering both volume and frequency, to optimize farm operations. Key aspects include managing water supply conditions, ensuring water quality, using water efficiently, and maintaining irrigation equipment effectively.

Additionally, it stresses the importance of soil moisture monitoring, upgrading old systems, and the strategic planning necessary when designing and installing new irrigation systems. This comprehensive approach aims to foster better irrigation practices that not only meet the specific needs of the farm but also contribute to responsible water management within the broader community.
"""

data = {
    "Q1": {
        "Question": "What is the primary consideration for starting spring irrigation on a dairy farm?",
        "Options": {
            "a": "Use real-time data from soil moisture sensors to determine irrigation needs",
            "b": "Irrigate based on current soil moisture data obtained through manual testing",
            "c": "Seek personalized advice from local agricultural experts based on current soil data",
            "d": "Initiate irrigation based on historical calendar dates commonly used in the region"
        },
        "Correct Option": "a"
    },
    "Q2": {
        "Question": "What is the most accurate method to assess soil moisture before initiating irrigation?",
        "Options": {
            "a": "Estimate soil moisture from visual inspections",
            "b": "Deploy soil moisture sensors for real-time data",
            "c": "Use historical weather patterns to predict needs",
            "d": "Follow a predetermined irrigation schedule"
        },
        "Correct Option": "b"
    },
    "Q3": {
        "Question": "What key factor influences the choice of an irrigation system for dairy farming?",
        "Options": {
            "a": "Prioritize systems from reputable local suppliers for faster initial support",
            "b": "Consider systems with automation and weather tracking for long-term efficiency",
            "c": "Evaluate ease of maintenance and operation to minimize future service costs",
            "d": "Choose the system that meets your minimum functional requirements at the lowest cost"
        },
        "Correct Option": "d"
    },
    "Q4": {
        "Question": "Why is it important to understand the water holding capacity (WHC) of your soil?",
        "Options": {
            "a": "Assume a pre-defined average water holding capacity for your crop type",
            "b": "Optimize irrigation based on real-time soil moisture data and historical water holding capacity",
            "c": "Follow regulatory guidelines for water usage, adjusting for local conditions if allowed"
        },
        "Correct Option": "b"
    },
    "Q5": {
        "Question": "What routine maintenance is essential for maintaining irrigation efficiency?",
        "Options": {
            "a": "Schedule regular preventive maintenance to optimize system performance",
            "b": "Perform reactive maintenance by addressing system failures as they occur",
            "c": "Update software systems and conduct basic inspections annually"
        },
        "Correct Option": "a"
    },
    "Q6": {
        "Question": "How should irrigation frequency be adjusted throughout the growing season?",
        "Options": {
            "a": "Maintain a consistent irrigation schedule based on historical averages",
            "b": "Adjust irrigation frequency dynamically based on real-time soil moisture and plant stress data",
            "c": "Incorporate weather forecast adjustments along with a baseline irrigation schedule"
        },
        "Correct Option": "b"
    },
    "Q7": {
        "Question": "Which irrigation method minimizes water loss in sandy soils?",
        "Options": {
            "a": "Utilize subsurface drip irrigation for precise water delivery to plant root zones",
            "b": "Employ overhead sprinklers with even water distribution across the field",
            "c": "Implement furrow irrigation for efficient water delivery along furrows"
        },
        "Correct Option": "a"
    },
    "Q8": {
        "Question": "What are the risks of irrigating when the soil is at field capacity?",
        "Options": {
            "a": "Disregard risks and follow standard irrigation volume",
            "b": "Address risks of over-watering and waterlogging",
            "c": "Optimize based on recent field capacity measurements"
        },
        "Correct Option": "b"
    },
    "Q9": {
        "Question": "What role does an efficient pump play in an irrigation system?",
        "Options": {
            "a": "To ensure efficient delivery at varied pressures",
            "b": "To minimize system maintenance needs",
            "c": "Use standard pumps without custom settings"
        },
        "Correct Option": "a"
    },
    "Q10": {
        "Question": "How should rainfall data integrate into irrigation planning?",
        "Options": {
            "a": "Ignore weather forecasts and rely on set schedules",
            "b": "Incorporate rainfall predictions into planning",
            "c": "Adjust plans based on soil saturation levels"
        },
        "Correct Option": "b"
    },
    "Q11": {
        "Question": "What common installation error should be avoided with irrigation nozzles?",
        "Options": {
            "a": "Reviewing local irrigation guidelines and adapting as necessary",
            "b": "Ignoring variations in soil types across fields",
            "c": "Analyzing historical crop response data to refine practices",
            "d": "Consulting with a water management specialist"
        },
        "Correct Option": "c"
    },
    "Q12": {
        "Question": "What is a major benefit of variable speed drives on irrigation pumps?",
        "Options": {
            "a": "Upgrade to variable speed drive pumps for better energy efficiency",
            "b": "Continue using older, less efficient pump technology",
            "c": "Implement automated water flow sensors to adjust rates"
        },
        "Correct Option": "a"
    },
    "Q13": {
        "Question": "What is the best strategy for irrigation during periods of high evapotranspiration?",
        "Options": {
            "a": "Increase watering frequency during periods of high heat",
            "b": "Maintain a constant irrigation schedule regardless of weather",
            "c": "Use evapotranspiration data to guide irrigation timing"
        },
        "Correct Option": "a"
    },
    "Q14": {
        "Question": "Why should irrigation systems be checked regularly?",
        "Options": {
            "a": "Schedule inspections after any significant weather events",
            "b": "Check irrigation equipment regularly to prevent failures",
            "c": "Only check systems when visible problems occur"
        },
        "Correct Option": "b"
    },
    "Q15": {
        "Question": "What should be considered first when installing a new irrigation system?",
        "Options": {
            "a": "Assess the water availability and regulatory constraints first",
            "b": "Choose an irrigation system based on lowest cost",
            "c": "Consider future scalability and potential technological upgrades"
        },
        "Correct Option": "a"
    },
    "Q16": {
        "Question": "How does the type of irrigation system affect water distribution uniformity?",
        "Options": {
            "a": "Evaluate the uniformity of water distribution in current systems",
            "b": "Assume all systems are equally effective regardless of design",
            "c": "Research new irrigation technologies for potential implementation"
        },
        "Correct Option": "a"
    },
    "Q17": {
        "Question": "Why should irrigation settings be adjusted according to soil type?",
        "Options": {
            "a": "Adjust settings based on soil composition and permeability",
            "b": "Set a uniform irrigation schedule for all soil types",
            "c": "Monitor soil moisture levels closely to avoid over-irrigation"
        },
        "Correct Option": "a"
    },
    "Q18": {
        "Question": "How can water wastage be effectively reduced during irrigation?",
        "Options": {
            "a": "Implement rain sensors to halt irrigation during downpours",
            "b": "Continue irrigation during rain to ensure schedule adherence",
            "c": "Use drought-resistant plants to reduce water needs"
        },
        "Correct Option": "a"
    },
    "Q19": {
        "Question": "What technique helps prevent nutrient leaching during irrigation?",
        "Options": {
            "a": "Collect runoff water for reuse in irrigation",
            "b": "Increase irrigation rates to promote deeper root growth",
            "c": "Integrate drip irrigation systems to reduce runoff"
        },
        "Correct Option": "c"
    },
    "Q20": {
        "Question": "Why is it crucial to maintain correct irrigation pressure?",
        "Options": {
            "a": "Use a single pressure setting for simplicity",
            "b": "Ensure that irrigation pressures are optimized for each crop type",
            "c": "Regularly test system pressure to detect any discrepancies"
        },
        "Correct Option": "b"
    },
    "Q21": {
        "Question": "What effect does soil temperature have on irrigation needs?",
        "Options": {
            "a": "Disregard soil temperature as a non-significant factor",
            "b": "Consider adjusting irrigation based on daily temperature fluctuations",
            "c": "Calibrate irrigation systems to respond automatically to temperature sensors"
        },
        "Correct Option": "c"
    },
    "Q22": {
        "Question": "What adjustments are necessary for irrigation during rainy periods?",
        "Options": {
            "a": "Reduce irrigation frequency during wet seasons",
            "b": "Enhance soil drainage systems to cope with excess water",
            "c": "Maintain a steady irrigation routine throughout the year"
        },
        "Correct Option": "b"
    },
    "Q23": {
        "Question": "How can irrigation schedules be adjusted to minimize plant stress?",
        "Options": {
            "a": "Optimize schedules to water during the cooler parts of the day",
            "b": "Stick to a fixed watering schedule to simplify management",
            "c": "Increase watering during hot periods to reduce plant stress"
        },
        "Correct Option": "a"
    },
    "Q24": {
        "Question": "How does irrigation equipment configuration affect its effectiveness?",
        "Options": {
            "a": "Adjust the irrigation equipment setup based on seasonal observations",
            "b": "Keep the irrigation setup consistent year-round",
            "c": "Periodically review and tweak equipment settings for efficiency"
        },
        "Correct Option": "a"
    },
    "Q25": {
        "Question": "What are the best practices for choosing irrigation times to maximize efficiency?",
        "Options": {
            "a": "Choose early morning hours to minimize evaporation losses",
            "b": "Irrigate at noon to coincide with peak sun and heat",
            "c": "Alternate irrigation times weekly to test different efficiencies"
        },
        "Correct Option": "a"
    },
    "Q26": {
        "Question": "How does the choice of crops affect irrigation strategies?",
        "Options": {
            "a": "Customize irrigation based on specific crop water needs",
            "b": "Apply the same amount of water regardless of the crop type",
            "c": "Focus on the most economically feasible option"
        },
        "Correct Option": "a"
    },
    "Q27": {
        "Question": "What impact does improper irrigation have on soil health?",
        "Options": {
            "a": "Minimize irrigation to encourage deeper root systems",
            "b": "Over-irrigate to ensure soil is always saturated",
            "c": "Balance water application based on soil health indicators"
        },
        "Correct Option": "a"
    },
    "Q28": {
        "Question": "How do return periods affect plant growth in irrigation settings?",
        "Options": {
            "a": "Plan irrigation frequency based on the plant growth stages",
            "b": "Ignore plant growth stages in scheduling irrigation",
            "c": "Use generic irrigation schedules regardless of plant growth"
        },
        "Correct Option": "a"
    },
    "Q29": {
        "Question": "What role do soil moisture sensors play in efficient irrigation?",
        "Options": {
            "a": "Implement soil moisture sensors to automate irrigation",
            "b": "Depend solely on manual checking for soil moisture",
           "c": "Use timed irrigation without soil moisture checks"
        },
        "Correct Option": "a"
    },
    "Q30": {
        "Question": "What are the important end-of-season maintenance actions for irrigation systems?",
        "Options": {
            "a": "Conduct thorough cleaning and maintenance at season's end",
            "b": "Perform minimal maintenance and prepare for unexpected repairs",
            "c": "Delay all maintenance until operational issues occur"
        },
        "Correct Option": "a"
    }
}


clues= {
    "Q1": {
        "Question": "What is the primary consideration for starting spring irrigation on a dairy farm?",
        "Clue": "Think about the advantages of utilizing technologies that can provide immediate feedback on soil conditions."
    },
    "Q2": {
        "Question": "What is the most accurate method to assess soil moisture before initiating irrigation?",
        "Clue": "Consider the method that allows for continuous, direct measurement from within the soil itself."
    },
    "Q3": {
        "Question": "What key factor influences the choice of an irrigation system for dairy farming?",
        "Clue": "Reflect on the importance of system features that cater specifically to the operational needs and efficiency."
    },
    "Q4": {
        "Question": "Why is it important to understand the water holding capacity (WHC) of your soil?",
        "Clue": "Explore the benefits of using real-time and historical data to make informed irrigation decisions."
    },
    "Q5": {
        "Question": "What routine maintenance is essential for maintaining irrigation efficiency?",
        "Clue": "Focus on the type of maintenance that helps prevent future issues and enhances system performance."
    },
    "Q6": {
        "Question": "How should irrigation frequency be adjusted throughout the growing season?",
        "Clue": "Consider a method that dynamically adapts to changing soil and plant needs based on real-time data."
    },
    "Q7": {
        "Question": "Which irrigation method minimizes water loss in sandy soils?",
        "Clue": "Think about an irrigation technique that directly targets the root zones with minimal waste."
    },
    "Q8": {
        "Question": "What are the risks of irrigating when the soil is at field capacity?",
        "Clue": "Consider the consequences of adding water to soil that may already be saturated."
    },
    "Q9": {
        "Question": "What role does an efficient pump play in an irrigation system?",
        "Clue": "Reflect on how variable settings on a pump can optimize both water use and energy consumption."
    },
    "Q10": {
        "Question": "How should rainfall data integrate into irrigation planning?",
        "Clue": "Think about how integrating current weather data can enhance irrigation scheduling and efficiency."
    },
    "Q11": {
        "Question": "What common installation error should be avoided with irrigation nozzles?",
        "Clue": "Consider how uniform water distribution affects the overall effectiveness of irrigation practices."
    },
    "Q12": {
        "Question": "What is a major benefit of variable speed drives on irrigation pumps?",
        "Clue": "Focus on the energy efficiency and adaptability of using advanced pump technology."
    },
    "Q13": {
        "Question": "What is the best strategy for irrigation during periods of high evapotranspiration?",
        "Clue": "Reflect on methods that adjust irrigation based on both weather conditions and plant needs."
    },
    "Q14": {
        "Question": "Why should irrigation systems be checked regularly?",
        "Clue": "Think about how regular checks can prevent failures and enhance the longevity of the system."
    },
    "Q15": {
        "Question": "What should be considered first when installing a new irrigation system?",
        "Clue": "Reflect on the foundational requirements such as water availability and regulatory considerations."
    },
    "Q16": {
        "Question": "How does the type of irrigation system affect water distribution uniformity?",
        "Clue": "Consider the importance of how evenly water is distributed across your fields."
    },
    "Q17": {
        "Question": "Why should irrigation settings be adjusted according to soil type?",
        "Clue": "Explore how different soil types can significantly influence water absorption and retention."
    },
    "Q18": {
        "Question": "How can water wastage be effectively reduced during irrigation?",
        "Clue": "Consider using smart technologies that respond to environmental changes to minimize excess water use."
    },
    "Q19": {
        "Question": "What technique helps prevent nutrient leaching during irrigation?",
        "Clue": "Think about the efficiency of drip systems in delivering water directly to the roots with minimal runoff."
    },
    "Q20": {
        "Question": "Why is it crucial to maintain correct irrigation pressure?",
        "Clue": "Reflect on the effects of proper pressure settings in achieving effective and even water distribution."
    },
    "Q21": {
        "Question": "What effect does soil temperature have on irrigation needs?",
        "Clue": "Consider how changes in temperature affect soil moisture levels and plant water uptake."
    },
    "Q22": {
       "Question": "What adjustments are necessary for irrigation during rainy periods?",
        "Clue": "Think about the role of enhanced drainage systems in managing excess water during prolonged wet conditions."
    },
    "Q23": {
        "Question": "How can irrigation schedules be adjusted to minimize plant stress?",
        "Clue": "Reflect on the timing of irrigation to avoid the hottest parts of the day and reduce evaporation."
    },
    "Q24": {
        "Question": "How does irrigation equipment configuration affect its effectiveness?",
        "Clue": "Consider how adjusting equipment setups seasonally can enhance the efficiency of water delivery."
    },
    "Q25": {
        "Question": "What are the best practices for choosing irrigation times to maximize efficiency?",
        "Clue": "Think about the benefits of selecting times that minimize water loss due to environmental factors."
    },
    "Q26": {
        "Question": "How does the choice of crops affect irrigation strategies?",
        "Clue": "Reflect on how different crops have varying water needs and how tailoring irrigation can improve water use efficiency."
    },
    "Q27": {
        "Question": "What impact does improper irrigation have on soil health?",
        "Clue": "Consider the long-term effects of over-irrigation or under-irrigation on soil structure and fertility."
    },
    "Q28": {
        "Question": "How do return periods affect plant growth in irrigation settings?",
        "Clue": "Think about how the timing and frequency of irrigation influence plant health and development stages."
    },
    "Q29": {
        "Question": "What role do soil moisture sensors play in efficient irrigation?",
        "Clue": "Reflect on the advantages of using automated systems that adjust irrigation based on real-time soil moisture data."
    },
    "Q30": {
        "Question": "What are the important end-of-season maintenance actions for irrigation systems?",
        "Clue": "Consider the importance of thorough cleaning and inspection to prepare the system for its next use cycle."
    }
}

st.title("Optimising Irrigation Practices for Dairy Farms: A Decision-Making Guide")
st.markdown(background_info)
# Display each question with its options and clue
for q_key, q_info in data.items():
    st.subheader(f"{q_key}: {q_info['Question']}")
    for opt_key, opt_value in q_info['Options'].items():
        st.text(f"{opt_key}: {opt_value}")
    st.text(f"Clue: {clues[q_key]['Clue']}")
    st.markdown("---")  # Adds a separator between questions