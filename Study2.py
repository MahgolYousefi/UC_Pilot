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
**Good Irrigation Practices for Dairy Farms**
The information in this guide is a compilation of established research and practical 
knowledge. 
A number of people have kindly contributed to the content, however special thanks 
must go to those who provided detailed reviews of various drafts and provided 
helpful suggestions along the way.
Much of the information enclosed was developed by Annabel Craw, Charlotte Glass 
and Claire Mulcock.
Special thanks to Aqualinc Research Ltd, for providing photographs.
For more information visit
dairynz.co.nz
DairyNZ
Corner Ruakura and Morrinsville Roads
Private Bag 3221
Hamilton 3240
Phone 0800 4 DairyNZ (0800 4 324 7969)
Version 1 – 09/2011
Disclaimer
DairyNZ Limited (“DairyNZ”, “we”, “our”) endeavours to ensure that the information in this publication is accurate and current. However we do not 
accept liability for any error or omission.
The information that appears in this publication is intended to provide the best possible dairy farm management practices, systems and advice that 
DairyNZ has access to. However, the information is provided as general guidance only and is not intended as a substitute for specific advice. Practices, 
systems and advice may vary depending on the circumstances applicable to your situation. The information may also be subject to change at any time 
without notice.  DairyNZ takes no responsibility whatsoever for the currency and/or accuracy of this information, its completeness or fitness for purpose. 
   
Increased competition for water means the whole community is looking at how irrigators use water. Good irrigation not only has benefits for the wider community, but for individual farms too. This is because:	
Pastures grow better, providing more feed which is easier to manage	
Fewer breakdowns occur and systems are simpler to operate.
 
To irrigate well, you should: Apply the right amount of water at the right time to get maximum growth from pasture. Put on too much water and it drains away below the pasture and leaches out some of your expensive nutrients; leave it too late and the plants may stress, which reduces growth rates. Maintain and manage the irrigation system to minimise wastage and leaks. There is little point in using expensive energy to pump water and then let it go to waste because of leaks in the system. Leaks may reduce the operating pressure so much that the system doesn’t apply water evenly, 
leading to patchy growth of pasture. Watering tracks and other non-productive areas wastes water.  Plan ahead for possible restrictions to water. If you depend on irrigation, decide on irrigation  priorities (for example, crops vs pastures, good pastures vs poor pastures, or shallow soils vs deeper soils) and develop a plan to best minimise the impacts of water restrictions.

 
Soil is a natural storage tank, holding water for pasture plants to absorb through their roots. Soils vary greatly in the amount of water they can hold onto. Clay soils have smaller pores and can hold more water, but hold onto the water tighter. Sandy soils have bigger pores and hold less water but make it easier for plant roots to extract the water. The amount of water a soil can hold is expressed in millimetres of water per metre depth of soil (mm/m) and is called water holding capacity (WHC). It varies from 175-190 mm/m for clay loam to 45-55 mm/m for sand.

Pastures receive the majority of the water they require through their roots. Therefore, the depth of the plant’s roots affect the amount of water a plant can uptake. A shallow rooting plant will have less water available through its root system than a deep-rooted plant. Annual and perennial pasture has a rooting depth between 0.3-0.8m, compared to lucerne’s 1.2-1.8m. The root zone will also be affected by the plant growth stage, so a seedling will have a smaller root area than an established plant. Ryegrass 0.3- 0.8 m 1.2-1.8m Lucerne Clay Soils, Sandy Soils

Plants use the majority of the water they require to keep themselves cool, pumping water from the roots to be transpired by the leaves. The rate at which they extract water from the soil is based on the evapotranspiration rate (ET). ET rates are affected by climatic conditions such as temperature, wind, humidity and growth stage of the plant. A hot windy day in the middle of summer will have a high ET rate because the plant needs more water to keep cool. In Canterbury, ET is high during the summer period and irrigation generally needs to proceed uninterrupted (until a significant rain). The “shoulders” of the season are generally where much of the water savings can be made:
In spring, soils are generally near field capacity (full of water) and temperatures are still low. There is good potential to save water by delaying the start of irrigation until it is actually needed, i.e. when a soil moisture deficit occurs and temperatures increase. Saving water in the spring, when ET is low (risk to crops is minimal) also means there will be more water left for the peak season. But care must be taken not to let the soil get too dry, as it may be hard to catch up, especially with irrigators that have a long return period (e.g. when it takes longer than 10 days to return back to a paddock).
Autumn ET rates can decrease rapidly in the autumn. This means irrigation water does not need to be applied as regularly. Minimising unnecessary irrigation in the autumn also helps minimise cooling of the soil, helping to keep plants growing longer.
Rainfall is the best form of irrigation as it does not cost anything. Where possible, leave enough room in the soil to absorb any rain so it can be utilised to naturally increase soil moisture, saving on irrigation. If soil is fully saturated and it rains, the water has nowhere to go except run-off or drain out the bottom of the soil, so it is not utilised and may take important nutrients along with it. 

