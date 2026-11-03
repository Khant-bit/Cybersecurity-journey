Wireshark capturing on kali and after filtering metasploiatable telnet 23, I was able to see the attempts i made to access metasploitable after trying to access it on kali linux.
I was also able to view my activities in metasploitable. This is a leak as it offers no confidentiality on the app and anyone can see what you are doing on the internet
What is saw while accessing the data
![655](file:///C:/Users/ochie/Pictures/Screenshots/Screenshot%202026-11-02%20082339.png)

This why ssh port 22 is adopted in this case scenario since it is encrypted and does not allow access and leakage of information in this manner.
You can also read the password on the right lower side on the last line as telnet send packets letter per letter.
For this you will have to go letter per letter for this....While in the user name entry point you notice that the letters are repeated twice.
![[Pasted image 20261102085259.png]]

==🟢ANALYSIS OF THE HEX LAYER==

![[Pasted image 20261102091716.png]]The left side shows the hexadecimal while the right side shows the ASCII version of them. Take for example the highlighted area  in ascii it is m but is ox6d.
The first line in this sample above shows the OUI(Organizationally Unique Identifier). This is used to identify the organization assigned that MAC address.

==🟢THE SSH CONTRAST AND THE DEFENDER'S VIEW==
The idea was to open the telnet port == 22 to see if i can access the data as i did when i opened the when i used port == 23..The expected result was to see a gibberish. Binary noise and no readable commands.
This info comes in handy as a SOC analyst since he/she wont need the password..Prescence of the metadata just shows that there was an activity here and that is the alarm needed.

But i ran into a problem my kali linux runs on a modern OpenSSH(2026), while Metaspoitable 2 runs on OpenSSH 4.7 from 2008.
The ancient server only offers ssh-rsa and ssh-dss host keys (based on SHA-1) while the modern OpenSSH deliberately disabled SHA-1.

![[Pasted image 20261102100246.png]]


- oHostKeyAlgorithms=+ssh-rsa msfadmin @192.168.56.102
Breaking down the  command above
-o      this passes a custom option.
HostKeyAlgorithms=+ssh-rsa        accept ssh-rsa in addition to the secure defaults
![[Pasted image 20261102100321.png|633]]

in order to create a config so that i cannot type that flag again
nano ~/.ssh/config


![[Pasted image 20261102100347.png]]