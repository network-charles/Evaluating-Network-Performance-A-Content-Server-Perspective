
import requests #HTTP request library to make API requests
from netaddr import * #module for working with IP address
import re  #regular expression (regex) module to manipulate strings
import pandas as pd

# An empty list to store public IPV4 addresses
public_ipv4_addresses  = []

# Opening the output of the traceroute data saved in .txt
with open('c:/Users/Admin/Documents/Project/file.txt', 'r') as file:
    for line in file:
	
        # A Regex that searches and captures all the IPv4 addresses inside the text file
        #shoutout to https://feralpacket.org/?p=817 for the IPV4 regex below
        ipv4_regex = re.compile(r'''(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}
                        (?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])''', re.VERBOSE)

        ipv4_address = ipv4_regex.search(line)
        
        # Defining a condition to save found IPV4 address to a variable.
        # Then the string IPV4 address found to actual IPV4 address using the Netaddr library.
        # Verify if the IP address is a public IP address and append to the public IPV4 list.
        if ipv4_address:
            ipv4_address = ipv4_address.group(0)            
            ipv4_address = IPAddress(ipv4_address)
            
        # Covert the public IPV4 address back to string format, so it can be added to the API url.
        # Store the API response as text.
        # Creating a file to save the text response of each API call to a JSON file. The 'a' options appends 	   each new response to the response to the end of the file.
        # Write the response for each API call to the JSON file on a new line.

    for idx, ipv4_address in enumerate(public_ipv4_addresses):
        #coverting the public IPV4 address back to string format
        ipv4_address = str(ipv4_address)

        ip_geolocation_info = requests.get('http://ipwhois.pro/' + str(ipv4_address) + '?key=API_Key')
        
        #storing the API response as text
        geo_information = ip_geolocation_info.text

        #creating a file to save the text response of each API call to a JSON file. The 'a' options appends the response to the end of the file.
        json_doc = open('c:/Users/Admin/Documents/Project/File.json', 'a')

        #writing the response for each API call to the JSON file on a new line
        json_doc.write(f'{geo_information}\n')

        #closing the file
        json_doc.close()

# Using Pandas to read the JSON file
# Converting the JSON file into an excel sheet
json_doc_to_excel = pd.read_json('c:/Users/Admin/Documents/Project/file.json', lines=True)
json_doc_to_excel.to_excel('c:/Users/Admin/Documents/Project/file.xlsx', sheet_name='ip_geoinformation', index=False)
