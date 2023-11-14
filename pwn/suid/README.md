## Name - no permission

## Description
I don't have permissions to read the flag! May be I can find something with `special` permissions. 

## Solution

flag.txt is owned by root. user is ctf. From the description we can infer that we need to find something. Next we google "special permissions linux". This leads to suid,guid. These are binaries that run with the owner permissions. We are supposed to find a suid binary. Google this and we find using `find / -perm /4000` -> `/opt/reader/suid_reader`. If we run this we get a message that says we need a file as argument. Provide the path to flag.txt as argument and should get the flag.
