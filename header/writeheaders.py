def header():
    headers = {}
    with open('header/headers.txt', 'r+') as f:
        lst = [item.strip() for item in f.readlines()]
        for item in lst:
            item = item.split(':')
            key, val = item[0], item[1].strip()
            headers[key] = val
    return headers