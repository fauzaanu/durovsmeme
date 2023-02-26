
import requests
from bs4 import BeautifulSoup


async def memedownloader():
    url = "https://imgflip.com/"
    r = requests.get(url)


    soup = BeautifulSoup(r.text, "html.parser")
    with open("index.html", "w") as f:
        f.write(soup.prettify())

    img = soup.find("img", {"class": "base-img"})
    img = img["src"]

    img = "https:" + img

    name = img.split("/")[-1]
    
    # get and delete the last meme if it exists
    try:
        os.remove(f"meme/{os.listdir('meme')[0]}")
    except:
        pass


    with open("meme\\"+name, "wb") as f:
        img = requests.get(img).content
        f.write(img)
        
        
    return name

if __name__ == "__main__":
    memedownloader()