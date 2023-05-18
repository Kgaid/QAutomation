import json

with open('group_people.json') as file:
    data = json.load(file)

max_women_count = 0
max_women_group_id = None

for group in data:
    group_id = group['id_group']
    people = group['people']
    women_count = 0

    for person in people:
        if person['gender'] == 'Female' and person['year'] > 1977:
            women_count += 1

    if women_count > max_women_count:
        max_women_count = women_count
        max_women_group_id = group_id

print(" Group with max count of women after 1977:", max_women_group_id)
print("Count of women born after 1977:", max_women_count)
print(data)




