# Development Log:
I've been writing my thoughts and progress here as I go. It's kind of like a daily log, just not updated every day.

- this file is currently being organized - 


##  03/04/2026
    ♡ starting with atmosphere 
    
    ♡ going to be using Dalton's Law 

    ♡ researched net habitat volume per crew member (average minimum of 25m3 pp), and I'm happy with keeping the habitat size at 2000m3 (~66 m3 pp)
    

#### Next Session:
    ♡  continue with atmosphere



##      03/05/2026
    ♡ taking a couple of days for research

    ♡ considering adding humidity contribution (1-2kPa ppH2O)



##      03/08/2026
    ♡ resuming atmosphere creation with updated knowledge

    ♡ co2 was defaulting to zero, need to fix my scrubbing system

    ♡ today I learned that I needed to get the skeleton figured out and that it's okay to refine the numbers afterwards

#### Next Session:
    ♡ finish scrubbing function in engine.py



##      03/09/2026
    ♡ continuing where I left off with scrubbing

    ♡ NASA references: crew co2 production is around 1kg pp/day

    ♡ researched o2 regeneration and electrolysis with focus on Oxygen Generation Assembly (OGA), MOXIE like Solid Oxide Electrolysis (SOXE), and Sabatier co2 reduction + electrolysis

    ♡ making separate functions for managing and checking gases

    ♡ more research on 02 regen and electrolysis

    ♡ implementing very basic OGA o2 generation function for now (handling power usage, total pressure updates, hydrogen(h2) production and handling/venting later)  

#### Next Session:
    ♡ add total pressure update

    ♡ add the o2 regen to quick_test and state.py



##      03/10/2026
    ♡ renamed checking_gases function to gas_alerts, moved the co2 removal function to before o2_regen

    ♡ I know that chemistry ratios use moles, but I really wanted to stick to kPa and kilograms (kg) to avoid my code being more complex, so I'll figure out the conversions to avoid that

    ♡ made the scrubber unable to remove more co2 than exists, and changed the kPa values to move 4 decimal places instead of two, updated target based co2 and oxygen control, added target gases as global variables in engine.py

    ♡ adding in the hydrogen that the OGA electrolysis makes and venting it FOR NOW and will do research on how I can use it later on (Sabatier?)

    ♡ adding OGA byproduct function in, first calculating 23C to Kelvin b/cI read the gas pressure depends on temp (pressure drops if it goes down) 

#### Next Session:
    ♡ consider breaking down the long conversion in oga_byproduct into multiple lines of code with notes explaining each step for easier understanding
    
    ♡ vent the h2 later, store for now



##       03/11/2026
    ♡ learned it's important to document types of measurements as I go for conversions and future better understanding when both using and reading code

    ♡ adding measurements on the end of certain variable names, moved some of the variables from the oga_byproduct function to be global variables for referencing them later

    ♡ oga_byproduct is now oga_h2_byproduct with more lines of code, breaking down the process better

    ♡ going to refine notes later, for now keeping them pretty descriptive, adding some notes beside instead of above variables to see if it looks cleaner

#### Next Session:
    ♡ store h2 for now



##      03/13/2026
    ♡ figure out how much water(H2O) the OGA and water electrolysis uses every time it runs, I'm going to find the fixed reaction ratio instead of a fixed ratio b/c the amount of o2 produced are going to change depending on habitat events

    ♡ going to use 1000kg of water to start as a placeholder to finish the OGA functions

    ♡ going to keep the OGA functions seperate instead of one big function with a comment to sort of group them together, I feel like that will be better for future readability

    ♡ arranged some comments to be beside the line of code, I find if it's short, it does look cleaner

    ♡ finished OGA and water electrolysis for now, moving onto argon and nitrogen

#### Next Session:
    ♡ figure out variable numbers for the variables commented out at the top of engine.py
    
    ♡ add in when the ar or n2 will be used from storage    
    


##      03/14/2026

    ♡ I added the variable co2_stored_kpa to collect and temporarily store the co2 the amine bed scrubs until I use it later in my code

    ♡ decided on adding kg/kpa as global variables so when I need to access the stored gases, I can convert them more efficiently

#### Next Session:
    ♡ continue fixing variables, making sure the files are correct and finish adding Major Constituent Analyzer (mca) function and adding n2 to low pressure



##      03/15/2026
    ♡ finished maintenance

    ♡ continuing with mca, and adding another function to handle buffer gas

    ♡ I am aware that my alert function in engine.py is going to need more work but I will focus more on that after I have more of my code implemented (I feel like this is a good call)

#### Next Session:
    ♡ add what I need to add to the other files from the new function I made today to handle the buffer gas



