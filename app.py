import numpy as np
from datetime import datetime
import time
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
def generate_power_data():
   p = 100 + np.random.normal(0,2)
   q = 20 + np.random.normal(0,5)
   thd = np.random.uniform(2,12)
   timestamp = datetime.now().strftime("%H:%M:%S")
   return timestamp, round(p,2), round(q,2), round(thd,2)

# STREAMLİT   page settings
st.set_page_config(page_title = "Energy Dashboard",layout = "wide")
st.title("Real-Time Energy Monitoring")

if 'df_history' not in st.session_state:
   st.session_state.df_history = pd.DataFrame(columns=['Time','Active','Reactive','THD'])


#STREAMLİT layout settings
col1,col2,col3 = st.columns(3)
p_metrics=col1.empty()
q_metrics=col2.empty()
thd_metrics=col3.empty()

plot_placeholder=st.empty()

#LOOP
while True:
    t,p,q,thd = generate_power_data()
    new_data=pd.DataFrame({'Time':[t],'Active':[p],'Reactive':[q],'THD':[thd]})
    st.session_state.df_history=pd.concat([st.session_state.df_history,new_data],ignore_index=True).tail(30)

    p_metrics.metric(label="Active Power kW" , value = f"{p} kW")
    q_metrics.metric(label="ReActive Power kVAr" , value = f"{q} kVAr")
    thd_metrics.metric(label="Total Harmonic Distortion", value = f"%{thd}")
    
    fig=go.Figure()
    fig.add_trace(go.Scatter(
    x = st.session_state.df_history['Time'],
    y = st.session_state.df_history['Active'],
    mode = 'lines+markers',
    name = 'Active Power (kW)',
    line =dict(color = '#1f77b4', width = 3)
    ))

    
    fig.add_trace(go.Scatter(
    x = st.session_state.df_history['Time'],
    y = st.session_state.df_history['Reactive'],
    mode = 'lines+markers',
    name = 'ReActive Power (kW)',
    line =dict(color = '#ff7f0e', width = 3, dash = 'dot')
    ))

    fig.update_layout(
    title = "Power Balance Analyze",
    xaxis_title = "Time",
    yaxis_title = "Value",
    template = "plotly_dark",
    legend = dict(orientation = "h", yanchor = "bottom", y = 1.02, xanchor = "right", x=1),
    margin = dict(l=20,r=20,t=50,b=20),
    height = 500
    )
    
    with plot_placeholder.container():
        st.plotly_chart(fig,width="stretch")

    time.sleep(1)



