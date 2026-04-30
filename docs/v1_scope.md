# MarsHSim

#### (name subject to change)

## Sim loop: 
    ♡ time steps

## V1 goal:
    ♡ closed loop ECLSS monitoring, logging, alerts, simple controllers

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

## ♡ Creation Notes:


##      03/04/2026
#### Habitat Info:
    ♡ location: 47° North, 184° East (Arcadia Planitia)

    ♡ 30 crew members to hint at an early colony

    ♡ habitat size of 2000 cubic meters (m3)


#### Atmosphere:
    ♡ target pressure:
        - lower (~65 kilopascals (kPa))
        - less catastrophic leaks

    ♡ buffer gases:
        - argon (Ar)
            - Mars atmosphere is ~1.6% Ar
            - non-reactive
        - nitrogen (N2)
            - Mars atmosphere is ~2.7% N2
            - humans are familiar with it


#### Crew:
    ♡ 30 person crew


#### Systems:
    ♡ (to be defined)


#### Atmosphere Design:
    ♡ wanting to keep lower pressure (~65 kilopascals (kPa) target) in habitat to make leaks not as catastrophic

    ♡ deciding to add argon as a buffer gas

    ♡ going to be using Dalton's Law

    ♡ researched net habitat volume per crew member (average minimum of 25m3 pp), and I'm happy with keeping the habitat size at 2000m3 (~66 m3 pp)

#### Gas Risks:    
    ♡ o2 < 12 kPa:
        - hypoxia risk
        - confusion
        - headaches
        - restlessness
        - shortness of breath
        - impaired judgment
        - cyanosis (bluish skin, severe)

    ♡ o2 < 18 kPa:
        - mild hypoxia possible (long exposure)
        - reduced cognitive performance

    ♡ o2 > 25 kPa:
        - mild hyperoxia
        - headaches
        - airway irritation
        - increased fire risk

    ♡ o2 > 50 kPa (sustained):
        - oxygen toxicity (lungs)
        - coughing
        - chest pain
        - reduced lung function

    ♡ co2 > 0.7 kPa:
        - headaches
        - difficulty concentrating
        - drowsiness
        - mild hypercapnia

    ♡ co2 > 1.5 kPa:
        - impaired thinking
        - fatigue
        - increased heart rate
        - stronger headaches

    ♡ co2 > 3 kPa:
        - dizziness
        - confusion
        - shortness of breath
        - flushed skin
        - reduced coordination

    ♡ co2 > 5 kPa:
        - severe hypercapnia
        - disorientation
        - panic
        - unconsciousness risk

    ♡ n2 high % (displacing oxygen):
        - hypoxia symptoms (from low o2, not n2 itself):
            - headaches
            - dizziness
            - fatigue
            - confusion
            - unconsciousness (severe)

        note:
        - n2 itself is not toxic at habitat pressures
        - acts as a buffer gas
        - danger = lowering o2 partial pressure

    ♡ h2 >= 4%:
        - explosive / flammability risk (very wide range)

    ♡ high concentrations (o2 displacement):
        - dizziness
        - headaches
        - fatigue
        - confusion

        note:
        - physiological effects come from oxygen displacement
        - main danger is explosion, not toxicity

    ♡ ch4 >= 5%:
        - flammability risk (lower explosive limit)
        - dizziness
        - headaches
        - nausea
        - impaired judgment

    ♡ ch4 >= 15%:
        - asphyxiation risk
        - unconsciousness

        note:
        - symptoms caused by reduced o2 availability            

#### Habitat Setup:
    ♡ location: 47° North, 184° East (Arcadia Planitia)

    ♡ 30 crew members to hint at an early colony

    ♡ habitat size of 2000 cubic meters (m3)
 
##      03/05/2026
#### Mars Environment / Seasons:
    ♡ 25% yearly atmosphere pressure changes from co2 freezing and sublimating at the poles

    ♡ dune migration (research this more)

    ♡ sun absorption changes from ice/dust


#### Seasonal Breakdown:
    ♡ N spring / S fall:
        - 194 sols
        - average temp: ~(-15°C) - ~(-5°C)
        - daytime highs: ~(0°C) - ~(-15°C)
        - nighttime lows: ~(-60°C) - ~(-80°C)
        - warms gradually
        - slightly better ice stability
        - dust: frequent dust devils (small, short dust whirlwinds)

    ♡ N summer / S winter:
        - 178 sols
        - average temp: ~(-5°C) - ~(5°C)
        - daytime highs: ~(10°C) - ~(25°C)
        - nighttime lows: ~(-80°C) - ~(-100°C)
        - better solar reliability
        - dust: lower risk

    ♡ N fall / S spring:
        - 142 sols
        - average temp: ~(-20°C) - ~(-5°C)
        - daytime highs: ~(-5°C) - ~(5°C)
        - nighttime lows: ~(-80°C) - ~(-110°C)
        - occasional high temp: ~(10°C) - ~(15°C)
        - cools gradually
        - dust: frequent dust devils

    ♡ N winter / S summer:
        - 154 sols
        - average temp: ~(-30°C) - ~(-10°C)
        - daytime highs: ~(-20°C) - ~(-5°C)
        - nighttime lows: ~(-100°C) - ~(-140°C)
        - dust: storms, sometimes global

    ♡ global dust storms can drop temp averages between 10-20°C for a little while

    ♡ I'm going off of approximate surface temp daily averages for mid-latitude from NASA missions


##      03/08/2026
#### Gas Modeling:
    ♡ tracking partial pressure changes per timestep instead of mass

    ♡ O2 drop:
        ~0.0033kPa pp/5min

    ♡ 288 five minute intervals in one day
        ~0.0033 * 288 = 0.9504kPa pp/day

    ♡ 30 crew members
        ~0.0033 * 30 = 0.099kPa/5min


#### CO2 Rise:
    ♡ ~0.0029kPa pp/5min

    ♡ ~0.0029 * 288 = 0.8352 kPa pp/day

    ♡ ~0.0029 * 30 = 0.087kPa/5min


#### CO2 Scrubber (Amine Beds):
    ♡ including two amine swing bed scrubbers as part of making energy efficiency and waste reduction / recycling priorities

    ♡ they aren't too expensive and this will help with humidity removal

    ♡ including two more beds as backup

    ♡ making them a list so when I add more features they will be easier to access


##      03/09/2026
#### Oxygen Generation (OGA):
    ♡ NASA references: crew co2 production is around 1kg pp/day

    ♡ pros:
        - reliable
        - efficient
        - works well with amine beds and humidity considerations
        - low power usage at ~5 - 10kW
        - ~500 - 800kg hardware

    ♡ cons:
        - requires water (not really a huge con b/c recycling is a main priority)
        - produces hydrogen (could use Sabatier or vent)


##      03/10/2026
#### OGA Byproduct (H2):
    ♡ h2_kg = (2 * o2_added_pa * hab_vol_m3 * 2.016) / (r * temp_k * 1000)

    ♡ 2.016 b/c:
        h2 gas = two h2 atoms bonded

        one h2 atom = 1.008 mol

        h2 = 1.008 + 1.008 = 2.016mol

    ♡ convert h2 mol to g, convert g to kg


##      03/13/2026
#### OGA Water Usage:
    ♡ ratio in kg is: 1.125kg of H2O per 1kg of O2 produced

##      03/21/2026
#### Time Variables:
    ♡ mission_time_s = current time of day

    ♡ dt_min = how long the step lasts

    ♡ hours_per_step = scaling, production, etc