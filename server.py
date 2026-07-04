import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Threat Intelligence MCP")

VT_API_KEY = "API_KEY"
ABUSE_API_KEY = "API_KEY"


@mcp.tool()
def lookup_ip_reputation(ip: str) -> dict:
    """
    Check an IP address using VirusTotal and AbuseIPDB.
    Returns a combined reputation report.
    """

    result = {
        "ip": ip,
        "virustotal": {},
        "abuseipdb": {}
    }

    # ----------------------------
    # VirusTotal
    # ----------------------------
    vt_headers = {
        "x-apikey": VT_API_KEY
    }

    vt_url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    try:
        vt_response = requests.get(
            vt_url,
            headers=vt_headers,
            timeout=30
        )

        if vt_response.status_code == 200:
            data = vt_response.json()

            stats = data["data"]["attributes"]["last_analysis_stats"]

            result["virustotal"] = {
                "malicious": stats.get("malicious"),
                "suspicious": stats.get("suspicious"),
                "harmless": stats.get("harmless"),
                "undetected": stats.get("undetected")
            }

        else:
            result["virustotal"] = {
                "error": vt_response.text
            }

    except Exception as e:
        result["virustotal"] = {
            "error": str(e)
        }

    # ----------------------------
    # AbuseIPDB
    # ----------------------------
    abuse_headers = {
        "Key": ABUSE_API_KEY,
        "Accept": "application/json"
    }

    abuse_url = "https://api.abuseipdb.com/api/v2/check"

    try:

        abuse_response = requests.get(
            abuse_url,
            headers=abuse_headers,
            params={
                "ipAddress": ip,
                "maxAgeInDays": 90
            },
            timeout=30
        )

        if abuse_response.status_code == 200:

            data = abuse_response.json()["data"]

            result["abuseipdb"] = {
                "abuseConfidenceScore": data["abuseConfidenceScore"],
                "countryCode": data["countryCode"],
                "usageType": data["usageType"],
                "isp": data["isp"],
                "totalReports": data["totalReports"]
            }

        else:
            result["abuseipdb"] = {
                "error": abuse_response.text
            }

    except Exception as e:
        result["abuseipdb"] = {
            "error": str(e)
        }

    return result


if __name__ == "__main__":
    mcp.run()
