# Selenium-Scrapper-Bot

Selenium scrapper bot

## Instructions

### Build Docker Image

```
docker build -t {name_of_image} .
```

### Running Dokcer container
```
docker run -dp 3000:3000 --shm-size="2g" {name_of_image}
```


### Test on local environment

* Create virtual environment -
```
python -m venv venv
```

* Activate virtual enviroment -
```
source venv/bin/activate
```

* Execute `flask` app via -
```
python app.py
```

* Sending request -
Send request to `/` route it returns json object
```
{'RES-STATUS': 'OK-200'}
```
That means your app is running successfully

* Scrapping data -
```
127.0.0.1:3000/scrape?page={page_no}&size={size}&token={TOKEN}
```
