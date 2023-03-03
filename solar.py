def main():
    import pandas as pd
    import pvlib

    from pvlib.modelchain import ModelChain
    from pvlib.location import Location
    from pvlib.pvsystem import PVSystem
    from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS

    location = Location(latitude=29.98253149331617, longitude=31.316339338615187, tz='Africa/Cairo',altitude=50, name='Carfore')
    
    sandia_modules = pvlib.pvsystem.retrieve_sam('SandiaMod')
    cec_inverters = pvlib.pvsystem.retrieve_sam('CECInverter')

    module = sandia_modules['Canadian_Solar_CS5P_220M___2009_']
    inverter = cec_inverters['ABB__MICRO_0_25_I_OUTD_US_208__208V_']
    temperature_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']
    system =PVSystem(surface_tilt=45, surface_azimuth=180, 
                     module_parameters=module, inverter_parameters=inverter, 
                     temperature_model_parameters=temperature_parameters)
    #print(system)
    modelchain = ModelChain(system,location)
    print(modelchain)
main()