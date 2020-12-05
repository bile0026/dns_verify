#!/usr/bin/python3

import dns
import dns.resolver as resolver
import dns.query as query
import csv

dns_server = "8.8.8.8"
resolver.override_system_resolver(resolver=dns_server)

filename = "dns.csv"
report_filename = "report.csv"

with open(filename, 'r') as records:
    # prep csv stuff
    with open(report_filename, 'w') as report:
        csvwriter = csv.writer(report)
        fields = ['Record', 'Assumed Address',
                  'Response Address' 'Type', 'Result']
        csvwriter.writerow(fields)

        for record in csv.reader(records):
            # print(record)
            try:
                answers = resolver.resolve(
                    qname=record[0], rdtype=record[2], search=dns_server)
                for rdata in answers:
                    if (record[1] == rdata.address):
                        print('Host', record[0], 'Address',
                              rdata.address, 'matches!')
                        row = [record[0], record[1], rdata.address,
                               record[2], 'Record Matches']
                        csvwriter.writerow(row)
                    else:
                        print('Host', record[0], 'Address',
                              rdata.address, 'DOES NOT MATCH!')
                        row = [record[0], record[1], rdata.address,
                               record[2], 'Record Does Not Match']
                        csvwriter.writerow(row)
            except dns.resolver.NoAnswer as e:
                print(e)
                row = [e]
                csvwriter.writerow(row)
