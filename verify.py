import dns.query as query
import dns.resolver as resolver
import csv

filename = "dns.csv"

with open(filename, 'r') as records:
    for record in csv.reader(records):
        # print(record)
        try:
            answers = resolver.resolve(record[0], record[2])
            for rdata in answers:
                print('Host', record[0], 'Address', rdata.address)
        except resolver.NoAnswer as e:
            print(e)
