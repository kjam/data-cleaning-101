output = []

for loc in locations:
    issloc = delayed(get_spaceship_location)()
    next_pass = delayed(iss_pass_near_loc)(loc)
    output.append((loc.get('name'), next_pass))

earliest = delayed(lambda x: sorted(x, key=itemgetter(1))[0])(output)

earliest.compute()
