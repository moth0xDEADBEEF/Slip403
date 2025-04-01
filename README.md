# Slip403

**Slip403** is a modular 403 bypass scanner built for ethical hackers, bug bounty hunters, and red teamers.  
It automates access control testing using path manipulation, header injection, method variation, and response fingerprinting.
This tool will (intentionally) not fly under the radar as it is never meant to be used out of scope or to attack unknowing targets.

---

## 🚀 Features

- ✅ 30+ URL/path modifiers (encoded slashes, dot tricks, etc.)
- ✅ Header-based bypasses (X-Forwarded-For, X-Host, etc.)
- ✅ Method override support (`GET`, `POST`, `TRACE`)
- ✅ Baseline detection to identify meaningful bypasses
- ✅ SHA-256 response hashing to reduce false positives
- ✅ Optional response saving for successful 200s
- ✅ Fully modular CLI, Python 3.8+

---

## 🛠 Installation

Clone the repo and install locally:

```bash
git clone https://github.com/moth0xDEADBEEF/slip403.git
cd slip403
pip install .
```

> This will install `slip403` as a global command.

---

## 💻 Usage

```bash
slip403 --url https://example.com --path admin
```

---

### Optional Flags

| Flag                 | Description                                              |
|----------------------|----------------------------------------------------------|
| `--delay`            | Delay between requests (default: `0.3`)                 |
| `--methods`          | Comma-separated HTTP methods (default: `GET,POST,TRACE`)|
| `--compare-baseline` | Compare against baseline forbidden response             |
| `--hash-responses`   | Enable SHA-256 response body hashing                    |
| `--save-responses`   | Save successful 200s that differ from baseline          |
| `--output`           | Output CSV file (default: `bypass_log.csv`)            |

---

## 📂 Example

```bash
slip403 --url https://target.com --path admin --compare-baseline --hash-responses --save-responses
```

---

## ⚠️ Legal Disclaimer

Slip403 is intended for **authorized testing only**.

This tool is provided for educational and ethical research purposes.  
Use of Slip403 without proper permission from the target system owner is **strictly prohibited**.

The author assumes **no liability** for any misuse or damage caused.  
Always stay in scope. Always get permission. Hack responsibly.
