# Amazon Product Scraper & Alert System
This is a simple Amazon Product Scraper & Alert System built using scrapy module in python

## Features



## Setup for Linux system
![For Linux](https://user-images.githubusercontent.com/80549753/216788195-692e245a-c8d4-4044-84e6-42c789d28a75.png)
```bash
sudo apt install python3-venv
python3 -m venv env
source env/bin/activate
# pip freeze > requirements.txt
# git rm --cached amazon-scraper-alert-system
pip install -r requirements.txt

```


## dev process
```bash
scrapy startproject amazon_scraper_alert_system
cd amazon_scraper_alert_system
scrapy genspider amazon-bot example.com
```