
# 🛡️ AI-Driven Vulnerability Detection & Testing System

This project is an internship-based initiative aimed at building an intelligent system that automates the process of detecting and testing vulnerabilities in software. The system fetches newly published vulnerabilities from a live CVE database (such as Vulners or NVD), uses AI/NLP to analyze them, and automatically tests the client’s software against those vulnerabilities.

It combines cybersecurity, software testing, and machine learning to automate vulnerability management and reporting.

---

## 🎯 Objectives

- 🛰️ **Fetch** real-time CVEs from a public vulnerability feed (e.g., Vulners API)
- 🧠 **Analyze** CVE data using AI/NLP to extract probable attack vectors
- 🔍 **Scan** client software for potential weak points
- 📊 **Generate** structured vulnerability reports with actionable insights

---

## ⚙️ Tech Stack

- **Python**
- **Vulners API / NVD Feed**
- **requests**, **dotenv**
- (Optional) React/Streamlit for dashboard

---

## 🚀 Planned Features

- ✅ Fetch newly published CVEs daily
- 🔍 AI model to map vulnerabilities to likely software risks
- 🧪 Automated testing based on CVE attack vectors
- 📄 Generate daily reports (text, PDF, or HTML)
- 📊 Dashboard for viewing scan results and risk levels

---

## 🗓️ Internship Duration: 6 Weeks

- **Week 1** – System Design & Architecture Planning
- **Week 2** – CVE Feed Research & API Integration
- **Week 3** – CVE Fetching & AI Risk Mapping
- **Week 4** – Test Algorithm Development
- **Week 5** – Report Generation & UI (Optional)
- **Week 6** – Final Integration, Testing & Documentation

---

## 📁 Project Structure (WIP)

```
project-root/
├── fetch_cves.py         # Daily CVE fetcher script
├── today_cves.txt        # Stores current day’s CVE logs
├── .env                  # Contains API key (not committed)
├── .gitignore            # Ignores .env and cache files
└── README.md             # This file
```

---

## 🔒 Security Notes

- API keys are securely stored using `.env` and `python-dotenv`
- `.env` is included in `.gitignore` to prevent leaks

---

## 📌 Disclaimer

This project is under active development as part of a 6-week summer internship focused on **cybersecurity** and **automated software testing**.
