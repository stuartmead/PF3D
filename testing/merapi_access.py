"""Configuration file for eruption scenario

Tephra modelling validation worksheet                 

Scenario Name: Mount Merapi 2010 (Predictive_scenario)                                                                    
Run Date: 2010_05_18           
Run number:1                                                                                   

Eruption observation details: 

"""

# Short eruption comment to appear in output directory.
Eruption_comment = 'using ACCESS-T data'

# Time (Volcanological input file)
#Eruption_Year = 2010                            # YYYY  
#Eruption_Month = 11                             # MM  
#Eruption_Day = 9                               # DD 
#Start_time_of_meteo_data = 12                    # Hours after 00 UTC
#Meteo_time_step = 180                            # Mins       
#End_time_of_meteo_data = 24                      # Hours after 00
#Start_time_of_eruption = 14              # Hours after 00
#End_time_of_eruption = 16                        # Hours after 00 
#End_time_of_run = 24                             # Hours after 00  

# When specified alone, these are in hours relative to the start of meteo data
Start_time_of_eruption = 2              
End_time_of_eruption = 4                
End_time_of_run = 8

# Location (Volcanological input file)
X_coordinate_of_vent = 439423                   # UTM zone implied by topography projection 
Y_coordinate_of_vent = 9167213                  # UTM zone implied by topography projection

# Vertical discretisation for model domain
Z_min = 0.0
Z_max = 50000
Z_increment = 10000

# Select meteorological parameters
wind_profile = 'IDY25100_2010110912_24h_merapi.profile'

# Granulometry (Volcanological input file)
Grainsize_distribution = 'GAUSSIAN'             # Possibilites are GAUSSIAN/BIGAUSSIAN
Number_of_grainsize_classes = 6
Mean_grainsize = 2.5                            # phi
Sorting = 1.5
Minimum_grainsize = 0                           # phi
Maximum_grainsize = 5                           # phi
Density_minimum = 1200                          # kg/m3
Density_maximum = 2300                          # kg/m3
Sphericity_minimum = 0.9
Sphericity_maximum = 0.9

# Source (Volcanological input file)
Vent_height = 2968
Source_type = 'suzuki'                          # Possibilities are 'plume', 'suzuki', 'point'
Mass_eruption_rate = 'estimate'                 # kg/s (if point, if suzuki or if plume where Height_or_MFR = MFR)
Height_above_vent = [40000, 30000, 20000, 10000, 5000, 2000, 1000] # m (if point, if suzuki or if plume where Height_or_MFR = Height)            
A = 3                                       # (suzuki only)            
L = 1                                       # (suzuki only)
Height_or_MFR = 'MFR'                           # plume only
MFR_minimum = 1e7                               # kg/s (plume only)
MFR_maximum = 1e9                               # kg/s (plume only) 
Exit_velocity = 100                             # m/s (plume only)
Exit_temperature = 1073                         # K (plume only)
Exit_volatile_fraction = 0                      # % (plume only)

# Fall3D (Volcanological input file)
Terminal_velocity_model = 'ganser'              # Possibilites are ARASTOOPOR/GANSER/WILSON/DELLINO
Vertical_turbulence_model = 'similarity'        # Possibilites are CONSTANT/SIMILARITY
Horizontal_turbulence_model = 'rams'            # Possbilities are CONSTANT/RAMS
Vertical_diffusion_coefficient = 100            # m2/s
Horizontal_diffusion_coefficient = 1000         # m2/s
Value_of_CS = 0.1                               # RAMS only

# Output (Volcanological input file)
Postprocess_time_interval = 1                   # Hours
Postprocess_3D_variables = 'No'                 # Yes/No
Postprocess_classes = 'No'                      # Yes/No
Track_points = 'No'                             # Yes/No

Topography_grid = 'merapi_topography.txt'       # Specify ASCII topography grid to use. 
                                                # If empty, AIM will look for a topography grid named
                                                # <scenario_name>.top (surfer GRD format)         
                                                
# Contouring:
#   False: Disabled
#   True: Provide a fixed number of contours covering entire range
#   Number: Fixed (vertical) interval between contours
#   List of numbers: Exact contour levels
Thickness_contours = [1, 2, 5, 50, 100]         # True, False, number or list of numbers
Thickness_units = 'cm'                          # mm/cm/m

Load_contours = 2000                            # True, False, number or list of numbers    

# Run model using specified parameters
if __name__ == '__main__':

    import time, random
    from aim import run_scenario
    
    run_scenario(__file__, 
                 timestamp_output=True,    
                 dircomment=Eruption_comment)


 



