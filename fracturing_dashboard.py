import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time



st.title("Fracturing Length and Pressure Measurements")
with st.sidebar:
    conversion_factor = 9.869233e-13
    st.write("Convert Darcy to SI unit")
    darcy = st.number_input("Darcy input", min_value=0.0)
    si_value = darcy * conversion_factor
    st.write(f"{si_value}")
    
tab_1, tab_2 = st.tabs(["Fracture Length", "Preassure based on fracture length and permeability"])

with tab_1:
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
            
            if st.button("Result", key="1",use_container_width=True):
                
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

with tab_2:
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            e = st.number_input(label="modulus young")      
            q = st.number_input(label="Constant flow rate")      
            mu = st.number_input(label="viscosity")      
            lf = st.number_input(label="Length Fracturing")      
            h = st.number_input(label="Fracture height")  
            Ptip = st.number_input(label="Fracture tip pressure")  

    with col2: 
        with st.container():
            st.write("""### Input the Net Pressure""")
            
            if st.button("Result", use_container_width=True):
                if h != 0:
                    P_net = (((e**(3/4))/h) * (mu * q * lf)**(1/4)) + Ptip 
                elif h==0:
                    st.warning("The height fracture must non-zero", icon="⚠️")
                
                st.markdown(f"<div style='text-align: center;'>Pressure Net: {round(P_net, 3)} psi</div>", unsafe_allow_html=True)
                st.latex(r"""P_{net} = \frac{E^{3/4}}{h} \left( \mu \times Q \times L \right)^{1/4} + P_{tip}""")
                st.markdown(f"<div style='text-align: center;'><span style='font-size: 1.5rem;'>Calculated Pressure Net: </span><span style='font-size: 2rem;'>{P_net:.3f} psi</span></div>",unsafe_allow_html=True
    )


