# daisy
basic auth bruteforce tool

## requirements:
```python3, scapy 2.4```

### installing scapy:
```
git clone https://github.com/secdev/scapy
cd scapy
sudo python setup.py install
```
### installing scapy-http:
```
pip3 install scapy-http
```

## installation & usage:
### basic auth brute attack:
```
git clone https://github.com/ryland192000/daisy
cd daisy
python3 daisy.py -u <usernames.txt> -p <passwords.txt> -r <url>
```
  
### basic auth sniffer:
```
python3 daisy.py --sniff
```

## breakdown:

### options:
`-u`: Path of usernames list file (example: usernames.txt)

`-p`: Path of passwords list file (example: passwords.txt)

`-r`: URL to attack (example: http://192.168.1.1)

### example of a username list file:
> !!! save as .txt file !!!
```
randy
admin
abc
test
```
### example of a password list file:
> !!! save as .txt file !!!
```
randy123
admin123
abc123
test123
```
