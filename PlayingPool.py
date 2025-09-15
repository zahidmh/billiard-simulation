from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time

print("Program Started")

client = RemoteAPIClient('127.0.0.1', 23000)
sim = client.require('sim')

# Start simulation
sim.startSimulation()

# Get handle for Sphere[6]
ball = sim.getObject('/Sphere[6]')

print("Listening for sandbox button presses...")

try:
    while True:
        cmd = sim.getStringSignal("control_cmd")

        if cmd == "w":
            sim.addForceAndTorque(ball, [0, 0, 0], [5, 0, 0])
            sim.clearStringSignal("control_cmd")
        elif cmd == "s":
            sim.addForceAndTorque(ball, [0, 0, 0], [-5, 0, 0])
            sim.clearStringSignal("control_cmd")
        elif cmd == "a":
            sim.addForceAndTorque(ball, [0, 0, 0], [0, 5, 0])
            sim.clearStringSignal("control_cmd")
        elif cmd == "d":
            sim.addForceAndTorque(ball, [0, 0, 0], [0, -5, 0])
            sim.clearStringSignal("control_cmd")

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Stopping simulation...")
    sim.stopSimulation()
