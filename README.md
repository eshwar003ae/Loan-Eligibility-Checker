# Loan Eligibility Checker

A Flask web application that determines loan eligibility based on user financial information using rule-based logic and machine learning capabilities.

## Features

- Web-based loan eligibility assessment
- Rule-based eligibility calculation
- Machine learning model training capability
- Responsive user interface
- Real-time loan limit calculation

## Project Structure

```
Loan Eligibility Checker/
├── app.py                 # Main Flask application
├── train.py              # ML model training script
├── requirements.txt      # Python dependencies
├── loan_model.pkl        # Trained ML model (generated)
├── loan_data.csv         # Training dataset
├── Loan_Status.csv       # Loan status dataset
├── static/
│   ├── assests/
│   │   └── money.jpg     # Image assets
│   └── style.css         # Stylesheet
└── templates/
    ├── index.html        # Main form page
    └── result.html       # Results display page
```

## Functions Documentation

### app.py

#### `home()`
- **Route**: `/` (GET)
- **Purpose**: Renders the main loan application form
- **Returns**: HTML template (index.html)

#### `predict()`
- **Route**: `/predict` (POST)
- **Purpose**: Processes loan application and determines eligibility
- **Input Parameters**:
  - `name`: Applicant's full name
  - `gender`: Male/Female
  - `monthly_income`: Monthly income in ₹
  - `annual_income`: Annual income in ₹
  - `loan_amount`: Requested loan amount in ₹
  - `property_worth`: Property value in ₹
  - `credit_score`: Credit score (numeric)
- **Logic**:
  - Calculates total worth: `annual_income + property_worth`
  - Determines loan limit: `total_worth * 0.4` (40% rule)
  - Approves if: `loan_amount <= loan_limit AND credit_score >= 650`
- **Returns**: Result page with approval/rejection status and reason

### train.py

#### Data Processing Functions
- **Dataset Loading**: Loads loan data from CSV file
- **Data Cleaning**: Removes rows with missing target values
- **Feature Engineering**: Separates features and target variables
- **Preprocessing Pipeline**:
  - Numeric features: Mean imputation
  - Categorical features: Most frequent imputation + One-hot encoding

#### Model Training Functions
- **Pipeline Creation**: Combines preprocessing and LogisticRegression
- **Model Training**: Fits the pipeline on training data
- **Cross Validation**: 5-fold cross-validation for accuracy assessment
- **Model Persistence**: Saves trained model as `loan_model.pkl`

## Installation & Setup

1. **Clone/Download** the project
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   python app.py
   ```
4. **Access**: Open browser to `http://localhost:5000`

## Usage

1. **Fill the form** with required financial information
2. **Submit** to get instant eligibility decision
3. **View results** showing approval/rejection with reasons

## Eligibility Criteria

- **Credit Score**: Minimum 650 required
- **Loan Limit**: Maximum 40% of (Annual Income + Property Worth)
- **Both conditions** must be satisfied for approval

## Dependencies

- Flask: Web framework
- pandas: Data manipulation
- numpy: Numerical operations
- scikit-learn: Machine learning
- joblib: Model serialization

## Model Training (Optional)

To retrain the model with new data:
```bash
python train.py
```

This will:
- Load data from `Loan_Status.csv`
- Train a new LogisticRegression model
- Save updated model as `loan_model.pkl`
- Display cross-validation accuracy

## File Descriptions

- **app.py**: Main Flask application with routing and business logic
- **train.py**: ML model training script with preprocessing pipeline
- **index.html**: User input form with validation
- **result.html**: Results display template
- **requirements.txt**: Python package dependencies
- **loan_model.pkl**: Serialized trained model (auto-generated)
- **CSV files**: Training and reference datasets

## Future Enhancements

- Integration of ML model predictions with rule-based logic
- Additional eligibility factors
- User authentication
- Application history tracking
- Enhanced UI/UX design