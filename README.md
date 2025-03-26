# Port Scanner GUI

## Overview
This Python script provides a **GUI-based port scanner** using `PyQt6`. It allows users to scan a target IP address for open ports within a specified range.

## Features
✅ GUI built with PyQt6  
✅ Scans a target IP for open ports  
✅ Allows user-defined start and end ports  
✅ Runs scanning in a separate thread to prevent UI freezing  

## Installation
1. Ensure you have Python 3.x installed.
2. Install required dependencies:
   ```bash
   pip install pyqt6
   ```

## Usage
1. Run the script:
   ```bash
   python port_scanner.py
   ```
2. Enter the target **IP address**.
3. Set the **start and end port** range.
4. Click **Scan** to begin port scanning.
5. Open ports will be displayed in the result box.

## How It Works
- Uses `socket` to check if a port is open.
- Scans ports in the provided range.
- Runs scanning in a separate thread to prevent UI freezing.

## Future Enhancements
- **Progress Bar**: Show scanning progress.
- **Save Results**: Export scan results to a file.
- **Multi-threaded Scanning**: Speed up the scanning process.

