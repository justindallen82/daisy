# daisy
basic auth bruteforce tool

## installation & usage:
```
git clone https://github.com/ryland192000/daisy
cd daisy
python3 daisy.py -u <usernames.txt> -p <passwords.txt> -r <url>
```
## breakdown:

### options:
`-r`: Path of usernames list file (example: usernames.txt)

`-p`: Path of passwords list file (example: passwords.txt)

`-u`: URL to attack (example: http://192.168.1.1)

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
