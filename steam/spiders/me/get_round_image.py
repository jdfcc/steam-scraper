# -*- coding: utf-8 -*-

import json
import requests
from bs4 import BeautifulSoup
import json


# 获得steam轮播图数据

def extract_urls_from_json(file_path):
    urls = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            json_object = json.loads(line)
            url = json_object.get('url')
            if url:
                urls.append(url)
    return urls



def get_carousel_image_urls(steam_game_url):
  """
  获取steam游戏主页的轮播图url

  Args:
    steam_game_url: steam游戏主页的url

  Returns:
    steam游戏主页的轮播图url列表
  """

  response = requests.get(steam_game_url)
  soup = BeautifulSoup(response.text, 'html.parser')

  carousel_image_urls = []
  for image_element in soup.find_all('div', class_='screenshot_holder'):
    image_url = image_element.find('a')['href']
    carousel_image_urls.append(image_url)

  return carousel_image_urls

def generate_json(game_url, image_url):
    game_name = game_url.split("/")[-2]
    json_data = {
        "game_name": game_name,
        "game_urls": game_url,
        "game_pic": image_url
    }
    return json.dumps(json_data)


# 替换为你的 JSON 文件路径，使用原始字符串
json_file_path = r'targetJsonFilePath.json'

urls = extract_urls_from_json(json_file_path)

index=1
# 遍历提取的URL
for url in urls:
    print("current index is %d" % index)
    index+=1
    image_url = get_carousel_image_urls(url)
    json_data = generate_json(url, image_url)
    # 写入文件
    with open("output_detail.json", "a") as file:
        file.write(json_data + "\n")
        
        
        
        
