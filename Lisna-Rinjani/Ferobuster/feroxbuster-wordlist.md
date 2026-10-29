```
┌──(gh0st4n㉿Gh0sT4n)-[/media/sf_kalilinux/UK2/UK2-SMKN3Banjar]
└─$ feroxbuster -u inventory.rinjaniproject.my.id -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt            
                                                                                                                                                                                                                          
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.13.1
───────────────────────────┬──────────────────────
 🎯  Target Url            │ https://inventory.rinjaniproject.my.id/
 🚩  In-Scope Url          │ inventory.rinjaniproject.my.id
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.13.1
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
403      GET       13l       61w      787c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
404      GET       13l       64w      796c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/components => https://inventory.rinjaniproject.my.id/e-inventory/supplier/components/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/cgi-bin => https://inventory.rinjaniproject.my.id/cgi-bin/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/login => https://inventory.rinjaniproject.my.id/e-inventory/supplier/login/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/database => https://inventory.rinjaniproject.my.id/e-inventory/supplier/database/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/template => https://inventory.rinjaniproject.my.id/e-inventory/supplier/template/
500      GET       13l       62w      800c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/pages => https://inventory.rinjaniproject.my.id/e-inventory/supplier/pages/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/function => https://inventory.rinjaniproject.my.id/e-inventory/supplier/function/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/cgi-sys => https://inventory.rinjaniproject.my.id/cgi-sys/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/mailman => https://inventory.rinjaniproject.my.id/mailman/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~ => https://inventory.rinjaniproject.my.id/~/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/mailman/archives => https://inventory.rinjaniproject.my.id/mailman/archives/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/pipermail => https://inventory.rinjaniproject.my.id/pipermail/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~joe => https://inventory.rinjaniproject.my.id/~joe/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/partials => https://inventory.rinjaniproject.my.id/e-inventory/supplier/partials/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/bandwidth => https://inventory.rinjaniproject.my.id/bandwidth/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~chris => https://inventory.rinjaniproject.my.id/~chris/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~site => https://inventory.rinjaniproject.my.id/~site/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~a => https://inventory.rinjaniproject.my.id/~a/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~admin => https://inventory.rinjaniproject.my.id/~admin/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~images => https://inventory.rinjaniproject.my.id/~images/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~mike => https://inventory.rinjaniproject.my.id/~mike/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~r => https://inventory.rinjaniproject.my.id/~r/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~sys~ => https://inventory.rinjaniproject.my.id/~sys~/
404      GET        0l        0w      796c https://inventory.rinjaniproject.my.id/~site/skidki
404      GET        0l        0w      796c https://inventory.rinjaniproject.my.id/~a/stampa
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~gary => https://inventory.rinjaniproject.my.id/~gary/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~tmp => https://inventory.rinjaniproject.my.id/~tmp/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~forum => https://inventory.rinjaniproject.my.id/~forum/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~blog => https://inventory.rinjaniproject.my.id/~blog/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~home => https://inventory.rinjaniproject.my.id/~home/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~alex => https://inventory.rinjaniproject.my.id/~alex/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~liam => https://inventory.rinjaniproject.my.id/~liam/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~js => https://inventory.rinjaniproject.my.id/~js/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~chat => https://inventory.rinjaniproject.my.id/~chat/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~css => https://inventory.rinjaniproject.my.id/~css/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~eric => https://inventory.rinjaniproject.my.id/~eric/
301      GET       13l       60w      795c https://inventory.rinjaniproject.my.id/~mark => https://inventory.rinjaniproject.my.id/~mark/
404      GET        0l        0w      796c https://inventory.rinjaniproject.my.id/~js/fcgi
404      GET        0l        0w      796c https://inventory.rinjaniproject.my.id/~a/cayman
[####################] - 9m    870000/870000  0s      found:39      errors:696    
[####################] - 4m     30000/30000   129/s   https://inventory.rinjaniproject.my.id/ 
[####################] - 4m     30000/30000   127/s   https://inventory.rinjaniproject.my.id/cgi-bin/ 
[####################] - 4m     30000/30000   125/s   https://inventory.rinjaniproject.my.id/cgi-sys/ 
[####################] - 4m     30000/30000   124/s   https://inventory.rinjaniproject.my.id/mailman/ 
[####################] - 4m     30000/30000   123/s   https://inventory.rinjaniproject.my.id/~/ 
[####################] - 4m     30000/30000   123/s   https://inventory.rinjaniproject.my.id/mailman/archives/ 
[####################] - 4m     30000/30000   122/s   https://inventory.rinjaniproject.my.id/pipermail/ 
[####################] - 4m     30000/30000   111/s   https://inventory.rinjaniproject.my.id/~joe/ 
[####################] - 5m     30000/30000   96/s    https://inventory.rinjaniproject.my.id/bandwidth/ 
[####################] - 5m     30000/30000   92/s    https://inventory.rinjaniproject.my.id/~chris/ 
[####################] - 6m     30000/30000   88/s    https://inventory.rinjaniproject.my.id/~admin/ 
[####################] - 6m     30000/30000   88/s    https://inventory.rinjaniproject.my.id/~site/ 
[####################] - 6m     30000/30000   88/s    https://inventory.rinjaniproject.my.id/~a/ 
[####################] - 6m     30000/30000   84/s    https://inventory.rinjaniproject.my.id/~images/ 
[####################] - 6m     30000/30000   84/s    https://inventory.rinjaniproject.my.id/~mike/ 
[####################] - 6m     30000/30000   84/s    https://inventory.rinjaniproject.my.id/~r/ 
[####################] - 6m     30000/30000   84/s    https://inventory.rinjaniproject.my.id/~sys~/ 
[####################] - 5m     30000/30000   98/s    https://inventory.rinjaniproject.my.id/~gary/ 
[####################] - 5m     30000/30000   98/s    https://inventory.rinjaniproject.my.id/~forum/ 
[####################] - 5m     30000/30000   98/s    https://inventory.rinjaniproject.my.id/~home/ 
[####################] - 5m     30000/30000   98/s    https://inventory.rinjaniproject.my.id/~alex/ 
[####################] - 5m     30000/30000   98/s    https://inventory.rinjaniproject.my.id/~blog/ 
[####################] - 5m     30000/30000   98/s    https://inventory.rinjaniproject.my.id/~chat/ 
[####################] - 5m     30000/30000   98/s    https://inventory.rinjaniproject.my.id/~css/ 
[####################] - 5m     30000/30000   98/s    https://inventory.rinjaniproject.my.id/~eric/ 
[####################] - 5m     30000/30000   98/s    https://inventory.rinjaniproject.my.id/~mark/ 
[####################] - 5m     30000/30000   98/s    https://inventory.rinjaniproject.my.id/~js/ 
[####################] - 5m     30000/30000   98/s    https://inventory.rinjaniproject.my.id/~liam/ 
[####################] - 5m     30000/30000   98/s    https://inventory.rinjaniproject.my.id/~tmp/
```