                                                             
                                       _/                  _/        _/  
                                      _/          _/_/    _/  _/         
                                    _/        _/    _/  _/_/      _/    
                                   _/        _/    _/  _/  _/    _/     
                                   _/_/_/    _/_/    _/    _/  _/      


created by Ely Schybol

## Introduction
This simple C2 HTTP Server is based on Python Flask and designed to assist you with your Pentest or Bug Bounty.
At the moment the Server comes with two features:

* displaying incoming HTTP Request Data at */honeypot*

* serving files at */dropper/<filename>*

Please make sure to add files you want to have served within the "dropper" folder.
I'm not responsible for misuse of this tool and recommend plazing save and legal while testing applications. 
Keep in mind that this is vulnerable and can provide an initial foothold into your system if opened within an public network. So please make sure you don't put yourself in risk! 

Chears

## Quickstart
```bash
git clone 
cd Loki 
python3 main.py
```

### requesting files
```bash
curl <ip>:5000/dropper/<filename>
```

### send request
```bash
curl <ip>:5000/honeypot
```
