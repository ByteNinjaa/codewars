#https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):
    if "https://" in url:
        url = url.replace("https://", "")
    if "http://" in url:
        url = url.replace("http://", "")
    if "www" in url:
        url = url.replace("www", "")

    url = url.split(".")
    
    if url[0] == "":
        return url[1]
    else:
        return url[0]
