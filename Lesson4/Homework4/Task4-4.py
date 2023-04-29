my_dict = {'Python': 'Guido van Rossum', 'PHP': 'Rasmus Lerdorf', 'Java': 'James Gosling',
           'Ruby': 'Yukihiro Matsumoto'}
for prog_lang, person in my_dict.items():
    print(f'My favorite programing language is {prog_lang}. It was created by {person}.')
del my_dict['PHP']
print(my_dict)