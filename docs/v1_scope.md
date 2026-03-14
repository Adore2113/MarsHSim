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
  
    -Engine uses configurable delta time(dt) (supperted timesteps will be: 1, 5, 10, 30 min)

    -Adaptive dt allowed during events (automatically reduces the timestep to 1 min, during critical events)

    -Track mission time in seconds internally, and converted to Mars sol and local time for display

#### Creation notes: 
        
        03/04/2026
    -Wanting to keep lower pressure (~65 kiloPascals (kPa) target) in habitat to make leaks not as catastrophic, and deciding to add argon as a buffer gas

    -30 crew members to hint at an early colony with a habitat size of 2000 cubic meters (m3)

    -going to be using Dalton's Law



        03/05/2026
    -considering adding humidity contribution (1-2kPa ppH2O)

    -reasearched net habitat volume per crew member (average minimum of 25m3 pp), and I'm happy with keeping the habitat size at 2000m3 (~66 m3 pp)

    -wanting to keep the habitat temp between 22- 24C ideally

    -taking seasons on Mars into consideration (how many sols, winter lows ~-140C, summer highs ~ 20C, 25% yearly atmosphere pressure changes from CO2 freezing and subliminating at the poles, dune migration, albedo changes from ice/dust, dust storms in the spring/summer while global storms can engluf the whole planet)

    -global dust storms can drop temp averages between 10-20C for a little while

    -N spring/S fall 194 sols, average temp:  
    -N summer/S winter: 178 sols, average temp:
    -N fall/S spring 142 sols, average temp:
    -N winter/S summer 154 sols, average temp: 
    (I am going off of aproximate surface temp daily averages for mid-latitude from NASA missions)



        03/08/2026
    -resuming atmosphere creation with more and updated knowledge

    -Tracking partial pressure changes per timestep instead of mass: 
    
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

    -including two amine swing bed scrubbers as part of making energy efficiency and waste reduction/recycling priorites, they aren't too expensive, and this will help with humidity removal

    -including two more beds as backup, deciding to make them a list so when I add more features they will be easier to access

    -co2 was defaulting to zero, need to fix my scrubbing system

    -Today I learned that I needed to get the skeleton figured out and that it's okay to refine the numbers afterwards

    -tomorrow finishing scrubbing function in engine.py



        03/09/2026
    -continuing where I left off with scrubbing

    - NASA references : crew co2 production is around 1kg pp/day

    -Making seperate functions for managing and checking gases

    -Researched o2 regeneration and electrolysis with focus on Oxygen Generation Assembly (OGA), MOXIE-like Solid Oxide Electrolysis (SOXE), and Sabatier co2 reduction + electrolysis

    -Implementing very basic OGA o2 generation function for now (handling power usage, total pressure updates, hydrogen(h2) production and handling/venting, later)  
    
    Pros: reliable, efficient, works well with amine beds and humidity considerations, low power usage at ~5 - 10kw, ~500-800kg hardware

    Cons: requires water (not really a huge con b/c recycling is a main priority), produces hydrogen (could use Sabatier or vent)

         **next session start:**
    -adding total pressure update tomorrow, remember to add the o2 regen to quick_test and state.py tomorrow, also starting this little part at the end of my notes



        03/10/2026
    -renamed checking_gases function to gas_alerts, moved the cs2 removal function to before o2_regen

    -made the scrubber unable to remove more cs2 than exists, and changed the kpa values to move 4 decimal places instead of two, updated target based co2 and oxygen control, added target gases as global variables in engine.py

    -adding in the hydrogen that the OGA electrolysis makes and venting it -FOR NOW- and will do research on how I can use it later on (Sabatier?)

    -adding OGA byproduct function in, first calculating 23C to Kelvin because I read the gas pressure depends on temp (pressure drops if it goes down) 

    -I know that chemistry ratios use moles, but I really wanted to stick to kPa and kilograms(kg) to avoid my code being more complex than, so I'll figure out the conversions to avoid that

    -h2_kg = (2 * o2_added_pa * hab_vol_m3 * 2.016) / (r * temp_k * 1000)
    
    -2.016 b/c h2 gas = two h2 atoms bonded, one h2 atom = 1.008 mol, h2 = 1.008 + 1.008 = 2.016mol
    
    -convert h2 mol to g, convert g to kg 

       **next session start:**
    -consider breaking down the long conversion in oga_byproduct into mulitple lines of code with notes explaining each step for easier understanding, vent the h2


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

    -I'm going to keep the oga functions seperate instead of one big function with a comment to sort of group them together, I feel like that will be better for future readability

    -arranged some comments to be beside the line of code, I find if it's short, it does look cleaner

    -finished oga and water electrolysis for now, moving onto argon and nitrogen 

        **next session start:**
    -figure out variable numbers for the variables commented out at the top of engine.py, add in when the ar or n2 will be used from storage    
    