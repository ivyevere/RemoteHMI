from pycomm3 import LogixDriver
from time import sleep


# Assign PLC IPs
PLC1 = '10.18.54.21'
PLC2 = '10.18.54.31'
PLC3 = '10.18.54.41'
PLC4 = '10.18.54.51'
PLC5 = '10.18.54.61'
PLC6 = '10.18.54.71'
PLC7 = '10.18.54.81'

# Assign Start/Stop Tags
startPLC1, stopPLC1,  = None, None
startPLC2 = None # Could use safety rated start button?
startPLC3 = None
startPLC4, stopPLC4 = 'HMI.SystemStartPB', None
startPLC5 = 'HMI.SystemStartPB'
startPLC6 = 'HMI_Start'
startPLC7 = None # Not used

# Assign Condensed Reset Tags [MTR, JAM, AIR, COMMS]
resetPLC3 = ['IN_032250_PBLT', None, 'IN_032252_PBLT', 'IN_032253_PBLT']
resetPLC4 = ['IN_042250_PBLT_MTRFLTRST', 'IN_042251_PBLT_JAMRST', 'IN_042252_PBT_LOWAIRRST', 'IN_042253_PBLT_COMMSFLTRST']

# Read tag from PLC. Inputs are PLC name(ip), Tag value string
def read_tag(ip, tag):
    with LogixDriver(ip) as PLC:
        PLC.read(tag)

# Write tag to PLC. Inputs are PLC name(ip), Tag value string, Boolean 
def write_tag(ip, tag, value):
    with LogixDriver(ip) as PLC:
        PLC.write(tag, value)

# Toggle tag to PLC. Inputs are PLC name(ip), Tag value string, Boolean 
def toggle_tag(ip, tag):
    with LogixDriver(ip) as PLC:
        PLC.write(tag, 1)
        # Wait two seconds before toggling again
        sleep(2)
        PLC.write(tag, 0)

#toggle_tag(PLC6, 'HMI_Start')
print("done")



