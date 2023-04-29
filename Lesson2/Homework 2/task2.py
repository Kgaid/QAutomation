v1 = float(input('Please enter first volume: '))
v2 = float(input('Please enter second volume: '))
t1 = float(input('Please enter first temperature: '))
t2 = float(input('Please enter second temperature: '))
vol = v1 + v2
temp = str((v1*t1 + v2*t2) / vol)
vol = str(vol)
print("Temperature =" + temp + "C", "Volume =" + vol + "l")