import vk_api
import requests

with open("TOKEN") as file:
    UTOKEN = file.readline()
session = vk_api.VkApi(token=UTOKEN)
vk = session.get_api()


def get_saved(url, name_template="0", offset=0, count = 25):
    owner_id = str(url).split("/")[-1].split("_")[0][5::]
    photos = vk.photos.get(owner_id=owner_id, album_id="saved", offset=offset, count=count)
    i = 1
    for x in photos['items']:
        print(x['sizes'][-1])

        photo = requests.get(f"{x['sizes'][-1]['url']}")
        with open(f"/home/augustus/Pictures/Wallpapers/saved/{name_template}{offset + i}.jpg", "wb") as file:
            file.write(photo.content)
        i += 1


if __name__ == "__main__":
    url = input("url")
    name_template = input("name")
    offset = int(input('offset'))
    count = int(input('count'))
    get_saved(url,name_template,offset,count)
