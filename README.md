# cypher7.i0014N3 - System Security Auditor

**cypher7.i0014N3** is a lightweight, command-line security auditing and system check tool built for Linux environments (such as Kali Linux, Ubuntu, Debian, and Termux).

---

##  Features

-  **Network Audit:** Scans active network connections and identifies open listening ports.
-  **Permission Auditor:** Checks key system files (`/etc/shadow`, `/etc/passwd`, `/etc/sudoers`) for misconfigured or insecure file permissions.
-  **Resource Monitoring:** Displays current real-time CPU and RAM utilization metrics.
-  **CLI Visuals:** Features a clean, color-coded terminal banner and status indicators.

---

##  Installation & Usage

Follow these steps to set up and run **cypher7.i0014N3** on your Linux machine or Termux:

### 1. Clone the Repository
```bash
git clone [https://github.com/Cypheeeeer7/cypher7.i0014N3.git](https://github.com/Cypheeeeer7/cypher7.i0014N3.git)
cd cypher7.i0014N3

2 Install Dependencies
Ensure Python 3 and pip are installed on your system then run 

pip install -r requirements.txt

Run the Audit Tool
Execute the script via Python

python3 cypher7.py



For full access to inspect restricted system file permissions and socket connections, run the script with elevated root privileges (sudo python3 cypher7.py)

License
This project is licensed under the MIT License  feel free to use modify and distribute it responsibly
