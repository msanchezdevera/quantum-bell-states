from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Crear circuito con 2 qubits y 2 bits clásicos
qc = QuantumCircuit(2, 2)

# Superposición
qc.h(0)

# Entrelazamiento
qc.cx(0, 1)

# Medición
qc.measure([0, 1], [0, 1])

# Simulador
simulator = AerSimulator()

# Ejecución con 1024 corridas
job_1024 = simulator.run(qc, shots=1024)
result_1024 = job_1024.result()
counts_1024 = result_1024.get_counts()

print("Resultados con 1024 corridas:")
print(counts_1024)

# Ejecución con 1 corrida
job_1 = simulator.run(qc, shots=1)
result_1 = job_1.result()
counts_1 = result_1.get_counts()

print("Resultado con 1 corrida:")
print(counts_1)