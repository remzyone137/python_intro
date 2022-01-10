import requests # perform http requests like GET or POST
import os
from dotenv import load_dotenv
load_dotenv()

if "WEATHERKEY" in os.environ:
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Barcelona&appid='+os.environ['WEATHERKEY'])
else:
    print("WEATHERKEY is not defined in .env")

data = r.json()
conditions = data['weather'][0]['main']
print(data['weather'][0]['main'])
if "BOTKEY" in os.environ:
    r = requests.post('https://api.telegram.org/bot'+os.environ['BOTKEY']+'/sendMessage', data={'chat_id': 1489050951, 'text': 'Remo is the coolest1. And the weateher in barcelona is ' + conditions})
else:
    print("BOTKEY is not defined in .env")
