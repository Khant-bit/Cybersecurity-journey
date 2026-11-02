Wireshark capturing on kali and after filtering metasploiatable telnet 23, I was able to see the attempts i made to access metasploitable after trying to access it on kali linux.
I was also able to view my activities in metasploitable. This is a leak as it offers no confidentiality on the app and anyone can see what you are doing on the internet
What is saw while accessing the data
![655](file:///C:/Users/ochie/Pictures/Screenshots/Screenshot%202026-11-02%20082339.png)

This why ssh port 22 is adopted in this case scenario since it is encrypted and does not allow access and leakage of information in this manner.
You can also read the password on the right lower side on the last line as telnet send packets letter per letter.
![[Pasted image 20261102085259.png]]

==🟢ANALYSIS OF THE HEX LAYER==

![[Pasted image 20261102091716.png]]The left side shows the hexadecimal while the right side shows the ASCII version of them. Take for example the highlighted area  in ascii it is m but is ox6d.
The first line in this sample above shows the OUI(Organizationally Unique Identifier). This is used to identify the organization assigned that MAC address.
![[Pasted image 20261102100246.png]]

![[Pasted image 20261102100321.png]]![[Pasted image 20261102100347.png]]