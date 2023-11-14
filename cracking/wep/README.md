## NAME : 
Wireless 1

## DESC : 
Can you find the Wifi Password? Wrap password with flag format e.g. if the password is `123` flag will be `casual{123}`

## POINTS: 
50

## Solution:
This is a cap file which can be opened in wireshark. SSID = "The Promised Lan", SSID = name of wifi. not the password. Search for how to crack wireless passwords. This leads to `aircrack-ng`. Use the tool. Since this is WEP no wordlist is needed. Running aircrack-ng on the cap gives the password. Sample output

```
 Aircrack-ng 1.1


                                     [00:00:01] Tested 32642 keys (got 20400 IVs)

   KB    depth   byte(vote)
    0    0/ 12   77(27392) 58(27392) 0F(26624) DF(25600) 30(25600) DD(25600) 99(25344) 73(24832) EC(24832)
    1    0/  2   46(28672) 01(27904) 10(25600) B7(25088) 68(25088) CE(24832) 23(24576) B4(24576) 9F(24576)
    2    0/ 34   6A(26112) D8(25600) 56(25088) E3(25088) FE(25088) 58(24832) F0(24832) 19(24832) 82(24576)
    3    7/  9   90(25088) A6(24576) 54(24576) 7D(24576) 07(24320) 5C(24320) CA(24064) F3(24064) 5D(23808)
    4    0/  5   2F(28928) 0E(26880) 64(26624) 34(26112) A6(25856) 42(25600) 71(25344) DB(25344) 68(25088)

                     KEY FOUND! [ 77:46:6A:56:2F ] (ASCII: wFjV/ )
        Decrypted correctly: 100%
```
Password = wFjV/. Flag = casual{wFjV/}
