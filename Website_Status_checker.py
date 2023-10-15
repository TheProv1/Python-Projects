import requests

def check_status(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            print("Website is up and running")
        else:
            print("Website is unreachable")

    except requests.ConnectionError:
        print("Error, website url or address is not currently available")

web_link = input("Enter the name of the website: ")

check_status(web_link)