# MarsHSim
    - this file is currently being organized -

#### (name subject to change)

## Sim loop: 
    ♡ time steps

## V1 goal:
    ♡ closed loop ECLSS monitoring, logging, alerts, simple controllers

    ♡ Habitat size of 2400 m3 in Arcadia Planitia (47° North, 184° East)

### V2 goal:
    ♡ AI autonomy, predictive control, fault detection

## No resupply assumption:
    ♡ finite buffers and recycling efficiency matter
    
## Time model:
    ♡ default timestep: 5 minutes

    ♡ engine uses configurable delta time (dt)
        - supported timesteps: 1, 5, 10, 30 min

    ♡ adaptive dt allowed during events
        - automatically reduces to 1 min during critical events

    ♡ track mission time in seconds internally
        - convert to Mars sol and local time for display

##  Creation Notes:
    These are just notes I wanted to keep together, they aren't in any specific order and they will be updated and edited every so often.

#### Systems:
    ♡ Crew metabolism
    ♡ OGA / electrolysis
    ♡ CO2 scrubber / amine beds
    ♡ Buffer gas control / MCA
    ♡ Sabatier reactor
    ♡ Water recovery systems (UPA / WPA / BPA)
    ♡ Humidity / CHX
    ♡ Thermal control
    ♡ Solar + battery power system
    ♡ Greenhouse subsystem
    ♡ Dust accumulation
    ♡ Alerts + monitoring 


#### Variables / Constants:
    ♡ - There are some variables that haven't been used, b/c I will need them for future plans and ideas

    ♡ - I can sort them and maybe rethink the constants and what variables will be in state, later on


### Mars / Time of Day / Season / Temp Notes:
    ♡ N spring / S fall:
        - 194 sols
        - average temp: ~(-25°C) - ~(-5°C)
        - daytime highs: ~(-10°C) - ~(10°C)
        - nighttime lows: ~(-80°C) - ~(-110°C)
        - warms gradually
        - slightly better ice stability
        - dust: frequent dust devils (small, short dust whirlwinds)

    ♡ N summer / S winter:
        - 178 sols
        - average temp: ~(-15°C) - ~(0°C)
        - daytime highs: ~(0°C) - ~(20°C)
        - nighttime lows: ~(-85°C) - ~(-115°C)
        - better solar reliability
        - dust: lower risk

    ♡ N fall / S spring:
        - 142 sols
        - average temp: ~(-25°C) - ~(-10°C)
        - daytime highs: ~(-15°C) - ~(5°C)
        - nighttime lows: ~(-90°C) - ~(-120°C)
        - occasional high temp: ~(10°C) - ~(15°C)
        - cools gradually
        - dust: frequent dust devils

    ♡ N winter / S summer:
        - 154 sols
        - average temp: ~(-35°C) - ~(-15°C)
        - daytime highs: ~(-25°C) - ~(-5°C)
        - nighttime lows: ~(-100°C) - ~(-130°C)
        - dust: storms, sometimes global

    ♡ global dust storms can drop surface temp averages by 10-20°C for weeks

    ♡ I'm going off of approximate surface temp daily averages for mid-latitude from NASA (Viking 2)

    
    ♡ mission_time_s = current time of day

    ♡ dt_min = how long the step lasts

    ♡ hours_per_step = scaling, production, etc

    ♡ using 0.50kW of sunlight for every 1 square meter (m2) for now

    ♡ Mars sunlight is between 0.4 - 0.6 kW / m2 during daytime

    ♡ Mars time runs at 24 hours and 39 minutes and 35 seconds

    ♡ I'm going to hardcode Mars' tilt to be 25.19 degrees b/c my model isn't going to run long enough to take that slow progression into consideration

    ♡ going to use the midpoint range of each season for now (v1?)


### Atmosphere Notes:
    ♡ target pressure:
        - lower (~65 kilopascals (kPa))
        - less catastrophic leaks

    ♡ 25% yearly atmosphere pressure changes from co2 freezing and sublimating at the poles

    ♡ kg for storage, kpa for atmosphere

    ♡ adding variables for each gas to have a base leak rate, to use for venting and other things (using individual ones b/c some leak faster than others)


