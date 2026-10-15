#!/usr/bin/env python3
import os
import sys
import psutil
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.GREEN}
  ██████╗██╗   ██╗██████╗ ██╗  ██╗███████╗██████╗ █║██████╗ ██████╗ ███╗   ██╗██████╗ 
 ██╔════╝╚██╗ ██╔╝██╔══██╗██║  ██║██╔════╝██╔══██╗██║██╔═██╗██╔═██╗████╗  ██║╚════██╗
 ██║      ╚████╔╝ ██████╔╝███████║█████╗  ██████╔╝██║██║  ██║██║  ██║██╔██╗ ██║ █████╔╝
 ██║       ╚██╔╝  ██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗██║██║  ██║██║  ██║██║╚██╗██║ ╚═══██╗
 ╚██████╗   ██║   ██║     ██║  ██║███████╗██║  ██║██║╚██████║╚██████║██║ ╚████║██████╔╝
  ╚═════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝╚═╝  ╚═══╝╚═════╝ 
                      // SECURITY & AUDIT SYSTEM v1.0 //
{Style.RESET_ALL}"""

def check_root():
    if os.geteuid() != 0:
        print(f"{Fore.YELLOW}[!] Warning: Running without root privileges. Some system checks may be restricted.{Style.RESET_ALL}")

def audit_system():
    print(f"\n{Fore.CYAN}[+] Starting System Audit & Security Checks...{Style.RESET_ALL}\n")

    # 1. Open Ports Check
    print(f"{Fore.BLUE}[1] Scanning Listening Network Services:{Style.RESET_ALL}")
    connections = psutil.net_connections(kind='inet')
    listening = [conn for conn in connections if conn.status == 'LISTEN']
    
    if listening:
        for conn in listening:
            print(f"    - Port {conn.laddr.port} is OPEN (PID: {conn.pid})")
    else:
        print(f"    {Fore.GREEN}[✓] No unauthorized listening ports found.{Style.RESET_ALL}")

    # 2. Critical File Permissions
    print(f"\n{Fore.BLUE}[2] Checking Critical System File Permissions:{Style.RESET_ALL}")
    critical_files = ['/etc/passwd', '/etc/shadow', '/etc/sudoers']
    
    for filepath in critical_files:
        if os.path.exists(filepath):
            st = os.stat(filepath)
            permissions = oct(st.st_mode)[-3:]
            if filepath == '/etc/shadow' and permissions != '600' and permissions != '640':
                print(f"    {Fore.RED}[×] WARNING: {filepath} permissions are insecure ({permissions}){Style.RESET_ALL}")
            else:
                print(f"    {Fore.GREEN}[✓] {filepath} permissions OK ({permissions}){Style.RESET_ALL}")

    # 3. System Memory and Resource Usage
    print(f"\n{Fore.BLUE}[3] System Resource Overview:{Style.RESET_ALL}")
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    print(f"    - CPU Usage: {cpu}%")
    print(f"    - Memory Usage: {memory}%")

    print(f"\n{Fore.GREEN}[✔] Audit Completed Successfully.{Style.RESET_ALL}")

if __name__ == '__main__':
    print(BANNER)
    check_root()
    audit_system()
  
