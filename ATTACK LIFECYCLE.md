Every attack cycle follows this cycle
1. Reconnaissance
2. Exploitation
3. Evidence capture
4. Documentation
5. Version control

This is my first project.... 
# First Blood
Kali and metasploitable2 are used in this case scenario
Step 1. Getting metasploitable ip address
Running command - ifconfig 
The ip address was 192.168.56.102

Step 2.Getting Kali's io address
Running command -ip a
The up address was 192.168.56.101
Ping 192.168.56.102
This is to confirm if the up is reachable
If not. The possible causes are:
- Typing in the wrong ip address
- the VirtualBox is Hostonly adapter is disabled in windows
- Both might not be running as a Hostonly adapter
# Step 3: Reconnaisance
Run command nmap -v 192.168.56.102
![[JPEG_20261028_001044_4250659961016988231.jpg]]
![[JPEG_20261028_001115_2186138625694732658.jpg]]￼￼Gh


| Port | Service | What it does in plain English | Why it's dangerous                   |
| ---- | ------- | ----------------------------- | ------------------------------------ |
| 21   | FTP     | Transfers files in cleartext  | Old daemons have backdoors/creds     |
| 22   | SSH     | Remote encrypted login        | Default/weak passwords               |
| 23   | Telnet  | Remote login, **unencrypted** | Everything readable — Wireshark gold |
| 25   | SMTP    | Sends email                   | Spam relay, user enumeration         |
| 80   | HTTP    | Web server                    | Web attacks (Phase 2)                |
| 3306 | MySQL   | Database                      | Default creds, sqli                  |
# Step 4 Exploit
![[JPEG_20261028_001810_4273483979744856536.jpg]]
Enable metasploitable by running command- msf console
Then we run command- search vsftpd
Pick the one you wish to exploit in my case use 1
So I run command -use 1
We run into a bit of a problem...... ![[JPEG_20261028_002834_7791965005471664452.jpg]]￼J


Your Kali's Metasploit defaulted to a reverse_meterpreter payload — and any "reverse" payload needs the target to call back  to you. It must know your IP to call back to. That missing piece is  LHOST  (Local HOST — your Kali machine).

RHOSTS = the victim  (where the vulnerable service runs)
 
LHOST = you  (where the shell should connect back to)
 
LPORT = the port on your machine listening for that connection (4444 default)

In this case you will have to manually set the victim by setting the RHOST to the metasploitable2 ip and kali as LHOST

WHAT BROKE: exploit failed "LHOST failed to validate" — reverse payload
needs the target to call back to me; RHOSTS (victim) ≠ LHOST (me).
LEARNED: bind vs reverse payloads. Reverse needs LHOST set. Meterpreter > plain shell.
![[JPEG_20261028_005441_4790566326627952912.jpg]]



Meterpreter is not like shell... Its commands should be written one at a time

| Meterpreter command | What it does                                                          |
| ------------------- | --------------------------------------------------------------------- |
| `sysinfo`           | OS, hostname, architecture ✅ (you got it: Ubuntu 8.04, kernel 2.6.24) |
| `getuid`            | who you are on the target                                             |
| `shell`             | **drops you INTO a real Linux shell** — *then* whoami/id/ls all work  |
| `pwd`, `ls`, `cat`  | file ops on the target                                                |
| `ps`                | list running processes                                                |
| `hashdump`          | dump password hashes (after privesc — later)                          |
| `background`        | park the session, return to msf prompt (like minimize)                |
| `help`              | full list                                                             |
￼￼￼

I have done this for a second te this time documenting every single process

