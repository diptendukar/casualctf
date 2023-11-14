## Name - PaaS

## Description
Welcome to PaaS (Ping as a Service). Ping anyone and see the results.

Can you do anything else? 🤔

## Solution
We are provided a text box where you can put ip/domain and the output will be shown after sometimes. If we put google.com we will get the results similar to if we run `ping google.com`. Now we can try and join commands via the text input. If we type `google.com;whoami` -> this on the backend becomes `ping google.com;whoami` which is 2 commands and not 1. The result should contain 2 outputs. At this point we can infer that we can run additional commands using `;`. So `ls` will show `index.php`. We can run `grep -Ril "casual"` or we can explore and the flag was in `/var/www/flag.txt`
