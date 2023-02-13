phrase = input('Enter a phrase: ')
lst_phrase = phrase.split()

acronym = ""

for i in lst_phrase:
    acronym = i[0] + acronym

print(acronym)