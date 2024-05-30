import requests

URL = "https://unsplash.com/"

#function to connect -----------------------------------------------------------------------
def send_req(url):

    response = requests.get(url)
    if response.status_code == 200:
        print("connected succesfully.")
    
    else:
        print("connection failed.")


#getting photos ----------------------------------------------------------------------------
def get_photos(url):
    response = send_req(url)
    if response:
        pass

    else:
        return[]
    
get_photos(URL)