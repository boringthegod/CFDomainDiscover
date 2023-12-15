# CFDomainDiscover

CFDomainDiscover is a command-line tool designed for security researchers and bug hunters. It allows you to discover all domains associated with a specific CloudFlare account. The tool uses a reverse WHOIS search to identify related domains based on CloudFlare's unique server names.


All credit and research for this technique comes from the blog : [dumping all domains from a CloudFlare account](https://celes.in/posts/cloudflare_ns_whois) by [c3l3si4n](https://twitter.com/c3l3si4n) 



## Features

- Automatic retrieval of server names (NS) for a given domain.
- WHOIS reverse lookup using WhoisXMLAPI API.
- Filtering and display of relevant domains.




# Requirements

- [Python 3](https://www.python.org/download/releases/3.0/)

- have `dig` installed 

- have an account (even free/trial) on [whoisxmlapi.com](whoisxmlapi.com) to get an *API key*



## Installation

`git clone https://github.com/boringthegod/CFDomainDiscover.git && cd CFDomainDiscover`


# Usage

To use CFDomainDiscover, run the command line script specifying the target domain name and your WhoisXMLAPI API key:


```bash
usage: cfdomaindiscover.py [-h] -d DOMAIN -k API_KEY

Domain Lookup Tool

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain to look up
  -k API_KEY, --api_key API_KEY
                        WhoisXMLAPI key
                            
Examples:
  ./cfdomaindiscover.py -d discord.com -k YOUR_API_KEY
```


## Demo

![](https://cdn.discordapp.com/attachments/890363963483758644/1185245536668885002/image.png)