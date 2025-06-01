
# SMSBomber

**Interactive Multi-API SMS Bomber**

A modern SMS bomber with support for Iranian and international APIs, interactive colored menu, smart phone number detection, proxy support, and more.

---

## 🚀 Features

- Interactive menu with colored output
- Smart phone number parsing (with country code)
- Multiple APIs (Iranian and international)
- Online API detection and selection
- Send SMS via one selected API or all online APIs
- Proxy support (SOCKS/HTTP)
- Adjustable message count and timeout
- Real-time sent/failed statistics
- Easy to add new APIs

---

## ⚙️ Installation

1. **Install Python 3.7 or higher**

   - [Download Python](https://www.python.org/downloads/)
   - On Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

2. **Download and extract the project**
   - If you have the zip file:
     ```bash
     unzip smsbomber.zip
     cd smsbomber
     ```
   - Or clone with git:
     ```bash
     git clone https://github.com/YOUR-USERNAME/smsbomber.git
     cd smsbomber
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Or, if you have multiple versions:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

---

## 💻 How To Run

```bash
python smsbomber.py
```
Or:
```bash
python3 smsbomber.py
```

---

## 🟢 Example

```bash
$ python smsbomber.py

[Banner and menu appear...]

Select an option: 1

Target phone number (with country code): 989123456789
Checking online APIs, please wait...

[ API Send Mode ]
[1] Send using one selected API
[2] Send using ALL available online APIs
[0] Cancel

Choose mode: 2
Number of messages (default 10): 10
Timeout between messages (seconds, default 1): 1
Proxy (leave blank for none):

[+] Sending 10 SMS to 989123456789 | Mode: all

[Snapp] SMS sent successfully!
[Divar] SMS sent successfully!
[OLX] SMS failed!
...
[=] Finished! Total sent: 18, failed: 2
```

---

## ⚠️ Disclaimer

This tool is for **educational and authorized testing purposes only**.  
We are not responsible for any misuse.  
**Do not use this tool without permission.**

---

## 📝 License

MIT

---

## 🤝 Contributing

Pull requests for new APIs and features are welcome!
