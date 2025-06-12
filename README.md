# Snowflake Flask Multi-Cloud Application

A full-stack Flask application with interactive data visualizations that displays live database information from Snowflake across three major cloud platforms. Features modern Three.js animations and responsive design with real-time data synchronization.

## 🌐 Live Deployments

| Cloud Provider | Service | Live URL |
|----------------|---------|----------|
| **Google Cloud** | Cloud Run | https://snow-flask-whoami-gpc-357277717136.us-central1.run.app |
| **AWS** | Lambda + API Gateway | https://efgl5d8ao9.execute-api.us-west-2.amazonaws.com/Prod |
| **Azure** | Functions | https://snow-flask-whoami-az.azurewebsites.net |

## ✨ Features

### Interactive Visualizations
- **Homepage (`/`)**: Dual-layer visualization with Vega-Lite charts and Three.js background animations
- **HardData Page (`/HardData`)**: Interactive 3D cards with drag controls and orbital camera navigation
- **Real-time Data**: Live Snowflake database connectivity with instant updates across all cloud instances

### Technical Stack
- **Backend**: Flask, Snowflake Python Connector
- **Frontend**: Vega-Lite, Three.js, Responsive CSS
- **Authentication**: RSA key-pair authentication with Snowflake
- **Deployment**: Multi-cloud serverless architecture

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Snowflake account with database access
- Cloud provider account (AWS/Azure/GCP)

### Local Development
```bash
# Clone repository with submodules
git clone https://github.com/HatmanStack/snow-flask-whoami.git
cd snow-flask-whoami
git submodule init
git submodule update --recursive --remote

# Set up Python environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
export SNOW_USERNAME=your_snowflake_username
export SNOW_PASSWORD=your_rsa_secure_passphrase
export SNOW_ACCOUNT=your_snowflake_account

# Run application
python main.py
```

## 🔐 Snowflake Authentication Setup

This application uses RSA key-pair authentication for secure Snowflake connectivity:

1. **Generate encrypted private key:**
   ```bash
   openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -v2 aes-256-cbc -passout pass:your-secure-passphrase
   ```

2. **Generate public key:**
   ```bash
   openssl rsa -in rsa_key.p8 -passin pass:your-secure-passphrase -pubout -out rsa_key.pub
   ```

3. **Configure Snowflake user:**
   ```sql
   ALTER USER your_service_user SET RSA_PUBLIC_KEY = '<paste_public_key_content_here>';
   ```

4. **Include credentials in your connection configuration**

## 🏗️ Cloud-Specific Deployments

Each cloud deployment is contained in its own sub-module with specific configuration:

| Sub-module | Target Platform | Architecture |
|------------|----------------|--------------|
| `snow-flask-whoami-aws/` | AWS Lambda + API Gateway | Serverless with SAM |
| `snow-flask-whoami-az/` | Azure Functions | Serverless HTTP trigger |
| `snow-flask-whoami-gpc/` | Google Cloud Run | Containerized serverless |

### Deployment Quick Commands

**AWS (SAM):**
```bash
cd snow-flask-whoami-aws/
sam build && sam deploy --guided
```

**Azure (Functions Core Tools):**
```bash
cd snow-flask-whoami-az/
func azure functionapp publish snow-flask-whoami-az
```

**GCP (Cloud Build):**
```bash
cd snow-flask-whoami-gpc/
gcloud builds submit --config=cloudbuild.yaml .
```

## 🔧 Development Notes

- **Linux users**: Replace `waitress` with `gunicorn` for better performance:
  ```bash
  gunicorn -w 2 main:app
  ```
- **Environment Variables**: All deployments require `USERNAME`, `PASSWORD`, and `REGION` configuration
- **Data Synchronization**: Changes made through any cloud instance are immediately reflected across all deployments

## 📁 Project Structure

```
snow-flask-whoami/
├── main.py                     # Core Flask application
├── templates/                  # Jinja2 templates
├── static/                     # CSS, JS, Three.js assets
├── snow-flask-whoami-aws/      # AWS Lambda deployment
├── snow-flask-whoami-az/       # Azure Functions deployment
└── snow-flask-whoami-gpc/      # Google Cloud Run deployment
```

For detailed deployment instructions, see the README in each sub-module directory.
