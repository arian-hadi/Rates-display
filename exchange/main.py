import requests
import json
from config import url,rules
from mail import send_smtp_email

def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None

def archive(filename, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates)) #this method is always used to get a specific value in JSON

def send_mail(timestamp, rates):
    subject  = f"{timestamp} rates"
    tmp = dict()
    if rules["preferred"] is not None:
        for exc in rules["preferred"]:
            tmp[exc] = rates[exc]
        rates = tmp 
    text = json.dumps(rates)
    send_smtp_email(subject, text)

    
if __name__ == "__main__":
    res = get_rates() #Gets the JSON values and turn them into dictionaries
    if rules["archive"]:
        archive(res["timestamp"], res["rates"]) #now we pick the only dictionary values we want and turn them into a string again
    if rules["send_mail"]:
        send_mail(res["timestamp"], res["rates"])
