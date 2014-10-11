# ip

## Description
This is a really simple public IP lookup web application (if you can even call it that).

## Example
``` bash
$ curl https://mrkc.me/ip                                                                                                  
54.235.221.217
```

## Apache Configuration
```
WSGIScriptAlias /ip /path/to/ip/app.wsgi
<Directory /path/to/ip>
    Order allow,deny
    Allow from all
</Directory>
```