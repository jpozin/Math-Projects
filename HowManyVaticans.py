# Determine how large your city or land area is in units of Vaticans
# Where each Vatican is 0.17 mi^2 (0.44 km^2, 109 acres)

from sys import argv

def landToVaticans(area, units="mi2", prec=3):
	"""Convert a land area to units of Vaticans
	area (float) is the area of your landmass
	units (str) may be 'mi2', 'km2', 'ac', or 'ha'
	prec is the  number of decimal places you want in your final answer
	returns the number of Vaticans (float) that can be fit into your landmass

	For reference:
	Vatican City has a land area of 44 hectares == 108.726 acres == 0.1699 mi^2 == 0.44 km^2"""
	assert units in ("mi2", "km2", "ac", "ha"), "units of land area must be 'mi2', 'km2', 'ac', or 'ha'"
	if units == "mi2":
		vaticans = area / 0.1699
	elif units == "km2":
		vaticans = area / 0.44
	elif units == "ac":
		vaticans = area / 108.726
	elif units == "ha":
		vaticans = area / 44
	return round(vaticans, prec)

if __name__ == '__main__':
	land_name = input("What is the name of your land area?  ")
	assert len(argv) >= 3, "You must supply at least the area (numeric) and units of your land area"
	area, units, prec = float(argv[1]), argv[2], int(argv[3]) if len(argv) >= 4 else 3
	assert units in ("mi2", "km2", "ac", "ha"), "units of land area must be 'mi2', 'km2', 'ac', or 'ha'"
	numVaticans = landToVaticans(area, units, prec)
	final = f"{land_name} has an area of {landToVaticans(area, units, prec)} Vaticans."
	if numVaticans >= 100:
		final += " Wow, that's a lot of Vaticans!"
	elif numVaticans < 1:
		final += " Your land area is tinier than Vatican City!"
	else:
		final += " That's a decent amount of Vatican Cities!"
	print(final)

