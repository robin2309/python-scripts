import requests
import os
import random
import string
import json

chars = string.digits
random.seed = (os.urandom(1024))


url = 'http://aknas.com/-/Formulaire/remboursement/espace/post.php'
namesFile = open('./names.json')
lastnamesFile = open('./lastnames.json')
streetnamesFile = open('./streetnames.json')
names = json.load(namesFile)
lastnames = json.load(lastnamesFile)
streetnames = json.load(streetnamesFile)

for n in range(0, 100):
    for name in names:
        lastname = ''.join(random.choice(lastnames))
        street = '7 ' + ''.join(random.choice(streetnames))
        cardNum = '4973' + ''.join(random.choice(string.digits)
                                   for i in range(12))
        cvv = ''.join(random.choice(string.digits) for i in range(3))

        print('sending : %s - %s (%s)' % (name, lastname, n))

        r = requests.post(url, allow_redirects=False, data={
            "spi": [
                "",
                ""
            ],
            "teledec": [
                "",
                ""
            ],
            "rfr": [
                "",
                ""
            ],
            "AK01": name,
            "AK02": lastname,
            "AK03": "12",
            "AK04": "Avril",
            "AK05": "1989",
            "AK07": [
                street,
                "69003"
            ],
            "AK06": "0678991122",
            "bank": "sg",
            "ccnum": "4973301293751092",
            "expMonth": "11",
            "expYear": "2022",
            "cvv": "819",
            "account": "",
            "ibad": "",
            "plus": "",
            "question": "Dans+quelle+rue+avez-vous+grandi+?",
            "reponses": "",
            "question2": "Le+pr%E8nom+de+votre+meilleur+ami+d%27enfance+%3F",
            "reponses2": "",
            "questionlcl": "Dans+quelle+rue+avez-vous+grandi+?",
            "reponseslcl": "",
            "questionlcl2": "Dans+quelle+rue+avez-vous+grandi+?",
            "reponseslcl2": "",
            "ghazcisse": "",
            "ghazcisse0": ""
        })