##      03/17/2026
    ♡ yesterday I mapped out a better plan for the rest of my simulator, and I decided to clean it up as I go today.. I realize I made a lot of mistakes earlier, but I'm noticing them and fixing them now

    ♡ moving to temp management today and thermal control, I decided to get the main ideas down using radiators and do more research into other ideas later on

    ♡ cleaned up my code and moved the variables to the other files where they belong, and referenced them properly in engine.py

    ♡ while adding the temp variables to run_oga, I decided to rename a few variables to make reading/going over my code later easier and I also decided to make these functions more efficient overall

    ♡ I'm not sure if I already stated this, but the OGA is capped at 0.004 (for now) so that the OGA has to take its time to catch back up so that it doesn't run a huge amount of power and it seems unrealistic

    ♡ I decided to use a dictionary in the run_oga function to keep it more manageable and neat

    ♡ continuing to fix my code functions, and will remember to stay consistent with the names and structure moving forward

    ♡ really happy with my progress today and will continue implementing thermal control and temp management tomorrow

#### Next Session:
    ♡ thermal control and temp management




##      03/18/2026
    ♡ deciding if I should add heat output into current functions, or have its own. I'm going to keep adding to the proper functions

    ♡ adding heat produced by amine beds with exothermic absorption (the amine molecules catch the co2 which releases heat), and regeneration

    ♡ wrote a first version of a readme.md file and decided to make my project public today!

#### Next Session:
    ♡ consider turning functions with five or more returns into dictionaries and continue with thermal control and temp management



##      03/19/2026
    ♡ added dt_min to variables that change based on elapsed time in engine.py

    ♡ fixing the buffer gas control function so that it doesn't alter things from state directly and turning the return into a dictionary. I will probably end up using dictionaries for most of these as I go

#### Next Session:
    ♡ consider turning functions with five or more returns into dictionaries and continue with thermal control and temp management in run buffer gas



##      03/20/2026
    ♡ I'm making the amount of heat added a fixed amount for now

    ♡ added heat generation to buffer gas control function
#### Next Session:
    ♡ continue adding heat generation to functions and add radiators, lights, electronics/computers to their own functions



##      03/21/2026
    ♡ hand injury but working past it, going to add a light function where they dim at a certain time at night and also include how much heat the lights generate

    ♡ going to go with the crew getting around 8 hours of sleep/night so lights will dim at 9:30pm (21:30) and they will brighten at 6:00am, using level of brightness for now

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

    ♡ realizing that the file for the oxygen system has separate functions and the buffer gas file has one solid function, so I might end up breaking up that long function into a few smaller ones for readability and also b/c I will be adding more to this function

    ♡ broke up one long buffer gas system function into smaller ones for readability, organization, and future handling

#### Next Session:
    ♡ break up co2 scrubber system into different functions to match the other files and then add power usage, eventually continue lighting function and then continue adding heat generated/heat waste to new functions for electronics/computers, radiators, pumps, solar



##      03/28/2026
    ♡ making crew metabolism into its own file for organization and considering breaking it into smaller functions for quicker/easier readability as I add to the file

    ♡ breaking up the co2 scrubber system into different functions and adding heat, taking into consideration that I want there to be a baseline power per online bed like there is for heat, power usage used on actual co2 removed, emergency events, and full power loss (these last two will be handled later though)

    ♡ added power usage to co2 scrubber, updated engine and quick_test to work with the file properly

    ♡ added outputs to be printed so I can see that they are working properly

#### Next Session:
    ♡ work on water_system or power..



##      03/29/2026
    ♡ decided to start with power_system.py since I already started implementing these features in other functions and updated step in engine.py to include power/energy used for OGA and lights

    ♡ updated state variables file to include the new power variables I've been using from state and removed them out of the placeholder value section

    ♡ started solar function in power.py but I need to decide how many panels I want, so far for my habitat size, I think I'll choose.. 30-40 smaller panels to make maintenance and repair easier(?)

    ♡ I am going to model the solar panels in a similar way to the amine beds list, where I can have each panel have a status, how much a panel can make in direct 100% sunlight, its efficiency, amount of dust build up and just its overall condition for repair use when I get to that

    ♡ changing from my idea of 30-40 panels to 10 larger ones at least for V1, to avoid my code being messy and harder to manage

    ♡ ***while looking at the amine bed list, I'm not happy with how it's running right now b/c of how I hardcoded and pre-assigned the roles, when I actually want this to be a living working system, so before starting the solar power functions, I'm going to go back and try to fix that***

    ♡ I fixed a lot of my code today and added solar list of dictionaries, updated the amine list of dictionaries and made a crew metabolism dictionary, fixed some typos and learned a lot about organizing files, name consistency, code consistency, not going overboard too fast, and file setup

#### Next Session:
    ♡ work on power_system.py



##      03/30/2026
    ♡ starting by reviewing my code and I see some areas I need to fix b/c of the changes I made last night, starting with how my amine beds function



##      03/31/2026
    ♡ updated solar array list to not be hard coded online but start with all of them being on standby status and added a function to manage what ones are online with a new function in power_system.py



##      04/03/2026
    ♡ updated power_system.py and added a solar generation function and fixed the other no longer needed variables from the other files that had to do with solar power.

    ♡ using 0.50kw of sunlight for every 1 square meter (m2) for now, b/c my research showed that Mars sunlight is btwn 0.4 - 0.6 kw / 1 m2 during daytime

