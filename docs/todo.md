# To Do List:

#### I will be adding and removing from this, but I needed somewhere to organize my ideas/thoughts

### Current Focus:
    ♡ add Sabatier info/logic into it's own file


### Next Focus:
    ♡ review heater logic:
        - add target_heaters_online to print for debugging

        - add heat_needed variable to print for debugging

    ♡ track system efficiency:
        - oga

        - scrubber

        - sabatier over time

    ♡ add limits instead of harsh cutoffs
        - systems gradually lose effectiveness near extremes

    ♡ add trend tracking to other systems (like "temp trend" in print)


### Later Focus:
    ♡ update alerts: thermal, water, etc.

    ♡ continue adding heat generated and heat waste

    ♡ add electronic heat and power

    ♡ add power priority systems

    ♡ go through all units and make them consistent (kpa, kg, kW, kWh)

    ♡ consider seperating files for values:
        - quick_test = starting values

        - state = things that change per timestep

        - separate file = constants, limits, targets

    ♡ define “normal ranges” for all systems in one place

    ♡ add system efficiency modifiers:
        - dust

        - wear

        - environment

    ♡ clean up how the subsystems interact


### Eventual Focus:
    ♡ add to file for handling dust:
        - finish dust accumulation function

    ♡ turn seasons into a list with different changes

    ♡ add crew scheduling

    ♡ havelogs for crew reacting to system events
        - "some of the crew members are starting to report headaches", etc.

    ♡ add maintenance scheduling

    ♡ add rations / food system:
        - add greenhouse (crucial for no resupply)

    ♡ add wind effects:
        - solar effects

        - external habitat effects

    ♡ add random events:
        - extra dust accumulation

        - wind removing dust from arrays

        - daily temperature and sunlight events

        - dust storms

        - leaks

        - micrometeorite damage (microscopic)? 

    ♡ add cute messages when system is running perfectly well