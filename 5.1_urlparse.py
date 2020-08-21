from urllib.parse import urlparse
url = 'http://taqm.epa.gov.te:80/pm25/ te/PM25A.aspx?area=1'
o = urlparse(url)
print(o)

print("scheme={}".format(o.scheme))  #協議：http
print("netloc={}".format(o.netloc))  #域名服務器：taqm.epa.gov.te:80
print("port={}".format(o.port))  #80
print("path={}".format(o.path))  #相對路徑 /pm25/ te/PM25A.aspx
print("query={}".format(o.query))  #查詢的條件area=1