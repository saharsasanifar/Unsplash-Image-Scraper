import requests
from bs4 import BeautifulSoup
import os

URL = "https://unsplash.com/"
BASE_DIR = "downloaded_images"

#function to connect -----------------------------------------------------------------------
def send_req(url):

    response = requests.get(url)
    if response.status_code == 200:
        print("connected succesfully.")
        return response
    
    else:
        print("connection failed.")
        return None

#getting photos ----------------------------------------------------------------------------
def get_photos_data(url):
    response = send_req(url)
    if response:
        soup = BeautifulSoup(response.text, 'html.parser')
        photos = soup.find_all('img')
        photos_data = []
        for photo in photos:
            title = photo.img['alt']
            img_link = photo.find('img')['src']
            img_link = URL + img_link
            user_name = photo.find('span', class_="N25dY")['href']
            data = {
                'title' : title,
                'img_link': img_link,
                'user_name' :user_name
            }
            photos_data.append(data)
        return photos_data

    else:
        return[]
    
#save imge--------------------------------------------------------------------
def save_img(content, path):
    try:
        with open(path , "wb" ) as img:       #wb ==> binary
            img.write(content)
    except Exception as e :
        print (e)

#download image----------------------------------------------------------------
def download_img(title, img_url, folder):
    response = send_req(img_url)
    if response:
        path = os.path.join(folder, title + ".jpg")
        save_img(response.content, path)  #use content becuse it's photo and binary
    else:
        return None
    
#create directory---------------------------------------------------------------
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    


#test for running_________________________________________________________
photos = get_photos_data(URL)
for photo in photos:
    title = photo['title']
    title = title.replace(" ", "_")
    photo_dir = os.path.join(BASE_DIR, title)  #make the direction
    create_dir(photo_dir)
    download_img(photo['img_link'], photo_dir)
