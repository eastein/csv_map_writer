import svgcuts
import csv
import sys
import math

if __name__ == '__main__' :
	polys = {}
	max_x = 0.0
	max_y = 0.0
	min_x = math.pow(2, 40)
	min_y = math.pow(2, 40)

	mult = 0.00000663790307274524
	for row in csv.DictReader(open(sys.argv[1])) :
		polyid = long(row['Polygon Id'])
		x = float(row['X'])
		y = float(row['Y'])
		max_x = max(max_x, x)
		max_y = max(max_y, y)
		min_x = min(min_x, x)
		min_y = min(min_y, y)

	w_x = max_x - min_x
	w_y = max_y - min_y
	mult = 8.0 / w_x

	for row in csv.DictReader(open(sys.argv[1])) :
		polyid = long(row['Polygon Id'])
		x = (float(row['X']) - min_x) * mult
		y = (float(row['Y']) - min_y) * mult

		polys.setdefault(polyid, list())
		polys[polyid].append(svgcuts.Point(x + 1.0, y + 1.0))

	#print max_x
	#print max_y

	sx = 8.0 + 2.0
	sy = 12.9549897848 + 2.0

	l = svgcuts.Layer(sx, sy, unit='in')

	for id, points in polys.items() :
		n = len(points)
		for i in range(n) :
			j = (i + 1) % n
			l.add_line(svgcuts.Line(points[i], points[j]))

	l.write('lol_map.svg')
