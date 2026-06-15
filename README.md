# CCNA Cybersecurity Lab Assets

Companion files for hands-on labs. Copy this folder alongside your module work, or clone the full repository.

## Quick start

```text
lab-assets/
  five-tuple-lab.csv          # Module 1 Lab 3 (import to spreadsheet)
  five-tuple-lab-KEY.txt      # Instructor / self-check answer key
  demo-tls.pcap               # Module 2 TLS visibility demo
  intrusion-lab.pcap          # Module 4 Lab 3 PCAP investigation
  windows-security-sample.txt # Module 3 Windows Event 4624/4625
  siem-json-sample.json       # Module 3 SIEM field mapping
  sandbox-report-invoice.txt  # Module 3 Lab 3 sandbox narrative
  module4-lab1-log-lines.csv  # Module 4 Lab 1 ten log lines
  module4-regex-answers.txt   # Module 4 Lab 3 regex key
  module2-classification-records.csv
  ngfw-log-sample.txt         # Module 2 objective 2.2.c--g samples
  avc-log-sample.txt
  web-filter-log-sample.txt
  email-filter-log-sample.txt
  netflow-export-template.csv
  cvss-worksheet-template.csv
  protected-data-inventory-template.csv
  raci-template.csv
  tabletop-timeline-template.csv
  soc-metrics-template.csv
  chain-of-custody-template.csv
  generate_pcaps.py           # Regenerate PCAPs if needed (requires scapy)
```

## Regenerating PCAP files

```bash
pip install scapy
python generate_pcaps.py
```

## Overleaf users

Upload `lab-assets/` and `figures/` to your Overleaf project root (same level as `main.tex`). Figures are optional until you add PNGs per `FIGURE.md`.

## Safety

All malware references use EICAR, fictitious domains, or sandbox reports. Do not execute unknown samples outside isolated lab targets.
