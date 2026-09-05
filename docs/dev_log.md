# Development Log:
I've been writing my thoughts and progress here as I go. It's kind of like a daily log, just not updated every day.

- this file is currently being organized - 


##  03/04/2026
    ♡ starting w. atmosphere 
    
    ♡ going to be using Dalton's Law 

    ♡ researched net habitat volume/crew member (average minimum of 25m3 pp) and I'm happy w. keeping the habitat size at 2000m3 (~ 66 m3 pp)    

#### Next Session:
    ♡  continue w. atmosphere


##      03/05/2026
    ♡ taking a couple of days for research

    ♡ considering adding humidity contribution (1-2kPa ppH2O)


##      03/08/2026
    ♡ resuming atmosphere creation w. updated knowledge

    ♡ CO₂ was defaulting to zero, need to fix my scrubbing system

    ♡ today I learned that I needed to get the skeleton figured out and that it's okay to refine the numbers afterwards

#### Next Session:
    ♡ finish scrubbing function in engine.py


##      03/09/2026
    ♡ continuing where I left off w. scrubbing

    ♡ NASA references: crew CO₂ production is ~ 1 kg pp/day

    ♡ researched O₂ regeneration and electrolysis w. focus on Oxygen Generation Assembly (OGA), MOXIE like Solid Oxide Electrolysis (SOXE) and Sabatier CO₂ reduction + electrolysis

    ♡ making separate functions for managing and checking gases

    ♡ more research on 02 regen and electrolysis

    ♡ implementing very basic OGA O₂ generation function for now (handling power usage, total pressure updates, hydrogen(h2) production and handling/venting later)  

#### Next Session:
    ♡ add total pressure update

    ♡ add the O₂ regen to quick_test and state.py


##      03/10/2026
    ♡ renamed checking_gases function to gas_alerts, moved the CO₂ removal function to before o2_regen

    ♡ I know that chemistry ratios use moles, but I really wanted to stick to kPa and kilograms (kg) to avoid my code being more complex, so I'll figure out the conversions to avoid that

    ♡ made the scrubber unable to remove more CO₂ than exists and changed the kPa values to move 4 decimal places instead of two, updated target based CO₂ and O₂ control, added target gases as global variables in engine.py

    ♡ adding in the hydrogen that the OGA electrolysis makes and venting it FOR NOW and will do research on how I can use it later on (Sabatier?)

    ♡ adding OGA byproduct function in, first calculating 23C to Kelvin b/cI read the gas pressure depends on temp (pressure drops if it goes down) 

#### Next Session:
    ♡ consider breaking down the long conversion in oga_byproduct into multiple lines of code w. notes explaining each step for easier understanding
    
    ♡ vent the h2 later, store for now


##       03/11/2026
    ♡ learned it's important to document types of measurements as I go for conversions and future better understanding when both using and reading code

    ♡ adding measurements on the end of certain variable names, moved some of the variables from the oga_byproduct function to be global variables for referencing them later

    ♡ oga_byproduct is now oga_h2_byproduct w. more lines of code, breaking down the process better

    ♡ going to refine notes later, for now keeping them pretty descriptive, adding some notes beside instead of above variables to see if it looks cleaner

#### Next Session:
    ♡ store h2 for now


##      03/13/2026
    ♡ figure out how much water(H2O) the OGA and water electrolysis uses every time it runs, I'm going to find the fixed reaction ratio instead of a fixed ratio b/c the amount of O₂ produced are going to change depending on habitat events

    ♡ going to use 1000kg of water to start as a placeholder to finish the OGA functions

    ♡ going to keep the OGA functions separate instead of one big function w. a comment to sort of group them together, I feel like that will be better for future readability

    ♡ arranged some comments to be beside the line of code, I find if it's short, it does look cleaner

    ♡ finished OGA and water electrolysis for now, moving onto argon and nitrogen

#### Next Session:
    ♡ figure out variable numbers for the variables commented out at the top of engine.py
    
    ♡ add in when the Ar or N₂ will be used from storage    
    

##      03/14/2026

    ♡ I added the variable CO₂_stored_kpa to collect and temporarily store the CO₂ the amine bed scrubs until I use it later in my code

    ♡ decided on adding kg/kpa as global variables so when I need to access the stored gases, I can convert them more efficiently

#### Next Session:
    ♡ continue fixing variables, making sure the files are correct and finish adding Major Constituent Analyzer (mca) function and adding N₂ to low pressure


##      03/15/2026
    ♡ finished maintenance

    ♡ continuing w. mca and adding another function to handle buffer gas

    ♡ I am aware that my alert function in engine.py is going to need more work but I will focus more on that after I have more of my code implemented (I feel like this is a good call)

#### Next Session:
    ♡ add what I need to add to the other files from the new function I made today to handle the buffer gas


##      03/17/2026
    ♡ yesterday I mapped out a better plan for the rest of my simulator and I decided to clean it up as I go today.. I realize I made a lot of mistakes earlier, but I'm noticing them and fixing them now

    ♡ moving to temp management today and thermal control, I decided to get the main ideas down using radiators and do more research into other ideas later on

    ♡ cleaned up my code and moved the variables to the other files where they belong and referenced them properly in engine.py

    ♡ while adding the temp variables to run_oga, I decided to rename a few variables to make reading/going over my code later easier and I also decided to make these functions more efficient overall

    ♡ I'm not sure if I already stated this, but the OGA is capped at 0.004 (for now) so that the OGA has to take its time to catch backup so that it doesn't run a huge amount of power and it seems unrealistic

    ♡ I decided to use a dictionary in the run_oga function to keep it more manageable and neat

    ♡ continuing to fix my code functions and will remember to stay consistent w. the names and structure moving forward

    ♡ really happy w. my progress today and will continue implementing thermal control and temp management tomorrow

#### Next Session:
    ♡ thermal control and temp management


##      03/18/2026
    ♡ deciding if I should add heat output into current functions, or have its own. I'm going to keep adding to the proper functions

    ♡ adding heat produced by amine beds w. exothermic absorption (the amine molecules catch the CO₂ which releases heat) and regeneration

    ♡ wrote a first version of a readme.md file and decided to make my project public today!

#### Next Session:
    ♡ consider turning functions w. five or more returns into dictionaries and continue w. thermal control and temp management


##      03/19/2026
    ♡ added dt_min to variables that change based on elapsed time in engine.py

    ♡ fixing the buffer gas control function so that it doesn't alter things from state directly and turning the return into a dictionary. I will probably end up using dictionaries for most of these as I go

#### Next Session:
    ♡ consider turning functions w. five or more returns into dictionaries and continue w. thermal control and temp management in run buffer gas


##      03/20/2026
    ♡ I'm making the amount of heat added a fixed amount for now

    ♡ added heat generation to buffer gas control function

#### Next Session:
    ♡ continue adding heat generation to functions and add radiators, lights, electronics/computers to their own functions


##      03/21/2026
    ♡ hand injury but working past it, going to add a light function where they dim at a certain time at night and also include how much heat the lights generate

    ♡ going to go w. the crew getting ~ 8 hours of sleep/night so lights will dim at 9:30pm (21:30) and they will brighten at 6:00am, using level of brightness for now

    ♡ considering moving the time conversion logic out of quick_test into engine, or into its own file to handle all timestep info b/c eventually it will be interactive

    ♡ considering adding separate helper files for handling certain things separately like one for amine scrubbers, OGA, etc after adding more code

#### Next Session:
    ♡ continue adding heat generation to lights and add electronics/computers, radiators to their own functions, reconsider lighting variable names


##      03/24/2026
    ♡ since I want to have solar, I'm going to need to have a huge battery storage for when there are dust storms and other impacting factors (I still have an injury, I am doing small blocks of code at a time) 
    
    ♡  making the battery capacity 4000.0 kWh for now

    ♡ I chose the starting amounts for some power variables and made a separate file for the OGA and water electrolysis

    ♡ added power consumed to lights function

#### Next Session:
    ♡ continue lighting function and then continue adding heat generated/heat waste to new functions for electronics/computers, radiators, pumps, solar

    ♡ update step in engine.py to call the run_oga function properly now


##      03/26/2026
    ♡ added some power consumption variables to oxygen_system.py

    ♡ adding files for separate logic systems

    ♡ for the mca function, I decided to not use state so I can manage/calculate both before and after control

    ♡ realizing that the file for the O₂ system has separate functions and the buffer gas file has one solid function, so I might end up breaking up that long function into a few smaller ones for readability and also b/c I will be adding more to this function

    ♡ broke up one long buffer gas system function into smaller ones for readability, organization and future handling

#### Next Session:
    ♡ break up CO₂ scrubber system into different functions to match the other files and then add power usage, eventually continue lighting function and then continue adding heat generated/heat waste to new functions for electronics/computers, radiators, pumps, solar


##      03/28/2026
    ♡ making crew metabolism into its own file for organization and considering breaking it into smaller functions for quicker/easier readability as I add to the file

    ♡ breaking up the CO₂ scrubber system into different functions and adding heat, taking into consideration that I want there to be a baseline power/online bed like there is for heat, power usage used on actual CO₂ removed, emergency events and full power loss (these last two will be handled later though)

    ♡ added power usage to CO₂ scrubber, updated engine and quick_test to work w. the file properly

    ♡ added outputs to be printed so I can see that they are working properly

#### Next Session:
    ♡ work on water_system or power..


##      03/29/2026
    ♡ decided to start w. power_system.py since I already started implementing these features in other functions and updated step in engine.py to include power/energy used for OGA and lights

    ♡ updated state variables file to include the new power variables I've been using from state and removed them out of the placeholder value section

    ♡ ***while looking at the amine bed list, I'm not happy w. how it's running right now b/c of how I hardcoded and pre-assigned the roles, when I actually want this to be a living working system, so before starting the solar power functions, I'm going to go back and try to fix that***

    ♡ I fixed a lot of my code today and added solar list of dictionaries, updated the amine list of dictionaries and made a crew metabolism dictionary, fixed some typos and learned a lot about organizing files, name consistency, code consistency, not going overboard too fast and file setup

#### Next Session:
    ♡ work on power_system.py


##      03/30/2026
    ♡ starting by reviewing my code and I see some areas I need to fix b/c of the changes I made last night, starting w. how my amine beds function

#### Next Session:
    ♡ update solar array list


##      03/31/2026
    ♡ updated solar array list to not be hard coded online but start w. all of them being on standby status and added a function to manage what ones are online w. a new function in power_system.py


##      04/03/2026
    ♡ updated power_system.py and added a solar generation function and fixed the other no longer needed variables from the other files that had to do w. solar power.

    ♡ using 0.50kw of sunlight for every 1 square meter (m²) for now, b/c my research showed that Mars sunlight is btwn 0.4 - 0.6 kw / 1 m² during daytime

