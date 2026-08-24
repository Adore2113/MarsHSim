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
    ♡ In-Situ Resource Utilization (ISRU)
    ♡ Water recovery systems (UPA / WPA / BPA)
    ♡ Humidity / CHX
    ♡ Thermal control
    ♡ Solar + battery power system
    ♡ Greenhouse subsystem
    ♡ Dust accumulation
    ♡ Alerts + monitoring 

### Mars / Time of Day / Season / Temp Notes:
##### see mars_stats.md

### Atmosphere Notes:
##### see atmosphere.md

#### Buffer Gas Notes:
    ♡ buffer gases:
        - argon (Ar)
            - Mars atmosphere is ~1.6% Ar
            - non-reactive

        - nitrogen (N2)
            - Mars atmosphere is ~2.7% N2
            - humans are familiar with it
     
     ♡ adding ISRU to pull both Ar and N2 from the Mars atmosphere and sorbent beds that need a regen cycle between intakes

    ♡ I decided I'm going to add the sorbent beds to the isru_atm file

    ♡ I'm going to use five sorbent beds in total, two as backups as I like to have, so there are enough to absorb while another bed regenerates

    ♡ sorbent beds trap CO2 from compressed Mars air before N2/Ar and gets added to storage. This is modeled as a swing bed cycle, like the amine beds in co2_scrub.py.

    ♡ regen stop processing taking that bed fully offline, fewer adsorbing beds online = less raw atmosphere gets processed, meaning less N2 and Ar gets added to storage too

    ♡ unlike isru water pipes that have a real physical deploy/retract travel time, a compressor has no mechanical delay, so it just flips between offline and extracting mode based on target amount needed online for each step

#### CO2 Scrubbing / Amine Bed Notes:
    ♡ ~0.0029kPa pp/5min

    ♡ ~0.0029 * 288 = 0.8352 kPa pp/day

    ♡ ~0.0029 * 30 = 0.087kPa/5min

    ♡ including two amine swing bed scrubbers as part of making energy efficiency and waste reduction / recycling priorities

    ♡ they aren't too expensive and this will help with humidity removal

    ♡ including two more beds as backup

    ♡ making them a list so when I add more features they will be easier to access

    ♡ adding heat produced by amine beds with exothermic absorption (the amine molecules catch the co2 which releases heat) and regeneration

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
##### see greenhhouse folder

### Power Notes:
##### see power.md

### Sabatier Notes:
##### see sabatier.md

### Water / CHX Notes:
##### see hab_water.md

### Crew Notes:
##### see crew.md

### Thermal Notes:
##### see thermal.md

### Mars Dust / Environment Factors:
##### see mars_stats.md

### ISRU Notes:
##### see isru.md

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


### UI Notes:
    ♡ considering different methods of adding my UI idea