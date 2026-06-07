# Rossmann Sales Forecasting

A machine learning application that predicts sales for Rossmann store using a trained Random Forest model.

## Features

- Interactive sales prediction interface using Streamlit
- Pre-trained Random Forest model (`rf_model_small.pkl`)
- Input parameters include store ID, day of week, promotions, and competition distance
- Real-time predictions

## Local Setup

### Prerequisites

- Python 3.11+
- pip or conda

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Richasinghh09/sales_forecasting.git
   cd sales_forecasting
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

Start the Streamlit application:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Deployment

### Deploy to Railway

1. Push your code to GitHub
2. Connect your repository to Railway
3. Set the start command to:
   ```
   streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```
4. Railway will automatically detect the `Procfile` and `requirements.txt`

### Deploy to Render

1. Push your code to GitHub
2. Create a new Web Service on Render and connect your repository
3. Set the build command to: `pip install -r requirements.txt`
4. Set the start command to: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

## Project Structure

```
├── app.py                      # Main Streamlit application
├── rf_model_small.pkl          # Pre-trained Random Forest model
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version specification
├── Procfile                    # Deployment configuration
├── .streamlit/config.toml      # Streamlit server configuration
└── README.md                   # This file
```

## Model Details

The model is trained on Rossmann store sales data with the following features:
- Store ID
- Day of Week
- Open/Closed status
- Promotion status
- School Holiday indicator
- Competition Distance
- Historical competition and promotion data

## Files to Clean Up (Not Included in Deployment)

The following files are used for local development and training but **should not be deployed**:
- `train.csv` (~39MB) - Training data
- `test.csv` (~1.4MB) - Test data
- `sample_submission.csv` (~317KB) - Sample submission format
- `eda.ipynb` (~720KB) - Exploratory Data Analysis notebook

Add these to `.gitignore` if not already present to keep your deployment slim.

## License

MIT License - See LICENSE file for details

## Author

Richasinghh09
