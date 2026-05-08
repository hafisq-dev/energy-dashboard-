import numpy as np
from datetime import datetime
import time
import streamlit as st

def generate_power_data():
   p = 100 + np.random.normal(0,2)
   q = 20 + np.random.normal(0,5)
   thd = np.random.uniform(2,12)
   timestamp = datetime.now().strftime("%H:%M:%S")
   return timestamp, round(p,2), round(q,2), round(thd,2)

# STREAMLİT   page settings
st.set_page_config(page_title = "Energy Dashboard",layout = "wide")
st.title("Real-Tiime Energy Monitoring")

#STREAMLİT interface settings
col1,col2,col3 = st.columns(3)
p_metrics=col1.empty()
q_metrics=col2.empty()
thd_metrics=col3.empty()

#LOOP
while True:
    t,p,q,thd = generate_power_data()
    p_metrics.metric(label="Active Power kW" , value = f"{p} kW")
    q_metrics.metric(label="ReActive Power kVAr" , value = f"{q} kVAr")
    thd_metrics.metric(label="Total Harmonic Distortion", value = f"%{thd}")
    time.sleep(1)



