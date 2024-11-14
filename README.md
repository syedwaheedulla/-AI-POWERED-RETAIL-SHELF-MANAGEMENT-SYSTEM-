# AI-Powered Retail Shelf Management System  

## 🚀 Project Overview  
The **AI-Powered Retail Shelf Management System** is designed to address critical challenges in retail management, such as fluctuating consumer demand, seasonal variations, and external influences (e.g., weather, economic conditions). By leveraging machine learning, this project provides retailers with actionable insights for smarter decision-making, optimized inventory management, and enhanced customer satisfaction.  

Key features include:  
- **Sales Prediction**: Accurate weekly sales forecasts using RandomForest Regressor.  
- **Interactive Interface**: Real-time data input and predictions via a user-friendly Streamlit web application.  
- **Data-Driven Insights**: Integration of external and temporal factors (e.g., seasonality, economic indicators) for enhanced accuracy.  

---

## 🛠️ Features  
- **Predictive Analytics**: Leverages historical data and machine learning to predict weekly sales.  
- **Streamlit Interface**: A visually engaging platform for real-time inputs and predictive outputs.  
- **Feature Engineering**: Incorporates temporal variables (e.g., day, month) and external factors (e.g., unemployment rate, CPI).  
- **Scalable Architecture**: Ready for integration with larger retail management systems.  

---

## 📁 Repository Structure  
```plaintext  
📂 walmart-sales-prediction  
├── 📄 README.md            # Project documentation  
├── 📂 data                 # Dataset folder (ensure CSV is included)  
├── 📂 models               # Trained model and joblib file  
├── 📂 app                  # Streamlit application files  
├── 📂 scripts              # Data preprocessing and model training scripts  
├── 📂 assets               # Lottie animations and visual resources  
└── 📄 requirements.txt     # Python dependencies  
```  

---

## 🔧 Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/username/walmart-sales-prediction.git  
   ```  
2. Navigate to the project directory:  
   ```bash  
   cd walmart-sales-prediction  
   ```  
3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

---

## 🚀 Usage  
1. **Run the Streamlit Application:**  
   ```bash  
   streamlit run app/app.py  
   ```  
2. Enter relevant retail data into the input fields.  
3. View weekly sales predictions and insights in real-time.  

---

## 📊 Results  
- **Mean Absolute Error (MAE):** `58,052.07`  
- Visual comparison of actual vs. predicted sales demonstrates high accuracy and reliability.  

---

## 🤝 Contributors  
- **Syed Waheedulla** - Data preprocessing, model training, and Streamlit development.  

---

## 📈 Future Scope  
- Incorporation of advanced models like Gradient Boosting or LSTM for improved temporal forecasting.  
- Integration with live retail datasets for continuous learning and adaptation.  
- Expansion to include more retail KPIs, such as customer footfall and profit margins.  

---  

## 📜 License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---  

## 📧 Contact  
For queries or collaboration opportunities, reach out to:  
**Email**: syedwaheedulla45@gmail.com  
**LinkedIn**: [Syed Waheedulla](https://www.linkedin.com/in/syedwaheedulla/)  