#### Next Session:
    ♡ work on power_system.py and figure out where I want daylight calculated (maybe state, or make a new separate file for handling calculating times of day, days and other related things)


##      04/04/2026
    ♡ while trying to come up w. a way to make the daylight run smoothly and over time (instead of hardcoding w. certain percentages), I learned what a sine wave is and I'm going to try to use that

    ♡ considering where to add a function for calculating daylight over time (power_system.py or in engine where it handles timestep math, or in its own file completely?)

    ♡ making a file for handling timesteps and related functions

    ♡ I learned today that instead of 24 hours, Mars time actually runs at 24 hours and 39 minutes and 35 seconds, not just 24 hours, so I'm going to fix that now, while I'm working on the new Mars_time.py file

    ♡ added a better looking print function for a nicer console view while I work w.out a UI and kept the original print function commented out for when I want it plain again

#### Next Session:
    ♡ work on power_system.py: finish solar updates and figure out how to handle dust and efficiency, update power storage and figure out how to implement that


##      04/05/2026
    ♡ fixing the lighting function to not be hardcoded and to react and adjust to the level of daylight

    ♡ considering a file that will handle the light level, but so far I'm leaving it in engine, b/c I can't justify a file dedicated to just one function

    ♡ adding in the coordinates for the location of the habitat to make time passing and daylight and everything that goes along w. that more accurate

    ♡ changed a ton in the Mars_time.py file, I'm still figuring it out

#### Next Session:
    ♡ REMEMBER TO COMMIT MORE!!

    ♡ do more research and figure out Mars_time.py, clean up step in engine.py


##      04/07/2026
    ♡ starting by reviewing my Mars_time file

    ♡ added Mars 24 hours time format

    ♡ added function to determine how the sun shifts from it's orbital position and hardcoded Mars' tilt to be 25.19°

#### Next Session:
    ♡ do more research and figure out Mars_time.py, clean up step in engine.py


##      04/08/2026
    ♡ continuing to fix the time file and updated engine and quick_test.py

    ♡ fix light function and resume the solar power set up

    ♡ added function to calculate daylight and sunset times to determine the dyalight fraction for one sol

    ♡ cleaned up and updated Mars_time.py and did some minor file organization w. section headers

#### Next Session:
    ♡ fix light function and resume solar power set up


##      04/09/2026
    ♡ fixed variables in v1_state_variables.md and added / fixed section headers in other files

    ♡ fixed light function to work w. daylight and sunlight logic

    ♡ considering extra lighting option for when there are times where there isn't any sunlight for so many days, to help keep crew moral up (wellness lights)

    ♡ going to add three more variables related to sunlight mostly for the UI later

    ♡ added a wellness light function b/c I figured that the crew would need a bit more if there are frequent dust storms or anything that would effect sunlight for a few days

#### Next Session:
    ♡ move to thermal after this (?)


##      04/10/2026
    ♡ added function for solar power recharging habitat batteries

    ♡ added more functions to power_system.py file for updating power storage and power being used

    ♡ I'm going to leave the dust factor (which will be 0.0 - 1.0) and random Mars wind cleaning the solar arrays alone for now

    ♡ I want to start to organize my engine file

    ♡ added a separate file for alerts that I will update more later on b/c it isn't really a priority right now

#### Next Session:
    ♡ print total power being used and a power priority system for when power is low and only runs essential power systems


##      04/11/2026
    ♡ moved alerts to its own new file that included the status updates as well

#### Next Session:
    ♡ print total power being used and a power priority system for when power is low and only runs essential power systems


##      04/12/2026
    ♡ started importing power_alerts from power_system to the new alerts file, but very busy today

#### Next Session:
    ♡ print total power being used and a power priority system for when power is low and only runs essential power systems


##      04/13/2026
    ♡ going to add power info to print function

    ♡ fixed peak daylight today to reset for each sol

    ♡ I'm trying to decide if I should keep my lights function so it's controlling the brightness based on its own battery storage check, or move it to the function where it handles low power.. I'm leaning towards the latter

    ♡ moved it and capped the min and max light level

#### Next Session:
    ♡ organize engine.py


##      04/14/2026
    ♡ starting by organizing engine.py

    ♡ I like how clean the dictionaries look in engine.py so I think if my returns return four or more variables, I'm going to make it into a dictionary (starting w. power_system.py w. lights and wellness lights)
    
    ♡ I cleaned up engine.py but quit pushing commits in the messy middle in case I had to undo everything I did anyway, but I got it sorted out and organized

    ♡ reviewing notes that I wrote and moving onto temp_system.py

    ♡ I'm going to focus on the thermal parts before considering humidity

    ♡ adding seasons to Mars_time.py to help w. my temp_system.py file

    ♡ I'm very happy w. my progress today

    ♡ I'm realizing when I have the UI up and running, a lot of the systems that are being used are going to need to be mentioned in an update log

#### Next Session:
    ♡ fix new variables added (insulation and thermal mass)


##      04/15/2026
    ♡ fixed insulation and thermal mass values

    ♡ adding electric heaters and radiators and I want to make both of them like I did some of the other systems w. lists (amine beds, etc.)

#### Next Session:
    ♡ finish adding heat and cooling to power_system


##      04/16/2026
    ♡ continuing w. radiator function

    ♡ going to change the way I have the radiators_online function set up b/c I don't like to hardcode the numbers like I did and I'm going to have a hysteresis so that my new setup doesn't turn on and off abruptly too often

    ♡ added radiator power usage and added radiator info to the other necessary files

    ♡ testing is running well

    ♡  still playing around w. insulation values (0.3 - 0.8?)

#### Next Session:
    ♡ add heaters

    ♡ consider implementing two backup radiators


##      04/18/2026
    ♡ starting w. my temp file

    ♡ I'm going to keep the radiators using the habitat temp directly to run and focus on adding in the electric heaters until then

    ♡ I am going to worry about emergencies later and just get the foundation down first, but I did add another two radiators to the radiator list

    ♡ making heaters their own list to be handled the same way the other systems are

    ♡ added thermal alerts to alerts file... still not really focused on alerts, but there are some that will actually be helpful w. printing now mostly for debugging

#### Next Session:
    ♡ add second and third heater stage triggers and look into insulation and mass values b/c habitat is losing 25kw and one heater only = 8kw


##      04/19/2026
    ♡ fixed alert file and a few related variable names

#### Next Session:
    ♡ add second and third heater stage triggers and look into insulation and mass values b/c habitat is losing 25kw and one heater only = 8kw


##      04/20/2026
    ♡ moving onto humidity in thermal b/c I decided I will alter the insulation and mass values once I have all the systems implemented including water and everything

    ♡ added moisture variables to the crew metabolism file and updated temp_system.py

    ♡ I'm considering adding a new file to handle humidity depending on how big that part gets

    ♡ started a lot of organization to keep things consistent between system files (removing unused imports, adding constants/globals, updating section headers)

#### Next Session:
    ♡ change hardcoding to calculations (stay minimal for now)


##      04/21/2026
    ♡ going back to CO₂_scrubber_system and changing hardcoding to calculations

    ♡ adding sunlight to the thermal system

    ♡ I realize that I should be making things change and come from state directly, not so many other things, so before starting water_system.py I'm going to do a complete refactor

    ♡ fixed time, solar and daylight update in step and renamed new state variable to NEW_STATE in caps to make it easier to see while I fix some parts of step

    ♡ finished updating the new state in step, so it's lowercase now and just fixing some layout issues (making long function signatures extend vertically, but I'm not sure I like the way this looks)

    ♡ considering changing my repetitive functions to be one function that switches modes based on different things ( VERY UNSURE ), but for now I will continue to keep doing this as I've been doing it

#### Next Session:
    ♡ -work on water_system.py


##      04/22/2026
    ♡ doing some research before starting water_system.py to know what kind of water system makes sense w. focus on reusability

    ♡ going w.:
        -Urine Processor Assembly (UPA)
        -Water Processor Assembly (WPA)
        -Brine Processor Assembly (BPA)

    ♡ worked on the water system file

    ♡ I read about In-Situ Resource Utilization (ISRU) to extract water locally but I'll worry about that later

#### Next Session:
    ♡ continue working on water_system.py:
    ♡ add new results to print function
        - add condensate
        - change oga to use water usage from water_system file and remove its own storage variable
        - don't forget about the CHX


##      04/23/2026
    ♡ adding condensate/CHX to water_system and engine and made OGA use potable water

    ♡ added new results to print function

    ♡ fixing heating issue, my hysteresis was WAY too high in temp_system.py

    ♡ added hysteresis for amine beds function, buffer gas system, wellness lights and OGA for turning off and on

#### Next Session:
    ♡ fix thermal mass from 800 to a much lower amount and check insulation value

    ♡ look into insulation and mass values b/c habitat is losing 25kw and one heater only = 8kw


##      04/24/2026
    ♡ starting by fixing my thermal mass value and insulation strength

    ♡ fixed thermal_system.py by cleaning up globals, changing placeholder values to real/accurate values and updating the rad heat function

    ♡ I'm reading about dust and how it's managed best on Mars, there are a lot of different ways it's handled.. I like the idea of:
        - electrostatic dust repulsion (EDS) b/c of the fact that it's passive

        - scheduled cleaning, although I like the idea of the crew having one less thing to worry about and maintain, if it can be done on its own
        
        - dust repellent coatings for sure that will need to be redone over a certain amount of times(?)

    ♡ started adding backup radiators and heaters

    ♡ started file for handling dust

#### Next Session:
    ♡ fix amine beds to show up as online


##      04/25/2026
    ♡ updated CHX to include cooling

    ♡ updated solar arrays list and function to run on how much charge the batteries need

    ♡ updated amine beds to come online w. how much CO₂ is needed, I used two different hysteresis for that

    ♡ updating a lot of variables for systems handling lists now that I've changed some logic to be a bit more complex

#### Next Session:
    ♡ go through files and update everything using state (starting w. thermal) and clean up inconsistencies


##      04/26/2026
    ♡ connecting files to state more directly

    ♡ figuring out how to reduce outputs in engine, while still keeping it

    ♡ started turning files into separate dictionaries to reduce the massive outputs dict in engine.py, started w. water, working on temp

    ♡ basically started refactoring

#### Next Session:
    ♡ finish working on breaking up outputs and making engine more organized


##      04/27/2026
    ♡ continue connecting files to state more directly and reducing outputs in engine

    ♡ added venting for OGA

    ♡ started to add sabatier info/logic into my water system file

    ♡ updated the print function to be a bit more organized and updated it to print every hour, instead of five minutes mostly for debugging / seeing how my system is working

    ♡ updated the print function to be a bit more organized and updated it to print every hour, instead of five minutes mostly for debugging / seeing how my system is working

