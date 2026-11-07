import sys
import json

AUTHORIZED_DIRECTORIES = {
    "vol-01-backups": {
        "name": "Main Backup Server",
        "allowed_quota_gb": 500.0,
        "role": "Historical Storage"
    },
    "vol-02-documents": {
        "name": "Legal Document Repository",
        "allowed_quota_gb": 150.0,
        "role": "Notarial Files"
    },
    "vol-03-transient": {
        "name": "Temporary Transit Buffer",
        "allowed_quota_gb": 50.0,
        "role": "Transit Queue"
    },
    "vol-04-external": {
        "name": "Remote Edge Node Mount",
        "allowed_quota_gb": 200.0,
        "role": "Peripheral Sync"
    }
}

NAS_REAL_CONSUMPTION = [
    {
        "identifier": "vol-01-backups",
        "used_space_gb": 650.0,
        "concept": "Backup overflow due to file duplication anomaly"
    },
    {
        "identifier": "vol-02-documents",
        "used_space_gb": 900.0,
        "concept": "Uncategorized massive file injection in protected volume"
    },
    {
        "identifier": "vol-03-transient",
        "used_space_gb": 45.0,
        "concept": "Operational load within expected thresholds"
    },
    {
        "identifier": "vol-04-external",
        "used_space_gb": 850.0,
        "concept": "Anomalous traffic volume stream from unrecognized external endpoint"
    }
]

def calculate_anomaly_threshold(quota, usage):
    if quota <= 0:
        return 999.0
    return round(usage / quota, 2)

def audit_nas_discrepancies():
    print("\n🔍 [FENIX FORENSIC AUDIT - NAS STORAGE ANOMALY DETECTOR]")
    print("=======================================================================\n")

    alerts = []

    for item in NAS_REAL_CONSUMPTION:
        target_id = item["identifier"]
        real_usage = item["used_space_gb"]
        concept = item["concept"]

        if target_id in AUTHORIZED_DIRECTORIES:
            volume = AUTHORIZED_DIRECTORIES[target_id]
            quota = volume["allowed_quota_gb"]
            discrepancy_factor = calculate_anomaly_threshold(quota, real_usage)

            if discrepancy_factor >= 1.2:
                alerts.append({
                    "identifier": target_id,
                    "volume_name": volume["name"],
                    "role": volume["role"],
                    "allowed_quota_gb": quota,
                    "actual_usage_gb": real_usage,
                    "discrepancy_factor_x": discrepancy_factor,
                    "operation_concept": concept,
                    "risk_level": "HIGH / QUOTA OVERCONSUMPTION" if discrepancy_factor < 3.0 else "CRITICAL / POTENTIAL INTRUSION OR DATA EXFILTRATION"
                })

    print("🚨 [TACTICAL FORENSIC REPORT GENERATED]:")
    print(json.dumps(alerts, indent=2, ensure_ascii=False))
    print(f"\n📊 Total volume anomalies detected: {len(alerts)}")
    print("-" * 71)

    output_filename = "fenix_tactical_report.json"
    report_export = {
        "metadata": {
            "tag": "FenixSecurityEngine",
            "objective": "NAS Volume Discrepancy & Quota Control Matrix",
            "total_alerts": len(alerts)
        },
        "alerts": alerts
    }

    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(report_export, f, indent=2, ensure_ascii=False)

    print(f"📁 Tactical report successfully exported to: {output_filename}\n")

if __name__ == "__main__":
    audit_nas_discrepancies()
