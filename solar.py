def main():
    import pandas as pd
    import matplotlib.pyplot as plt
    import pvlib

    from pvlib.modelchain import ModelChain
    from pvlib.location import Location
    from pvlib.pvsystem import PVSystem
    from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS

    location = Location(latitude=29.98253149331617, longitude=31.316339338615187, tz='Africa/Cairo',altitude=50, name='Carfore')
    
    sandia_modules = pvlib.pvsystem.retrieve_sam('SandiaMod')
    cec_inverters = pvlib.pvsystem.retrieve_sam('CECInverter')

    module = sandia_modules['Canadian_Solar_CS5P_220M___2009_']
    inverter = cec_inverters['iPower__SHO_5_2__240V_']
    temperature_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']
    system =PVSystem(surface_tilt=45, surface_azimuth=180, 
                     module_parameters=module, inverter_parameters=inverter, 
                     temperature_model_parameters=temperature_parameters,
                     modules_per_string=10, strings_per_inverter=3)
    #print(module['Impo'] * module['Vmpo'] * 10)
    #print(inverter)
    modelchain = ModelChain(system,location)
    #print(modelchain)
    times = pd.date_range(start='2021-07-01', end='2021-07-02', freq='30min', tz=location.tz)
    clear_sky = location.get_clearsky(times)

    clear_sky.plot(figsize=(9,4))
    plt.show()

    modelchain.run_model(clear_sky)
    modelchain.results.dc.plot(figsize=(9,4))
    plt.show()
main()