# https://infraligne.evonesuivenete.com/id=1/infoz/infos.php
# 104.21.3.51
#{
# 	"nom": "Spinoza",
# 	"prenom": "Costa",
# 	"ddn": "03/04/2000",
# 	"email": "spinoza.costa@gmail.com",
# 	"tel": "06+92+84+75+76"
# }

import concurrent.futures
import requests
import os
import random
import string
import json
import traceback
import requests_cache
import threading

chars = string.digits
random.seed = (os.urandom(1024))

# Initialize a lock for thread-safe cache access
cache_lock = threading.Lock()

# Set the maximum number of requests to send concurrently
max_concurrent = 10

requests_cache.install_cache('my-cache', expire_after=600)
requests_cache.clear()  # Clear old cache entries

url = 'https://infraligne.evonesuivenete.com/id=1/infoz/infos.php'
namesFile = open('../../names.json')
lastnamesFile = open('../../lastnames.json')
domainnamesFile = open('../../mail-domains.json')
birthDatesFile = open('../../birth-dates.json')
names = json.load(namesFile)
lastNames = json.load(lastnamesFile)
domainNames = json.load(domainnamesFile)
birthDates = json.load(birthDatesFile)

bodies = []

def processBody(body):
    try:
        with cache_lock:
            return requests.post(url, json=body)
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()
        None

shortenedNames = names[:10]

for n in range(0, 3):
    for name in names:
        lastName = ''.join(random.choice(lastNames))
        birthDate = ''.join(random.choice(birthDates))
        domainName = ''.join(random.choice(domainNames))
        num1 = ''.join(random.choice(string.digits) for i in range(2))
        num2 = ''.join(random.choice(string.digits) for i in range(2))
        phoneNumber = '+'.join(['06', num1, num2, num1, num2])

        bodyToAdd = {
            "nom": lastName,
            "prenom": name,
            "ddn": birthDate,
            "email": name + '.' + lastName + '@' + domainName,
            "tel": phoneNumber
        }

        bodies.append(bodyToAdd)

print('bodies prepared : %s' % (len(bodies)))

# Use a ThreadPoolExecutor to send the requests concurrently
with concurrent.futures.ThreadPoolExecutor(max_concurrent) as executor:
  # Submit a task to send each request
  futures = [executor.submit(processBody, body) for body in bodies]
  
  # Iterate through the completed tasks
  for i, future in enumerate(concurrent.futures.as_completed(futures)):
    response = future.result()
    if response.status_code == 200 or response.status_code == 302:
      print(f'Successfully sent request {i}')
    else:
      print(f'Error sending request {i}: {response.status_code}')