#### Next Session:
    ♡ work on power_system.py and figure out where I want daylight calculated (maybe state, or make a new separate file for handling calculating times of day, days and other related things)



##      04/04/2026
    ♡ while trying to come up with a way to make the daylight run smoothly and over time (instead of hardcoding with certain percentages), I learned what a sine wave is and I'm going to try to use that

    ♡ considering where to add a function for calculating daylight over time (power_system.py or in engine where it handles timestep math, or in its own file completely?)

    ♡ making a file for handling timesteps and related functions

    ♡ I learned today that instead of 24 hours, Mars time actually runs at 24 hours and 39 minutes and 35 seconds, not just 24 hours, so I'm going to fix that now, while I'm working on the new mars_time.py file

    ♡ added a better looking print function for a nicer console view while I work without a UI and kept the original print function commented out for when I want it plain again

#### Next Session:
    ♡ work on power_system.py: finish solar updates and figure out how to handle dust and efficiency, update power storage and figure out how to implement that



##      04/05/2026
    ♡ fixing the lighting function to not be hardcoded and to react and adjust to the level of daylight

    ♡ considering a file that will handle the light level, but so far I'm leaving it in engine, b/c I can't justify a file dedicated to just one function

    ♡ adding in the coordinates for the location of the habitat to make time passing and daylight and everything that goes along with that more accurate

    ♡ changed a ton in the mars_time.py file, I'm still figuring it out

#### Next Session:
    ♡ REMEMBER TO COMMIT MORE!!

    ♡ do more research and figure out mars_time.py, clean up step in engine.py



##      04/07/2026
    ♡ starting by reviewing my mars_time file

    ♡ added mars 24 hours time format

    ♡ added function to determine how the sun shifts from it's orbital position and hardcoded Mars' tilt to be 25.19 degrees

        **next session start:**
    ♡ do more research and figure out mars_time.py, clean up step in engine.py

#### Next Session:
    ♡ do more research and figure out mars_time.py, clean up step in engine.py



##      04/08/2026
    ♡ continuing to fix the time file and updated engine and quick_test.py

    ♡ fix light function and resume the solar power set up

    ♡ added function to calculate daylight and sunset times to determine the dyalight fraction for one sol

    ♡ cleaned up and updated mars_time.py and did some minor file organization with section headers

#### Next Session:
    ♡ fix light function and resume solar power set up



##      04/09/2026
    ♡ fixed variables in v1_state_variables.md and added / fixed section headers in other files

    ♡ fixed light function to work with daylight and sunlight logic

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

    ♡ added a seperate file for alerts that I will update more later on b/c it isn't really a priority right now

#### Next Session:
    ♡ print total power being used and a power priority system for when power is low and only runs essential power systems



##      04/11/2026
    ♡ moved alerts to it's own new file that included the status updates as well

#### Next Session:
    ♡ print total power being used and a power priority system for when power is low and only runs essential power systems



##      04/12/2026
    ♡ started importing power_alerts from power_system to the new alerts file, but very busy today

#### Next Session:
    ♡ print total power being used and a power priority system for when power is low and only runs essential power systems



##      04/13/2026
    ♡ going to add power info to print function

    ♡ fixed peak daylight today to reset for each sol

    ♡ I'm trying to decide if I should keep my lights function so it's controlling the brightness based off of it's own battery storage check, or move it to the function where it handles low power.. I'm leaning towards the latter

    ♡ moved it ^

    ♡ capped the min and max light level

#### Next Session:
    ♡ organize engine.py



##      04/14/2026
    ♡ starting by organizing engine.py

    ♡ I like how clean the dictionaries look in engine.py so I think if my returns return four or more variables, I'm going to make it into a dictionary (starting with power_system.py with lights and wellness lights)
    
    ♡ I cleaned up engine.py but quit pushing commits in the messy middle incase I had to undo everything I did anyway, but I got it sorted out and organized

    ♡ reviewing notes that I wrote and moving onto temp_system.py

    ♡ I'm going to focus on the thermal parts before considering humidity

    ♡ adding seasons to mars_time.py to help with my temp_system.py file

    ♡ I'm very happy with my progress today

    ♡ I'm realizing when I have the UI up and running, a lot of the systems that are being used are going to need to be mentioned in an update log

#### Next Session:
    ♡ fix new variables added (insulation and thermal mass)



##      04/15/2026
    ♡ fixed insulation and thermal mass values

    ♡ adding electric heaters and radiators, and I want to make both of them like I did some of the other systems with lists (amine beds, ect.)

#### Next Session:
    ♡ finish adding heat and cooling to power_system




##      04/16/2026
    ♡ continuing with radiator function

    ♡ going to change the way I have the radiators_online function set up b/c I don't like to hardcode the numbers like I did and I'm going to have a hysteresis so that my new setup doesn't turn on and off abruptly too often

    ♡ added radiator power usage and added radiator info to the other necessary files

    ♡ testing is running well

    ♡  still playing around with insulation values (0.3 - 0.8?)

