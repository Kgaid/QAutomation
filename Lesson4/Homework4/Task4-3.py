# 3.
import re

cc_list = ["FirstItem", "FriendsList", "MyTuple"]
sc_list = []
for letter in cc_list:
    sc_var = re.sub(r'(?<!^)(?=[A-Z])', '_', letter).lower()
    sc_list.append(sc_var)
print(sc_list)
