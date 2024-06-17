def get_wave_type(wavelength):
    if wavelength < 1e-11:
        type_of_wave = "a Gamma wave"
    elif 1e-11 <= wavelength < 1e-8:
        type_of_wave = "an X-Ray wave"
    elif 1e-8 <= wavelength < 3.8e-7:
        type_of_wave = "an Ultraviolet wave"
    elif 3.8e-7 <= wavelength < 7.5e-7:
        type_of_wave = "a Visible wave"
    elif 7.5e-7 <= wavelength < 1e-3:
         type_of_wave = "an Infrared wave"
    elif 1e-3 <= wavelength < 1:
        type_of_wave = "a Microwave wave"
    else:
        type_of_wave = "a Radio wave"
    return type_of_wave