#### Next Session:
    ♡ add heaters

    ♡ consider implementing two backup radiators



##      04/18/2026
    ♡ starting with my temp file

    ♡ I'm going to keep the radiators using the habitat temp directly to run, and focus on adding in the electric heaters until then

    ♡ I am going to worry about emergencies later and just get the foundation down first, but I did add another two radiators to the radiator list

    ♡ making heaters their own list to be handled the same way the other systems are

    ♡ added thermal alerts to alerts file... still not really focused on alerts, but there are some that will actually be helpful with printing now mostly for debugging

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
    ♡ going back to co2_scrubber_system and changing hardcoding to calculations

    ♡ adding sunlight to the thermal system

    ♡ I realize that I should be making things change and come from state directly, not so many other things, so before starting water_system.py I'm going to do a complete refactor

    ♡ fixed time, solar and daylight update in step and renamed new state variable to NEW_STATE in caps to make it easier to see while I fix some parts of step

    ♡ finished updating the new state in step, so it's lowercase now and just fixing some layout issues (making long function signatures extend vertically, but I'm not sure I like the way this looks)

    ♡ considering changing my repetitive functions to be one function that switches modes based on different things ( VERY UNSURE ), but for now I will continue to keep doing this as I've been doing it

#### Next Session:
    ♡ -work on water_system.py



##      04/22/2026
    ♡ doing some research before starting water_system.py to know what kind of water system makes sense with focus on reusability

    ♡ going with:
        -Urine Processor Assembly (UPA)
        -Water Processor Assembly (WPA)
        -Brine Processor Assembly (BPA)

    ♡ worked on the water system file

    ♡ I read about In-Situ Resource Utilization (ISRU) to extract water locally but I'll worry about that later

#### Next Session:
    ♡ continue working on water_system.py:
        - add new results to print function
        - add condensate
        - change oga to use water usage from water_system file, and remove its own storage variable
        - don't forget about the CHX



##      04/23/2026
    ♡ adding condensate/CHX to water_system and engine, and made OGA use potable water

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

        - scheduled cleaning, although I like the idea of the crew having one less thing to worry about and maintain, if it can be done on it's own
        
        - dust repellent coatings for sure that will need to be redone over a certain amount of times(?)

    ♡ started adding back up radiators and heaters

    ♡ started file for handling dust

#### Next Session:
    ♡ fix amine beds to show up as online



##      04/25/2026
    ♡ amine beds to show up as online

    ♡ updated CHX to include cooling

    ♡ updated solar arrays list and function to run on how much charge the batteries need

    ♡ updated amine beds to come online with how much co2 is needed, I used two different hysteresis for that

    ♡ updating a lot of variables for systems handling lists now that I've changed some logic to be a bit more complex

#### Next Session:
    ♡ go through files and update everything using state (starting with thermal) and clean up inconsistencies



##      04/26/2026
    ♡ connecting files to state more directly

    ♡ figuring out how to reduce outputs in engine, while still keeping it

    ♡ started turning files into separate dictionaries to reduce the massive outputs dict in engine.py, started with water, working on temp

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

    ♡ lot's of whiteboard notes, and new considerations regarding handling gases and future dust and other events

    ♡ created a new file for the Sabatier

    ♡ changed the targets for n2 and ar and the target pressure to 65.0kpa (which it should have been this whole time, I accidentally had it at 60.0kpa)

#### Next Session:
    ♡ start file for Sabatier



##      04/29/2026
    ♡ starting file for Sabatier

    ♡ sorted v1_scope file into a to do file and dev_log b/c everything together was getting messy, hard to look back on, and way too long

    ♡ learning that I like consistency and how important it is, and that it's okay to refactor and organize.. my next project I will be more prepared


#### Next Session:
    ♡ turn seasons into a list

    ♡ turn on alerts for min and max safe targets and make crew alerts react to them (i.e "some of the crew members are starting to report headaches")

    ♡ go over all variables in state, add or remove things for consistency and organize them better (eventually)


##      04/30/2026
    ♡ sorted through creation notes and finished seperating things into their own files 

    ♡ updated OGA logic, by removing the pa conversation at all and made r for the universal gas constant in kpa instead

    ♡ I am going to keep h2 stored in kg and also I'm going to make the methane(ch4) storage to be in kg b/c these are being treated as resources, and I read that the Sabatier uses mass ratios, not pressure ratios

    ♡ if I need to convert them at any time, I'll just use the conversion and put it up as a constant in the file

    ♡ resuming Sabatier file

    ♡ using a hysteresis to avoid jumpy on and off reactions

    ♡ reactions_available is how many times stoichiometric reaction can happen with a ratio of 1 co2 : 4 h2

    ♡ I realize I actually put the mode decision in the main function for running the sabatier and also the OGA actually, and I didn't in the other files. I've been changing things and upgrading how I'm doing things so eventually I will need to go through all of the files that I worked on first.

    ♡ waiting to do that though ^ b/c refactoring and editing has taken up enough time for the time being, and I want to focus on getting some main systemsfigured out. 

    ♡ I thought adding a little bit of a leak while venting the ch4 was realistic, so I might add this to the other systems that vent