Not all irrigation systems can apply the same amount of water. The amount of water that can be applied varies depending on the type of irrigation system (border dyke, centre pivot, rotary boom etc). Other influences include:

The overall capability of a system is referred to as system capacity and describes the maximum amount of water able to be applied in a given timeframe (e.g. mm/day, l/s/ha or mm/wk). Because the main aim of irrigation is to keep up with ET rates (plants demand for water), system capacity should try to match ET levels. As it can be impractical or uneconomic to have an irrigation system which is able to match ET rates at their peak, decisions have to be made on how to manage this limitation. During the season, options may include reducing the area of land irrigated, feeding supplements, or reducing stock numbers. Long-term options include reviewing the irrigation system and making changes to improve the efficiency of the existing irrigation, increasing irrigators or installing more efficient irrigation types. To improve the reliability of water supply, development of seasonal storage or applying for additional water allocation may be required. 
 

When irrigating, the objective is to Apply	water	when	the	plant	needs	it,	to	maximise	plant	growth
Not	overfill	soil,	which	wastes	water.

There is no value (only cost) in applying more water than the soil can store, but if water isn’t applied before critical soil water deficit is reached, pasture growth will slow down. If the irrigation system and water supply arrangements allow, irrigation should happen when the soil moisture level reduces to refill point. Up until this point, moisture levels will not limit pasture growth and no visual signs of plant stress will be occurring. 
The diagram below illustrates how plant growth is affected at each level of soil moisture.
Soil is totally saturated and unable to hold any more water. Excess water lost to deep drainage. Surface ponding may occur.  Optimum level of soil moisture, all water is 
available to plant. Soil becoming drier. Soil very dry. Plant growth is restricted through lack of oxygen and nutrient loss. 
Ideal plant growth.
Plants under stress, growth 
impaired (survival mode).
Plant dies.
(stress point)
Field capacity
Refill point
Permanent
wilting point
Drainage
Soil 
moisture 
levels
Plant
 growth
Saturation


Refill point for your farm needs to be customised, as it is dependent on soil and crop type. However, a simple rule of thumb is 50% of plant available water. In the early and later months (the ‘shoulders’ of the irrigation season) soil moisture levels can be kept closer to refill point because ET rates are lower, and irrigation and rainfall are able to keep up with plant demand for water. When soil moisture levels fall below refill point, plant roots have to work harder to find water, slowing down plant growth. To demonstrate how soil releases water for plant growth, it can be compared to a sponge. The sponge is the soil and the hand represents the energy required by the plant to extract water from the soil. Soil moisture monitoring is an accurate way to measure and monitor soil moisture and temperature levels during the irrigation season, to ensure irrigation is scheduled appropriately. Monitoring tells you when the soil is at field capacity to stop watering and when it is at the refill point to start irrigating. By combining soil moisture information with soil temperature data, the greatest benefit is usually achieved at the start and end of the irrigation season, when the aim is to ensure soil moisture levels are sufficient without reducing soil temperature to a level which will reduce plant growth. This is because soil is easier to heat than water, meaning drier soils heat faster and maintain heat for longer. Irrigation management in spring should focus on not irrigating too early, so soil temperature can increase faster; and in autumn 
not over-watering and dropping soil temperature at a quicker rate, slowing down pasture growth rates.  Irrigating too early in the season can waste water, as plants use less water when temperatures and evaporation are low, but letting the soil get too dry before starting to irrigate may make it hard to catch up, depending on soil and irrigation type. 
Although soil moisture can be monitored manually, the most common way is by a handheld meter such as a neutron probe or a permanently installed strip. Data can be collected by a consultant or the farmer, or sent direct to a personal computer.


How to decide when to start/stop irrigating. It is important to know who has the responsibility of deciding when to start and stop irrigation, and how that decision 
is made. Copying the neighbours is not good practice. Below is the process to follow before starting to irrigate.	
Soil temperature – Check soil temperature before irrigating. Grass growth is slow below 10ºC at 10cm depth. 
Drier soils warm more quickly than wet soils. Also, applying water can cool the soil further	
Soil moisture status – Check soil moisture status is between refill point and field capacity (with room for irrigation and rainfall).


