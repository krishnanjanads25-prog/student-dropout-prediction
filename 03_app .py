import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import time

# ==========================================
# 1. PAGE CONFIGURATION & CUSTOM CSS
# ==========================================
st.set_page_config(page_title="Dropout Alert System", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    /* Dark Theme Backgrounds */
    .stApp { background-color: #0b0f19; color: #e2e8f0; }
    
    /* Custom Card Styling for Forms and Layouts */
    div[data-testid="stForm"] {
        background-color: #151a23;
        border: 1px solid #2d3748;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    /* Header styling */
    h1, h2, h3 { color: #cbd5e1 !important; font-family: 'Inter', sans-serif; }
    
    /* Custom Recommendation Cards */
    .rec-card {
        background-color: #1e293b;
        border-left: 4px solid #0ea5e9;
        padding: 15px;
        margin-bottom: 10px;
        border-radius: 4px;
        font-size: 0.95rem;
    }
    
    /* Gradient Predict Button */
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6 0%, #0ea5e9 100%);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0px 8px 15px rgba(14, 165, 233, 0.4); }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. HEADER & SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("### ⚙️ Admin Console")
    st.divider()
    st.button("🏠 Dashboard", use_container_width=True)
    st.button("👤 Student Directory", use_container_width=True)
    st.divider()
    st.success("🟢 Model Health: Online\n\nReady for Prediction")

st.markdown("## Predictive Student Retention Platform | Dropout Alert System")
st.divider()

# ==========================================
# 3. MAIN LAYOUT (INPUTS LEFT, OUTPUTS RIGHT)
# ==========================================
col_left, col_right = st.columns([1, 1.2], gap="large")

with col_left:
    st.markdown("### 📊 Student Profile Inputs")
    
    # FUNCTIONAL INPUT FORM
    with st.form("prediction_form"):
        st.markdown("#### 📚 Academic Details")
        attendance = st.slider("Attendance Performance (%)", 0, 100, 75)
        marks = st.slider("Academic Marks (%)", 0, 100, 60)
        study_hours = st.slider("Study Hours / Day", 0.0, 15.0, 4.0, 0.5)
        
        st.markdown("<br>🧠 Behavioural Factors", unsafe_allow_html=True)
        stress_index = st.slider("Stress Index (1-10)", 1, 10, 5)
        assignment_delay = st.slider("Assignment Delay (days)", 0, 30, 3)
        
        # Add any other inputs you need for your model here (like department, etc.)
        # department = st.selectbox("Department", [1, 2, 3, 4], index=0)
        # parental_edu = st.selectbox("Parental Education Level", [1, 2, 3, 4], index=0)

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🚀 Run Advanced Risk Analysis", use_container_width=True)

with col_right:
    st.markdown("### 🎯 Advanced Risk Analysis")
    
    if not submitted:
        st.info("👈 Adjust the student profile metrics on the left and click 'Run Analysis' to generate the report.")
        # Blank placeholder radar chart
        fig_blank = go.Figure(go.Scatterpolar(r=[0,0,0,0,0], theta=['Marks', 'Stress', 'Attendance', 'Study', 'Delay'], fill='toself'))
        fig_blank.update_layout(polar=dict(radialaxis=dict(visible=False)), height=350, paper_bgcolor="rgba(0,0,0,0)", font={'color': "gray"})
        st.plotly_chart(fig_blank, use_container_width=True)

    if submitted:
        with st.spinner("Executing RandomForest Pipeline..."):
            time.sleep(1) # Visual loading effect
            
            # =================================================================
            # 🛑 4. PASTE YOUR MACHINE LEARNING CODE HERE 🛑
            # =================================================================
            
            # 1. Build your input dictionary exactly like you had it. 
            # CRITICAL: Make sure there are EXACTLY 19 items in this dictionary to fix your ValueError!
            # Example:
            # input_dict = {
            #     'attendance': attendance, 'marks': marks, 'study_hours': study_hours,
            #     'stress': stress_index, 'delay': assignment_delay, 'department': department,
            #     'parental_education': parental_edu, 
            #     # ... add the missing 12 features here so it totals 19!
            # }
            # input_df = pd.DataFrame([input_dict])
            # input_scaled = scaler.transform(input_df)
            # pred_array = model.predict(input_scaled)
            # prediction = pred_array[0]
            # probability = model.predict_proba(input_scaled)[0][1]
            
            # --- DUMMY LOGIC (Delete this when you paste your code above) ---
            fake_score = (100 - attendance)*0.4 + (100 - marks)*0.3 + (stress_index*4) + (assignment_delay*2) - (study_hours*2)
            probability = min(max(fake_score / 100, 0.05), 0.95) 
            prediction = 1 if probability > 0.5 else 0
            # ----------------------------------------------------------------

            prob_percentage = probability * 100
            
            # =================================================================
            # 5. DYNAMIC UI UPDATES BASED ON YOUR MODEL
            # =================================================================
            
            # Determine colors based on risk
            if prediction == 1:
                gauge_color = "#f43f5e" # Red
                status_msg = "🚨 High Risk of Dropout Detected"
                radar_color = "#f43f5e"
            else:
                gauge_color = "#10b981" # Green
                status_msg = "✅ Stable Retention Trajectory"
                radar_color = "#10b981"

            # GAUGE CHART
            c1, c2 = st.columns([1, 1])
            with c1:
                fig_risk = go.Figure(go.Indicator(
                    mode="gauge+number", value=prob_percentage, number={'suffix': "%", 'font': {'color': gauge_color}},
                    title={'text': "Dropout Probability", 'font': {'color': 'white'}},
                    gauge={
                        'axis': {'range': [0, 100]},
                        'bar': {'color': gauge_color},
                        'bgcolor': "#1e293b",
                        'steps': [
                            {'range': [0, 35], 'color': "rgba(16, 185, 129, 0.2)"},
                            {'range': [35, 65], 'color': "rgba(245, 158, 11, 0.2)"},
                            {'range': [65, 100], 'color': "rgba(244, 63, 94, 0.2)"}
                        ]
                    }
                ))
                fig_risk.update_layout(height=250, margin=dict(l=20, r=20, t=30, b=10), paper_bgcolor="rgba(0,0,0,0)")
                st.plotly_chart(fig_risk, use_container_width=True)

            # RADAR CHART (Reacts to the sliders!)
            with c2:
                # Convert slider values to a 0-100 scale for the radar chart
                scaled_stress = stress_index * 10
                scaled_study = (study_hours / 15) * 100
                scaled_delay = (assignment_delay / 30) * 100
                
                categories = ['Attendance', 'Marks', 'Study Habits', 'Stress Level', 'Submission Delay']
                fig_radar = go.Figure()
                # Student Profile
                fig_radar.add_trace(go.Scatterpolar(
                    r=[attendance, marks, scaled_study, scaled_stress, scaled_delay], 
                    theta=categories, fill='toself', name='Current Student', line_color=radar_color
                ))
                # Class Average Benchmark
                fig_radar.add_trace(go.Scatterpolar(
                    r=[75, 65, 50, 40, 20], theta=categories, fill='none', name='Class Avg', line_color='#64748b', line_dash='dash'
                ))
                fig_radar.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                    showlegend=False, height=250, margin=dict(l=40, r=40, t=20, b=20),
                    paper_bgcolor="rgba(0,0,0,0)", font={'color': "white"}
                )
                st.plotly_chart(fig_radar, use_container_width=True)

            # RECOMMENDATIONS
            st.markdown(f"**System Status:** {status_msg}")
            
            if prediction == 1:
                st.markdown("""
                <div class="rec-card" style="border-left-color: #f43f5e;">
                    <strong>🚨 Immediate Intervention Required</strong><br>
                    <span style="color:#94a3b8">Schedule an urgent meeting with the academic counselor.</span>
                </div>
                <div class="rec-card" style="border-left-color: #f59e0b;">
                    <strong>📚 Academic Peer Tutoring</strong><br>
                    <span style="color:#94a3b8">Enroll student in mandatory peer tutoring for lagging subjects.</span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="rec-card" style="border-left-color: #10b981;">
                    <strong>✅ Continue Current Academic Path</strong><br>
                    <span style="color:#94a3b8">Student is performing within safe parameters. No immediate action needed.</span>
                </div>
                """, unsafe_allow_html=True)
