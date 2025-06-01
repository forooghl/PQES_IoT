# **Post-Quantum IoT Security with Edge Computing (PQES) - Simulation**  
*A Python-based simulation of the paper:  
["Edge-Computing-Based Scheme for Post-Quantum IoT Security for e-Health"](https://ieeexplore.ieee.org/document/10571574)*  

---

## **📌 Project Overview**  
This project simulates the **Post-Quantum Edge Server (PQES)** architecture proposed in the IEEE paper, which offloads post-quantum cryptographic (PQC) operations from resource-constrained IoT devices to an edge server. The simulation includes:  
- **IoT devices** (simulated sensors).  
- **PQES** (Edge server handling PQC operations).  
- **Destination server** (Cloud/backend server).  

🔹 **Key Features:**  
✅ Simulates **Dilithium** (for signatures) and **Kyber** (for key encapsulation mechanism) using `liboqs-python`.  
✅ Measures **CPU/RAM usage** (like the original paper).  
✅ Works on **Windows/Linux** without physical hardware.  

---

## **🚀 Quick Start**  

### **1. Prerequisites**  
- Python 3.8+  
- Libraries:  
  ```bash
  pip install -r requirements.txt
  ``` 

### **2. Run the Simulation**  
1. **Start the Destination Server** (Cloud backend):  
   ```bash
   python destination_server.py
   ```
2. **Start the PQES (Edge Server)**:  
   ```bash
   python pqes_server.py
   ```
3. **Simulate IoT Devices**:  
   ```bash
   python iot_device.py
   ```
   *(Run multiple instances for concurrent testing.)*
   
4. **Monitoring Dashboard**:  
   ```bash
   python monitoring_dashboard.py
   ```
   *(Monitor cpu and memory usage.)*  
---

## **📂 Files & Structure**  
| File | Description |  
|------|-------------|  
| `destination_server.py` | Simulates the cloud server receiving PQ-encrypted data. |  
| `pqes_server.py` | Edge server handling PQC operations (Dilithium/Kyber). |  
| `iot_device.py` | Simulates IoT sensors sending health data (e.g., heart rate). |  
| `monitoring_dashboard.py` | Monitoring cpu and memmory usage of the project. |  
| `requirements.txt` | Lists all dependencies (`pip install -r requirements.txt`). |  

---

## **📊 Performance Metrics (vs. Paper)**  
| **Metric**          | **Paper (Hardware)** | **This Simulation** |  
|----------------------|----------------------|---------------------|  
| **Max RAM (PQES)**   | 13.4 MB              | ~13 MB              |  
| **Max CPU (PQES)**   | 1.75%                | ~2%                 |  
| **Latency**          | <1 ms                | <8 ms (simulated)  |  

---

## **🔧 Customization**  
1. **Change PQC Algorithms** (in `pqes_server.py` and `destination_server.py`):  
   ```python
   # Replace "Dilithium2" with other options (e.g., "Falcon-512")
   sig = Signature("Dilithium2")  
   kem = KeyEncapsulation("Kyber512")  
   ```
2. **Scale IoT Devices**:  
   ```python
   # In iot_device.py, launch multiple threads:
   for i in range(10):  
       threading.Thread(target=simulate_iot_device, args=(f"IoT-{i}",)).start()  
   ```

---

## **📜 Citation**  
If you use this code for research, cite the original paper:  
```bibtex
@article{minhas2024edge,
  title={Edge-Computing-Based Scheme for Post-Quantum IoT Security for e-Health},
  author={Minhas, Noman Nasir and Mansoor, Khwaja},
  journal={IEEE Internet of Things Journal},
  year={2024}
}
```

--- 

**🎉 Happy Post-Quantum Securing!**  
```bash
# Keep your IoT safe from quantum hackers! 🔒
```
