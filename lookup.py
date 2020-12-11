import csv
from os import error
import re
import socket
from datetime import datetime

filename = "hosts.csv"
cur_date = datetime.now().strftime("%m-%d-%Y")
cur_time = datetime.now().strftime("%H-%M")
report_filename = "reports/report_" + cur_date + "_" + cur_time + ".csv"

regexIP = '^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'


def validateIP(strIP):
    if(re.search(regexIP, strIP)):
        return True
    else:
        return False


with open(filename, 'r') as records:
    # prep csv stuff
    with open(report_filename, 'w') as report:
        csvwriter = csv.writer(report)
        fields = ['Record', 'Result']
        csvwriter.writerow(fields)

        for record in csv.reader(records):
            try:
                if (validateIP(record[0])):
                    print(record[0], "is a valid IP")
                    result = socket.gethostbyaddr(record[0])
                    if (validateIP(result[0])):
                        row = [record[0], "No hostname found"]
                        csvwriter.writerow(row)
                    else:
                        row = [record[0], result[0]]
                        csvwriter.writerow(row)
                else:
                    print(record[0], "is NOT a valid IP")
                    result = socket.gethostbyname(record[0])
                    row = [record[0], result]
                    csvwriter.writerow(row)

            except socket.herror as e:
                row = [record[0], e]
                csvwriter.writerow(row)
            except TypeError as e:
                row = [record[0], e]
                csvwriter.writerow(row)
            except:
                row = [record[0], error]
                csvwriter.writerow(row)
