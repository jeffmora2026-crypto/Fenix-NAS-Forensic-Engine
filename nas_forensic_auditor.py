import sys
import json
import urllib.request
import urllib.error

RISK_VECTOR_MATRIX = [
    {
        "vector_id": "SEC-01",
        "description": "Privilege escalation or unauthorized access attempts in system logs",
        "target_pattern": "permission_denied",
        "category": "Access Control"
    },
    {
        "vector_id": "SEC-02",
        "description": "Block corruption or checksum failure (Bit Rot / Data degradation)",
        "target_pattern": "checksum_mismatch",
        "category": "Data Integrity"
    },
    {
        "vector_id": "SEC-03",
        "description": "Mass file modification or anomalous directory purge",
        "target_pattern": "bulk_modification",
        "category": "Volume Anomaly"
    },
    {
        "vector_id": "SEC-04",
        "description": "Unrecognized external IP connection attempts in trace logs",
        "target_pattern": "unauthorized_ip",
        "category": "Perimeter Security"
    }
]

def audit_nas_integrity_patterns(endpoint_url):
    print(f"\n🛡️ [STARTING FORENSIC NAS INTEGRITY & SECURITY AUDIT]")
    print(f"📡 Target Endpoint: {endpoint_url}\n" + "=" * 65)

    try:
        req = urllib.request.Request(
            endpoint_url,
            headers={
                'User-Agent': 'Mozilla/5.0 (FenixForensicIntelligenceEngine)',
                'Accept': 'application/json'
            }
        )

        with urllib.request.urlopen(req, timeout=12) as response:
            data_raw = response.read().decode('utf-8')
            data = json.loads(data_raw)
            records = data if isinstance(data, list) else [data]

            findings = []

            for vector in RISK_VECTOR_MATRIX:
                pattern = vector["target_pattern"].lower()
                matches_count = 0

                for reg in records:
                    reg_str = json.dumps(reg, ensure_ascii=False).lower()
                    if pattern in reg_str:
                        matches_count += 1

                if matches_count > 0:
                    findings.append({
                        "vector_id": vector["vector_id"],
                        "description": vector["description"],
                        "category": vector["category"],
                        "detected_pattern": pattern,
                        "total_alerts": matches_count
                    })

            print("📋 [FINDINGS & NAS RISK VECTOR REPORT]:")
            if findings:
                print(json.dumps(findings, indent=2, ensure_ascii=False))
                print(f"\n🚨 Detected {len(findings)} critical alert vectors in target storage endpoint.")
            else:
                print("✅ No direct anomaly patterns found for the defined risk matrix.")

    except urllib.error.URLError as e:
        print(f"❌ Network connection error: {e.reason}")
    except json.JSONDecodeError:
        print("⚠️ Target endpoint did not return valid interpretable JSON.")
    except Exception as e:
        print(f"❌ Execution error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/nas_forensic_auditor.py <api_endpoint_url>")
        sys.exit(1)

    url_target = sys.argv[1]
    audit_nas_integrity_patterns(url_target)
