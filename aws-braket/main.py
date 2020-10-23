from braket.aws import AwsDevice
from braket.devices import LocalSimulator
from braket.circuits import Circuit

def bell_state_example():
  # Our Quantum Circuit
  # (h) Apply the Hadamard gate to the first qubit, this puts it into superposition
  # (cnot) Apply a Controlled Not gate to the first qubit (control) and a second qubit (target)
  # This entagles the two qubits. This is known as the Bell State.
  
  bell_state = Circuit().h(0).cnot(0, 1)
  
  # AWS Braket can print a textual representation of your circuit
  print(bell_state)
  
  # This will run a quantum simulation on your local machine, try to keep below 20-ish qubits
  simulator = LocalSimulator()
  
  # AWS Braket simulations are ran async, but here we can block on the result for a local simulation.
  # Shots is unique to quantum computing, you must run the same algorithm multiple times to get ample
  # enough results for your probability distribution of results. This is where you decide the most
  # probable result of your algorithm, which may be the "right" result
  simulation = simulator.run(bell_state, shots=1000)
  result = simulation.result()
  
  # Measure our results
  counts = result.measurement_counts
  
  # What this displays is how often your entagled qubits ended up in the states of '11' or '00'.
  # This sums to the number of shots
  print(counts)
  
  return
  
if __name__ == "__main__":
  bell_state_example()