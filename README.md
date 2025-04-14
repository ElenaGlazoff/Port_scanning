##Project Title: TCP Port Scanner in Python

##Intended Audience:
This project has been developed as part of a Cyber Security course assessment. It is intended for students and learners who are exploring fundamental concepts in network security and vulnerability scanning.

## Objective and Requirements:
The objective of this project is to implement a basic Python-based TCP port scanner with the following functionalities:

- Accepts user input for hostnames or IP address.
- Resolves the selected hostname to its corresponding IPv4 address.
- Scans TCP ports in the range of 50 to 499 on the target host.
- Displays a list of open ports along with the time taken to complete the scan.

##Functionality Overview:
The script begins by prompting the user to input a list of hostnames or IP addresses.

-  ends when the user presses Enter on an empty line.
- A numbered list (starting from index 0) of the entered hostnames is displayed.
- The user selects a target host by entering the corresponding index number.
- The script resolves the selected hostname using DNS lookup to obtain its IPv4 address.
- A TCP scan is performed on ports 50 to 499 using socket connections.
- Open ports are identified based on successful connection attempts.
- A list of discovered open ports is displayed.
- The total duration of the scan (in seconds) is reported.
- Pressing Enter on an empty line during selection safely terminates the script.

##Error Handling:
The script will terminate and display appropriate error messages in the following scenarios:

- No hostnames were entered.
- An invalid index was entered (e.g., a number outside the list range, or a non-integer value).
- The selected hostname could not be resolved to an IP address.

##Development Environment:

- Operating System: Windows
- IDE/Text Editor: Visual Studio Code
- Programming Language: Python 3.11

##Required Library: 

- socket (Standard Python Library)
- The socket library enables low-level networking operations and is used to resolve hostnames to their respective IPv4 addresses using the function: socket.gethostbyname(hostname)
- List: A list is used to store the entered hostnames. Lists in Python can hold multiple data types and allow indexed access to elements.

##Getting Started:

1. Running the Script
Launch the script using your preferred Python environment.

2. Entering Hostnames or IP Addresses
You’ll be prompted to enter one or more hostnames or IP addresses.
Press Enter on an empty line to finish input.
Example:

www.google.com  
www.facebook.com  
www.rmit.edu.au

3. Selecting a Hostname
After input, a numbered list of hostnames is displayed.
Enter the index number of the desired hostname to resolve its IP and begin scanning ports 50–499.

Example:

Available Hostnames:  
0: www.google.com  
1: www.facebook.com  
2: www.rmit.edu.au  

Enter the number of the host to scan: 1  
IPv4 address for host www.facebook.com is 157.240.8.35  

Port 80: OPEN  
Port 443: OPEN  

Scan completed.  
Time taken: 227.57 seconds

##Terminating the Script:

- Press Enter on an empty line during index selection to exit.
- The script also exits automatically after displaying the IP address or if any error is encountered.

