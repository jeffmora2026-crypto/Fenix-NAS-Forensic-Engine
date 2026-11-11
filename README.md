# Sovereign NAS Forensic Engine (Fénix-NAS) 🛡️🔍

**High-precision forensic auditing and storage anomaly cross-referencing engine for Sovereign NAS.**

---

## 📋 Overview
The **Sovereign NAS Forensic Engine (Fénix-NAS)** is an engineering-grade solution designed for forensic analysis of self-hosted storage systems (*Sovereign NAS*). Built entirely in pure Python with a minimalist architecture, it operates through register cross-referencing, early detection of hardware/software anomalies, and deterministic data integrity at the edge.

Designed and developed under strict resource-optimization and data-sovereignty principles, it executes seamlessly within high-constraint and mobile processing environments (*Termux / Linux ARM*).

---

## 🛠️ Repository Architecture
The core engine consists of specialized, dependency-free modules:

* **`nas_forensic_auditor.py`**: Central volume scanning and integrity auditing module, responsible for auditing the trace of storage blocks.
* **`nas_anomaly_crosser.py`**: Cross-referencing algorithm designed to correlate performance deviations, I/O drops, and logical corruption patterns.
* **`HABILIDAD.md`**: Detailed technical documentation of the engine's operational and vector capabilities.
* **`LICENCIA`**: Intellectual property protection and exclusive authorship clause.

---

## 🔒 Resilience & Deterministic Recovery (Anti-Corruption)
Specifically engineered for critical storage and video surveillance environments exposed to abrupt power outages:
* **SHA-256 Integrity:** Every critical data block is backed by an immutable reference hash signature.
* **Post-Reboot Self-Restructuring:** Following a power failure or bit-level corruption on the hard drive, the engine executes an instant forensic audit, detecting hash discrepancies and isolating compromised sectors to guarantee logical consistency and automatic recovery of video surveillance streams without manual intervention.

---

## ⚙️ Technical Specifications & Execution

The engine requires no heavy virtual environments or complex external library installations. To execute a forensic audit and cross-reference analysis on your local server, run:

```bash
# Clone the repository
git clone [https://github.com/jeffmora2026-cripto/Motor-forense-Fenix-NAS.git](https://github.com/jeffmora2026-cripto/Motor-forense-Fenix-NAS.git)
cd Motor-forense-Fenix-NAS

# Execute the base forensic auditor
python3 nas_forensic_auditor.py

# Execute the anomaly cross-reference engine
python3 nas_anomaly_crosser.py
