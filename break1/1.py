for x in range(int(1000** 1/3)):
    for y in range(int(1000 ** 1 / 4)):
        for z in range(int(1000 ** 1 / 2)):
            if x**3 + y ** 4 + z ** 2 == 1000:
                print(f'x={x}, y={y}, z={z}')