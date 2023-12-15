#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import subprocess
import requests
import json

def get_nameservers(domain):
    result = subprocess.run(["dig", "NS", domain, "+short"], capture_output=True, text=True)
    return result.stdout.strip().split("\n")

def query_whoisxmlapi(nameservers, api_key):
    url = "https://reverse-whois.whoisxmlapi.com/api/v2"
    data = {
        "apiKey": api_key,
        "searchType": "current",
        "mode": "purchase",
        "advancedSearchTerms": [
            {"field": "NameServers", "term": nameservers[0]},
            {"field": "NameServers", "term": nameservers[1]}
        ]
    }
    response = requests.post(url, json=data)
    return response.json()

def filter_domains(domains, keyword):
    filtered = [domain for domain in domains if keyword in domain]
    return filtered

def main(domain, api_key):
    base_keyword = domain.split('.')[0]
    nameservers = get_nameservers(domain)
    if len(nameservers) < 2:
        print("Unable to find nameservers.")
        return

    whois_data = query_whoisxmlapi(nameservers, api_key)
    domains = whois_data.get("domainsList", [])
    filtered_domains = filter_domains(domains, base_keyword)

    print("Filtered Domains:")
    for d in filtered_domains:
        print(d)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Domain Lookup Tool")
    parser.add_argument("-d", "--domain", required=True, help="Domain to look up")
    parser.add_argument("-k", "--api_key", required=True, help="WhoisXMLAPI key")
    args = parser.parse_args()

    main(args.domain, args.api_key)

