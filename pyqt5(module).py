import sys
import socket
import threading
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class PortScannerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Port Scanner")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        # Target IP
        self.label_ip = QLabel("Target IP:")
        layout.addWidget(self.label_ip)
        self.input_ip = QLineEdit()
        layout.addWidget(self.input_ip)

        # Start Port
        self.label_start_port = QLabel("Start Port:")
        layout.addWidget(self.label_start_port)
        self.input_start_port = QLineEdit()
        layout.addWidget(self.input_start_port)

        # End Port
        self.label_end_port = QLabel("End Port:")
        layout.addWidget(self.label_end_port)
        self.input_end_port = QLineEdit()
        layout.addWidget(self.input_end_port)

        # Scan Button
        self.scan_button = QPushButton("Scan")
        self.scan_button.clicked.connect(self.start_scan)
        layout.addWidget(self.scan_button)

        # Result Box
        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        layout.addWidget(self.result_box)

        self.setLayout(layout)

    def start_scan(self):
        target = self.input_ip.text()
        try:
            start_port = int(self.input_start_port.text())
            end_port = int(self.input_end_port.text())
        except ValueError:
            self.result_box.append("[!] Please enter valid port numbers.")
            return

        self.result_box.append(f"Scanning {target} from port {start_port} to {end_port}...\n")
        
        # Run scan in a separate thread to avoid freezing the GUI
        scan_thread = threading.Thread(target=self.scan_ports, args=(target, start_port, end_port))
        scan_thread.start()

    def scan_ports(self, target, start_port, end_port):
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                self.result_box.append(f"[+] Port {port} is open")
            s.close()
        
        self.result_box.append("Scan complete!\n")

# Run the PyQt Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PortScannerApp()
    window.show()
    sys.exit(app.exec())
