# Sites Monitoring Utility

The app checks status of URLs from file

# How to Install

Python 3 should be already installed. 
Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
$ pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclop
edia/pip/pip_virtualenv/) for better isolation.

# Quickstart

The path to the file with URLs is specified when running after the script name
```bash
$ python check_sites_health.py urls.txt
http://google.com
Server responds with HTTP OK: True
Domain was paid by more than 1 month: True

http://ya.ru
Server responds with HTTP OK: True
Domain was paid by more than 1 month: True

http://devman.org
Server responds with HTTP OK: True
Domain was paid by more than 1 month: True
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
