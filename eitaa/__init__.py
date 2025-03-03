# Eitaa PyKit
# v1.0
import requests
from bs4 import BeautifulSoup 
def get_info(channel_id):
    r = requests.get(f"https://eitaa.com/{channel_id}")
    soup = BeautifulSoup(r.text, 'html.parser')
        
    channel_name = soup.find('div', attrs = {'class':'tgme_page_title'}).text
    
    channel_image_url = soup.find('img', attrs = {'class':'tgme_page_photo_image'})['src'] 

    users_count = (str(soup.find('div', attrs = {'style':'display: block;text-align: center;font-weight: bold'}).text).split(' '))[0]
    desc = soup.find('div', attrs = {'class':'text-center'}).text 

    

    result = {
        'name' : " ".join(channel_name.split()),
        'image_url' : channel_image_url,
        'users' : users_count,
        'desc' : desc,
    }
    return result

def send_message(token,chat_id,text,pin=False):
    r = requests.post(
        f"https://eitaayar.ir/api/{token}/sendMessage",
        data = {
            'chat_id' : chat_id,
            'text' : text,
            'pin' : int(pin)
        }
    )
    return bool(r.json()['ok'])

def send_file(token,chat_id,caption,file,pin=False):
    r = requests.post(
        f"https://eitaayar.ir/api/{token}/sendFile",
        data = {
            'chat_id' : chat_id,
            'caption' : caption,
        },
        files={
            'file': open(file,'rb'),
        }
    )
    print(r.json())
    return bool(r.json()['ok'])