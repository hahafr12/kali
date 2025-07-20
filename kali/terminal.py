# kali/terminal.py

import os
import subprocess
import pyfiglet
from termcolor import colored

def load_bashrc():
    bashrc_path = os.path.expanduser("~/.fake_bashrc")
    if os.path.exists(bashrc_path):
        print(colored(">> ~/.bashrc yüklendi", "cyan"))
        with open(bashrc_path, "r") as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    try:
                        subprocess.run(line.strip(), shell=True)
                    except Exception as e:
                        print(colored(f"Hata: {e}", "red"))
    else:
        print(colored(">> ~/.bashrc bulunamadı, atlanıyor.", "yellow"))

def show_banner():
    banner = pyfiglet.figlet_format("KALI TERM", font="slant")
    print(colored(banner, "red"))

def main():
    show_banner()
    load_bashrc()

    while True:
        try:
            cwd = os.getcwd()
            user_input = input(colored(f"┌──(root㉿kali)-[{cwd}]\n└─$", "green")).strip()

            if user_input == "":
                continue
            elif user_input in ['exit', 'quit']:
                print(colored("Terminal kapatılıyor...", "yellow"))
                break
            elif user_input == "neofetch":
                print(colored("User: root", "cyan"))
                print(colored("OS: Kali Linux Rolling", "cyan"))
                print(colored("Kernel: 6.3.0-kali1", "cyan"))
                print(colored("Shell: bash", "cyan"))
                print(colored("Terminal: FakeKali", "cyan"))
            elif user_input.startswith("cd "):
                try:
                    os.chdir(user_input[3:].strip())
                except Exception as e:
                    print(colored(f"cd hatası: {e}", "red"))
            elif any(user_input.startswith(cmd) for cmd in ["git clone", "nmap", "whois", "curl", "ping", "touch", "mkdir", "rm", "ls", "cat "]):
                os.system(user_input)
            else:
                print(colored("Komut tanınmadı!", "red"))

        except KeyboardInterrupt:
            print("\n" + colored("Ctrl+C ile çıkış yapıldı.", "yellow"))
            break
