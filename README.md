# dns_verify
Takes a list of dns records and reports any variance

`verify.py` takes a csv of DNS records and types. (See dns.csv for example). It will query 1 or more dns servers you place in the `dns_servers` list. It will dump a csv file into the reports folder with the results.

Requires dnspython package
`pip install --user dnspython`