#### Gas Notes:
    ♡ going to be using Dalton's Law

    ♡ tracking partial pressure changes per timestep instead of mass

    ♡ O2 drop:
        ~0.0033kPa pp/5min

    ♡ 288 five minute intervals in one day
        ~0.0033 * 288 = 0.9504kPa pp/day

    ♡ 30 crew members
        ~0.0033 * 30 = 0.099kPa/5min

    ♡ SpaceX: combines oxygen production with making methane rocket fuel with Sabatier + electrolysis

#### Buffer Gas Notes:
    ♡ buffer gases:
        - argon (Ar)
            - Mars atmosphere is ~1.6% Ar
            - non-reactive

        - nitrogen (N2)
            - Mars atmosphere is ~2.7% N2
            - humans are familiar with it

#### CO2 Scrubbing / Amine Bed Notes:
    ♡ ~0.0029kPa pp/5min

    ♡ ~0.0029 * 288 = 0.8352 kPa pp/day

    ♡ ~0.0029 * 30 = 0.087kPa/5min

    ♡ including two amine swing bed scrubbers as part of making energy efficiency and waste reduction / recycling priorities

    ♡ they aren't too expensive and this will help with humidity removal

    ♡ including two more beds as backup

    ♡ making them a list so when I add more features they will be easier to access

    ♡ adding heat produced by amine beds with exothermic absorption (the amine molecules catch the co2 which releases heat), and regeneration

    ♡ amine beds come online based on how much co2 is needed using two different hysteresis
    

#### O2 / OGA Notes:
    ♡ NASA references: crew co2 production is around 1kg pp/day

    ♡ pros:
        - reliable (proven on ISS for many years)
        - efficient for recycling water into oxygen
        - works well with amine beds and humidity considerations
        - integrates easily with Sabatier reactor for hydrogen utilization
        - SpaceX: combines oxygen production with making methane rocket fuel with Sabatier + electrolysis

    ♡ cons:
        - requires water (not really a huge con b/c recycling + local ice mining is a main priority at Arcadia Planitia)
        - high power demand overall
        - produces hydrogen (can feed Sabatier for methane/oxygen or vent)
        - big hardware mass when scaled to 30 crew

    ♡ h2_kg = (2 * o2_added_kpa * hab_vol_m3 * 2.016) / (r * temp_k * 1000)

    ♡ r:
        - 0.008314 in kPa

    ♡ why * 2:
        - from electrolysis: 2 H2O » 2 H2 + O2
        - you get twice as many H2 molecules as O2 molecules

    ♡ why 2.016:
        - H2 = 2 hydrogen atoms bonded together
        - each hydrogen atom = ~ 1.008 g/mol
        - H2 = ~ 2.016 g/mol

    ♡ what it does:
    - converts oxygen pressure (kPa) into moles of oxygen gas
    - for every oxygen made, you also get hydrogen (2 hydrogen for 1 oxygen)
    - converts hydrogen grams into kg

    ♡ water usage:
        - about 1.125 kg of water is needed to get 1 kg of oxygen


