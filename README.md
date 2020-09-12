# Scan_Port

## Install
```
pip3 install requests
pip3 install colorama
```

## Usage:
```
python3 scan_port.py -p 1-3000 host/ip
```

## Output:
```

  .----. .---.   .--.  .-. .-.
 { {__  /  ___} / {} \ |  `| | * # +
 .-._} }\     }/  /\  \| |\  |   + * #
 `----'  `---' `-'  `-'`-' `-' + # *
    * + # .----.  .----. .----.  .---.
  * + #   | {}  }/  {}  \| {}  }{_   _}
    # + * | .--' \      /| .-. \  | |
  * + +   `-'     `----' `-' `-'  `-'


  HOST/IP        PORT      STATE  SERVICE
github.com   :    25/tcp   open   smtp
github.com   :   110/tcp   open   POP3
github.com   :   143/tcp   open   imap
github.com   :   119/tcp   open   nntp
github.com   :    22/tcp   open   ssh
github.com   :    80/tcp   open   http
github.com   :  9418/tcp   open   git
github.com   :   443/tcp   open   secure http
github.com   :   21 is closed
```

## Info:
