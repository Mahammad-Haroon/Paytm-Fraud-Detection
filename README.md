#💳 Paytm Fraud Detection System
A data science project that detects fraudulent transactions on Paytm-like digital payment platforms using supervised machine learning. It analyzes transaction patterns and user behavior to classify activities as legitimate or fraudulent in real time.

📌 Objectives
Clean and preprocess transaction data

Perform exploratory data analysis (EDA)

Train and optimize models: Logistic Regression, Random Forest, Gradient Boosting

Visualize transaction and fraud trends

Evaluate models with precision, recall, F1-score, ROC-AUC

Deploy real-time predictions via Flask API

🗂️ Project Structure
graphql
Copy
Edit
Paytm-Fraud-Detection/
├── data/                # Dataset files
├── notebooks/           # Jupyter notebooks for analysis
├── app/                 # Flask API files (app.py)
├── models/              # Trained ML models (.pkl)
├── static/              # Static files (optional)
├── requirements.txt     # Dependencies
├── .gitignore           # Ignored files
└── README.md            # Project documentation
🛠️ Tools & Libraries
Python 3.7+, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Flask

⚙️ Installation
bash
Copy
Edit
git clone https://github.com/Mahammad-Haroon/Paytm-Fraud-Detection.git
cd Paytm-Fraud-Detection
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cd app
python app.py
📈 Model Evaluation Metrics
Accuracy | Precision | Recall | F1 Score | ROC-AUC | Confusion Matrix

🔒 Significance
Real-time fraud detection

Improved security and user trust

Scalable for large fintech platforms

Applicable to Paytm and similar apps

📂 Dataset
Dataset is simulated or anonymized Paytm transaction data; see data/README.md for details.

🤝 Contributors
Mahammad Haroon — GitHub

📬 Contact
Email: mahammadharoon14@gmail.com