#### Next Session:
    ♡ continue adding sabatier info/logic into water system file

    ♡ look at the heater logic and consider adding a target heaters online and heat needed variable to print for debugging


##      04/28/2026
    ♡ mostly a research day about Mars and seasons, temperature, atmosphere and more on systems that would be needed in a real Mars habitat

    ♡ lot's of whiteboard notes and new considerations regarding handling gases and future dust and other events

    ♡ created a new file for the Sabatier

    ♡ changed the targets for N₂ and Ar and the target pressure to 65.0kpa (which it should have been this whole time, I accidentally had it at 60.0kpa)

#### Next Session:
    ♡ start file for Sabatier


##      04/29/2026
    ♡ starting file for Sabatier

    ♡ sorted v1_scope file into a to do file and dev_log b/c everything together was getting messy, hard to look back on and way too long

    ♡ learning that I like consistency and how important it is and that it's okay to refactor and organize.. my next project I will be more prepared

#### Next Session:
    ♡ turn seasons into a list
    ♡ turn on alerts for min and max safe targets and make crew alerts react to them (i.e "some of the crew members are starting to report headaches")
    ♡ go over all variables in state, add or remove things for consistency and organize them better (eventually)


##      04/30/2026
    ♡ sorted through creation notes and finished seperating things into their own files 

    ♡ updated OGA logic, by removing the pa conversation at all and made r for the universal gas constant in kpa instead

    ♡ I am going to keep h2 stored in kg and also I'm going to make the methane(ch4) storage to be in kg b/c these are being treated as resources and I read that the Sabatier uses mass ratios, not pressure ratios

    ♡ if I need to convert them at any time, I'll just use the conversion and put it up as a constant in the file

    ♡ resuming Sabatier file

    ♡ using a hysteresis to avoid jumpy on and off reactions

    ♡ reactions_available is how many times stoichiometric reaction can happen w. a ratio of 1 CO₂ : 4 h2

    ♡ I realize I actually put the mode decision in the main function for running the sabatier and also the OGA actually and I didn't in the other files. I've been changing things and upgrading how I'm doing things so eventually I will need to go through all of the files that I worked on first.

    ♡ waiting to do that though ^ b/c refactoring and editing has taken up enough time for the time being and I want to focus on getting some main systemsfigured out. 

    ♡ I thought adding a little bit of a leak while venting the ch4 was realistic, so I might add this to the other systems that vent

#### Next Session:
    ♡ get back to the Sabatier file w. power and heat produced fixed
    ♡ figure out what to put gases at in quick_test for starting values
    ♡ figure out values for new commented out variables in state and quick_test and if I really even need them
    ♡ add a little bit of a leak while venting


##      05/01/2026
    ♡ added sabatier outputs and updates into engine.py and fixed variables for ch4 where I accidentally put kpa insted or kg

    ♡ code is running again

#### Next Session:
    ♡ update print to show sabatier information
    ♡ get back to the Sabatier file w. power and heat produced fixed
    ♡ figure out what to put gases at in quick_test for starting values
    ♡ figure out values for new commented out variables in state and quick_test and if I really even need them
    ♡ add a little bit of a leak while venting


##      05/03/2026
    ♡ updating print to show sabatier information

    ♡ I decided to track gases in the atmosphere in kpa and h2 and ch4 in kg for storage and I'm not 100% sure about the other ones yet

    ♡ going to keep things consistent: kg for storage, kpa for atmosphere

    ♡ adding variables for each gas to have a base leak rate, to use for venting and other things (using individual ones b/c some leak faster than others)

#### Next Session:
    ♡ get back to the Sabatier file w. power and heat produced fixed
    ♡ figure out what to put gases at in quick_test for starting values
    ♡ figure out values for new commented out variables in state and quick_test and if I really even need them
    ♡ add a little bit of a leak while venting


##      05/05/2026
    ♡ working on CO₂_scrubber_system.py making the logic closer to the sabatier and other systems logic

    ♡ considering adding a file for handling helper logic, to make things like handling primary systems and stuff before backups

    ♡ updated current systems to return output and update dicts and updated engine.py to accommodate that

    ♡ I realized that I have been wasting a lot of time refactoring and trying to keep my files consistent, which I'm sure is a good thing later on, but for now there's a lot to be done so I'm going to switch focus a

#### Next Session:
    ♡ finish updating current systems to return output and update dicts and updated engine.py to accommodate that, left off on oga and getting the code to run, pick backup tomorrow and fix printing issues


##      05/06/2026
    ♡ finished updating current systems to return output and update dicts and updated engine.py to accommodate that

    ♡ I need to look over Mars_time.py and go over that logic again, but I might wait until I get the greenhouse and other systems set up

    ♡ I haven't decided if the greenhouse will be easier to implement after or before I update the Mars_time..

    ♡ updated Mars_time file

#### Next Session:
    ♡ start focusing on greenhouse variables and systems needed, starting w. light for the greenhouse


##      05/08/2026
    ♡ updated README.md and renamed a lot of files today

    ♡ start focusing on greenhouse variables and systems needed, starting w. light for the greenhouse

    ♡ going w. a hydroponic set up, I updated v1_scope to include all my notes about a greenhouse 

    ♡ going to add to my habitat size after I have the greenhouse set up, so for now I'm going to treat it as if it is a separate building, running on all the same systems

    ♡ I like the idea of the plants having a set percentage of sunlight that is let in, so even if it's low they're still getting at least a good portion of what IS available, but I'm not entirely sure I'll stick w. 70

    ♡ trying to set up my file so that it will be easy to incorporate changing seasons and days w.out sunlight, etc.

    ♡ reconsidering my modes being two separate words instead of snake case?

#### Next Session:
    ♡ continue greenhouse 
 

 ##      05/09/2026
    ♡ research for plants and nutrition (I updated notes in v1_scope.md)

    ♡ I'm going to make a list for the different plants, to keep it simple, I'm not going to have a list for each separate plant, instead I'm going to go by plant area

    ♡ adding plant list to state, I want to take how much spacing the plants need into consideration

    ♡ this isn't a greenhouse simulator it's a Mars habitat simulator, so it doesn't need to be as complex as it could be

#### Next Session:
    ♡ continue greenhouse 


##      05/10/2026
     ♡ busy day, but I was able to go over the lighting function I had made in greenhouse.py and decided to add zones for each type of container the plants are in, I'm going to use the averages of thet crop types in the containers

#### Next Session:
    ♡ continue greenhouse    


