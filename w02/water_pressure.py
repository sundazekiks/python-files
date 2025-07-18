# Water Pressure Milestone Project CSS111

# Water Column Height Function
def water_column_height(tower_height, tank_height):

    h = tank_height + (3 * tower_height / 4)
    return h
# Pressure Gain From Height Function
def pressure_gain_from_water_height(height):
    p = (998.2 * 9.80665 * height) / 1000
    return p
# Calculate the lost pressure in kilopascals
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    p = (friction_factor * pipe_length * fluid_velocity**2) / (2000 * pipe_diameter)
    return p
# Pressure lost from fittings function
def pressure_lost_from_fittings(fluid_velocity, quantity_fittings):
    p = (-0.04 * 998.2 * fluid_velocity**2 * quantity_fittings) / 2000
    return p
# Reynolds Number
def reynolds_number(hydraulic_diameter, fluid_velocity):
    r = (998.2 * hydraulic_diameter * fluid_velocity) / 0.0010016
    return r
# Pressure loss from pipe reduction function
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, renolds_number, smaller_diameter):
    
    k = (0.1 + (50 / renolds_number)) * ((larger_diameter / smaller_diameter)**4 - 1)
    p = (-k * 998.2 * fluid_velocity**2) / 2000
    
    return p