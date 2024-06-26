Python Port Scanner

Overview

This Python script is a simple yet effective port scanner that allows users to scan for open ports on a specified target host. It supports both hostname and IP address inputs and allows users to specify a custom port range for scanning.


Features
Scan for open TCP ports on a target host.
Support for both hostname and IP address inputs.
Customizable port range for scanning.
Visual indication of scanning activity using a spinning cursor.
Error handling for keyboard interrupts and socket-related errors.

Requirements

Python 3.x
Python pyfiglet library (install using pip install pyfiglet)

Usage

Clone or download the repository to your local machine.
Navigate to the directory containing the script.
Run the script using the command:
python portscanner.py [target]
Replace [target] with the hostname or IP address of the target host.
Follow the on-screen prompts to specify the port range for scanning.

Example

$ python port_scanner.py example.com
Enter port range (e.g., '1-100', '80,443', or '22'): 1-100

Notes

Ensure that you have proper authorization before scanning any target host.
Running port scans against hosts without permission may violate network policies and legal regulations.
