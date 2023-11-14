## NAME : 
Wireless 2

## DESC : 
Can you find the Wifi Password? You might need a dictionary. Use the well known one. Wrap password with flag format e.g. if the password is `123` flag will be `casual{123}`

## POINTS: 100

## Solution:

We can open in wireshark and find SSID="TP-LINK_8076E4". Wireshark shows `WPA Version:1`. Follow up to wireless 1. This is wpa2. We need a wordlist as mentioned and `rockyou` is a pretty well known list. Use the same aircrack-ng with rockyou on the cap file. Sample output

```

                                 Aircrack-ng 1.1


                   [00:00:38] 185776 keys tested (4956.35 k/s)


                        KEY FOUND! [ blueberrymuffin ]


      Master Key     : 5A 75 D7 85 D4 01 7C 70 20 E9 65 FD FC E5 45 4B
                       DD DC 99 33 93 23 81 52 D7 FD CA 4E A8 34 82 C0

      Transient Key  : 29 AE 08 6D 9C 01 BD 98 D3 AB 2E 2B 25 1B FE 2C
                       45 1A AD D7 79 B7 02 FB 5E 25 A3 44 3B 82 DB B5
                       19 6C EA 12 1A 5D 15 51 29 0F C0 22 CA 16 10 6B
                       E0 49 44 D4 1A CF D4 04 A3 17 E9 6C B0 12 9C 83

      EAPOL HMAC     : 11 F0 85 20 D7 F6 B5 BB A6 69 61 9C 04 DC 50 AB
```
Password  = blueberrymuffin. Flag = casual{blueberrymuffin}
