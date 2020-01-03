![Breech](https://i.imgur.com/VhtxAsL.png)

# Breech
Application made with <3 in Python which scans websites for hidden directories.

## Install
1. Clone.
```
git clone https://github.com/devkbnkz/Breech.git && cd Breech
```
2. Install Python required libraries.
```
pip install -r requirements.txt
```
3. Run it.
```
python breech.py
```
## Usage
1. Set the target.
```
Breech > set TARGET https://example.com
```
2. Set the payload.
```
Breech > set PAYLOAD /home/devkbnkz/rockyou.txt
```
3. Run it.
```
Breech > run
```
## Features
- [x] Makes use of the multiple CPU cores, which means it's faster than running on a single core.
- [ ] Requests can be made with different user agent or even multiple user agents.
- [x] Support for multiple extensions. (.php|.html|.htm) or user defined extensions.
- [x] Simple to use user interface.



---
Made with ❤ in Python.
