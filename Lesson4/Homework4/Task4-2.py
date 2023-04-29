# 2.
names1 = ["John", "Marta", "James", "Amanda", "Marianna"]
list_header = 'NAME'.center(10, '*')
print(f"{list_header}\n")
for name in names1:
 print(name.rjust(10))