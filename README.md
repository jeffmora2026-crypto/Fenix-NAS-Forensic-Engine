# Fenix Security Skill

> **Sovereign NAS Forensic Audit & Storage Anomaly Cross-Referencing Engine**

Fenix Security Skill is a high-performance, zero-dependency security tool optimized for Network Attached Storage (NAS) systems, edge nodes, and resource-constrained Linux environments.

---

## 🌟 Key Features

* **Zero-Dependency Architecture:** Written in standard Python 3; runs standalone without heavy third-party packages or external database servers.
* **Forensic Log Audit:** Scans JSON-formatted system streams for security risk vectors (`permission_denied`, `checksum_mismatch`, `bulk_modification`).
* **Volume Quota Anomaly Detection:** Calculates mathematical discrepancy factors between defined volume quotas and actual disk consumption.
* **Automated Tactical Reporting:** Generates structured JSON security reports for downstream SIEM integration or operator analysis.

---

## 🛠️ Usage

### 1. Forensic Log Integrity Audit
```bash
python3 scripts/nas_forensic_auditor.py <target_json_endpoint_url>
python3 scripts/nas_anomaly_crosser.py