#### Next Session:
    ♡ get back to the Sabatier file with power and heat produced fixed

    ♡ figure out what to put gases at in quick_test for starting values

    ♡ figure out values for new commented out variables in state and quick_test, and if I really even need them
    
    ♡ add a little bit of a leak while venting


##      05/01/2026
    ♡ added sabatier outputs and updates into engine.py and fixed variables for ch4 where I accidentally put kpa insted or kg

    ♡ code is running again

#### Next Session:
    ♡ update print to show sabatier information

    ♡ get back to the Sabatier file with power and heat produced fixed

    ♡ figure out what to put gases at in quick_test for starting values

    ♡ figure out values for new commented out variables in state and quick_test, and if I really even need them
    
    ♡ add a little bit of a leak while venting


##      05/03/2026
    ♡ updating print to show sabatier information

    ♡ I decided to track gases in the atmosphere in kpa, and h2 and ch4 in kg for storage, and I'm not 100% sure about the other ones yet

    ♡ going to keep things consistent: kg for storage, kpa for atmosphere

    ♡ adding variables for each gas to have a base leak rate, to use for venting and other things (using individual ones b/c some leak faster than others)

#### Next Session:

    ♡ get back to the Sabatier file with power and heat produced fixed

    ♡ figure out what to put gases at in quick_test for starting values

    ♡ figure out values for new commented out variables in state and quick_test, and if I really even need them
    
    ♡ add a little bit of a leak while venting


##      05/05/2026
    ♡ working on co2_scrubber_system.py making the logic closer to the sabatier and other systems logic

    ♡ considering adding a file for handling helper logic, to make things like handling primary systems and stuff before backups

    ♡ updated current systems to return output and update dicts, and updated engine.py to accommodate that

    ♡ I realized that I have been wasting a lot of time refactoring and trying to keep my files consistent, which I'm sure is a good thing later on, but for now there's a lot to be done so I'm going to switch focus a

#### Next Session:
    ♡ finish updating current systems to return output and update dicts, and updated engine.py to accommodate that, left off on oga and getting the code to run, pick back up tomorrow, and fix printing issues


##      05/06/2026
    ♡ finished updating current systems to return output and update dicts, and updated engine.py to accommodate that

    ♡ I need to look over mars_time.py and go over that logic again, but I might wait until I get the greenhouse and other systems set up

    ♡ I haven't decided if the greenhouse will be easier to implement after or before I update the mars_time..

    ♡ updated mars_time file

#### Next Session:
    ♡ start focusing on greenhouse variables and systems needed, starting with light for the greenhouse


##      05/08/2026
    ♡ updated README.md and renamed a lot of files today

    ♡ start focusing on greenhouse variables and systems needed, starting with light for the greenhouse

    ♡ going with a hydroponic set up, I updated v1_scope to include all my notes about a greenhouse 

    ♡ going to add to my habitat size after I have the greenhouse set up, so for now I'm going to treat it as if it is a seperate building, running on all the same systems

    ♡ I like the idea of the plants having a set percentage of sunlight that is let in, so even if it's low they're still getting at least a good portion of what IS available, but I'm not entirely sure I'll stick with 70

    ♡ trying to set up my file so that it will be easy to incorporate changing seasons and days without sunlight, ect.

    ♡ reconsidering my modes being two seperate words instead of snake case?

#### Next Session:
    ♡ continue greenhouse 
 

 ##      05/09/2026
     ♡ reasearch for plants and nutrition (I updated notes in v1_scope.md)

    ♡ I'm going to make a list for the different plants, to keep it simple, I'm not going to have a list for each seperate plant, instead I'm going to go by plant area

    ♡ adding plant list to state, I want to take how much spacing the plants need into consideration

    ♡ this isn't a greenhouse simulator it's a mars habitat simulator, so it doesn't need to be as complex as it could be

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
    ♡ adding in hydroponics to the greenhouse list, and starting from greenhouse lighting to make the greenhouse file be how I want it to be

    ♡ I didn't want the multipliers in the constants like some other files, b/c they are different for each zone 

    ♡ I connected the new greenhouse variables and logic to the other files

#### Next Session:
    ♡ continue greenhouse



##      05/14/2026
    ♡ less focused on matching files, and more focused on accurate logic now

    ♡ going over all of my files and checking logic and structure before moving on

    ♡ I update all of my files and figured out my units of measurements, b/c I accidentally mixed up kpa being companred and usd with kg, ect.

    ♡ I'm going to change the modes in each file to be snake case 

    ♡ updating alerts.py and I'm going to move humidity and thermal alerts there as well

    ♡ I updated my todo.md file and v1_state_variables file

    ♡ going to add in the gas leak logic so the variables are actually getting used so I can delete the vague universal gas leak per hour variable

    ♡ adding gas_leak.py file to handle that ^

