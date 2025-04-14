import socket  # For network communication
import time    # For measuring scan duration

# Create an empty list to store hostnames
nameList = []

# Counter for how many hostnames have been entered
count = 0

# Collect hostnames from the user
name = "Project"
while name != '':
    name = input("Please enter an IP address or hostname, or press ENTER to finish: ")

    if name == '' and len(nameList) == 0:
        print("You haven't entered any host names.")
        print("Goodbye")
    elif name != '':
        nameList.append(name)
        count += 1

# If there are valid hostnames, allow user to select one
if len(nameList) > 0:
    host_selection = "Project"
    valid_selection = True

    while valid_selection and host_selection != '':
        # Display the list of hostnames with index
        print("\nAvailable Hostnames:")
        for index in range(count):
            print(f"{index}: {nameList[index]}")

        # User selects one by number
        host_selection = input("Enter the number of the host to scan, or press ENTER to quit: ")

        if host_selection == '':
            print("Goodbye")
            break
        elif "." in host_selection:
            print("Your input is a float. Please enter a whole number.")
            print("Goodbye")
            break
        elif int(host_selection) in list(range(count)):
            try:
                selected_host = nameList[int(host_selection)]
                ip_address = socket.gethostbyname(selected_host)
                print(f"\nIPv4 address for host '{selected_host}' is: {ip_address}")

                # Start scanning the selected host
                print(f"Starting port scan on {ip_address} (ports 50-499)...\n")
                start_time = time.time()

                for port in range(50, 500):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.5)  # Reduce wait time for unresponsive ports
                    result = s.connect_ex((ip_address, port))
                    if result == 0:
                        print(f"Port {port}: OPEN")
                    s.close()

                print("\nScan completed.")
                print("Time taken: %.2f seconds" % (time.time() - start_time))

            except socket.gaierror:
                print(f"Host name '{selected_host}' is not valid.")
                print("Goodbye")
                valid_selection = False
        else:
            print("Invalid selection. Please enter a valid number.")
            print("Goodbye")
            valid_selection = False