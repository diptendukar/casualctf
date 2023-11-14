##DESC - Even if you manage to login, only admin can see the flag. 😝

##Solution - 
from the login page -> view source get the login password from comment 

<!-- TODO: remove backup testing creds user123/password321 -->

Use this to login - you will get the text - Welcome User. Only Admin can see the flag. 

The name of the challenge - should point you towards `cookie`. Open dev tools / inspect -> Cookies. You will see a cookie `isAdmin=False`. Set this to `isAdmin=True`. Reload page and should get the flag.
