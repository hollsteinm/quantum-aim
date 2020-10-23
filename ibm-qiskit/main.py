import qiskit as q

def bell_state_example():
  # Our Quantum Circuit
  # For Qiskit we will initialize our quantum circuit with two quibts
  # and two classical bits for output after measurement
  c = q.QuantumCircuit(2, 2)
  
  # Build our bell state
  # First we apply the Hadamard gate to the first quibit
  c.h(0)
  
  # Then we apply a controlled not with the first quibit being the control
  # and the second being the target
  c.cx(0, 1)
  
  # Measurement collapses the wave function and can write results to classical
  # bits for classical use
  c.measure([0, 1], [0, 1])
  
  # We can draw our circuit to the console, this also supports more
  # academic and visual outputs as well
  print(c.draw('text'))
  
  # Aer and a *_simulator are the local simulators for qiskit
  backend = q.Aer.get_backend('qasm_simulator')
  
  # This is where we execute the async operation for the quantum circuit
  job = q.execute(c, backend, shots=1000)
  
  # We are doing a simulation so a blocking call is just fine
  result = job.result()

  # We can now visualize our results
  outputstate = result.get_counts()
  print(outputstate)

  return


if __name__ == "__main__":
  bell_state_example()