# Snowflake Flask App
This repository contains an Application written using Flask and Vega-Lite charts hosted on the Major Cloud providers that displays Database information from a single Snowflake Database. The data is Live so changes on one cloud provider affect all other providers.

## Clouds
* GPC: https://snow-flask-whoami-gpc-k6cy6vf2la-uc.a.run.app/
* AWS: https://jrjo3dsku7.execute-api.us-west-1.amazonaws.com/dev
* Azure: https://snow-flask-whoami-az.azurewebsites.net/Home

## Prerequisites
* Python 3.x
* Flask
* Vega-Lite
* Major Cloud Provider
* Snowflake Database

## Installation

Replace `USERNAME`. `PASSWORD`, `REGION` with your snowflake credentials.

```
git clone https://github.com/HatmanStack/snow-flask-whoami.git
cd snow-flask-whoami
```

For all Submodules

```
git submodule init
git submodule update --recursive --remote
```

```
python -m venv venv

Windows:
venv/scripts/activate

Linux/Mac:
source /venv/bin/activate

cd ../..
pip install -r requirements.txt
python main.py
```

If you're running Linux change from waitress to gunicorn.  Replace `waitress.serve(app, listen='0.0.0.0:8000')` with `gunicorn.run(app, host='0.0.0.0', port=8000)`, or remove waitress and run gunicorn from the command line with: `gunicorn -w 2 main:app`