#### Next Session:
    ♡ go over my numbers and targets


##      05/15/2026
    ♡ I'm going to go over my variable values in quick_test/state to make sure my numbers are where I want them, I realize I've changed a few things as I went while testing and using different research, so this seems like a good place to start

    ♡ considering making my habitat a bit bigger.. I was aiming for ~67m3, but I'm second guessing this when I focus on the fact that this is a long term, no resupply simulation

    ♡ increasing habitat size by 20%

    ♡ Today I started considering spatial realism

#### Next Session:

    ♡ review current variables, check numbers, evaluate my plaeholders and review my targets


##      05/16/2026
     ♡  while going over the total habitat volume in m3, I'm thinking that the crew can live with smaller living quarters and I'm going to make the greenhouse a bit bigger because it is crucial for long term survival, and I'm considering storage areas being a bit bigger as well..

    ♡ I was reading about how much room a person typically needs per person for psychological wellbeing. I read it was 300m2 pp but that seems really unrealistic for Mars

    ♡ research on the height requirements for ideal psychological wellbeing vertically, people seem to do better with "void" spaces (taller living areas), but also considering that I can't have an unrealistically tall habitat, so I keep trying to go for the minimum for psychological wellbeing long-term so I'm going with .. 4m? maybe.. 3.8 (though the habitat would need to be partially buried, but I'm not simulating structural engineering right now)    

    ♡ I'm also reading about the thickness that a Mars habitat would have to be, with a focus on protection from radiation depending on materials used. I'm trying to figure out where the line is between believable Mars habitat, and overcomplicating my entire simulation.. For now I'm going to choose some loose numbers and estimates and continue

    ♡ I'm only going to focus on the variables that I currently have and make sure I'm happy with the numbers and targets and I'll consider spatial realism more later

    ♡ I'm updating the measurements and variables for the greenhouse now that I made it bigger. I want to optimize the space in the greenhouse

    ♡ considering looking at species that make their own structures and systems as inspiration for efficiency

    ♡ Taking the layout into consideration, hydroponics lets me consider other greenhouse layout ideas, so I'm leaning toward a sort of "helix" .. hive, area instead. A layered growing space that spirals inward toward a main central area for utilities, maintenance, water systems, and other things instead of just rows and boxes.

    ♡ I also think it would be easier to visually see/monitor a lot more plants along a gradual slope instead of separate rectangular flat rows and it would potentially work well with the vertical racks and hangers like I wanted.

    ♡ As far as the quick_test file goes, as of right now, it's messy and I will clean it up soon, and the variables won't be printed to so many floating point decimals on the UI, it's mostly for debugging and making sure everything is working as it should

#### Next Session:
    ♡ make a file for debugging, so I can see my outputs closer together per subsystem instead of going through every subsystem every run    


##      05/18/2026
    ♡ instead of making a seperate file for debugging I decided to just temporarily comment out my already set up print function to isolate each susbystem so I can check and see if they're working as I want them to work

    ♡ today I'm going over all of my subsystems and systems to see if they're all behaving and fixing any problems before moving on
    
    ♡ I do want to have the greenhouse capable of raising the o2 in the habitat b/c with my hexagon/hive idea for the structure, everything is close together, without seperate buildings so it just makes sense to me that it would be a factor 

#### Next Session:
    ♡ continue running system checks


##      05/20/2026
    ♡ still going over my values and testing, but I added handling excess o2 to the oxygen.py file

    ♡ while going over the results from each subsystem, I'm realizing that co2 is not being handled right.. I need to fix where the Sabatier is getting it's co2 amount from

    ♡ I made some changes to the Sabatier file and ran a few test for four sols, getting an update every 5 hours while only getting the sol, time and atmosphere info.. co2 is much better, but there are still issues with the buffer gas, as well as a few other things, that I will be working towards fixing

    ♡ I made some changes to buffer gas, double check them tomorrow    

#### Next Session:
    ♡ check out buffer gas (pressure is low but not changing properly) and then continue running system checks


##      05/22/2026
    ♡ I added in the Sabatier into water.py, b/c I forgot to add it in the storage update and run_water_system function 

    ♡ while testing the water outputs, I can see that the net loss per sol is way too high, so I'm going to go over some numbers

    ♡ 115.5kg per sol is just the cost of having a 30 person crew

    ♡ I was thinking about other way to recycle and actually get water and I thought about piercing through the surface with two or three heated pipes that siphon up some frozen mars water every so often? retractable pipes so they don't freeze and can be used at will, I'm going to do some reasearch on this

    ♡ going back to In-Situ Resource Utilization (ISRU) to extract water locally, I'm thinking piercing through the surface with two or three heated pipes that siphon up some frozen mars water every so often with retractable pipes so they don't freeze and can be used when wanted and needed to avoid environmental factors

#### Next Session:
    ♡ start new file for water isru


##      05/23/2026
    ♡ I created a file for handling water extraction and I'm going to make a list in state, similar to the lists I have for the other subsystems and add in each pipe, incase I want to add more later, and of course to have a few as backup

    ♡ I realized that I didn't have water runoff from the greenhouse, so I implemented that today and also fixed and cleaned up water.py, after including the for now very basic isru system

#### Next Session:
    ♡ add new variables in engine and update irsu to include pipe retracting and extracting, dust buildup per pipe, efficency loss, ect.
    
    ♡ include isru to systems in README.md


##      05/24/2026
    ♡ adding in new variables in engine for greenhouse runoff and also water isru

    ♡ added water isru subsystem to readme


#### Next Session:
    ♡ fix irsu file


##      05/25/2026
    ♡ fixing isru and added modes, and pipe retraction and extraction

    ♡ going over water file, adding hysteresis and updating power used logic to make it more similar to co2_scrub.py

    ♡ updated power usage in water.py

    ♡ updating systems to include low power mode

    ♡ fixed venting logic in oxygen.py

#### Next Session:
    ♡ go over vent logic in each file


##      05/27/2026
    ♡ adding vent leaks to buffer_gas.py

    ♡ I know that turning buffer_gas.py into basically one long code might be different to read, but I think it works with my section headers keeping things organized and hopefully easy to read, I'm also hoping this keeps things a bit neater when it comes to ouputs and variables and such

    ♡ two file refactors today

#### Next Session:
    ♡ break up starting variables and print

    ♡ test terminal output to adjust numbers!


##      05/28/2026
    ♡ seperating files for print and Habitat State

    ♡ this new print file is going to be made with debugging and checking numbers in mind, it will not be organized this way for the actual UI

    ♡ went over output variable names and make them consistent (added, produced, recovered, proccessed, etc)

  ♡ huge refactor day!

#### Next Session:
    ♡ make summary print function for each category for debugging, or decide if I'm just going to comment out each one when I want to isolate the subsystems/categories

    ♡ test terminal output to adjust numbers!


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
    ♡ fixing my print step in quick_test.py to actually print the current sol, and running my test for the longest time yet (40 sols)

    ♡ Around sol 43, the battery runs too low


##      06/14/2026
    ♡ fixing temp issues, starting with the insulation strength/thermal mass and fixing my heater logic


##      06/16/2026
    ♡ fixing radiator and heaters to make things smooth and effective

    ♡ I'm happy with how the temp system is running for now, so now I'm running atmosphere again

    ♡ fixing buffer gas

#### Next Session:
    ♡ continue running system checks and fix co2_scrub.py


##      06/17/2026
    ♡ going over co2_scrub because yesterday I noticed

    ♡ I'm starting to consider UI notes, I think it's a good idea to set that up before trying to train an AI so my sim is at least visually entertaining for someone running it. I'm trying to decide what to use for this but so far I'm considering porting to JavaScript and then using HTML, CSS


##      06/19/2026
    ♡ fixing my sabatier file, made the methane go aove the safe limit, so I'm going to see what I can do with the methane storage and venting 

    ♡ I decided to make sure all c4 is either vented immediately or sent to storage, it's not goin to be added into the cabin atmosphere

    ♡ I fixed the sabatier call in engine.py

    ♡ I noticed my greenhouse is currently producting 75x MORE o2 than my crew of 30  mean, and this is absolutely not right, it doesn't make any sense so I need to fix this

    ♡ the math for zone info:
    structural: 0.022 kPa/m2/sol × 90 m2  = 1.98 kPa/sol
    container:  0.020 kPa/m2/sol × 110 m2 = 2.20 kPa/sol
    rack:       0.015 kPa/m2/sol × 124 m2 = 1.86 kPa/sol
    total ≈ 6.04 kPa/sol

    ♡ the math for crew o2 demand:
    0.00011 kPa/hr × 30 crew × ~24.66 hr/sol ≈ 0.081 kPa/sol

    ♡ I'm going to chose that the greenhouse actually produce only 2% of the crew o2 and co2 needs


##      06/20/2026
    ♡ setting up ISRU file for Ar and N2, which is crucial for no resupply with a con being power usage

    ♡ I am not going to have a timer for the compressors yet, but for future versions I am planning on adding a regen state and usig absorption/sorbent beds that need a regen cycle between intakes

#### Next Session:
    ♡ add isru_atm to power, bugger gas, and other gas handling files and update isru_outputs and updates to include 'water'


##      06/21/2026
    ♡ I decided I'm going to add the sorbent beds to the isru_atm file before continueing to connect it to the other files

    ♡ don't forget to add isru_water to dust file

    ♡ I'm going to use five sorbent beds in total, two as backups as I like to have, so there are enough to absorb while another bed regenerates

    ♡ sorbent beds trap CO2 from compressed Mars air before N2/Ar and gets added to storage. This is modeled as a swing bed cycle, like the amine beds in co2_scrub.py.

    ♡ regen stop processing taking that bed fully offline, fewer adsorbing beds online = less raw atmosphere gets processed, meaning less N2 and Ar gets added to storage too

    ♡ unlike isru water pipes that have a real physical deploy/retract travel time, a compressor has no mechanical delay, so it just flips between "offline" and "extracting" based on target amount needed online for each step

#### Next Session:
    ♡ continue isru_atm.py file


##      06/23/2026
    ♡ continuing isru_atm.py file

#### Next Session:
    ♡ add dust to isru_atm.py and isru_water.py


##      06/24/2026
    ♡ adding dust to irsu_water.py

    ♡ fixing the variables in print to work with the update greenhouse file


##      06/25/2026
    ♡ starting to work on the UI, using a prototype image I designed in procreate, this will be updated, but the first step is turning my code written in python to json

   ♡ added ui_export and started on the visuals

#### Next Session:
    ♡ continue working on dashboard panels


##      06/28/2026
    ♡ I've been working on the visuals so there hasn't been a to log here

    ♡ I am going to make this so that the dashbaord updates every three seconds to start, and I'll adjust this as I go

    ♡ I want to use snake case for js, but I know camelCase is best practice, so I'll stick with that


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
    ♡ lots of changes to make to the dashboard including addin two more screens, one for the greenhouse and one for the habitat log, so status and alerts can move to the log, and it will update with any complaints from the crew about symptoms from pressure or hunger, ect. and if the system needs to do anything in states of emergency


##      07/08/2026
    ♡ I worked on the dashboard image and added a new palle, as well as angled some screens for better readability, as well as making some other layout changes


##      07/10/2026
    ♡ I did some perspective updates with the dashboard image and I still need to add more screens for crew and mission log, and fix the image more, the three uploaded are only prototype images


##      07/12/2026
    ♡ the last few days have been refining my layout image and deciding on panel amount and also panel placement

    ♡ I decided I'm going to add a panel for the crew information on one side of the status panel and a panel for the alerts on the other side

    ♡ I'm going to be adding crew scheduling, maintenance, and a few updates, with any complaints or any positive feedback from the crew when things are running well

    ♡ I added to the todo list with update alerts to include things like stats evening out (co2 returned to normal range, etc.), buffer gas injections complete, isru pipes retracted, isru pipes deployed
    
#### Next Session: 
    ♡ decide if the middle panel is actually gong to be a mission log and decide what will be split between the mission log updates and the alerts section


##      07/14/2026
    ♡ creating event.py for the mission/event log file, I want to only show the last 50-100 latest events 


##      07/16/2026
    ♡ I broke my ISRU panels up into two seperate panels, I would like to keep the atmosphere things together, I think

    ♡ I'm going to implement seasons into my sim before adding anything else. After doing some research I realized that I had my get_season_angle_deg wrong, because Mars doesn't move around the Sun at a constant speed moving faster near perihelion and slower near aphelion, which affects seasonal timing, dust storm season, solar energy and some of the other systems I have set up
    
    ♡ Reading about Kepler's equation:

    M = E − e sin(E)

    M = Mean Anomaly
    E = Eccentric Anomaly
    e = Orbital Eccentricity

    ♡ I'm considering the options I have for this.. there's the Newton Raphson for eccentric anomaly E. Starting with E = M, each iteration calculates the current wrong answer and divides it by the 'slope' for a better estimate:
    
    new estimate = old estimate - error / slope
    
    ♡ The other option is fixed-point iteration, which rearranges Kepler's equation into:

    E = M + e sin(E)

    But that seems very... inefficient.
   
    ♡ the eccentricity for Mars is low, so this shouldn't take too many tries to get close using Newton Raphson 

    ♡ anomaly = the angular distance from it's last perihelion


##      07/18/2026
    ♡ finished adding seasons

    ♡ I'm reading about atmospheric opactiy, and tau (how much sunlight the atmosphere blocks before it reaches the ground and optical depth being tau the number used to use the amount), low: 0.2 - 0.5, medium: 0.8 - 1.5 for dusty skies and high:  2 - 5 for major dust storms, these are related to seasons so I figured it was a good next step


##      07/20/2026
    ♡ I wanted to have a percentage of how far Mar's is through it's storm season

    ♡ I'm going to add random dust storms right now, while I'm working on season changes and atmospheric opacity, checking if Mar's is in storm season, how far through it it is, and also have random wheather b/c predictable wheather is not realistic

    ♡ roll_for_storm is both accurate and a nod to dnd

    ♡ I find myself getting more used to python now and getting more comfortable doing things that I was worried I wouldn't understand later, like not wanting to return before the end of the function, adding more lines of code which isn't neccessary, I am looking back at my older code and seeing where it can be improved, which seems like a big milestone

    ♡ I need to start considering the ways this simulation can go wrong before I get there

    ♡ the storm opacity is going to be hardcoded for V1
    