scores = {"Meera": 88, "Rohan": 95, "Kabir": 79}

by_key = dict(sorted(scores.items()))

by_value = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))

