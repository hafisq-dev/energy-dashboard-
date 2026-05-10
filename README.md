#  Real-Time Energy Quality Monitoring Dashboard

A high-fidelity, industrial-grade energy monitoring dashboard built with **Python**, **Streamlit**, and **Plotly**. This application simulates real-time electrical power data and provides interactive visualizations for power quality analysis.

##  Key Features

- **Real-Time Data Streaming:** Simulates live energy metrics (Active Power, Reactive Power, and THD) using Gaussian noise for realistic industrial scenarios.
- **Dynamic Metrics Display:** Instant tracking of P (Active Power), Q (Reactive Power), and THD (%) with status indicators.
- **Interactive Time-Series Analysis:** Professional-grade charts powered by Plotly, featuring a dark theme, zoom capabilities, and detailed tooltips for engineering analysis.
- **State Management:** Efficient data handling using Streamlit's `session_state` to maintain a rolling window of the most recent data points.
- **Industrial UI/UX:** A clean, boxed layout (using Streamlit Containers) designed for high readability in monitoring environments.

##  Technology Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Data Visualization:** [Plotly](https://plotly.com/python/)
- **Data Processing:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Environment:** Developed and tested on **Ubuntu (WSL)**

##  Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME

2. **Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate

3. **Install dependencies:**
```bash
pip install streamlit pandas numpy plotly

4. **Run the application:**
```bash
streamlit run app.py


## 📊 Preview

<img width="1913" height="970" alt="EnergyDashboard_SS" src="https://github.com/user-attachments/assets/ddf26b54-9f03-4a20-a5ad-c4c1e4c352fc" />


## 🎓 Academic Context
This project was developed as a foundational tool for real-time power quality analysis, bridging the gap between electrical engineering concepts and modern data science visualization techniques during Ph.D. research workflows.
**Developed by:** Hafis Quliyev
**Academic Focus:** Electrical Engineering / Power Systems Analysis
