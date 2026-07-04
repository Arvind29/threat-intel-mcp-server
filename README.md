# Threat Intelligence MCP Server

A Python-based Model Context Protocol (MCP) server that exposes Threat Intelligence tools for AI assistants such as Claude Desktop.

This project demonstrates how to build a custom MCP server that integrates with:

- VirusTotal
- AbuseIPDB

The server exposes AI-callable tools that retrieve IP reputation data from multiple threat intelligence providers.

---

## Features

- MCP Server built using the official Python MCP SDK
- IP reputation lookup
- VirusTotal integration
- AbuseIPDB integration
- JSON response suitable for AI agents
- Compatible with Claude Desktop (Local MCP)

---

## Architecture

```
                    User
                      │
                      ▼
             Claude Desktop
             (MCP Client)
                      │
                      ▼
      Threat Intelligence MCP Server
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
 VirusTotal API             AbuseIPDB API
        │                           │
        └─────────────┬─────────────┘
                      ▼
             Combined Reputation
                      │
                      ▼
              Claude Response
```

---

## Technologies

- Python 3.14+
- Model Context Protocol (MCP)
- Requests
- VirusTotal REST API
- AbuseIPDB REST API

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/threat-intel-mcp.git

cd threat-intel-mcp
```

Install dependencies

```bash
pip install "mcp[cli]" requests
```

---

## Configuration

Edit `server.py`

Replace:

```python
VT_API_KEY = "YOUR_VIRUSTOTAL_API_KEY"

ABUSE_API_KEY = "YOUR_ABUSEIPDB_API_KEY"
```

with your own API keys.

---

## Running the Server

```bash
python server.py
```

To launch the MCP Inspector

```bash
mcp dev server.py
```

---

## Claude Desktop Configuration

Example configuration

```json
{
  "mcpServers": {
    "ThreatIntel": {
      "command": "python",
      "args": [
        "C:\\path\\to\\server.py"
      ]
    }
  }
}
```

Restart Claude Desktop after updating the configuration.

---

## Available Tool

### lookup_ip_reputation(ip)

Checks an IP address against:

- VirusTotal
- AbuseIPDB

Example:

```
Check IP 8.8.8.8
```

Example Response

```json
{
    "ip":"8.8.8.8",
    "virustotal":{
        "malicious":0,
        "suspicious":0
    },
    "abuseipdb":{
        "abuseConfidenceScore":0
    }
}
```

---

## Project Structure

```
.
├── server.py
├── README.md
└── requirements.txt
```

---

## Learning Objectives

This project demonstrates:

- Building a custom MCP Server
- Creating AI tools using FastMCP
- Integrating external REST APIs
- Returning structured JSON to AI clients
- Connecting a local MCP server to Claude Desktop

---

## References

- Model Context Protocol
- VirusTotal API
- AbuseIPDB API

---

## License

MIT License

---

## Disclaimer

This project is intended for educational purposes and demonstrates how to integrate external threat intelligence APIs with the Model Context Protocol (MCP). API usage is subject to the terms and rate limits of VirusTotal and AbuseIPDB.
