#!/usr/bin/python3

import dns
import dns.resolver as resolver
import dns.query as query
import csv

filename = "dns.csv"

dns_servers = ["8.8.8.8", "1.1.1.1"]

for dns_server in dns_servers:
    resolver.override_system_resolver(resolver=dns_server)

    report_filename = "report_" + dns_server + ".csv"

    with open(filename, 'r') as records:
        # prep csv stuff
        with open(report_filename, 'w') as report:
            csvwriter = csv.writer(report)
            fields = ['Record', 'Assumed Address',
                      'Response Address', 'Type', 'DNS Server', 'Result']
            csvwriter.writerow(fields)

            for record in csv.reader(records):
                # print(record)
                try:
                    answers = resolver.resolve(
                        qname=record[0], rdtype=record[2], search=dns_server)
                    for rdata in answers:
                        if (record[1] == rdata.address):
                            print('Response from', dns_server, 'Host', record[0], 'Address',
                                  rdata.address, 'matches!')
                            row = [record[0], record[1], rdata.address,
                                   record[2], dns_server, 'Record Matches']
                            csvwriter.writerow(row)
                        else:
                            print('Response from', dns_server, 'Host', record[0], 'Address',
                                  rdata.address, 'DOES NOT MATCH!')
                            row = [record[0], record[1], rdata.address,
                                   record[2], dns_server, 'Record Does Not Match']
                            csvwriter.writerow(row)
                except dns.resolver.NoAnswer as e:
                    print(e)
                    row = [record[0], record[1], ' ', record[2], dns_server, e]
                    csvwriter.writerow(row)
