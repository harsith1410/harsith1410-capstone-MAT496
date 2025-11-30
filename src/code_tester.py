import random

l=[]

for i in range(1000000):
    bias = [0.2, 0.8]
    weather = random.choices(["Wet", "Dry"], weights=bias, k=1)[0]
    l.append(weather)


print(l.count("Wet"),"------",l.count("Dry"))
