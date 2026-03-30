# Project name: MarsHSim (will eventually change this)

## Sim loop: time steps

### V1 goal: 
    -closed loop ECLSS monitoring, logging, alerts, simple controllers

### V2 goal: 
    -AI autonomy, predictive control, fault detection

### No resupply assumption: 
    -finite buffers and recycling efficiency matter

#### Time model:

    -Default timestep: 5 minutes
  
    -Engine uses configurable delta time(dt) (supported timesteps will be: 1, 5, 10, 30 min)

    -Adaptive dt allowed during events (automatically reduces the timestep to 1 min, during critical events)

    -Track mission time in seconds internally, and converted to Mars sol and local time for display

#### Creation notes: 
        
        03/04/2026
    -Wanting to keep lower pressure (~65 kilopascals (kPa) target) in habitat to make leaks not as catastrophic, and deciding to add argon as a buffer gas

    -30 crew members to hint at an early colony with a habitat size of 2000 cubic meters (m3)

    -going to be using Dalton's Law



        03/05/2026
    -considering adding humidity contribution (1-2kPa ppH2O)

    -researched net habitat volume per crew member (average minimum of 25m3 pp), and I'm happy with keeping the habitat size at 2000m3 (~66 m3 pp)

    -wanting to keep the habitat temp between 22-24C ideally

    -taking seasons on Mars into consideration (how many sols, winter lows ~-140C, summer highs ~20C, 25% yearly atmosphere pressure changes from CO2 freezing and sublimating at the poles, dune migration, albedo changes from ice/dust, dust storms in the spring/summer while global storms can engulf the whole planet)

    -global dust storms can drop temp averages between 10-20C for a little while

    -N spring/S fall 194 sols, average temp:  
    -N summer/S winter: 178 sols, average temp:
    -N fall/S spring 142 sols, average temp:
    -N winter/S summer 154 sols, average temp: 
    (I am going off of approximate surface temp daily averages for mid-latitude from NASA missions)



        03/08/2026
    -resuming atmosphere creation with more and updated knowledge

    -tracking partial pressure changes per timestep instead of mass: 
    
    -O2 drop: 
    ~0.0033kPa pp/5min
    -288 five minute intervals in one day
    ~0.0033 * 288 = 0.9504kPa pp/day
    -30 crew members
    ~0.0033 * 30 = 0.099kPa/5min

    CO2 rise: 
    ~0.0029kPa pp/5min
    ~0.0029 * 288 = 0.8352 kPa pp/day
    ~0.0029 * 30 = 0.087kPa/5min

    -including two amine swing bed scrubbers as part of making energy efficiency and waste reduction/recycling priorities, they aren't too expensive, and this will help with humidity removal

    -including two more beds as backup, deciding to make them a list so when I add more features they will be easier to access

    -co2 was defaulting to zero, need to fix my scrubbing system

    -today I learned that I needed to get the skeleton figured out and that it's okay to refine the numbers afterwards

    -tomorrow finishing scrubbing function in engine.py



        03/09/2026
    -continuing where I left off with scrubbing

    -NASA references: crew co2 production is around 1kg pp/day

    -making separate functions for managing and checking gases

    -researched o2 regeneration and electrolysis with focus on Oxygen Generation Assembly (OGA), MOXIE-like Solid Oxide Electrolysis (SOXE), and Sabatier co2 reduction + electrolysis

    -implementing very basic OGA o2 generation function for now (handling power usage, total pressure updates, hydrogen(h2) production and handling/venting later)  
    
    Pros: reliable, efficient, works well with amine beds and humidity considerations, low power usage at ~5-10kW, ~500-800kg hardware

    Cons: requires water (not really a huge con b/c recycling is a main priority), produces hydrogen (could use Sabatier or vent)

         **next session start:**
    -adding total pressure update tomorrow, remember to add the o2 regen to quick_test and state.py tomorrow, also starting this little part at the end of my notes



        03/10/2026
    -renamed checking_gases function to gas_alerts, moved the co2 removal function to before o2_regen

    -made the scrubber unable to remove more co2 than exists, and changed the kPa values to move 4 decimal places instead of two, updated target based co2 and oxygen control, added target gases as global variables in engine.py

    -adding in the hydrogen that the OGA electrolysis makes and venting it -FOR NOW- and will do research on how I can use it later on (Sabatier?)

    -adding OGA byproduct function in, first calculating 23C to Kelvin because I read the gas pressure depends on temp (pressure drops if it goes down) 

    -I know that chemistry ratios use moles, but I really wanted to stick to kPa and kilograms (kg) to avoid my code being more complex, so I'll figure out the conversions to avoid that

    -h2_kg = (2 * o2_added_pa * hab_vol_m3 * 2.016) / (r * temp_k * 1000)
    
    -2.016 b/c h2 gas = two h2 atoms bonded, one h2 atom = 1.008 mol, h2 = 1.008 + 1.008 = 2.016mol
    
    -convert h2 mol to g, convert g to kg 

       **next session start:**
    -consider breaking down the long conversion in oga_byproduct into multiple lines of code with notes explaining each step for easier understanding, vent the h2



        03/11/2026
    -learned it's important to document types of measurements as I go for conversions and future better understanding when both using and reading code

    -adding measurements on the end of certain variable names, moved some of the variables from the oga_byproduct function to be global variables for referencing them later

    -oga_byproduct is now oga_h2_byproduct with more lines of code, breaking down the process better

    -going to refine notes later, for now keeping them pretty descriptive, adding some notes beside variables to see if it looks cleaner

    -instead of venting, I'm going to store the h2
    


         03/13/2026
    -going to use 1000kg of water to start as a placeholder to finish the OGA functions

    -to figure out how much water(H2O) the OGA and water electrolysis uses every time it runs, I'm going to find the fixed reaction ratio instead of a fixed ratio b/c the amount of o2 produced are going to change depending on habitat events

    -ratio in kg is:  1.125kg of H2O per 1kg of O2 produced

    -I'm going to keep the OGA functions seperate instead of one big function with a comment to sort of group them together, I feel like that will be better for future readability

    -arranged some comments to be beside the line of code, I find if it's short, it does look cleaner

    -finished OGA and water electrolysis for now, moving onto argon and nitrogen 

        **next session start:**
    -figure out variable numbers for the variables commented out at the top of engine.py, add in when the ar or n2 will be used from storage    
    


        03/14/2026
    -I added the variable co2_stored_kpa to collect and temporarily store the co2 the amine bed scrubs until I use it later in my code 
    
    -decided on adding kg/kpa as global variables so when I need to access the stored gases, I can convert them more efficiently 

        **next session start:**
    -continue fixing variables, making sure the files are correct and finish adding Major Constituent Analyzer (mca) function and adding n2 to low pressure



        03/15/2026
    -finished maintenance

    -continuing with mca, and adding another function to handle buffer gas

    -I am aware that my alert function in engine.py is going to need more work but I will focus more on that after I have more of my code implemented (I feel like this is a good call)

         **next session start:**
    -add what I need to add to the other files from the new function I made today to handle the buffer gas



        03/17/2026
    -yesterday I mapped out a better plan for the rest of my simulator, and I decided to clean it up as I go today..I realize I made a lot of mistakes earlier, but I'm noticing them and fixing them now

    -moving to temp management today and thermal control, I decided to get the main ideas down using radiators and do more research into other ideas later on

    -cleaned up my code and moved the variables to the other files where they belong, and referenced them properly in engine.py

    -going to use kilowatts (kW) for heat sources (kW = change) (C = result)

    -while adding the temp variables to run_oga, I decided to rename a few variables to make reading/going over my code later easier and I also decided to make these functions more efficient overall

    -I'm not sure if I already stated this, but the OGA is capped at 0.004 (for now) so that the OGA has to take its time to catch back up so that it doesn't run a huge amount of power and it seems unrealistic

    -I decided to use a dictionary in the run_oga function to keep it more manageable and neat

    -continuing to fix my code functions, and will remember to stay consistent with the names and structure moving forward

    -really happy with my progress today and will continue implementing thermal control and temp management tomorrow

        **next session start:**
    -thermal control and temp management



        03/18/2026
    -deciding if I should add heat output into current functions, or have its own. I'm going to keep adding to the proper functions

    -adding heat produced by amine beds with exothermic absorption (the amine molecules catch the CO2 which releases heat), and regeneration

    -wrote a first version of a readme.md file and decided to make my project public today

        **next session start:**
    -consider turning functions with five or more returns into dictionaries and continue with thermal control and temp management



        03/19/2026
    -added dt_min to variables that change based on elapsed time in engine.py

    -fixing the buffer gas control function so that it doesn't alter things from state directly and turning the return into a dictionary. I will probably end up using dictionaries for most of these as I go

        **next session start:**
    -consider turning functions with five or more returns into dictionaries and continue with thermal control and temp management in run buffer gas



        03/20/2026
    -I'm making the amount of heat added a fixed amount for now

    -added heat generation to buffer gas control function

        **next session start:**
    -continue adding heat generation to functions and add radiators, lights, electronics/computers to their own functions



        03/21/2026
    -hand injury but working past it, going to add a light function where they dim at a certain time at night and also include how much heat the lights generate

    -going to go with the crew getting around 8 hours of sleep/night so lights will dim at 9:30pm (21:30) and they will brighten at 6:00am, using level of brightness for now

    -remember: mission_time_s = current time of day, dt_min = how long the step lasts, hours_per_step = scaling, production, etc

    -considering moving the time conversion logic out of quick_test into engine, or into its own file to handle all timestep info because eventually it will be interactive

    -considering adding separate helper files for handling certain things separately like one for amine scrubbers, OGA, etc after adding more code

        **next session start:**
    -continue adding heat generation to lights and add electronics/computers, radiators to their own functions, reconsider lighting variable names



        03/24/2026
    -since I want to have solar, I'm going to need to have a huge battery storage for when there are dust storms and other impacting factors (I still have an injury, I am doing small blocks of code at a time) so I'll make the battery capacity 4000.0 kWh for now

    -I chose the starting amounts for some power variables and made a separate file for the OGA and water electrolysis

    -added power consumed to lights function

        **next session start:**
    -continue lighting function and then continue adding heat generated/heat waste to new functions for electronics/computers, radiators, pumps, solar and need to update step in engine.py to call the run_oga function properly now



        03/26/2026
    -added some power consumption variables to oxygen_system.py

    -adding files for separate logic systems

    -for the mca function, I decided to not use state so I can manage/calculate both before and after control

    -realizing that the file for the oxygen system has separate functions and the buffer gas file has one solid function, so I might end up breaking up that long function into a few smaller ones for readability and also because I will be adding more to this function

    -broke up one long buffer gas system function into smaller ones for readability, organization and future handling

        **next session start:**
    -break up co2 scrubber system into different functions to match the other files and then add power usage, eventually continue lighting function and then continue adding heat generated/heat waste to new functions for electronics/computers, radiators, pumps, solar



        03/28/2026
    -making crew metabolism into its own file for organization and considering breaking it into smaller functions for quicker/easier readability as I add to the file

    -breaking up the co2 scrubber system into different functions and adding heat, taking into consideration that I want there to be a baseline power per online bed like there is for heat, power usage used on actual co2 removed, emergency events, and full power loss (these last two will be handled later though)

    -added power usage to co2 scrubber, updated engine and quick_test to work with the file properly

    -added outputs to be printed so I can see that they are working properly

        **next session start:**
    -work on water_system
    -eventually... lighting function and then continue adding heat generated/heat waste to new functions for electronics/computers, radiators, pumps, solar



        03/28/2026
    -decided to start with power_system.py since I already started implementing these features in other functions and updated step in engine.py to include power/energy used for OGA and lights

    -updated state variables file to include the new power variables I've been using from state and removed them out of the placeholder value section

    -started solar function in power.py but I need to decide how many panels I want, so far for my habitat size, I think I'll choose.. 30-40 smaller panels to make maintenance and repair easier(?)

    -I am going to model the solar panels in a similar way to the amine beds list, where I can have each panel have a status, how much a panel can make in direct 100% sunlight, its efficiency, amount of dust build up and just its overall condition for repair use when I get to that

    -changing from my idea of 30-40 panels to 10 larger ones at least for V1, to avoid my code being messy and harder to manage

    -**while looking at the amine bed list, I'm not happy with how it's running right now because of how I hardcoded and pre-assigned the roles, when I actually want this to be a living working system, so before starting the solar power functions, I'm going to go back and try to fix that**

    -side note: I thought about having panels on the outside of my habitat that are foil on one side and black on the other (like a car window shield), that could be flipped like a billboard (one of the ones that have two images on them and they flip to reveal the other image)

    -I fixed a lot of my code today and added solar list of dictionaries, updated the amine list of dictionaries and made a crew metabolism dictionary, fixed some typos and learned a lot about organizing files, name consistency, code consistency, not going overboard too fast, and file setup

        **next session start:**
    -work on power_system.py
    -eventually... work on water_system, lighting function and then continue adding heat generated/heat waste to new functions for electronics/computers, radiators, pumps