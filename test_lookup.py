import socket
import re

records = ["8.8.8.8", "1.1.1.1", "google.com"]

regexIP = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''


def validateIP(strIP):
    if(re.search(regexIP, strIP)):
        return True
    else:
        return False


try:
    for record in records:
        if(validateIP(record)):
            print(record, "is a valid IP")
        else:
            print(record, "is not a valid IP")
except:
    print("name not found")
