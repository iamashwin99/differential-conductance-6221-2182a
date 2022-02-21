import os
import streamlit as st
import numpy as np
from PIL import  Image
from k6221 import *
import plotly.express as px
from measurements import dcon,delta,sinewave,lsweep,lsweep_delta

# Custom imports 
from multipage import MultiPage

#Iport visa resource
rm = pyvisa.ResourceManager()
x = None

address = "TCPIP::10.0.4.138::1394::SOCKET"
dev = Keithley6221(address=address, rm=rm)



# Create an instance of the app 
app = MultiPage()

# Title of the main page
#display = Image.open('Logo.png')
#display = np.array(display)
col1, col2 = st.columns(2)
col1.image('Logo.png', width = 300)
col2.title("Differential Conductance Measurement Application")

# Add all your application here
app.add_page("Differential Conductance", dcon.app)
app.add_page("Delta measurement", delta.app)
app.add_page("Linear Sweep", lsweep.app)
app.add_page("Sine Output", sinewave.app)


# The main app
app.run()