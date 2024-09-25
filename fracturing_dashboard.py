import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



st.title("Fracturing Length Measurements")

col1, col2 = st.columns(2)
# input for fracturing parameter
with col1:
    with st.container():
        qi = st.number_input(label='Injection rate (bbl/min)')
        tp = st.number_input(label=' Pumping Time (min)')
        Cl = st.number_input(label=' Fluid-loss coefficient(typically from 0.0005 to 0.05 ft/min^1/2)')
        hl = st.number_input(label=' Permeable or fluid-loss height (ft)')
        sp = st.number_input(label=' Spurt loss(typically from 0 to 50 gal/100 ft^2)')
        w = st.number_input(label=' Fracture Width (in.)')
        hf = st.number_input(label=' Fracture Height (ft)')

        

with col2:
    with st.container():
        st.write("""### Input the Fracturing Parameter""")
        
        if st.button("Result", use_container_width=True):
            
            st.image("frac.jpg")
            try:
                numerator = qi * tp
                # Prevent division by zero by checking denominator
                denomirator = float(6*Cl*hl*tp**(1/2)) + (4*hl*sp) + (2*w*hf)
                
                if denomirator == 0:  # Check for zero denominator
                    st.warning("Input the number correctly", icon="⚠️")
                
                length = numerator / denomirator
                st.markdown(f"<div style='text-align: center;'>Fracture Length: {round(length, 3)} ft</div>", unsafe_allow_html=True)
            
            except Exception as e:
                 st.write(f"Error: {str(e)}")

            with st.container():
                st.latex(r"""L \approx \frac{q_i t_p}{6C_L h_L \sqrt{t_p} + 4 h_L S_p + 2 \bar{w} h_f}""")
            
            st.markdown(
    f"<div style='text-align: center;'><span style='font-size: 1.5rem;'>Calculated Fracture Length: </span><span style='font-size: 2rem;'>{length:.3f} ft</span></div>",
    unsafe_allow_html=True
)

        
         


