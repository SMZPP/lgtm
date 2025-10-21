import os
import requests
from datetime import datetime

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
SAVE_DIR = "images"

def fetch_image():
    headers = {"Authorization": PEXELS_API_KEY}
    query = "nature"  # キーワード（例：風景）
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=1"

    response = requests.get(url, headers=headers)
    data = response.json()

    if "photos" not in data or len(data["photos"]) == 0:
        print("画像が見つかりませんでした。")
        return None

    photo = data["photos"][0]
    image_url = photo["src"]["large2x"]

    os.makedirs(SAVE_DIR, exist_ok=True)
    filename = f"{datetime.now().strftime('%Y%m%d')}.jpg"
    filepath = os.path.join(SAVE_DIR, filename)

    img_data = requests.get(image_url).content
    with open(filepath, "wb") as f:
        f.write(img_data)

    print(f"✅ 画像を保存しました: {filepath}")
    return filepath

if __name__ == "__main__":
    fetch_image()
