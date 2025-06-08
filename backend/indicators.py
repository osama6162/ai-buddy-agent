import re

def extract_indicators(email_data):
    body = email_data.get("body", "")

    urls = re.findall(r'https?://[^\s]+', body)
    domains = list(set(re.findall(r'[\w\.-]+\.(?:com|net|org|info|gov|edu)', body)))
    ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', body)

    return {
        "urls": urls,
        "domains": domains,
        "ips": ips
    }

