import numpy as np
from datetime import datetime
import time
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def generate_power_data():
    """
    Simulates real-time energy data using normal and uniform distributions.
    Returns: timestamp, active power (P), reactive power (Q), and THD levels.
    """
    p = 100 + np.random.normal(0,2)
    q = 20 + np.random.normal(0,5)
    thd = np.random.uniform(2,12)
    timestamp = datetime.now().strftime("%H:%M:%S")
    return timestamp, round(p,2), round(q,2), round(thd,2)

# --- STREAMLIT PAGE CONFIGURATION ---
# Sets the dashboard to wide mode and defines the browser tab title
st.set_page_config(page_title="Energy Dashboard", layout="wide")
st.title("⚡ Real-Time Energy Monitoring")

# --- INITIALIZE SESSION STATE ---
# This ensures that our data history is preserved across Streamlit's rerun cycles.
# It creates an empty DataFrame if it doesn't already exist.
if 'df_history' not in st.session_state:
    st.session_state.df_history = pd.DataFrame(columns=['Time', 'Active', 'Reactive', 'THD'])

# --- UI LAYOUT SETUP ---
# Create three columns for top-level metrics
col1, col2, col3 = st.columns(3)
p_metrics = col1.empty()   # Placeholder for Active Power
q_metrics = col2.empty()   # Placeholder for Reactive Power
thd_metrics = col3.empty() # Placeholder for THD

# Placeholder for the main Plotly chart to prevent screen flickering
plot_placeholder = st.empty()

# --- REAL-TIME DATA LOOP ---
while True:
    # 1. Generate new simulated data point
    t, p, q, thd = generate_power_data()
    
    # 2. Update the rolling history (Keeping only the last 30 data points)
    new_data = pd.DataFrame({'Time': [t], 'Active': [p], 'Reactive': [q], 'THD': [thd]})
    st.session_state.df_history = pd.concat([st.session_state.df_history, new_data], ignore_index=True).tail(30)

    # 3. Update Numeric Metrics (Top Row)
    p_metrics.metric(label="Active Power (kW)", value=f"{p} kW")
    q_metrics.metric(label="Reactive Power (kVAr)", value=f"{q} kVAr")
    thd_metrics.metric(label="Total Harmonic Distortion", value=f"%{thd}")
    
    # 4. Create the Interactive Plotly Figure
    fig = go.Figure()

    # Add Active Power Trace
    fig.add_trace(go.Scatter(
        x=st.session_state.df_history['Time'],
        y=st.session_state.df_history['Active'],
        mode='lines+markers',
        name='Active Power (kW)',
        line=dict(color='#1f77b4', width=3)
    ))

    # Add Reactive Power Trace
    fig.add_trace(go.Scatter(
        x=st.session_state.df_history['Time'],
        y=st.session_state.df_history['Reactive'],
        mode='lines+markers',
        name='Reactive Power (kVAr)',
        line=dict(color='#ff7f0e', width=3, dash='dot')
    ))

    # 5. Styling the Chart (Dark Theme & Layout)
    fig.update_layout(
        title="Live Power Balance Analysis",
        xaxis_title="Time (Local)",
        yaxis_title="Value",
        template="plotly_dark",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=50, b=20),
        height=500
    )
    
    # 6. Render the chart in the designated placeholder
    with plot_placeholder.container():
        st.plotly_chart(fig, width="stretch")

    # Wait for 1 second before the next update
    time.sleep(1)



