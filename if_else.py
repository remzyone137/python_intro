name = input('Bitte gib deinen Namen ein: ')
mein_name = 'Klaus'
age = '12'
city = 'Gotham City'

is_woman = input('Bitte gib dein Geschlecht an (w/m/d): ') # ??? true/false

# is_woman = True

if is_woman == "w":
    print('Sehr geehrte Frau ' + name + ',')
elif is_woman == "m":
    print('Sehr geehrter Herr ' + name + ',')
else:
    print('Sehr geehrte Person ' + name + ',')


print('mein Name ist ' + mein_name + '.')
print('Ich bin ' + age + ' Jahre alt,')
print('und komme aus ' + city + '.')
