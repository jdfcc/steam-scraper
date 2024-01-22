import requests
from bs4 import BeautifulSoup
import json


# 获得steam大图数据


def extract_urls_from_json(file_path):
    urls = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            json_object = json.loads(line)
            url = json_object.get('url')
            if url:
                urls.append(url)
    return urls

def extract_ids_from_json(file_path):
    ids = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            json_object = json.loads(line)
            id = json_object.get('id')
            if id:
                ids.append(id)
    return ids

def generate_json(game_url, image_url,id):
    game_name = game_url.split("/")[-2]
    json_data = {
        "id": id,
        "game_name": game_name,
        "game_url": game_url,
        "game_pic": image_url
    }
    return json.dumps(json_data)



# def get_image_url(steam_game_url):
#     """
#     获取steam游戏主页的主图url

#     Args:
#         steam_game_url: steam游戏主页的url

#     Returns:
#         steam游戏主页的主图url
#     """
#     response = requests.get(steam_game_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     image_url = soup.find('meta', property='og:image')['content']
#     return image_url


def get_image_url(steam_game_url):
    """
    获取steam游戏主页的主图url

    Args:
        steam_game_url: steam游戏主页的url

    Returns:
        steam游戏主页的主图url
    """
    response = requests.get(steam_game_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for image_element in soup.find_all('div', class_='game_header_image_ctn'):
      image_url = image_element.find('img')['src']
    return image_url


# 替换为你的 JSON 文件路径，json内容为
# targetJsonFilePath.json
# {"url": "https://store.steampowered.com/app/1623730/Palworld/", "reviews_url": "http://steamcommunity.com/app/1623730/reviews/?browsefilter=mostrecent&p=1", "id": "1623730", "title": "Palworld", "genres": ["Action", "Adventure", "Indie", "RPG", "Early Access"], "developer": "PocketpairPublisher:Pocketpair            Release Date: 18 Jan, 2024", "publisher": "Developer:PocketpairPocketpair            Release Date: 18 Jan, 2024", "release_date": "Developer:PocketpairPublisher:Pocketpair             18 Jan, 2024", "app_name": "Palworld", "tags": ["Multiplayer", "Open World", "Creature Collector", "Survival", "Open World Survival Craft", "Crafting", "Co-op", "Adventure", "Sandbox", "Third-Person Shooter", "Action", "Automation", "Anime", "RPG", "Looter Shooter", "PvE", "3D", "Indie", "Early Access", "Hack and Slash"], "price": "¥ 700", "sentiment": "Very Positive", "early_access": true}
# {"url": "https://store.steampowered.com/app/2381590/not_available/", "reviews_url": "http://steamcommunity.com/app/2381590/reviews/?browsefilter=mostrecent&p=1", "id": "2381590", "title": "not available", "genres": ["Adventure", "Casual", "Indie", "Simulation"], "developer": "IndiesolodevPublisher:Indiesolodev            Release Date: 24 May, 2023", "publisher": "Developer:IndiesolodevIndiesolodev            Release Date: 24 May, 2023", "release_date": "Developer:IndiesolodevPublisher:Indiesolodev             24 May, 2023", "app_name": "not available", "tags": ["Parkour", "3D Platformer", "Difficult", "Psychological Horror", "Casual", "Adventure", "Third Person", "Bullet Time", "Open World", "Physics", "Exploration", "Platformer", "Story Rich", "Arcade", "Replay Value", "Atmospheric", "Multiplayer", "Roguelike", "Simulation", "Cinematic"], "sentiment": "Mostly Positive", "early_access": false}
# {"url": "https://store.steampowered.com/app/105600/Terraria/", "reviews_url": "http://steamcommunity.com/app/105600/reviews/?browsefilter=mostrecent&p=1", "id": "105600", "title": "Terraria", "genres": ["Action", "Adventure", "Indie", "RPG"], "developer": "Re-LogicPublisher:Re-Logic            Release Date: 16 May, 2011", "publisher": "Developer:Re-LogicRe-Logic            Release Date: 16 May, 2011", "release_date": "Developer:Re-LogicPublisher:Re-Logic             16 May, 2011", "app_name": "Terraria", "tags": ["Open World Survival Craft", "Sandbox", "Survival", "2D", "Multiplayer", "Adventure", "Pixel Graphics", "Crafting", "Building", "Exploration", "Co-op", "Open World", "Online Co-Op", "Indie", "Action", "RPG", "Singleplayer", "Replay Value", "Platformer", "Atmospheric"], "price": "¥ 1200", "sentiment": "Overwhelmingly Positive", "metascore": 83, "early_access": false}
# {"url": "https://store.steampowered.com/app/289070/Sid_Meiers_Civilization_VI/", "reviews_url": "http://steamcommunity.com/app/289070/reviews/?browsefilter=mostrecent&p=1", "id": "289070", "title": "Sid Meier’s Civilization® VI", "genres": ["Strategy"], "developer": "Firaxis Games, Aspyr (Mac), Aspyr (Linux)Publisher:2K, Aspyr (Mac), Aspyr (Linux)Franchise:Sid Meier's Civilization            Release Date: 20 Oct, 2016", "publisher": "Developer:Firaxis Games, Aspyr (Mac), Aspyr (Linux)2K, Aspyr (Mac), Aspyr (Linux)Franchise:Sid Meier's Civilization            Release Date: 20 Oct, 2016", "release_date": "Developer:Firaxis Games, Aspyr (Mac), Aspyr (Linux)Publisher:2K, Aspyr (Mac), Aspyr (Linux)Franchise:Sid Meier's Civilization             20 Oct, 2016", "app_name": "Sid Meier’s Civilization® VI", "tags": ["Strategy", "Turn-Based Strategy", "Multiplayer", "Historical", "Singleplayer", "Grand Strategy", "Turn-Based", "4X", "War", "Simulation", "City Builder", "Tactical", "Building", "Management", "Great Soundtrack", "Moddable", "Online Co-Op", "Co-op", "Hex Grid", "Atmospheric"], "price": "¥ 9791", "sentiment": "Very Positive", "metascore": 88, "early_access": false}

json_file_path = r'targetJsonFilePath.json'

urls = extract_urls_from_json(json_file_path)
ids=extract_ids_from_json(json_file_path)

index=0
# 遍历提取的URL
for url in urls:
    print("current index is %d" % index)
    id=ids[index]
    index+=1
    image_url = get_image_url(url)
    json_data = generate_json(url, image_url,id)
    # 写入文件
    with open("output.json", "a") as file:
        file.write(json_data + "\n")