#!/usr/bin/python3

import dns
import dns.resolver as resolver
import dns.query as query
import csv

dns_server = "192.168.252.5"
resolver.override_system_resolver(resolver=dns_server)

filename = "dns.csv"

with open(filename, 'r') as records:
    for record in csv.reader(records):
        # print(record)
        try:
            answers = resolver.resolve(
                qname=record[0], rdtype=record[2], search=dns_server)
            for rdata in answers:
                print('Host', record[0], 'Address', rdata.address)
        except dns.resolver.NoAnswer as e:
            print(e)