#### Greenhouse Notes:
    ♡ these notes are a mess while I organize my thoughts 

    ♡ considering hydroponics, a set up between waste water and filtering and that filtered water 

    ♡ gray/black water to water filtration to UPA/WPA to potable to greenhouse

    ♡ loop = crew waste to treatment to greenhouse nutriant solutio to plants to humidity to CHX capture to water system!

    ♡ pros : massive water recylcing!

    ♡ cons: nutrient imbalance and pathogens (plant disease)
    
    ♡ lightweight clayballs from earth able to pack in tightly and securely in the starship, slow degration over years to Mars instead of soil

    ♡ grow racks, artificial grow lights

    ♡ humidity control

    ♡ plants that help scrub the co2, and generate o2

    ♡ really contemplating how to approach this, without it turning into a detailed greenhouse simulator.. I've considered:
        - each individual crop type having specific growing conditions, but this would be way to complex for this sim in genreal, let alone compared to my other systems..
        
        - each conainer type having their own specific growing conditions
        
        - having one overall setting for the greenhouse, but this just seems to simple  

    ♡ I've decided to go with three seperate zones seperated by container type and use the averages of the plants for the information to work with

    ♡ I am using the idea of the crew maintaining:
        -40% carbs:
            - I'm even open to making this a lower percentage, but after doing my own reasearch from different sites and things, I'm choosing this for now
        
        -45% fat:
            - these are very dense in calories and  keep people full longer

        -15% protein:
            - high protein just doesn't seem ideal for a survival environment for multiple reasons
            - humans can survive off of 15% protein

    ♡ I didn't want to have foods that need a lot of processing, at least to start

    ♡ food choices/considerations:
            - sweet potato (high in calories, higher nutrients than regular potatoes, edible leaves, easy to grow, ect.): 
                - can grow vertically
                -germination 1-14 days, vegetative 2-8 weeks, flowering 6-12 weeks, harvest ~3 months
            

            - quinoa (protein, very low prep after harvest, resiliant, carbs)
                -germination 2-3 weels, vegetative 2-4 weeks, flowering 4-6 weeks, harvest 3-4 months


            - corn (mulitpurpose, starchy, easy growth) - 
                -germination 5-10 days, vegetative 10-50 days, flowering 50-70 days, harvest 90-140 days
            

            - dwarf banana trees (familiar, sweet, sort of a morale fruit):
                -germination 2-3 weeks, vegetative 3-6 months, flowering 6-12 months, fruit development 11-14 months


            - peanut (high in fat, protein and calories)
                -germination 5-10 days, vegetative 10-40 days, flowering 40-50, harvest 120-160 days


            - sunflowers for seeds, morale, ect.
                -germination 7-10 days, vegetative 20-40 days, flowering 30-50 days, harvest 70-120 days


            - peas (fast growth)
                -germination 7-14 days, vegetative 12-42 days, flowering 28-45 days, harvest 60-70 days 


            - spinach
                -germination 7-14 days, vegetative 30-45 days, flowering 42-56 days, harvest 37-60 days 


            - plantain leaf ( medicinal, anti-inflammatory, wound care, teas, ect.)
                -germination 7-21 days, vegetative 14-42 days, flowering 120-365 days, harvest 1-2 years (this is way to long, I'm removing this from the list) 


            - drwaf passionfruit trees (protein, vitamins, nice smell for morale) 
                -germination 7-28 days, vegetative 60-182 days, flowering 182-547 days, harvest 1-1.5 years 


            - lentils don't seem realistic to harvest and process, so I was thinking there could be a food storage/rations that include them to start or have as an emergency back up,as well as freeze dried protiens and other emergency rations


    ♡  herbs?( small amount, dual purpose only (reasearch this))

    ♡ fleshy fruits = high water content (peaches, apples, )
    ♡ dry fruits = good for seeds and plant reproduction,  fruit protect their seeds well    

    ♡ plant disease, labor hours, morale value, spoilage rate, water use, ect. 


### Ration Notes:
    ♡ lentils/beans


### Crew Notes:
    ♡ crew getting around 8 hours of sleep/night (9:30pm (21:30)- 6:00am)


### Power Notes:
    ♡ lights will dim at 9:30pm (21:30) and they will brighten at 6:00am

    ♡ battery capacity: 4000.0 kWh (for now)

    ♡ changing from 30-40 smaller panels to 10 larger ones

    ♡ solar panels modeled similarly to amine beds:
        - each panel has a status
        - power output in full sunlight
        - efficiency
        - dust build up
        - overall condition (for future repair handling)
    
    ♡ I thought about having panels on the outside of my habitat that are foil on one side and black on the other (like a car window shield), that could be flipped like a billboard (one of the ones that have two images on them and they flip to reveal the other image)

    ♡ I want the lights to adjust to time as well as sunlight level and never go below 0.2 light level

    ♡ 0.3 as a daytime light level support if there is enough sunlight

    ♡ an emergency minimum with enough sunlight will be 0.1 in case of very low power

    ♡ normal:
        - obviously everything runs as it should

    ♡ low:
        - lights dim
        - disable wellness lights
        - keep life support and everything else running

    ♡ critical:
        - lights turned down to minimum
        - reduce non-essential systems (implementing this later)
        - prioritize OGA and co2 scrubber


### Printing Notes:



### Sabatier Notes:
    ♡ reactions_avaliable is how many times stoichiometric reaction can happen with a ratio of 1 co2 : 4 h2



### Thermal Notes:
    ♡ going to use kilowatts (kW) for heat sources (kW = change) (C = result)

    ♡ adding a variable for the habitat's insulation as a heat leak rate, and I'm using 1.0 kw/C as a starter value

     ♡ I'm thinking about radiators, electric heaters, obvious insulation, fans and maybe.. a condensing heat exchanger (CHX) which I read removes humidity while it could cool the cabin

    ♡ I decided to go with radiator arrays, mostly to keep my code more manageable

    ♡ after doing some research, I decided to go with a 6 array set up with a total of 50 panels for now

    ♡ all humidity will be mostly internal, through crew perspiration, breathing, etc. 
    
    ♡ considering having a greenhouse b/c of the no resupply

    ♡ a condensing heat exchanger (CHX) which I read removes humidity while it could cool the cabin but I'm going to make it mainly a humidity control subsystem first with slight cooling, b/c I already have the radiators



### Water / CHX Notes:
    ♡ water recovery systems I'm going to use:
        - Urine Processor Assembly (UPA)
        - Water Processor Assembly (WPA)
        - Brine Processor Assembly (BPA)

    ♡ so the urine goes through the UPA and gets clean water and brine, and the brine goes through the BPA and gets some more clean water and a smaller amount of brine (that's the goal anyway)

    ♡ I read about In-Situ Resource Utilization (ISRU) to extract water locally but I'll worry about that later

    ♡ OGA uses potable water

    ♡ electrostatic dust repulsion (EDS) b/c of the fact that it's passive

    ♡ scheduled cleaning (possibly automated)

    ♡ dust repellent coatings that need to be reapplied over time


### Mars Dust / Environment Factors:

    ♡ dune migration (research this more)

    ♡ sun absorption changes from ice/dust


    ♡ dust factor ranges from 0.0 - 1.0

    ♡ eventually have Mars dust storms and things added in with random, maybe wind cleaning off some of the dust from the solar arrays as well



    
### Alert Notes:
        ♡ Gas alert ideas for future log:
        (o2): 
        ♡ o2 < 12 kPa:
            - severe hypoxia
            - crew: confusion, dizziness, rapid blackout
        ---------------------------------------
        ♡ o2 < 16–18 kPa:
            - mild hypoxia
            - crew: headache, fatigue, shortness of breath
        ---------------------------------------
        ♡ o2 > 25 kPa (sustained):
            - mild hyperoxia + fire risk
            - crew: dry throat, cough
        ---------------------------------------
        ♡ o2 > 50 kPa (sustained):
            - severe oxygen toxicity
            - crew: chest pain, nausea, seizures
        ---------------------------------------

        (co2):
            ♡ co2 > 0.7 kPa:
                - mild hypercapnia
                - crew: headache, flushed skin
        ---------------------------------------
            ♡ co2 > 1.5 kPa:
                - moderate hypercapnia
                - crew: strong headache, drowsiness
        ---------------------------------------
            ♡ co2 > 3 kPa:
                - high hypercapnia
                - crew: severe headache, disorientation
        ---------------------------------------
            ♡ co2 > 5 kPa:
                - severe hypercapnia
                - crew: extreme drowsiness, coma risk
        ---------------------------------------

        (n2):
            ♡ high n2 (≥ 80% or o2 low):
                - hypoxia from low o2
                - crew: headache, dizziness, confusion, blackout
            note: 
                - main danger = reduced oxygen
        ---------------------------------------
        
        (h2):
            ♡ h2 ≥ 4%:
                - explosion/fire risk
                - crew: headache, dizziness, confusion, blackout (if o2 drops)
            note: 
                - main danger = fire/explosion
        ---------------------------------------
        
        (ch4):
            ♡ ch4 ≥ 5%:
                - explosion/fire risk
                - crew: headache, dizziness, confusion, blackout (if o2 drops)
            note: 
                - main danger = fire/explosion
        ---------------------------------------
        
    (symptom references):
        ♡ hypoxia / asphyxiation: headache » fatigue » dizziness » confusion » unconsciousness
        
        ♡ hypercapnia: headache » drowsiness » disorientation » coma risk
        
        ♡ oxygen toxicity: dry throat/cough » chest pain » nausea » seizures


