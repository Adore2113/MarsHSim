# MarsHSim
    - this file is currently being organized -

## Sim loop: 
    ♡ time steps

## V1 goal:
    ♡ closed loop ECLSS monitoring, logging, alerts, simple controllers

    ♡ Habitat size of 8,191 m² (44,762 m³) in Arcadia Planitia (47° North, 184° East)

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


