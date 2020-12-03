dict = {'x': 500, 'y': 5874, 'z': 560}

max = max(dict.keys(), key=(lambda k: dict[k]))
min = min(dict.keys(), key=(lambda k: dict[k]))

print('Maximum Value: ', dict[max])
print('Minimum Value: ', dict[min])