##      05/11/2026
     ♡ adding heat from the LED lights in my greenhouse_lighting function

     ♡ I might shorten the variable names as my sim gets bigger

     ♡ still going to use the layout to match my other files (I'm wondering how important this is in big projects)
     
     ♡ I updated the list for the greenhouse zones 


#### Next Session:
    ♡ continue greenhouse and start by adding ideal_temp


##      05/13/2026
    ♡ adding in hydroponics to the greenhouse list and starting from greenhouse lighting to make the greenhouse file be how I want it to be

    ♡ I didn't want the multipliers in the constants like some other files, b/c they are different for each zone 

    ♡ I connected the new greenhouse variables and logic to the other files

#### Next Session:
    ♡ continue greenhouse


##      05/14/2026
    ♡ less focused on matching files and more focused on accurate logic now

    ♡ going over all of my files and checking logic and structure before moving on

    ♡ I update all of my files and figured out my units of measurements, b/c I accidentally mixed up kpa being companred and usd w. kg, etc.

    ♡ I'm going to change the modes in each file to be snake case 

    ♡ updating alerts.py and I'm going to move humidity and thermal alerts there as well

    ♡ I updated my todo.md file and v1_state_variables file

    ♡ going to add in the gas leak logic so the variables are actually getting used so I can delete the vague universal gas leak/hour variable

    ♡ adding gas_leak.py file to handle that ^

#### Next Session:
    ♡ go over my numbers and targets


##      05/15/2026
    ♡ I'm going to go over my variable values in quick_test/state to make sure my numbers are where I want them, I realize I've changed a few things as I went while testing and using different research, so this seems like a good place to start

    ♡ considering making my habitat a bit bigger.. I was aiming for ~ 67m3, but I'm second guessing this when I focus on the fact that this is a long term, no resupply simulation

    ♡ increasing habitat size by 20%

    ♡ Today I started considering spatial realism

#### Next Session:

    ♡ review current variables, check numbers, evaluate my placeholders and review my targets


##      05/16/2026
     ♡  while going over the total habitat volume in m3, I'm thinking that the crew can live w. smaller living quarters and I'm going to make the greenhouse a bit bigger b/c it is crucial for long term survival and I'm considering storage areas being a bit bigger as well..

    ♡ I was reading about how much room a person typically needs/person for psychological wellbeing. I read it was 300m² pp but that seems really unrealistic for Mars

    ♡ research on the height requirements for ideal psychological wellbeing vertically, people seem to do better w. "void" spaces (taller living areas), but also considering that I can't have an unrealistically tall habitat, so I keep trying to go for the minimum for psychological wellbeing long-term so I'm going w. .. 4m? maybe.. 3.8 (though the habitat would need to be partially buried, but I'm not simulating structural engineering right now)    

    ♡ I'm also reading about the thickness that a Mars habitat would have to be, w. a focus on protection from radiation depending on materials used. I'm trying to figure out where the line is between believable Mars habitat and overcomplicating my entire simulation.. For now I'm going to choose some loose numbers and estimates and continue

    ♡ I'm only going to focus on the variables that I currently have and make sure I'm happy w. the numbers and targets and I'll consider spatial realism more later

    ♡ I'm updating the measurements and variables for the greenhouse now that I made it bigger. I want to optimize the space in the greenhouse

    ♡ considering looking at species that make their own structures and systems as inspiration for efficiency

    ♡ Taking the layout into consideration, hydroponics lets me consider other greenhouse layout ideas, so I'm leaning toward a sort of "helix" .. hive, area instead. A layered growing space that spirals inward toward a main central area for utilities, maintenance, water systems and other things instead of just rows and boxes.

    ♡ I also think it would be easier to visually see/monitor a lot more plants along a gradual slope instead of separate rectangular flat rows and it would potentially work well w. the vertical racks and hangers like I wanted.

    ♡ As far as the quick_test file goes, as of right now, it's messy and I will clean it up soon and the variables won't be printed to so many floating point decimals on the UI, it's mostly for debugging and making sure everything is working as it should

#### Next Session:
    ♡ make a file for debugging, so I can see my outputs closer together/subsystem instead of going through every subsystem every run    


##      05/18/2026
    ♡ instead of making a separate file for debugging I decided to just temporarily comment out my already set up print function to isolate each susbystem so I can check and see if they're working as I want them to work

    ♡ today I'm going over all of my subsystems and systems to see if they're all behaving and fixing any problems before moving on
    
    ♡ I do want to have the greenhouse capable of raising the O₂ in the habitat b/c w. my hexagon/hive idea for the structure, everything is close together, w.out separate buildings so it just makes sense to me that it would be a factor 

#### Next Session:
    ♡ continue running system checks


##      05/20/2026
    ♡ still going over my values and testing=

    ♡ I added handling excess O₂ to oxygen.py

    ♡ while going over the results from each subsystem, I'm realizing that CO₂ is not being handled right.. I need to fix where the Sabatier is getting it's CO₂ amount from

    ♡ I made some changes to the Sabatier file and ran a few test for four sols, getting an update every 5 hours while only getting the sol, time and atmosphere info.. CO₂ is much better, but there are still issues w. the buffer gas, as well as a few other things, that I will be working towards fixing

    ♡ I made some changes to buffer gas, double check them tomorrow

#### Next Session:
    ♡ check out buffer gas (pressure is low but not changing properly) and then continue running system checks


##      05/22/2026
    ♡ I added in the Sabatier into water.py, b/c I forgot to add it in the storage update and run_water_system function 

    ♡ while testing the water outputs, I can see that the net loss/sol is way too high, so I'm going to go over some numbers

    ♡ 115.5kg/sol is just the cost of having a 30 person crew

    ♡ I was thinking about other way to recycle and actually get water and I thought about piercing through the surface w. two or three heated pipes that siphon up some frozen Mars water every so often? retractable pipes so they don't freeze and can be used at will, I'm going to do some research on this

    ♡ going back to In-Situ Resource Utilization (ISRU) to extract water locally, I'm thinking piercing through the surface w. two or three heated pipes that siphon up some frozen Mars water every so often w. retractable pipes so they don't freeze and can be used when wanted and needed to avoid environmental factors

#### Next Session:
    ♡ start new file for water isru


##      05/23/2026
    ♡ I created a file for handling water extraction and I'm going to make a list in state, similar to the lists I have for the other subsystems and add in each pipe, in case I want to add more later and of course to have a few as backup

    ♡ I realized that I didn't have water runoff from the greenhouse, so I implemented that today and also fixed and cleaned up water.py, after including the for now very basic isru system

#### Next Session:
    ♡ add new variables in engine and update irsu to include pipe retracting and extracting, dust buildup/pipe, efficency loss, etc.
    ♡ include isru to systems in README.md


##      05/24/2026
    ♡ adding in new variables in engine for greenhouse runoff and also water isru

    ♡ added water isru subsystem to readme

#### Next Session:
    ♡ fix irsu file


##      05/25/2026
    ♡ fixing isru and added modes and pipe retraction and extraction

    ♡ going over water file, adding hysteresis and updating power used logic to make it more similar to CO₂_scrub.py

    ♡ updated power usage in water.py

    ♡ updating systems to include low power mode

    ♡ fixed venting logic in oxygen.py

#### Next Session:
    ♡ go over vent logic in each file


##      05/27/2026
    ♡ adding vent leaks to buffer_gas.py

    ♡ I know that turning buffer_gas.py into one long code might be different to read, but I think it works w. my section headers keeping things organized and hopefully easy to read, I'm also hoping this keeps things a bit neater when it comes to ouputs and variables and such

    ♡ two file refactors today

#### Next Session:
    ♡ break up starting variables and print
    ♡ test terminal output to adjust numbers!


##      05/28/2026
    ♡ seperating files for print and Habitat State

    ♡ this new print file is going to be made w. debugging and checking numbers in mind, it will not be organized this way for the actual UI

    ♡ went over output variable names and make them consistent (added, produced, recovered, proccessed, etc)

  ♡ huge refactor day!

#### Next Session:
    ♡ make summary print function for each category for debugging, or decide if I'm just going to comment out each one when I want to isolate the subsystems/categories
    ♡ test terminal output to adjust numbers


##      05/29/2026
    ♡ fixing  ch4 venting logic

    ♡ the methane leak is going to only be relevant in future events, maybe

#### Next Session:
    ♡ continue running system checks


##      06/01/2026
    ♡ running system tests, checking my numbers


##      06/10/2026
    ♡ back from a trip, back to my simulator


##      06/12/2026
    ♡ fixing my print step in quick_test.py to actually print the current sol and running my test for the longest time yet (40 sols)

    ♡ around sol 43, the battery runs too low


##      06/14/2026
    ♡ fixing temp issues, starting w. the insulation strength/thermal mass and fixing my heater logic


##      06/16/2026
    ♡ fixing radiator and heaters to make things smooth and effective

    ♡ I'm happy w. how the temp system is running for now, so now I'm running atmosphere again

    ♡ fixing buffer gas

#### Next Session:
    ♡ continue running system checks and fix CO₂_scrub.py


##      06/17/2026
    ♡ I'm starting to consider UI notes, I think it's a good idea to set that up before trying to train an AI so my sim is at least visually entertaining for someone running it. I'm trying to decide what to use for this but so far I'm considering porting to JavaScript and then using HTML, CSS


##      06/19/2026
    ♡ fixing my sabatier file, made the methane go aove the safe limit, so I'm going to see what I can do w. the methane storage and venting 

    ♡ I decided to make sure all ch4 is either vented immediately or sent to storage, it's not going to be added into the cabin atmosphere

    ♡ I fixed the sabatier call in engine.py

    ♡ I noticed my greenhouse is currently producting 75x MORE O₂ than my crew of 30  mean and this is absolutely not right, it doesn't make any sense so I need to fix this

    ♡ the math for zone info:
    structural: 0.022 kPa/m²/sol × 90 m²  = 1.98 kPa/sol
    container:  0.020 kPa/m²/sol × 110 m² = 2.20 kPa/sol
    rack:       0.015 kPa/m²/sol × 124 m² = 1.86 kPa/sol
    total ≈ 6.04 kPa/sol

    ♡ the math for crew O₂ demand:
    0.00011 kPa/hr × 30 crew × ~ 24.66 hr/sol ≈ 0.081 kPa/sol

    ♡ I'm going to chose that the greenhouse actually produce only 2% of the crew O₂ and CO₂ needs


##      06/20/2026
    ♡ setting up ISRU file for Ar and N₂, which is crucial for no resupply w. a con being power usage

    ♡ I am not going to have a timer for the compressors yet, but for future versions I am planning on adding a regen state and usig absorption/sorbent beds that need a regen cycle between intakes

#### Next Session:
    ♡ add isru_atm to power, bugger gas and other gas handling files and update isru_outputs and updates to include 'water'


##      06/21/2026
    ♡ I decided I'm going to add the sorbent beds to the isru_atm file before continueing to connect it to the other files

    ♡ don't forget to add isru_water to dust file

    ♡ I'm going to use five sorbent beds in total, two as backups as I like to have, so there are enough to absorb while another bed regenerates

    ♡ sorbent beds trap CO₂ from compressed Mars air before N₂/Ar and gets added to storage. This is modeled as a swing bed cycle, like the amine beds in CO₂_scrub.py.

    ♡ regen stop processing taking that bed fully offline, fewer adsorbing beds online = less raw atmosphere gets processed, meaning less N₂ and Ar gets added to storage too

    ♡ unlike isru water pipes that have a real physical deploy/retract travel time, a compressor has no mechanical delay, so it just flips between "offline" and "extracting" based on target amount needed online for each step

#### Next Session:
    ♡ continue isru_atm.py file


##      06/23/2026
    ♡ continuing isru_atm.py file

#### Next Session:
    ♡ add dust to isru_atm.py and isru_water.py


##      06/24/2026
    ♡ adding dust to irsu_water.py

    ♡ fixing the variables in print to work w. the update greenhouse file


##      06/25/2026
    ♡ starting to work on the UI, using a prototype image I designed in procreate, this will be updated, but the first step is turning my code written in python to json

   ♡ added ui_export and started on the visuals

#### Next Session:
    ♡ continue working on dashboard panels


##      06/28/2026
    ♡ I've been working on the visuals so there hasn't been a to log here

    ♡ I am going to make this so that the dashbaord updates every three seconds to start and I'll adjust this as I go

    ♡ I want to use snake case for js, but I know camelCase is best practice, so I'll stick w. that


##      06/30/2026
    ♡ I am deciding how to categorize my variables in the ui panels

    ♡ right now I'm putting amine beds in the atmosphere panel, but I think I'll add two more panels for OGA and amine beds after I finish putting all of my variables in dashboard.js

    ♡ I need to decide if I want to keep the water outputs in water, but that's 27 lines which is a lot for on panel, so I need to choose if I want to keep them in water, or put them in their corrosponding panels

    ♡ realized that I didn't rename my isru water variables to include the word water after adding isru_atm

#### Next Session:
    ♡ continue adding to dashboard.js and consider fixing output in print and ui_export.py to be in the same order


##      07/01/2026
    ♡ added to dashboard.js and started considering dashboard changes, like expanding screens and adding two more for the oga and isru

#### Next Session:
    ♡ work on dashboard.css


##      07/04/2026
    ♡ lots of changes to make to the dashboard including addin two more screens, one for the greenhouse and one for the habitat log, so status and alerts can move to the log and it will update w. any complaints from the crew about symptoms from pressure or hunger, etc. and if the system needs to do anything in states of emergency


##      07/08/2026
    ♡ I worked on the dashboard image and added a new palle, as well as angled some screens for better readability, as well as making some other layout changes


##      07/10/2026
    ♡ I did some perspective updates w. the dashboard image and I still need to add more screens for crew and mission log and fix the image more, the three uploaded are only prototype images


##      07/12/2026
    ♡ the last few days have been refining my layout image and deciding on panel amount and also panel placement

    ♡ I decided I'm going to add a panel for the crew information on one side of the status panel and a panel for the alerts on the other side

    ♡ I'm going to be adding crew scheduling, maintenance and a few updates, w. any complaints or any positive feedback from the crew when things are running well

    ♡ I added to the todo list w. update alerts to include things like stats evening out (CO₂ returned to normal range, etc.), buffer gas injections complete, isru pipes retracted, isru pipes deployed
    
#### Next Session: 
    ♡ decide if the middle panel is actually gong to be a mission log and decide what will be split between the mission log updates and the alerts section


##      07/14/2026
    ♡ creating event.py for the mission/event log file, I want to only show the last 50-100 latest events 


##      07/16/2026
    ♡ I broke my ISRU panels up into two separate panels, I would like to keep the atmosphere things together, I think

    ♡ I'm going to implement seasons into my sim before adding anything else. After doing some research I realized that I had my get_season_angle_deg wrong, b/c Mars doesn't move around the Sun at a constant speed moving faster near perihelion and slower near aphelion, which affects seasonal timing, dust storm season, solar energy and some of the other systems I have set up
    
    ♡ Reading about Kepler's equation:

    M = E − e sin(E)

    M = Mean Anomaly
    E = Eccentric Anomaly
    e = Orbital Eccentricity

    ♡ I'm considering the options I have for this.. there's the Newton Raphson for eccentric anomaly E. Starting w. E = M, each iteration calculates the current wrong answer and divides it by the 'slope' for a better estimate:
    
    new estimate = old estimate - error / slope
    
    ♡ The other option is fixed-point iteration, which rearranges Kepler's equation into:

    E = M + e sin(E)

    But that seems very... inefficient.
   
    ♡ the eccentricity for Mars is low, so this shouldn't take too many tries to get close using Newton Raphson 

    ♡ anomaly = the angular distance from it's last perihelion


##      07/18/2026
    ♡ finished adding seasons

    ♡ I'm reading about atmospheric opactiy and tau (how much sunlight the atmosphere blocks before it reaches the ground and optical depth being tau the number used to use the amount), low: 0.2 - 0.5, medium: 0.8 - 1.5 for dusty skies and high:  2 - 5 for major dust storms, these are related to seasons so I figured it was a good next step


##      07/20/2026
    ♡ I wanted to have a percentage of how far Mar's is through it's storm season

    ♡ I'm going to add random dust storms right now, while I'm working on season changes and atmospheric opacity, checking if Mar's is in storm season, how far through it it is and also have random wheather b/c predictable wheather is not realistic

    ♡ roll_for_storm is both accurate and a nod to dnd

    ♡ I find myself getting more used to python now and getting more comfortable doing things that I was worried I wouldn't understand later, like not wanting to return before the end of the function, adding more lines of code which isn't neccessary, I am looking back at my older code and seeing where it can be improved, which seems like a big milestone

    ♡ I need to start considering the ways this simulation can go wrong before I get there

    ♡ the storm opacity is going to be hardcoded for V1


##      07/21/2026
    ♡ the severity of the same storm stays the same for v1

    ♡ my ui_export.py file is messy right now and unorganized, while I make other changes and make more decisions about the panels for the ui, so I'm going to wait to update that for now and add the dust/storm updates to the alerts.py

    ♡ I've used dust and storm as the same thing in the file, hopefully that isn't confusing for anyone checking it out, I might change this even though the storms on Mars are dust storms

    ♡ I've decided to make a separate file that updates the probability/prediction logicm like the chances of a sotrm today, thermal issues, etc.

    ♡ keeping events.py for when I add in Murphy's Law disasters

    ♡ I'm going to focus on making the mission log next and make some decisions there

    ♡ while going over my isru files, the pipes in my isru file are set up so that they can switch their decision to deploy or retract, in case of low water emergencies

    ♡ I am considering if all of a sudden the pipes are deploying and the low power mode hits or I lose power if the pipes don't retract, they will freeze or use a lot of power w. the heated pipes, but retracting doesn't use power in v1, which I'm questioning now


##      07/22/2026
    ♡ today I was thinking about my power reserves and power set up

    ♡ I am really starting to consider what can break my simulation

    ♡ I need to consider more of a crew psychology

    ♡ I realized today I still had some variable name mismatches in my power file, I need to go over my power set up b/c now that I see the real amount of power being used, I need to consider more power


##      07/23/2026
    ♡ since adding in seasons, the daily solar power isn't going to be enough for even daily consumption, I need to consider more options for power

    ♡ I'm going to add a funcion in my print file to show totals for each sol

    ♡ my sim is running on average:  Solar Generated = 559.26 kwh, Total Power Used = 649.12 kWh, Net Energy = -89.86 kWh 

    ♡ I isolated the subsystems and the greenhouse light power is taking up a high percentage of the power, I have it set up to be running w. daylight, but now I'm thinking about having the lights on a 12 hour cycle

    ♡ finished updating the greenhouse lights, at 16 base hours for the greenhouse lights I've manaed to get the Greenhouse energy usage to : 260.46 kwh, instead of 325.55kwh

    ♡ I am reading about RTG, considering more arrays, like I mentioned in the past.. 


##      07/25/2026
    ♡ I've started designing a 50-acre solar field. I actually chose 50 acres b/c of where I grew up. I can picture the size and I can definitely see that being a manageable area for this.

    ♡ Right now, the design consists of 101, 250 solar panels organized into 2,250 arrays, grouped into 50 independent control blocks of 45 arrays each. This should make maintenance, fault isolation and power management much more practical than treating the entire field as one massive solar farm. I'm setting the panels

    ♡ I plan on using electrostatic dust shields, vibration cleaning which I looked at previously as well as protective covers and a system that sets off a scheduled flip upside down and a cover that protects the arrays from damage and extra dust buildup when they are offline and weight-sensor-triggered panel flips, that briefly flip upside down and backup after so much build up. 

    ♡ maintenance itself will consume power and temporarily take equipment offline, creating another engineering trade off for the habitat

    ♡ add these to v1_scope notes ^

    ♡ making a separate file for the solar fields

#### Next Session:
    ♡ go over notes about solar power and power in v1_scope.md and add these notes there, try to organize a bit (I like to reorganize my notes after doing more research and making new notes) 


##      07/26/2026
    ♡ organizing notes and files before implementing updated 50 acre solar plan

    ♡ I've decided to move my notes out of v1_scope.md and create a file called creation_notes and have a file for the systems so I can quick reference them, I need to decide if they all get their own files w. current notes and note histories, or one large file. separate files seems more efficient but it adds more folders and I haven't decided if that's unappealing or not 


##      07/30/2026
    ♡ research day


##      08/02/2026
    ♡ starting to implement my 50 acre solar plan starting w. updating state and run.py before adding to solar_field.py , I'm wondering if some of these variables should be in state, or in their own relevant files

    ♡ my state variables are the values that change during the simulation, but also vairables that I chose, not universal known constants

    ♡ I'm chosing to stick w. consistency at this point, especially b/c state isn't really that long

    ♡ choosing the mid point to the estimates in my notes for variable values

    ♡ I'm going to stick w. a hardcoded tilt angle for v1 instead of adding in the sun's elevation angle

    ♡ I'm consiering what happens w. my panels at night, I was thinking they be flipped and covered at night but that would be a lot of wear on the panels over time.. I suppose this is okay for v1 but needs to be revisited

    ♡ I'm going to have them flip over at a certain time per night and flip back over when it senses daylight, and when the habitat is in a storm situation during the day while the panels are flipped up, they will flip over and protect themselves, perhaps after they detect high wind, the habitat could detect this and they would flip for this too

    ♡ add wind calculations to Mars_time.py for v2?

    ♡ I considered adding the wind speed to solar_field.py to inlcude them flipping when so much wind has picked up, but I feel like this could cause problems, like constant fliping and covering, and potentially missing out on sunlight in crucial conditions, along w. wasted energy and mechanical wear.. this could have an option to be overwritten during low sol streaks, and set so the wind would have to be very harsh for them to cover

    ♡ I need to add cleaning/fliping: duration, queue, maximum number of simultaneous cleanings and cleaning availability state

    ♡ I updated the files to now run the updated solar field and removed the old array variables and system, now I need to incorporate the tilt

    ♡ right now I have ~ 69,000 + kWh/sol extra being generated, b/c I haven't set up a true power storage system and a separate large capacity power storage that only fills once the primary is topped off, and only sends it back into the primary storage battery

#### Next Session:
    ♡ start incorporating battery and power storage as mentioned above, continue sorting notes starting w. updating solar_fields.md and then lights and greenhouse


##      08/03/2026
    ♡ I'm going to set the primary battery at 25,000 kWh for now, until I have the true average energy used from longer testing and thes econday I'm going to set for 1,500,000 kWh (1.5 GWh)  (I might move this up to 2,000,000 kWh), which might seem excessive but I'm going for long-term w. no resupply

    ♡ there will be thresholds for the power pulls and when to accept charging for the second battery

    ♡ renamed battery_max_capacity_kwh to primary_battery_max_capacity_kwh

    ♡ seperating habitat lighting into its own file, I'll probably leave the greenhouse lights in the greenhouse file though

    ♡ I'm considering files for constants b/c some of my files have a ton, but I'm not sure which seems more cluttered.. more files or longer constants


##      08/04/2026
    ♡ research day while I really look into the greenhouse, updated and more detailed

    ♡ created Arcadia Planitia: Hive-8 Arcadia greenhouse plan, w. updated specs

    ♡ created a separate file for greenhouse creation notes, b/c one file was simply too small and there are too many considerations and components to put into one file

    ♡ updated greenhouse variables that changed when I decided on measurements and other specifics

#### Next Session:
    ♡ continue figuring out the greenhouse plan, and separate notes into separate files


##      08/09/2026
    ♡ going over nutrition plan and macronutrient targets

    ♡ I chose these targets intitally (carbohydrates: 40%, fat: 45%, protein: 15%) b/c I was taking crew stability into consideration, as well as crew performance, cognition and overall wellbeing. I need to choose between this and a conventional nuritional range, so I decided to try to stay closer to the suggested range but still make it a bit different like a sort of compromise 

    ♡ I want the habitat food system biased toward steady energy, satiety, minimally processed foods and avoiding excessive carbohydrate dependence still so I will change the fat and protein goals, and keep the carb target as is

    ♡ thinking about seasons and crop growth but b/c of the greenouse being fully controlled all the time, the conditions stay the same, I also considered crop changes after certon harvests, but maybe this can be applied in future versions, it's just not a priority


##      08/11/2026
    ♡ I'm going over greenhouse power and waste heat, now that a lot of changes have been made to the greenhouse

    ♡ NASA style and long duration designs run moderate light levels instead of Earth's commercial maximums, so 100-160 W/m² electrical is common for efficient systems that mix sunlight + LEDs

    ♡ more modern LEDs deliver ~ 2.7-3.5 µmol/J, at 0.12 kW/m² (120 W/m²) electricalao I can expect ~ 320-400 µmol/m²/s (micromole, 1 mole = 1000000 umol)

    ♡ I read about crop needs:
        Spinach, peas, most leafy/herbs:
             150-300 µmol/m²/s (happy ~ 200-250)
        
        Quinoa, many medium crops:
             300-500
        
        Sweet potato, peanuts (higher light demand):
             400-600+ for strong yields

    ♡ so I'm chanding my light targets per m² to structural zone: 0.26, container zone "light_target_kw_per_m²": 0.23, rack zone "light_target_kw_per_m²": 0.19,

    ♡ updating greenhouse to include new values, and equipment power

    ♡ moving onto greenhouse water/hydroponic file


##      08/12/2026
    ♡ I'm looking into hydroponic set ups and how they work today, I'm not going to go too far into this, again b/c I don't want this to become a main focus, it's not a greenhouse simulator

    ♡ I'm looking into Nutrient Film Technique (NFT) where the plants need a constant flowing nutrient solution, and it seems like this is better for more shallow plans, so it would make sense that the rack system has these

    ♡ reading about recirulating drip systems using dutch bucket set ups, meaning each plant or small group gets its own bucket, all connected sharing plumbing which is exactly what I had planned so this is perfect

    ♡ I'm choosing targets to be averaged per zone

    ♡ I'm trying to decide how in depth to make this, I was considering pH, EC nutrients, solution temp and dissolved O₂, but these are all things that really would only impact plant health and growth rate, so I'll just make note of them for now, for potential future reference

    ♡ I put a lot of notes right into the hydroponic.md file instead of here

    ♡ EC (Electrical Conductivity) is measures in mS/cm, indicating how concentraed the solution is, not which nutrients are present or if the ratios are perfect, just the overall ionic concentration (so you can tell if the concentration has changed)

    ♡ DO (Dissolved Oxygen)how many O₂ molecules a present in water, essential for the respiration of fish, bacteria, and other aquatic organisms, making it a key indicator of water quality. Low DO stresses roots, slows uptake, and raises the risk of root problems. 

    ♡ the rack zone naturally gets good O₂ exposure from the thin moving film, while the LECA zones rely more on drainage, air gaps, and reservoir aeration

    ♡ I'm not so worried about an upper range for the dissolved O₂ target b/c the most important thing is if it's high enough

    ♡ considering equipment for hydroponics, and reservoir sizes.. all three zones will have a different L/m² b/c of the differnt systems and containers holding water differently (LECA beds retain a lot of moisture in the root zone, Dutch bucket style containers retain some moisture and NFT channels don't hold very much) 

    ♡ continue hydroponics including ciruclation pumps, add that to power, calculate flow rate, etc.

    ♡ updated a few values and calculations in greenhouse\gases.md, but I need to come back to this file after I finalize the layout to get the true calculations

    ♡ renamed system_design folder to notes, the previous name was just too long and this is obvious


##      08/14/2026
    ♡ considering pumps for each greenhouse zone, I want to have one backup  in case the prmary fails that would be automatic 

    ♡ I was reading that the structural LECA zone would be able to handle pump failure better than the container and rack, especially the rack b/c it is relying on the continuous flow

    ♡ the sizes for the zonnes for the containers and growing space, are rough estimates, I didn't think it was neccessary to have an exact amount of boxes or containers for v1, and they are going to be made using the zones plant averages and growing area

    ♡ I'm going to decide starting module sizes based on the measurements I have already for Hive-8 Arcadia

    ♡ I'm going over gases.md now

    ♡ removing the forced 2% result 

    ♡ implementing the photosynthesis behavior that changes during the 16 hour light and 8 hour dark period,starting w. the light period

    ♡ I'm going to use mol/m²/sol for my sim b/c It alread uses sol fractions

    ♡ I'm using NASA's potato and sweet potato information b/c they are studied as space crops and I'm including those in the sim: 45 µmol CO₂/m²/s at peak photosynthesis, w. night time respiration ~ 9 µmol CO₂/m²/s in those high light experiments

    ♡ my sim is using more moderate lighting, and my zones are mixed crops so I'll look into more conservative averages

    ♡ considering plants being at different growing phases and not all of them being so dense

    ♡ structual: for every m² of structural growing area, while photosynthesis is active, the zone average plants remove ~ 10 µmol/m²/s in this simplified model below the ~ 45 µmol/m²/s

    ♡ container: 
        - ~ 12 µmol/m²/s for V1 zone average
        
        - sweet corn can get to ~  28-34 µmol/m²/s under ideal controlled conditions, while passionfruit seems to commonly be ~ 10-30 µmol/m²/s, also consindering different growth stages, again

    ♡ rack: 
        - ~ 10 µmol CO₂/m²/s for V1 zone average
        
        - hydroponic spinach studies say that photosynthetic rates can be much higher than 10 µmol CO₂/m²/s under ideal controlled lighting, using 10 is a conservative mixed zone average instead of than every rack is a mature and perfectly lit

#### Next Session:
    ♡ start figuring out values for the plants dark period respiration


##      08/15/2026
    ♡ I've decided to zone averages again for each zone's light period CO₂ uptake rate as the dark period's CO₂ release rate, b/c NASA controlled enviornments show that the exact fraction can be very different depending on crop and environment, but b/c of the fractions being so different this will be a pretty rough average

    ♡ structural zone will have the highest night time respiration average for my project at ~ 3.0 µmol CO₂/m²/s

    ♡ ~ 1.5 µmol CO₂/m²/s for container b/c the sunflower respiration specifically seems to be measured as pretty low, especially compared to the crops in the structural and rack zone

    ♡ ~ 2.5 µmol CO₂/m²/s for the rack zone, b/c spinach specifically is measured at ~ 5 µmol CO₂/m²/s so I decided to use that as a half the mixed zone average, just as something to go off of

    ♡ I had considered using the 1:1 simplified photosynthesis equation, but that doesn't seem realistic and NASA life support work treats CO₂/O₂ ratios as different

    ♡ PQ = photosynthetic quotient
    ♡ RQ = respiratory quotient

    ♡ I read that PQ depends on species, what kind of nitrogen the plants are taking in, what biomass they are building, and how nutrient conditions can even have an impact.. my simulator isn't going this far in depth for v1
    
    ♡ Structural: PQ ≈ 1.10, this zone has more storage root/seed/fat producing crops

    ♡ Container: PQ ≈ 1.08, this zone has very mixed crops

    ♡ Rack: PQ ≈ 1.05, this zone is dominated more by leafy vegetative crops like spinach and herbs, so I'll keep it simple w. ~ 1.1 ratio

    ♡ I read that PQ depends on species, what kind of nitrogen the plants are taking in, what biomass they are building, and how nutrient conditions can even have an impact.. my simulator isn't going this far in depth for v1 so I'm going to go w. one value for the O₂ exchange so for light periods it will be 1.03 for all zones 

    ♡ I read that RQ depends on what the plants are respiring, first they respire glucose/carbs, then fats, and then sometimes proteins

    ♡ carb respiration is ~ 1.0, whil emore lipid/proteins can lower it, so I'm going w. 0.90 as a simplified value for all zones, it seems like a conservative mixed average
    
    ♡ pressure change: ΔP = nRT ÷ V  (Δ = delta)
        n = gas exchanged (mol)
        R = 0.008314 kPa·m³/(mol·K)
        T = atmospheric temperature in Kelvin
        V = connected atmospheric free volume in m³

    ♡ moving on to water for the greenhouse now

    ♡ w. so many changes I'm pretty much starting over for the water plan for the greenhouse, using my old information as reference

    ♡ starting w. plant water demand, the old value was 3.4 kg/m²/sol × 1.15 = ~ 3.91 kg/m²/sol, looking over the NASA study w. potatoes I've been referencing the total system water was ~ 2 L/m²/day, since water is ~ 1 kg/L, ≈ 2 kg/m²/day, a Mars sol = ~ 1.0275 Earth days, 2.0 kg/m²/day × 1.0275 day/sol ≈ 2.06 kg/m²/sol

    ♡ b/c my structural zone isn't all potato, I need to increase the mixed zone average probably above that b/c the banana is also very water demanding.. so for structural preliminary value I'll use the plant water uptake rate of ~ 2.5 kg/m²/sol

    ♡ containers contain med/tall crops and the hydroponic recircle the water efficiently, so it doesn't need to include the solution in the containers, NASA emphasizes that in closed CEA (Chemical Equilibrium w. Applications), the major crop water requirement is what plants transpire, w. irrigation water recirculated

    ♡ ~ 2.2 kg/m²/sol for container as a V1 zone average b/c it stays close to the crop water scale used for structural while being under ~ 2.5 since that zone includes the larger and more water demanding crops

    ♡ this one can be low considering growing conditions and crop choices for the rack zone, so ~ 1.8 kg/m²/sol will work for now

    ♡ replacing the old percentages for transpiration and plant mass, or at least going over the calculations

    ♡ plant water uptake seems to be mainly transpiration.. in some hydroponic experiments, water disappearing from sealed nutrient containers is treated essentially as transpiration, b/c only the above ground plants are exposed to the air, the water retained is actually quite low compared to that

    ♡ NASA ECLSS systems treat condensate as a recoverable wastewater stream, and plant growth life support research looks into recovering and reusing transpired water vapor, so using ~ 95% capturing efficiency seems right so that the recovery isn't perfect, but still a small amount doesn't get collected

    ♡ things like maintenance/flushing, minor leakage, evaporation from exposed solution or wet surfaces, and solution retained in equipment/LECA during servicing all add into the the water losses, but I think I'm just going to use a small recirculation loss, and make each zone have a different percentage, mostly b/c of the different growing conditions, considering the ~ 95% capturing efficiency

    ♡ the biomass water will eventually be calculated from crop production, but not for v1, so in the meantime the placeholder is just going to be ~ 5%

    ♡ starting to go over my greenhouse.py file and implement the new updated greenhouse plan

    ♡ I want to consider a file for a zone overview, leaving out a lot of notes and math, mainly for easy reference

    ♡ greenhouse.py is now updated, and now I have to make transpiration no longer count as a fixed, greenhouse owned recovery system

#### Next Session:
    ♡ create atmosphere.py potentially
    ♡ put the mol to kPa calculation there and remove the helper from engine.py
    ♡ go over water.py notes and system design, then temp notes and system design


##      08/17/2026
    ♡ since changing the habitat size and slowly figuring out the layout of the habitat, certain measurements that include the volume should really only be considered as placeholders

    ♡ I didn't consider how the greenhouse zones O₂ and CO₂ will be worked in.. I need to decide if they will be separate or part of the overall habitat

    ♡ I will focus on water for the time being, and I think continue going through everything as I have been w. updates and more research before focusing on atmosphere.py so I can be more accurate and have some extra time to decide how to handle the greenhouse zone ideas

    ♡ I have to decide what to do w. the greenhouse zones, also I think the zones themselves being separate for control wasn't the best call. The greenhouse should've been handled in four quadrants or something for quarantine so I'll add this to Future Considerations in docs\notes\greenhouse layout.md I had intended for crop type grouping and area containment as two separate parts, but that isn't a priority right now


##      08/18/2026
    ♡ today I'll be going over my entire habitat's water system

    ♡ I need to remember to go back over my make-up water demand values so they don't dominate the water balance after I get the water system set up

    ♡ consider crew laundry and other misc. things

    ♡ I'm going to lower my UPA rate b/c reasaech shows that my previously decided system was a bit optimistic, so I will lower it from 0.94 to between 0.70 - 0.87. I'm also going to increase the recovery fraction from the BPA. I read that it usually recovered more, so I can move this to between 0.95-0.98

    ♡ I'm going to look at my storage tank capacities and then figure out how I want the layout to be, this is a simulator and only v1, so I'm not going to have incredibly detailed layout plans

    ♡ current tank capacities:  
        - potable_water_storage_capacity_kg = 6500.0,
        - gray_water_storage_capacity_kg = 1200.0,
        - black_water_storage_capacity_kg = 800.0,
        - condensate_storage_capacity_kg = 250.0,
        - brine_storage_capacity_kg = 400.0,

    ♡ increasing these tank capacities, b/c they were too small, the condensation alone can go up to 2,600 k/sol, and I need there to be a lot more water storage for long term survival

    ♡ adding an extra tank for the isru system

    ♡ ISS keeps a minimum reserve of ~ 800-1,600 kg of potable water in contingency after containers and MASA studies size water storage for only ~ 30 days of open-loop operation, and I read that you should plan for the largest expected daily usage plus unanticipated events

    ♡ potable water storage capacity: 10,000.0 kg, 
        usage/sol: ~ 70.5 k (drinking / nourishment only)
        this would last ~ 142 sols

    ♡ gray water storage capacity: 3,500.0 kg
        usage/sol: ~ 45 kg (hygiene)
        this would last ~ 78 sols
        
    ♡ black water storage capacity: 1,800.0 kg
        usage/sol: ~ 54 kg/sol
        this would last ~ 33 sols

    ♡ condensate storage capacity: 5,000.0 kg
        usage/sol: ~ 54 kg (breath / skin)
        this would last ~ 93 sols

    ♡ brine storage capacity:1000.0 kg
        usage/sol: depends on recovery efficiency..
        this would last ~ 

    ♡ greenhouse reservoirs (total): ~ 2,000 kg
        usage/sol: recirculating

    ♡ I need to decide on layout.. originally I had planned for the rooms to be the same shape as the greenhouse, I had considered different heights too for notes mentioned previously

    ♡ sticking w. my octagon/hive style layout, I can work on a central utility module for the water

    ♡ I want a central hub w. clean, distinct corridors leading off to different rooms/octagons in the habitat, I think there should be an obvious split between the greenhouse/food area and the utilities that handle things like wastewater and things you don't really want to think about while wanting a clean area

    ♡ I am picturing an area that's clean, open, and psychologically pleasant. By that I'm talking about environmental psychology, biophilic design (I believe this one is very important for a long term habitat for numerous reaons like reminding the crew of home to.. so many other reasons, I'll add later), indoor environment quality and salutogenic design. The goal is to prevent chronic stress, monotony, sensory deprivation, loss of control and social friction.

    ♡ considerations: 
            - indoor vegetation ()
           
            - simulated natural views (lakes, forests, aurora borealis, natural wonders, perhaps in the living quarters the crew has options to choose from)
           
            - plants (connection to home and living things, caretaking, flowering, etc.)
           
            - as mentioned before room height variations matter, but predictability also matters
           
            - smaller areas a bit secluded for socializing (two or three of different sizes I think, for small social gatherings, one can dual serve as a meeting/conference room), quiet soundproof areas for study/focused work

            - cruise size library
            
            - tiny place for worship potentially?? This seems important to some people
            
            - gym for exercise and a running track potentially
            
            - a steam room for relaxation, physical ailments and transpiration over the greenhouse
            
            - potential observation area that is VERY well structured and supported like you walk into one of 
            those clear geometric greenhouse domes that some places have in the summer where you can sit and eat
        
            - crew quarter considerations:
                    - private crew quarters, that are small but large enough to be alone and not have to lie in a pod/bed, a place to actually relax, I'm thinking basing it on cruise rooms and how they have the storage and bathrooms, and down hallways that actually separate them from the main rooms of the habitat

                    - figure out how to handle smell?

                    - things that give the crew a sense of control over their environment like  temperature controls
                    - ambient controllable lighting
                    - enough storage you can feel organized and clean
                    
                    - transparent observation area that is VERY well structured and supported:
                     a clear geometric dome that are lit through solar lights or string lights w. the same customization options as the bedroom by choosing ambient sound/music w. either modular furniture or more outdoor furniture, the crew can have the option of having a room extension of their choice it can be a personal greenhouse, patio, living room, hobby/music/art area, sleeping won't be recommended b/c the bed is ideal for a solid rest but it's their choice
                    
                    - including picture frames
                    - soft/natural patterns and textures (things like mock wood or stone appearance or texture)
                    - and something on the roof that the crew member gets to choose
                    - perhaps this can also be simulated
                    - a soft carpet
                    - shelves
                    - humidifier or dehumidifier
                    - those vanity/counter/drawer areas you can sit at on cruise ships
                    - separate small bathrooms
                    - a small area for beverages
                    - like hot water and tea or something noise cancellation
                    - soft bedding is important
                    - rest is important
                    - speakers/music
                    - ambient sound options(noisy cafe
                    - calming rain sounds
                    - the sound of an ocean to remind the crew of home etc. or they can close their eyes and imagine they are on earth somewhere)
                    - very comfortable rooms and furniture
                    - the crew quarters are VERY important
                    - I will add more as I think of more things (I am basing a lot of this on my own experience and preferences while considering observations about friends and family) personnel need to feel cared for and very comfortable

    ♡ the thing about a habitat like this, is that the crew needs to feel not only lucky to be going b/c of the oportunity but also feel as if they are getting special luxuries from earth, that ultimately don't even neccessarily need to be too expensive, the rooms are small, this sounds like a lot but when you consider the risk the crew is taking and how important their mental state is, a bit of extra items and options won't hurt in the long run
    
    ♡ some kind of specific decoration to mark certain areas so when you see them it will be obvious where you are, and it will become a symbol of familiarity and comfort after a while

    ♡ I want to consider some seasonal changes that are subtle but noticeable, like special lighting, seasonal ambient sounds or visuals that are exclusive to those seasons w. hidden easter eggs or something, nothing too complex but I'm sure there are ways that an artist could have a lot of fun w.
        
    ♡ psychology is almost it's own subsystem
        
    ♡ constant access to personal AIs for numerous reasons
    
    ♡ I'm picturing a few different hub areas, that are obvious as to what they are a hub to (utility, social/cafeteria, hallway to living quarters) w. hallways to avoid there only being one entrance to utility rooms mainly, in case there are emergencies, maintenance, or just busy areas

    ♡ steam room can be a potential future version consideration ( pros: real benefits, high recovery rate and a small earth luxury.. cons: extra water demand (hardly b/c of recovery, extra head and humidity load, ventilation is important but maintenance and cleaning needs to be considered), I will add it in my notes though b/c I am undecided

    ♡ crew water demand are rough estimates for now, overassumed instead of under, and the drinking and food rehydration is based on NASA's baseline, the personal hygiene value is higher than the ISS minimum, and some other values are averaged

    ♡ I think that the crew should be able to have showers w. constant water, there are only 30 of them but there should be a max time amount, I'm thinking 15 minutes as a hard maximum, 10 minutes as standard, 5 minutes in low water mode, and a very short, low-flow shower mode; "Navy" shower mode 1. water on = wet yourself, 2. water off = soap/shampoo 3. water on = rinse 4.done ( maybe controlled w. a push button?)

    ♡ making the shower cut off at 20 minutes instead of 15, some people like longer showers and if I will reduce it to 15 if need be

    ♡ I am using misc to represent little things like eye washing stations, extra consumption, etc.

    ♡ the water utility area containing the water tanks, aren't going to be light-admitting, or if they are, it won't be a priority b/c I want to make sure enough true light gets in here to see well

    ♡ I did consider the tanks outside of the habitat, but that opens up a lot of other issues like maintenece issues, but I am thinking about partially burried tanks, where only about 30-40% of the large tanks only show in the warm water utility room so everything can stay in the heated room, but I will have to add extra heaters, insulation, leak detection, etc. and the freezing risk is massive, for v1 I'm sticking w. keeping the tanks fully inside the water utility room

    ♡ I decided to size the water utility room around the water equipment

    ♡ I'm partial to symmetrical designs and shapes for layout

    ♡ I considered keeping water tanks in the storage under the ramps in the greenhouse but I decided to keep those seperate

    ♡ small permanent losses = uncaptured vapor, operational losses, biomass water, residual brine

    ♡ I don't know why I didn't notice how big the greenhouse reservoirs are compared to how much my plants actual take in per sol, so I'm going to lower some of those values, still keeping an extra amount as a buffer.. NASA's emphasizes fluid delivery/recovery, reliability, maintainability, aeration, low mass and low volume instead of universal L/m² reservoir rule

#### Next Session:
    ♡ add treated crew waste nutrient interface
    ♡ revisit greenhouse make-up water demand
    ♡ continue habitat water system
    ♡ finish UPA / WPA / BPA assumptions in water.md


##      08/19/2026
    ♡ starting w. crew waste to the nutritent interface today

    ♡ crew waste goes to wastewater, to water/nutrient recovery, to treated nutrient concentrate to greenhouse to zoner reservoirs


##      08/20/2026
    ♡ raised BPA handling capacity from 0.25 kg/h to 0.5 kg/h and added daily capacity calculations for water recovery


##      08/22/2026
    ♡ not every room in the habitat is going to be an octagon shape, only the areas that would be better for effiency and space

    ♡ I'm now looking into the power storage rooms, if I get the size of the subsystems figured out I can get the net habitat volume and then make my calculations include real values instead of a placeholder

    ♡ breaking the secondary power storage into multiple smaller rooms or pod areas seems like it would be neater, less overwhelming in emergencies, easier to maintain and easier to isolate issues if they came up later

    ♡ for the secondary battery storage, I'm picturing a hallway w. walls that act like partitioners, so you can walk down the hallway, and on the sides there would be like.. rooms/bays/pods w.:
            - rows of tall metal battery cabinets or racks
            - smaller rectangular battery modules inserted into those racks
            - thick electrical cables, etc.
            - coolant pipes and manifolds
            - battery management electronics
            - breakers and electrical isolation equipment
            - fire detection and suppression equipment
            - narrow but not too narrow maintenance aisles between rack rows
    
    ♡ each area would have it's own fire resistant walls and doors, independent thermal monitoring, independent electrical isolation, controlled ventilation, its own suppression system and no unrestricted airflow into the central corridor
                
    ♡ I was thinking a backup battery can be allowed to be in a more inconvenient spot, meaning it can be a lesser priority for easiest access areas, I want this area to be quite compact, and not too high b/c I want this to be clean, easy and boring to walk through

    ♡ if I make each area about 1,000 m³, and the corridor about 4 m wide, w. six rooms on each side, so 12 in total, that would be around the size of a medium size-ish grocery store

    ♡ I'm picturing a specific grocery store that I go to in town, considering the main floor space, not including employee only areas,  1.5 GWh battery capacity in 12 isolated battery ares, that would be around tree quarters of the shopping area, it should lead into another room, but not be the main door b/c it's small 
    
    ♡ by "system level energy density: ~ 125 kWh/m³" under the secondary batter bank physical layout, I am talking about much battery capacity fits in the complete installed battery system w. supporting equipment and maintenance space

    ♡ for the main battery room doesn't need to be huge and can be a taller industrial room, though, I think that there should be seperate battery areas that can be seperated and isolated for maintentence and for emergency handling

    ♡ added full Sabatier behaviour, modes, chemistry, and water contribution into its own note file
    
    ♡ documented the intended integration between OGA hydrogen production, Sabatier water recovery, methane handling, and possible future propellant production

    ♡ I think that adding the Sabatier either into the same room or very close to the atmosphere/resource recovery area is a good idea, I've found that the Sabatier rack is around 2.0 m high × 1.05 m wide × 0.86 m deep on the ISS, a ~ 0.4 m³ of rack volume that includes the reactor, condensor, water seporator, vales, sensors, controllers and plumbing (so ~ the size of a washing machine).. the actual reactor is supposed to be smaller

    ♡ I'm wondering if my habitat will need more than one Sabatier, I like to have backup equpiment whever possible so I'll add another one now that i know th actual size. I might have three, depending on room space

    ♡ if I can fit three Sabatier racks and reactors in the same room as the safter pipes from the OGA (the hydrogen buffer), the co2 piip from the atmosphere or storage together I want to do that. 

    ♡ while I consider where to keep the Sabatier I'm going to move to the water processing assembly rooms, I want to avoid contamination, and for everything to stay clean overall, and to make maintenence easier, the potable water will have it's own clean room and area

    ♡ I considered keeping all the non-potable water tanks together, but I'd like the seperation between the ISRU raw water to have it's own area


##      08/23/2026
    ♡ making the changes to move the water processing systems to have rooms to serperate by water quality and function

    ♡ adding in three Sabatier systems, potentially more b/c this IS no resupply, but three for now will be okay

    ♡ hectic day, so I will go over more sytems one at a time that have to do w. the atmosphere

#### Next Session:
    ♡ sabatier.py: ch4_leaked_kpa is adding storage leak into cabin ch4_kpa, it should vent to Mars exterior per sabatier.md, not cabin atmosphere
    ♡ design decision + follow-through
        - decide: implement Sabatier to WPA water routing in water.py
        - new sabatier_water_storage_kg holding tank (like condensate)
        - WPA priority branch: condensate to sabatier water to gray to raw ISRU
        - stop adding sabatier_water_produced_kg directly in update_water_storages_kg()
        - update hab_water.md "Water Processing Order" line it still says UPA + WPA + BPA + Sabatier (outdated, doesn't match sabatier.md anymore)
    ♡ room sizing
        - finalize Wastewater Storage Room (currently 80-100 m² range)
        - finalize ISRU Water Room (currently 40-60 m² range)
        - write atmosphere.md:  OGA / CO₂ scrub / buffer gas / Sabatier room layout (next room on the tracker)
    ♡ potable water storage room says "shape: rectangle" but still has leftover octagon phrasing (width across opposite walls / wall length)


##      08/24/2026
    ♡ originally I had pictured the greenhouse as a kind of central hub for the entire habitat, but now I'm thinking of having four central hub areas one for a living/social almost wing area, greenhouse/food hub, a resource and utility hub and a power/energy hub, wher the surrounding rooms branch off from those hubs and there are corridors/secondary loops that connect the outer rooms so the crew could move between zones w.out going back through the center always

    ♡ the atmosphere are will be w. the utility/resource area b/c a lot of those sytems have certain connections to the water eqipment and storage so it makes sense that they are kept in closer proximity

    ♡ after entering the total floor area and volume for the utility / resource area, the water rooms seem small compared to the power rooms, but potable holds ~ 10 m³ of water itself, so ~ 110 m² room gives generous tank space, access, and structure, the other gray, black and brine water are smaller, so that space makes sense as well, the raw ISRU water at 4,000kg fits in 40-60 m² and the UPA, WPA and BPA equipment fits in ~ 90 m² with aisles sounds good for a 30 crew plan.. power just seems massive in comparison b/c the secondary battery corridor I made is bigger than my original habitat plan b/c of the amount of space they need.. when I add more rooms to the resource recovery area it will be bigger for sure

    ♡ creating file for amine swing bed notes

    ♡ increasing the scrubber set from six to eight beds to improve redundancy, maintenance availability and recovery from elevated CO₂

    ♡ a single swingbed system together is ~ 40 × 43 × 30 cm (16" × 17" × 12")

    ♡ solid amine swing beds have been used and demonstrated for spacecraft CO₂ removal for 30+ years (CAMRAS, Amine Swingbed Payload, TAS, RCA)

    ♡ the beds are thermally linked so adsorption heat helps desorption (low extra heater demand in some designs)
    
    ♡ I am comparing each bed to the size of a washing machine

    ♡ a lot of amine systems take up water vapor along with CO₂

    ♡ absorption is often stronger when air is humid; some designs I found intentionally managed both CO₂ and humidity in the same swing beds

    ♡ water with CO₂ is usually released during regeneration (vacuum or thermal swing)
    
    ♡ for my surface habitat I can consider regenerating beds can return moisture to a recovery path or to a vent system, CHX / humidity control and amine beds both affect cabin water vapor and scrubbed CO₂ sent to storage / Sabatier should be considered for residual moisture for product purity

    ♡ I will save this for the future, not V1

    ♡ updating co2_scrub.py to stop just using the beds online in the order they are on the list, and the co2_load needs to be implemented like the sorbent beds so the bed switching is actually calculated and based on saturation instead of the automatic 55min timer, so even though with capacity at 3.0kg per bed, the beds probably won't reach full saturation within the 55 min, so it will still sort of be the same

    ♡ updated co2_scrub to have regeneration, standby and online, there are now four beds primary, four beds backup, added kg to capacity in the amine beds list, 

    ♡ CO₂ now goes into CO₂ storage


##      08/25/2026
    ♡ I was lookig over co2_scrub.py..real amine swing beds run by the CO₂ bonding to the sorbant, removing it from the air. That CO₂ isn't actually a usable capturable resource b/c it's bonded ot the bed material. The regeneration is made to sent that CO₂ off of the sorbant as a captured gas steam where it then becomes something that can be captured and routed.

    ♡ right now, the CO₂ gets sent to storage as soon as it's bonded, so my simplification is actually wrong b/c rigt now it's saying it's stored AND bonded, which doesn't make any sense,so I just need to move the storage step higher to fix this so it's included in the regen/release step

    ♡ max_time_on_bed_min = 55.0 < placeholder, research actual time 


##      08/26/2026
    ♡ fixed methane venting from inside the habitat to outside

    ♡ I realize that I also had a storage leak which I'm questioning now.. the gas leaking in the atmosphere makes sense, but leaking from storage is a problem, and unrealistic

    ♡ fixing sabatier water produced, and making it go to it's greenhouse CHX

    ♡ fixing plant transpiration, and renaming some variables from saying "greenhouse" to "gh"


##      08/27/2026
    ♡ I still need to update the thermal system and the CHX needs to be taken care of, I'm starting with the gh CHX first

    ♡ sabatier.py: ch4_leaked_kpa is adding storage leak into cabin ch4_kpa, it should vent to Mars exterior per sabatier.md, not cabin atmosphere
   

##      08/30/2026
    ♡ adding function in greenhouse.py for greenhouse CHX

    ♡ while going over my habitat systems, the layout is starting to become muddy. I am deciding on a shape and overall rough size of the habitat, and I'm going to use Arcadia Planitia: 50 Acre Solar Plan for sizing references and ideas

    ♡ after looking at NASA habitat and construction studies, I think a ratio of 1 m² for everu ~ 20 - 25 m² of solar field area seems like a starting point

    ♡ I also wanted to consider Space X as well. Considering the initial base into a self-sustaining city plan, an idea could be to create a habitat that could eventually be a kind of settlement block that can handle attachments for repeatable settlement blocks, this won't be simulated in v1 though

    ♡ I'm definitely sticking with the dome idea for each individual cabin, the dome is a customizable room extension, not a space intended to hold every option at once

#### Next Session:
    ♡ to do: 
        -add crew quarter power usage estimates to total power, include the dome shutters, can use the solar array covers as reference for power usage  ♡ design decision + follow-through
        - WPA priority branch: condensate to sabatier water to gray to raw ISRU
    
    ♡ room sizing
        - finalize Wastewater Storage Room (currently 80-100 m²)
        - finalize ISRU Water Room (currently 40-60 m²)
        - write atmosphere.md:  OGA / CO₂ scrub / buffer gas / Sabatier room layout
    
    ♡ continue mapping habitat layout

    ♡ move onto OGA system after/during layout plans

##      09/03/2026
    ♡ looking at the dining area and food storage to wrap up the crew part of the habitat, I think ~ 300 m² (around the floor area of a large house)

    ♡ I decided on some floor space for food and kitcen areas

    ♡ I don't like the idea of having one large communal recreation hall area, b/c it seems exposed, awkward, and more institutional like a hotel lobby or something. I like the idea of having a space for events, but the dining hall seems like it would work for that. 

    ♡ I decided to have a few different living space areas, like a lounge, more private areas and other places I mentioned in my notes previously

##      09/04/2026
    ♡ looking back at my layout notes, I am going to include my idea of including those study pod / sound proof cubicles I've seen ads for online for work spaces

    ♡ I decided that two larger, quieter focus rooms and private spaces can be used for areas for smaller groups to study 

    ♡ this simulation is assumed to have a lot of full autonomy to stay functional with only 30 crew to run it

    ♡ I'm considering the space for the creative / media / game room area, for sure media and game room can go together, and they can go into a casual lounge area or private social rooms

    ♡ I've decided that the private pods can go in the library which can be ~ a small community library room, with a mixture of physical and digital books and comfortable reading areas where the lighting is warmer and softer than in general work areas while still bright enough for comfortable reading

    ♡ a separate game or media room isn't included for V1

    ♡ games and media are distributed through existing shared and private spaces like:
        - large shared living room for group video games, movies and party games
        - casual lounge for card games and casual multiplayer games
        - small lounge for board games, puzzles and quieter games
        - private social room for RPGs or activities requiring concentration
        - main dining hall for occasional tournaments or whole crew meetings
        - library for chess, puzzles and other quiet games
        - Crew Quarters and personal domes for private media and gaming

#### Next Session:
    ♡ include Kitchen / Dining or Crew Quarter volumes in living.md