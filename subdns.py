import requests


def dnsfuzz(dns)
    file = open("subdomains.txt")
    content = file.read()
    subdomains = content.splitlines()
    discovered_subdomains = []
    for subdomain in subdomains:
        url = f"http://{subdomain}.{dns}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("[+] Discovered subdomain:", url)
            

