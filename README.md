### README.md

```markdown
# Multi-Threaded Port Scanner

A multi-threaded port scanner that efficiently scans ports for a given IP or hostname using Python. It supports scanning common ports, top 100 ports, or all ports in the range `1-65535`. This tool is designed for speed and reliability, with user-friendly options and detailed reporting.

---

## Features

- **Multi-threaded Scanning**: Uses threading for faster scans.
- **User Options**:
  - Scan common ports (e.g., 21, 22, 80, 443).
  - Scan top 100 ports.
  - Perform an extensive scan (1-65535).
- **IPv4 and IPv6 Support**.
- **Real-time Status**: Displays open and closed ports during the scan.
- **Report Generation**: Saves scan results to a file for future reference.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/port-scanner.git
   ```
2. Navigate to the project directory:
   ```bash
   cd port-scanner
   ```
3. Install the required dependencies:
   ```bash
   pip install termcolor
   ```

---

## Usage

1. Run the script:
   ```bash
   python port_scanner.py
   ```

2. Follow the prompts:
   - Enter the target IP address or hostname.
   - Choose the scan option:
     - Common ports
     - Top 100 ports
     - All ports (1-65535)

3. Review the results in the terminal or save them to a report file.

---

## Example

```plaintext
////////////////////////////////////////////////////////////////////////
//   _   _      _                      _                              //
//  | \ | | ___| |___      _____  _ __| | __                          //
//  |  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /                          //
//  | |\  |  __/ |_ \ V  V / (_) | |  |   <                           //
//  |_|_\_|\___|\__| \_/\_/ \___/|_|  |_|\_\                          //
//  |  _ \ ___  _ __| |_     / ___|  ___ __ _ _ __  _ __   ___ _ __   //
//  | |_) / _ \| '__| __|    \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|  //
//  |  __/ (_) | |  | |_      ___) | (_| (_| | | | | | | |  __/ |     //
//  |_|   \___/|_|   \__|    |____/ \___\__,_|_| |_|_| |_|\___|_|     //
//                                                                    //
////////////////////////////////////////////////////////////////////////

Made by - Aariz S

Enter target (IP or Hostname): 192.168.1.1
Select Scan Option:
1. Common ports (21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 8080)
2. Top 100 ports
3. All ports (Extensive Scan: 1-65535)
Enter your choice (1/2/3): 1

Starting scan on 192.168.1.1...
Port 21: Closed
Port 22: Open
Port 80: Open
...

Do you want to save the report to a file? (y/n): y
Report saved to scan_report_192.168.1.1.txt
```

---

## File Structure

```
port-scanner/
├── port_scanner.py   # Main script
├── README.md         # Documentation
```

---

## Dependencies

- Python 3.6+
- [termcolor](https://pypi.org/project/termcolor/)

---

## Notes

- This tool is for educational purposes only. Use it responsibly and ensure you have permission to scan any target.
- Extensive scans (`1-65535`) can take significant time depending on your system and network conditions.

---

## Author

**Aariz S**
- GitHub: [github.com/aariz-s](https://github.com/aariz-s)
- Email: <your-email@example.com>

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
``` 

Let me know if you'd like any changes!
