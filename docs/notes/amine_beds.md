# CO₂ Scrubbing (Amine Swing Beds) 
### General Notes:
    ♡ removes CO₂ from the cabin atmosphere

    ♡ uses amine swing beds to absorb, regenerate, and cycle

    ♡ multiple beds so some can adsorb while others regenerate

    ♡ includes primary beds and backups

### ----------------------------------------
## CO₂ Scrubbing Plan (updated 08/24/2026):

### Layout:
    ♡ bed bay: ~ 50-60 m²

    ♡ shared resource recovery room: ~ 120–140 m²

    ♡ beds and support equipment are part of the atmosphere / resource area
    
    ♡ see atmosphere.md for room placement and connections
    
    ♡ full set of 8 beds, manifolds, valves, blowers and aisles fit as a bay inside the resource recovery room at ~ 50-60 m² of floor space for the bed row

### Beds:
    ♡ total beds: 8
    ♡ max beds online: 8
    ♡ beds have type: primary or backup
    ♡ each bed tracks: status, co2 load, capacity in kg and regen_timer_min
    
    ♡ primary beds are preferred when bringing capacity online
    
    ♡ backup beds are preferred when shedding capacity

### Scrub Efficiency:
    ♡ efficiency depends on current CO₂ level:
        - ≤ 0.2 kPa → 0.55
        - 0.2–0.4 kPa → ramps 0.55 → 0.85
        - 0.4–0.5 kPa → ramps 0.85 → 1.00
        - > 0.5 kPa → 1.00

    ♡ calculation:
        max removal this step =
            beds_online × scrub_per_bed_kpa × efficiency

### Operating Modes and States:
    ♡ offline
    ♡ standby
    ♡ online (adsorbing / removing CO₂)
    ♡ regenerating
    ♡ emergency behaviour later

### Operating Logic:
    ♡ CO₂ above target decides the number of beds actively adsorbing
    
    ♡ scrubbed CO₂ from the cabin is converted to kg and added to CO₂ storage
    
    ♡ CO₂ released during bed regeneration is also added to CO₂ storage for the Sabatier system
   
    ♡ cannot remove more CO₂ than exists above target or than online beds have room for

    ♡ hysteresis:
        - co2_hysteresis_for_off = 0.03
        - once any beds are online, at least 1 stays until CO₂ drops below target minus the off hysteresis

    ♡ cannot remove more CO₂ than currently exists above target

    ♡ scrubbed CO₂ is converted to kg and added to CO₂ stored for Sabatier / storage

### Bed Switching
    ♡ when an online bed reaches capacity it switches to regenerating

    ♡ regen duration: 55 min
    
    ♡ during regen, CO₂ load is released over time into storage
    
    ♡ when regen finishes, the bed returns to standby
    
    ♡ on any bed-switch this step:
        - max scrub reduced to 80%
        - power multiplied by 1.25
    
    ♡ standby beds can be brought online the same step to replace a saturated bed

### Power & Heat
    ♡ base power per online bed: 0.65 kW
    ♡ base heat per online bed: 0.35 kW
    ♡ extra power from removal: ~ 4.2 kW per kPa removed
    ♡ extra heat from removal: 1.8 kW per kPa removed

    ♡ calculation:
        baseline_power:
            beds_online × 0.65

        removal_power:
            co2_removed_kpa × 4.2

        total_power:
            baseline_power + removal_power
        (same pattern for heat)

### Connections
    ♡ input: cabin CO₂ kPa
    ♡ output: reduced cabin CO₂, buffered/stored CO₂ 
    ♡ connects to: crew metabolism, Sabatier (CO₂ source), MCA (monitoring), thermal (heat)

### ----------------------------------------

## Design Evolution:
#### Starting Plan:
    ♡ hard-coded / pre assigned bed roles
    
    ♡ changed so beds come online from calculated CO₂ need

    ♡ brought closer to other subsystems (clear modes, power/heat split, dictionary returns)

### ----------------------------------------

## Future Considerations:
    ♡ degraded or failed bed behaviour

    ♡ more detailed regeneration energy if beds get individual timers

    ♡ change beds online and offline to more specific, generating, regenerating, etc.

### ----------------------------------------

## Design Decisions:
#### Why 2–8 beds instead of one large unit?
    ♡ for continuous capacity scaling
    
    ♡ redundancy for no resupply
    
    ♡ so it's easier to take individual beds offline

    ♡  8 beds still fit as a bay inside the shared resource recover room

#### Why drive bed count from CO₂ above target?
    ♡ it's more realistic

    ♡ saves power when CO₂ is already near target
    
    ♡ it responds naturally to crew activity and events

#### Why buffer scrubbed CO₂ as kg?
    ♡ supports Sabatier and other system uses
    
    ♡ keeps cabin tracking in kPa and stored resources in kg, for consistency

#### Why the efficiency curve?
    ♡ so I could model lower efficiency at low CO₂ and higher efficiency when CO₂ is elevated

### ----------------------------------------

### Dev Log Notes:
##### see atmosphere.md

###### 08/24/2026
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