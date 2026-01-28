# GLSevereNetwork (GLSN) Lite

[![Label Sync](https://github.com/GLSevereNet/GLSN-lite/actions/workflows/auto-labels.yml/badge.svg)](https://github.com/GLSevereNet/GLSN-lite/actions/workflows/auto-labels.yml)
[![Auto Assign](https://github.com/GLSevereNet/GLSN-lite/actions/workflows/auto-assign.yml/badge.svg)](https://github.com/GLSevereNet/GLSN-lite/actions/workflows/auto-assign.yml)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/github/license/GLSevereNet/GLSN-lite)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)

---

GLSN Lite is a lightweight, open-source Python tool that fetches and displays **active weather alerts for Great Lakes Region** using the [National Weather Service (NWS) API](https://www.weather.gov/documentation/services-web-api).  
It is a simplified, community-friendly edition of the private GLSN project, designed for transparency & educational use.

---

## ✨ Features
- Fetches **live weather alerts** for WI, MI, OH, IL, and IN directly from NWS.
- Displays event type, severity, affected areas, and effective/expiration times.
- Command-line interface (CLI) with **no extra setup required**.
- Lightweight – only depends on `requests` and colorama.

---

## 📦 Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/GLSevereNet/GLSN-lite.git
cd GLSN-lite
pip install -r requirements.txt
python main.py
```

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo, open an issue, or submit a pull request to suggest improvements.

## 📜 License

This project is licensed under the GNU GPLv3 License.
