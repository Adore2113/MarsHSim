# CO₂ Scrubbing (Amine Swing Beds) 
### General Notes:
    ♡ removes CO₂ from the cabin atmosphere

    ♡ uses amine swing beds to absorb, regenerate, and cycle

    ♡ multiple beds so some can adsorb while others regenerate

    ♡ includes primary beds and backups

### ----------------------------------------
## CO₂ Scrubbing Plan (updated 08/24/2026):

### Layout
    ♡ bed bay footprint: ~ 50-60 m²

    ♡ room size in shared process room: ~ 90-110 m²

    ♡ beds and support equipment are part of the atmosphere / resource area
    
    ♡ see atmosphere.md for room placement and connections
    
    ♡ full set of 8 beds, manifolds, valves, blowers and aisles fit as a bay inside the resource recovery room at ~ 50-60 m² of floor space for the bed row

### Beds
    ♡ total beds: 8
    ♡ min beds online: 2
    
    ♡ stored as a list so individual beds can be "online" or "standby"
    
    ♡ number of beds online is calculated from CO₂ load

### Operating Modes / States (per bed or system)
    ♡ offline
    ♡ standby / idle
    ♡ adsorbing / removing CO₂
    ♡ regenerating
    ♡ emergency behaviour later

### Operating Logic
    ♡ CO₂ above target decides how many beds are needed:
        - ≤ 0.0 kPa above target: 0 beds
        - > 0.012 kPa: 1 bed
        - > 0.03 kPa: 2 beds
        - > 0.06 kPa: 3 beds
        - > 0.12 kPa: 4 beds
        - > 0.25 kPa: 5 beds
        - > 0.40 kPa: 6 beds
        - > 0.55 kPa: 7 beds
        - > 0.70 kPa: 8 beds

    ♡ hysteresis:
        - co2_hysteresis_for_on = 0.05
        - co2_hysteresis_for_off = 0.03
        - once any beds are online, at least 1 stays until CO₂ drops below target minus the off hysteresis

    ♡ cannot remove more CO₂ than currently exists above target

    ♡ scrubbed CO₂ is converted to kg and added to CO₂ stored for Sabatier / storage

### Scrub Efficiency
    ♡ efficiency depends on current CO₂ level

    ♡ calculation:
        max removal this step =
            beds_online × scrub_per_bed_kpa × efficiency

### Bed Switching
    ♡ every 3300 s (~ 55 min) a bed-switch event can occur
    ♡ during switch: max scrub is reduced to 80%
    ♡ power is multiplied by 1.25 during the bed switch that step

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
    ♡ fuller adsorb and regenerate cycle per bed 

    ♡ humidity interaction with amine beds

    ♡ degraded or failed bed behaviour

    ♡ more detailed regeneration energy if beds get individual timers

    ♡ if adding more beds, add another room for all beds

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
######