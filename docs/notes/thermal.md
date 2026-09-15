# Thermal / Humidity Control
### General Notes:
    ♡ preliminary estimates

    ♡ V1 uses one shared cabin temperature

    ♡ heaters, radiators, solar gain, heat leakage, crew heat and equipment heat all affect that one temperature

    ♡ kW represents heat flow

    ♡ °C represents the resulting temperature after the net heat flow affects the habitat's thermal mass

### ----------------------------------------

## Habitat Thermal Plan (updated 09/15/2026):

### Temperature and Humidity Targets:
    ♡ habitat starting temperature / target: ~ 23.0 °C
    ♡ comfort range: ~ 20.0-25.0 °C
    ♡ too hot alert: > 28.0 °C
    ♡ too cold alert: < 18.0 °C
    ♡ low-power target: ~ 21.0 °C
    ♡ critical-power target: ~ 19.0 °C
    ♡ habitat starting humidity / target: ~ 48 %
    ♡ allowed humidity range: 20-80 %

    ♡ V1 uses one temperature for the whole habitat

### ----------------------------------------

### Insulation and Thermal Mass:
    ♡ insulation: ~ 0.65 kW/°C
    ♡ thermal mass: ~ 95 kWh/°C
    ♡ calculation:
        - heat leakage:
            (habitat °C - Mars °C) × 0.65
        = heat_loss_kw

        - approx. thermal response time:
            95 ÷ 0.65
            ≈ 146 hours
    
    ♡ used for:
        - calculating how quickly heat leaves through the habitat hull

        - calculating how slowly the habitat temperature changes

    ♡ the 95 kWh/°C thermal mass includes walls, water, tanks, equipment and other internal material, not only the cabin air

### Outside Environment and Solar Gain:
    ♡ outside temperature uses a seasonal base temperature plus a day / night swing based on sunlight

    ♡ northern spring:
        - base temperature: -10 °C
        - day / night swing: 12 °C

    ♡ northern summer:
        - base temperature: 0 °C
        - day / night swing: 15 °C

    ♡ northern autumn:
        - base temperature: -15 °C
        - day / night swing: 12 °C

    ♡ northern winter:
        - base temperature: -25 °C
        - day / night swing: 10 °C

    ♡ V1 weather is used to calculate:
        - Mars outside air temperature
        - sunlight heating ~ 48 m² of habitat surface

    ♡ sunlight-facing area: ~ 48.0 m²
    ♡ maximum daylight intensity: ~ 0.59 kW/m²
    ♡ how much of that heat gets through: ~ 0.75
    
    ♡ calculation:
        sunlight intensity × sunlight-facing area × solar heat-transfer fraction
        = solar gain
 
    ♡ V1 weather is used for:
        - Mars air temperature
        - sunlight hits about 48 m² of the habitat in this calculation

### ----------------------------------------

## Heaters:
    ♡ total units: 6
    ♡ primary units: 4
    ♡ backup units: 2
    ♡ maximum online: 6
    ♡ hysteresis: ~ 0.5 °C
    ♡ total heating capacity: 52 kW
    ♡ calculation:
        - 4 × 9.0 kW = 36 kW
        - 2 × 8.0 kW = 16 kW
        - 36 + 16 = 52 kW

    ♡ includes:
        - 4 primary heaters, 9.0 kW each
        - 2 backup heaters, 8.0 kW each

    ♡ used for:
        - heating when the habitat is below its active temperature target

        - covering winter heat leakage with some extra capacity

    ♡ primary units come on first
    ♡ if heaters come on, radiators go to standby

#### Radiators:
    ♡ total units: 7
    ♡ primary units: 5, 68 m²/unit
    ♡ backup units: 2, 55 m²/unit
    ♡ maximum online: 7
    ♡ total radiator area: ~ 450 m²
    ♡ primary radiator area: 340 m²
    ♡ backup radiator area: 110 m²
    ♡ hysteresis: ~ 0.10 °C
    ♡ pump power: ~ 0.08 kW per active radiator

    ♡ calculation:
        - 5 × 68 m² = 340 m²
        - 2 × 55 m² = 110 m²
        - 340 + 110 = 450 m²
        
        number of active radiators × 0.08 kW
        = number of active radiators

    ♡ used for:
        - dealing with extra heat when the habitat is above target
    
    ♡ primary radiators come online first
    ♡ if radiators come online, heaters enter standby
    ♡ V1 compares habitat temperature to Mars air temperature

### Condensing Heat Exchangers (CHX):
    ♡ habitat CHX power: ~ 0.35 kW when removing vapor
    ♡ 60 % of power comes back as waste heat
    ♡ removes 0.85 of the extra vapor above target
    ♡ condensation heat: 2,260 kJ/kg

    ♡ greenhouse CHX stays in Hive-8 and habitat CHX stays in the Atmosphere / Resource Recovery Room
    
    ♡ both still change the same habitat temperature in V1

    ♡ CHX is for humidity first
    ♡ radiators do most of the cooling

