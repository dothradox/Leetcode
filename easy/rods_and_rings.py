rings = "B0B6G0R6R0R6G9"
pole = {}
color = {}
for i in range(0, len(rings), 2):
    if rings[i] not in pole[rings[i + 1]]:
        pole[rings[i + 1]] = color.add(rings[i])

    print(rings[i], rings[i + 1])
