# Project name: MarsHSim

## Sim loop: discrete time steps

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