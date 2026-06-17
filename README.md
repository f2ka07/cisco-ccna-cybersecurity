# CCNA Cybersecurity: Hands-On SOC Operations from Zero to Certification Lab Assets

**Canonical source** for hands-on lab files in *CCNA Cybersecurity: Hands-On SOC Operations from Zero to Certification* (Cisco exam **200-201 CCNACBR** v1.2).

The book is accessible at: [Book Title](https://skilleo.web.app/books)  
Practice Mock Tests are accessible at: [Practice Mock Tests](https://www.udemy.com/course/cisco-ccna-cybersecurity-200-to-201-complete-exam-prep/?referralCode=3E9FAF32B7ACDB2809C7)

The print and digital book **does not bundle** these files. This GitHub repository is the permanent home for worksheets, sample logs, JSON alerts, sandbox reports, and synthetic PCAPs. Every lab file cited in the book (by bare filename) lives at the repository root below.

**Repository:** https://github.com/f2ka07/cisco-ccna-cybersecurity

## Quick start

```bash
git clone https://github.com/f2ka07/cisco-ccna-cybersecurity.git
cd cisco-ccna-cybersecurity
```

All files are at the **repository root** (no subfolder). After cloning, open files by the bare filename cited in the book (for example `five-tuple-lab.csv`).

Download a single file: use **Code > Download ZIP**, or open the file on GitHub and click **Raw**.

## Module index

| Module | File | Used in |
|--------|------|---------|
| 1 | `five-tuple-lab.csv` | Lab 3 -- 5-tuple hunt worksheet |
| 1 | `five-tuple-lab-KEY.txt` | Lab 3 answer key (suspect host) |
| 1 | `cvss-worksheet-template.csv` | Lab 2 CVSS worksheet |
| 2 | `demo-tls.pcap` | Guided demo and Lab 2 TLS visibility |
| 2 | `module2-classification-records.csv` | Lab 2 Part C -- data types 2.4 |
| 2 | `ngfw-log-sample.txt` | Lab 2 Part D -- NGFW/FTD 2.2.c |
| 2 | `avc-log-sample.txt` | Lab 2 Part D -- AVC 2.2.e |
| 2 | `web-filter-log-sample.txt` | Lab 2 Part D -- web filter 2.2.f |
| 2 | `email-filter-log-sample.txt` | Lab 2 Part D -- email filter 2.2.g |
| 3 | `windows-security-sample.txt` | Labs -- Event ID 4624/4625 |
| 3 | `siem-json-sample.json` | Lab 2 Part C -- SIEM field mapping 3.5 |
| 3 | `sandbox-report-invoice.txt` | Lab 3 -- sandbox narrative |
| 3 | `wazuh-ssh-brute-rule.xml` | Optional HIDS rule example 3.1.a |
| 4 | `module4-lab1-log-lines.csv` | Lab 1 -- ten log lines 4.1/4.2 |
| 4 | `module4-regex-answers.txt` | Lab 3 Part D regex key 4.10 |
| 4 | `intrusion-lab.pcap` | Lab 3 -- intrusion analysis pack |
| 4 | `netflow-export-template.csv` | Lab 2 -- NetFlow column template 4.5 |
| 5 | `protected-data-inventory-template.csv` | Project -- data classes 5.9 |
| 5 | `raci-template.csv` | Project -- RACI starter 5.5 |
| 5 | `tabletop-timeline-template.csv` | Demo -- IR tabletop 5.3--5.4 |
| 5 | `soc-metrics-template.csv` | Demo -- TTDetect / TTContain 5.11 |
| 5 | `chain-of-custody-template.csv` | Appendix -- forensic custody 5.6 |

## Answer keys and instructor checks

| File | Purpose |
|------|---------|
| `five-tuple-lab-KEY.txt` | Module 1 Lab 3 suspect host `192.168.56.101` |
| `module4-regex-answers.txt` | Module 4 Lab 3 regex patterns |
| `module2-classification-records.csv` | Includes `exam_objective` column for Part C |

Assessment keys in the book (Appendix H) align with these files.

## Regenerating PCAP files

Synthetic captures ship as `demo-tls.pcap` and `intrusion-lab.pcap`. To rebuild:

```bash
pip install scapy
python generate_pcaps.py
```

## Fictitious data

All IPs use RFC 5737 documentation ranges (`192.168.56.0/24`, `203.0.113.0/24`, etc.). Domains such as `evil.test` are reserved for examples. Malware references use EICAR, sandbox text reports, or isolated lab scenarios only.

**Do not** execute unknown samples or run attack tools against networks you do not own.

## Exam alignment

Files support the five CCNACBR v1.2 domains mapped to book Modules 1--5. Verify current exam topics on the [Cisco Learning Network](https://learningnetwork.cisco.com/) before your exam date.

## Updates

Corrections and new lab files are published on the `main` branch of this repository. Clone again or `git pull` if a lab chapter cites a file you do not have locally.