Application depth = how much water is applied. To apply 1 mm (depth) you need 1 litre/m² or 10 m³/ha. Application rate (or application intensity) = how fast the water goes on. It is measured by the depth of water applied in a fixed time. It is usually measured in mm/hr. Distribution uniformity (Du) = the evenness with which the soil receives water across the irrigated area. The higher the distribution uniformity, the better the system is 
performing. A Du of 85-90% should be readily achievable under a centre pivot. Infiltration = the movement of water from the soil surface into the soil. Infiltration rate of soil indicates the speed water can be applied and soaks into the soil without causing 
run-off or ponding. Infiltration rate varies according to soil type, crops and slope. 
Carrying out a ‘bucket test’ will help determine the application depth, rate and how uniformly water is being applied during an irrigation event. The ‘bucket test’ method is based on collecting irrigation water in strategically placed buckets and measuring 
what water is collected over a certain period of time. The ‘IRRIG8Quick’ system checks provide instructions on how to carry out this test and others for pivot, linear, traveller and sprayline irrigators. Go to pagebloomer.co.nz/resources/tools. Irrigation system and application depth. The amount of water an irrigator applies (application depth) varies hugely and depends on how the irrigation system has been designed. If a farm’s irrigation system has been designed to return to a paddock frequently (every 3 to 4 days) then a lower application depth can be used, because it is only a short period of time before water will be applied again. Conversely if an irrigation system is designed to only return to the paddock every 15 days, then a higher application depth is required to keep the soil moisture levels above refill point and limit plant stress over the longer period of time. Below is an example of two different irrigation systems which deliver 4 mm of water per day but at different application depths. The ‘bucket test’ helps determine correct application of water.
Irrigation type
Return period
Application depth 
per irrigation pass
mm/day
System A
Centre pivot
3 days
12 mm
4 mm (12 mm/3 days)
System B
Rotary boom
15 days
60 mm
4 mm (60 mm/15 days)
 
Centre pivot length and application rate. With a centre pivot, the outside span needs to travel faster than the inside span in order to keep in line. Because the outer span covers greater distances, the application rate varies along the length of the pivot to achieve the same application depth. At the centre it will be a low application rate (light drizzle) 
and at the end span, a higher application rate (heavy downpour). The longer the pivot, the greater the application rate will be at the end span. This can cause problems, especially on rolling country, if the application rate is too high and the water is being applied faster than the soil can absorb it, increasing the risk of puddles and run-off. Because of uneven infiltration into the plant root zone, grass production can also be reduced. Any steps that reduce very high application rates will be beneficial. 
For example Installing sprinklers with greater coverage and which spread water over a larger area
and decreasing the application depth for each watering and returning more frequently.

Minimising the pump’s energy use. For spray irrigators the pump is the centre of the irrigation system, much like the human heart is to the body. If the irrigation pump is not working properly, the whole irrigation system will suffer. A pump requires energy to move the water to the irrigator. The force at which the water is delivered is pressure (m, kPa, bar, psi), the amount of water sent to the irrigator is the volume (m3) and the speed at which the water is moving through the pipe is the flow rate (l/sec, m3/hr, gpm). 
The pump’s role is to supply the irrigator with the correct volume of water at the right pressure level and flow rate, using as little energy as possible. It should run smoothly and perform efficiently.
By having a healthy pump fewer breakdowns will occur, less energy will be used, the correct amount of water will be delivered to the irrigator.
If a leak occurs in the system, the pump will have to work harder (using more energy) to achieve the same amount 
of pressure. 
How to maintain the irrigation system: Catastrophic failures of pumps and irrigation equipment during the season can waste a lot of time, restrict pasture growth and 
create stress. Regular equipment checks and ongoing maintenance is vital in preventing breakdowns and reducing the chance of serious damage. Having a weekly or monthly and annual task list for irrigation maintenance, where you can check tasks off easily, ensures maintenance is kept up-to-date. Below is a summary of some essential maintenance procedures for most irrigation systems. For more detail specific to your 
system, contact the service provider. If you install a new pump, ensure the supplier provides the specifications and a pump commissioning report. These will serve as benchmarks for future checks. Maintenance throughout the season. Before the irrigation season starts. 

If pumps wear or corrode, more power is used and less water is delivered at lower pressure. The irrigation system no longer does what it is designed to do. Pump is incorrectly adjusted, worn out or broken. Contact service provider.


The following are the questions and options extracted from the above information from dairyNZ. Also, we created the clues
for the correct option for the guiding users.

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