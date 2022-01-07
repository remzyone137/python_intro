import requests
   
# Making a GET request
r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Barcelona&appid=6b0c557e8fdcf766b82c030af6dc1b10')
  
# check status code for response received
# success code - 200

# print content of request
data = r.json()
conditions = data['weather'][0]['main']
print(data['weather'][0]['main'])
# 1489050951
# curl -s -X POST https://api.telegram.org/bot5077725422:AAHMHH5S9_dzJt0UuSjMSCuwJ-BlTkonxFY/sendMessage -d chat_id=1489050951 -d text="Remo is the coolest1"
r = requests.post('https://api.telegram.org/bot5077725422:AAHMHH5S9_dzJt0UuSjMSCuwJ-BlTkonxFY/sendMessage', data={'chat_id': 1489050951, 'text': 'Remo is the coolest1. And the weateher in barcelona is ' + conditions})