stundenlohn = input('Bitte gebe Deinen STundenlohn ein: ')
tag = 8 * int(stundenlohn)
monat = tag * 20
year = monat * 12

print('Dein Stundenlohn beträgt ' + str(stundenlohn) + '€')
print('Du verdienst ' + str(tag) + '€ pro Tag')
print('Und Du verdienst pro Monat ' + str(monat) + '€')
print('Und im Jahr bekommst Du gerade mal ' + str(year) + '€')

input('')