### ----------------------------------------

## Design Evolution:
    ♡ first insulation idea was 1.0 kW/°C
    ♡ later tested with 0.3-0.8 and now uses 0.65
    ♡ CHX started as humidity only
    ♡ cooling from condensation was added later
    ♡ radiators stayed the main heat reject
    ♡ 6 array / 50 panel note was an early count
    ♡ code now uses 7 radiator units, 450 m² total
    ♡ started with radiators only, then heaters as a list like amine beds

### ----------------------------------------

## Future Considerations:
    ♡ separate greenhouse air temperature from cabin temperature and potentially battery rooms

    ♡ use a colder sky temperature instead of Mars air, potentially

    ♡ decide if my habiatat will be half buried or not, if so change 0.65

    ♡ figure out humidity volume vs layout volume

### ----------------------------------------

## Design Decisions:
#### Why one cabin temperature?
    ♡ V1 only needs to know if the crew volume is too hot or too cold

    ♡ splitting Hive-8 batteries and utility into their own loops is another subsystem to be considered in the future

#### Why radiators plus heaters, not only CHX?
    ♡ CHX follows the humidity
    
    ♡ you can need cooling when the air is already dry and you can need heat when CHX is running

#### Why keep greenhouse CHX out of the utility room?
    ♡ condensation from the plants is in Hive-8 and habitat CHX is in the atmosphere room, I am keeping them seperate
    
    ♡ both still add their leftover heat into the same V1 cabin

### ----------------------------------------

### Dev Log Notes:
###### From v1_scope:
    ♡ going to use kilowatts (kW) for heat sources (kW = change) (C = result)

    ♡ adding a variable for the habitat's insulation as a heat leak rate and I'm using 1.0 kw/C as a starter value

    ♡ I decided to go with radiator arrays, mostly to keep my code more manageable

    ♡ after doing some research, I decided to go with a 6 array set up with a total of 50 panels for now

    ♡ a condensing heat exchanger (CHX) which I read removes humidity while it could cool the cabin but I'm going to make it mainly a humidity control subsystem first with slight cooling, b/c I already have the radiators

###### 03/17/2026
    ♡ moving to temp management today and thermal control, I decided to get the main ideas down using radiators and do more research into other ideas later on

###### 03/18/2026
    ♡ deciding if I should add heat output into current functions, or have its own. I'm going to keep adding to the proper functions

    ♡ adding heat produced by amine beds w. exothermic absorption (the amine molecules catch the CO₂ which releases heat) and regeneration

###### 04/14/2026
    ♡ I'm going to focus on the thermal parts before considering humidity

###### 04/15/2026
    ♡ fixed insulation and thermal mass values

    ♡ adding electric heaters and radiators and I want to make both of them like I did some of the other systems w. lists (amine beds, etc.)

###### 04/16/2026
    ♡ going to change the way I have the radiators_online function set up b/c I don't like to hardcode the numbers like I did and I'm going to have a hysteresis so that my new setup doesn't turn on and off abruptly too often

    ♡ added radiator power usage and added radiator info to the other necessary files

    ♡  still playing around w. insulation values (0.3 - 0.8?)

###### 04/18/2026
    ♡ I'm going to keep the radiators using the habitat temp directly to run and focus on adding in the electric heaters until then

    ♡ I am going to worry about emergencies later and just get the foundation down first, but I did add another two radiators to the radiator list

    ♡ making heaters their own list to be handled the same way the other systems are

###### 04/20/2026
    ♡ moving onto humidity in thermal b/c I decided I will alter the insulation and mass values once I have all the systems implemented including water and everything

    ♡ added moisture variables to the crew metabolism file and updated temp_system.py

    ♡ I'm considering adding a new file to handle humidity depending on how big that part gets

###### 04/21/2026
    ♡ adding sunlight to the thermal system

###### 04/23/2026
    ♡ adding condensate/CHX to water_system and engine and made OGA use potable water

    ♡ fixing heating issue, my hysteresis was WAY too high in temp_system.py

###### 04/24/2026
    ♡ starting by fixing my thermal mass value and insulation strength

    ♡ fixed thermal_system.py by cleaning up globals, changing placeholder values to real/accurate values and updating the rad heat function

    ♡ started adding backup radiators and heaters

###### 04/25/2026
    ♡ updated CHX to include cooling

###### 06/14/2026
    ♡ fixing temp issues, starting w. the insulation strength/thermal mass and fixing my heater logic

###### 06/16/2026
    ♡ fixing radiator and heaters to make things smooth and effective

    ♡ I'm happy w. how the temp system is running for now, so now I'm running atmosphere again




