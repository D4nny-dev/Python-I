def format_data(city,country,population=''):
    if population:
        format = city.title() +" "+ country.title()+" | "+ str(population)
    else:
        format = city.title() +" "+ country.title()
    return format