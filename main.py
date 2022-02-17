import pyvisa
from functions import *
rm = pyvisa.ResourceManager()
k6221=rm.open_resource("TCPIP::10.0.4.138::1394::SOCKET")
k6221.read_termination = '\n'
k6221.write_termination = '\n'
k6221.query('*IDN?')
