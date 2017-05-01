def parse_email(email):
    result = re.match('(?P<username>[\w\-]+).(?P<domain>[\w\.\-]+)', email).groups()
    return result
