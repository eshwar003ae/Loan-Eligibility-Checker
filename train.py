import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib

# 1️⃣ Load dataset
df = pd.read_csv("Loan_status.csv")  # your dataset file

# 2️⃣ Remove rows without Loan_Status (target column)
df = df.dropna(subset=['Loan_Status'])

# 3️⃣ Separate features (X) and target (y)
X = df.drop(columns=['Loan_Status', 'Loan_ID'], errors='ignore')
y = df['Loan_Status'].map({'Y': 1, 'N': 0})  # Convert to 1/0

# 4️⃣ Identify categorical & numeric columns
categorical_cols = X.select_dtypes(include=['object']).columns
numeric_cols = X.select_dtypes(exclude=['object']).columns

# 5️⃣ Preprocessing for numeric data
numeric_transformer = SimpleImputer(strategy='mean')

# 6️⃣ Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# 7️⃣ Combine preprocessors
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_cols),
        ('cat', categorical_transformer, categorical_cols)
    ]
)

# 8️⃣ Create pipeline with Logistic Regression model
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000))
])

# 9️⃣ Train model
pipeline.fit(X, y)

# 🔟 Evaluate with cross-validation
scores = cross_val_score(pipeline, X, y, cv=5)
print(f"Model Accuracy: {scores.mean():.2f}")

# 1️⃣1️⃣ Save model for Flask app
joblib.dump(pipeline, "loan_model.pkl")
print("✅ Model saved as loan_model.pkl")
