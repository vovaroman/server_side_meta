import requests
from bs4 import BeautifulSoup
import re
import json

r = requests.get('http://fmstream.org/index.php?c=AFG')


soup = BeautifulSoup(r.text, "html.parser")

script = soup.find_all('script')[2]

script = str(script)[19:str(script).find(']]];') + 3]

sentence = re.sub(r"\s+", "", script, flags=re.UNICODE)

sentence = re.sub(r'(?<=,)\s*,', ' null,', sentence)

print(sentence)

data = json.loads(sentence)

print(sentence)

