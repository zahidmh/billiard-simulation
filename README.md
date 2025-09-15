# billiard-simulation
Using Coppelia Sim with ZEMQ Remote Python API to simulate a game of billiard

## How to Run the Simulation
1. Download and Open the (Billiard_Scene.ttt) file
2. Click on "start/resume simulation" button
3. Download and open the (PlayingPool.py) file
4. Change the port number based on which port Coppelia is opening (ie. 23000)
```python
client = RemoteAPIClient('127.0.0.1', 23000)
```
5. Run the Python file
6. Give the control input within Coppelia Sim Scene
