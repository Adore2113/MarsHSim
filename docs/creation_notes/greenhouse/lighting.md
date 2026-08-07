# Greenhouse Lighting:
### General Notes:
    ♡ lighting is a hybrid system: natural light through the angled roof + LED support
    
    ♡ LEDs offset lower natural light
    
    ♡ LED support fills whatever gap is left below each zone's light target
    
    ♡ this is intentionally kept simpler than a full greenhouse research model
    
    ♡ lighting has a major effect on habitat power demand and thermal load

    ♡ actual light exposure depends on:
        - season / daylight fraction
        - zone light target
        - zone light absorption
        - LED support level
        - power mode (normal / low / critical)

 ### ----------------------------------------

### Light Targets & Natural Light:
    ♡ default zone light target: 
        0.70 kW/m²

    ♡ best expected natural sunlight:
        0.45 kW/m²

    ♡ minimum useful natural sunlight:
        0.15 kW/m²

    ♡ full led support: 
        - used when effective natural light is at or below 0.15 kW/m²

    ♡ sunlight only:
        - effective light ≥ the zone's target, LEDs off

### ----------------------------------------

### LED System:
    ♡ LED power density:
        0.12 kW per m² of effective grow area

    ♡ LED heat ratio: 
        0.68 (68% of LED power becomes heat)

    ♡ LEDs are dimmable and respond to power modes

    ♡ calculation (led support level):
        - (light_target − effective_light) ÷ light_target

#### Power Modes:
    ♡ normal: 
        full LED support as needed (level 1.0)

    ♡ low power: 
        LED level × 0.6

    ♡ critical power: 
        LED level × 0.2

### ----------------------------------------

### Plant Lighting Schedule:
    ♡ light period: 
        16 hours per sol

    ♡ lights on: 
        05:00 – 21:00 LMST

    ♡ dark period: 
        - 8 hours (21:00 – 05:00 LMST)
        - outside scheduled hours, LEDs off

    ♡ outside the scheduled hours, LEDs remain off (dark cycle)
    
    ♡ calculation: 
        -light end hour: 
            (5 + 16) % 24 = 21:00

### ----------------------------------------

### How Light Level Is Calculated:
    ♡ natural light is reduced by the zone’s light absorption percentage
    
    ♡ day_length_bonus adjusts for seasonal daylight changes:
        day_length_bonus = 0.70 + (0.30 × daylight_fraction)

    ♡ effective natural light = natural_light × absorption × day_length_bonus

    ♡ LED support is applied only when effective light is below the zone target and above the minimum useful level

### ----------------------------------------

### Zone Light Targets:
    ♡ structural zone: 0.75 kW/m²
    ♡ container zone: 0.70 kW/m²
    ♡ rack zone: 0.60 kW/m²

### ----------------------------------------

## Design Evolution:
#### Early Lighting Plan:
    ♡ considered allowing plants to use ~70% of the available natural sunlight

    ♡ this became the default 70% light-absorption value
    
    ♡ originally had no lighting schedule


### ----------------------------------------

## Design Decisions:
#### Why timed greenhouse lights?
    ♡ constant lights were taking up too much power (this was before my upgraded 50acre solar plan)

    ♡ plants require a controlled photoperiod rather than continuous lighting

    ♡ timed lighting gives crops consistent lighting even as natural daylight changes by season
    
    ♡ the dark cycle provides a regular period without plant lighting
    
    ♡ natural sunlight reduces the LED support required during the scheduled light period

    ♡ 16 hour light period was chosen as a balance between plant needs and power use

#### Why sync greenhouse habitat lights?
    ♡ greenhouse plant lights already provide visibility while they are active

    ♡ keeping the habitat lights off during that time avoids unnecessary duplicate lighting

    ♡ when the plant lights are off, the greenhouse follows the same lighting conditions as the rest of the habitat

### ----------------------------------------

### Dev Log Notes:
###### 05/13/2026:
    ♡ started building the greenhouse lighting system

###### 06/23/2026:
    ♡ considered switching to a timed lighting cycle that still turns off when natural sunlight is sufficient

###### 07/23/2026:
    ♡ tested 16-hour plant lighting schedule
    ♡ reduced greenhouse energy use by approximately 20%

###### 08/03/2026:
    ♡ greenhouse plant lighting remains with the greenhouse subsystem