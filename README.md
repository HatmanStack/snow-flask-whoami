# Snowflake Flask App

This repository contains an Application written using Flask and Vega-Lite charts hosted on the Major Cloud providers that displays Database information from a single Snowflake Database. The data is Live so changes on one cloud provider affect all other providers. The application now features enhanced Three.js visualizations for a more interactive experience.

## Clouds
* GPC: https://snow-flask-whoami-gpc-k6cy6vf2la-uc.a.run.app/
* AWS: https://akxv1pi5yc.execute-api.us-west-1.amazonaws.com/dev
* Azure: https://snow-flask-whoami-az.azurewebsites.net/Home

## Enhanced Visualizations

### Homepage (/)
The homepage features a dual-layer visualization:
1. **Vega-Lite Chart**: A bar chart showing name counts from the Snowflake database
2. **Three.js Background Animation**: A dynamic background with falling data sprites representing database entries

### HardData Page (/HardData)
The HardData page has been completely overhauled with an interactive 3D visualization:
1. **Interactive 3D Cards**: Each database record is represented as a 3D card in a Three.js scene
2. **Drag Controls**: Users can click and drag cards to rearrange them in 3D space
3. **Orbit Controls**: Users can rotate and zoom the camera to explore the data from different angles

## Prerequisites
* Python 3.x
* Flask
* Vega-Lite
* Three.js
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

## Cloud-Specific Deployments

This repository contains three sub-modules, each configured for deployment to a specific cloud provider:

* **snow-flask-whoami-aws**: Configured for AWS Lambda with API Gateway
* **snow-flask-whoami-azure**: Configured for Azure Functions
* **snow-flask-whoami-gpc**: Configured for Google Cloud Run

Each sub-module contains its own README with specific deployment instructions.
