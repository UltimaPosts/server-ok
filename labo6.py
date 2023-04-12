import os
import sys
import json
import logging
import time
from colorama import Fore, Style







def check_ping():

    with open("servers.json", "r") as servers:
        hostnames = json.load(servers)
    with open("index.html", "r") as html_logger:
        html_text = html_logger.read()
    content = ""
    for hostname in hostnames:
        response = os.system("ping -n 1 " + hostname)
        # and then check the response...
        if response == 0:
            pingstatus = "Network Active"
        else:
            pingstatus = "Network Error"

        print(Fore.GREEN + pingstatus)
        print(Style.RESET_ALL)

        content = content + f"<li>{hostname} --- {pingstatus}</li>"

    front = html_text[:263]
    middle = html_text[263: -24]
    end = html_text[-24:]

    html_join = front + middle + content + end
    with open("index.html", "w") as html_logger:
        html_logger.write(html_join)





while(True):
    pingstatus = check_ping()
    print(pingstatus)
    logging.basicConfig(filename = "LogFile.json", 
                        format = "%(asctime)s %(message)s", filemode = "w")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info(pingstatus)
    time.sleep(5)




