# pip install pyzmq cbor keyboard
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import keyboard
 
# Connecting to the CoppeliaSim server
client = RemoteAPIClient('localhost', 23000)
 
print('Program started')
sim = client.getObject('sim')
 
# Get the handle for the slider (prismatic joint)
slider = sim.getObject('/Prismatic_joint')
 
# Starting the simulation
sim.startSimulation()
print('Simulation started')
 
# Main control loop
def main():
    # Keep running until simulation is stopped
    while True:
        if keyboard.is_pressed('w'):  # Move slider to -0.15 position
            print("w is pressed")
            sim.setJointTargetPosition(slider, -0.15)
         
        if keyboard.is_pressed('s'):  # Reset slider to the original position
            print("s is pressed")
            sim.setJointTargetPosition(slider, 0.0)  # Reset to the initial position
 
        if keyboard.is_pressed('q'):  # Stop the simulation when 'q' is pressed
            print("q is pressed - stopping simulation")
            sim.stopSimulation()
            break
 
# Start the main control loop
main()