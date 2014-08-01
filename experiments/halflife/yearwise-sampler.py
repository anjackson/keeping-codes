import urllib

urlo=urllib.URLopener()

q = "http://chrome.bl.uk:8080/solr/select/?q=*:*&rows=100&sort=random_42 desc&wt=json&indent=true&fq=timestamp:[%s-01-01T00:00:00Z TO %s-01-01T00:00:00Z%%2B1YEAR]"

for y in range(2004,2015):
	url = q % (y,y)
	print(url)
	output = "random-sample-for-%s.json" % y
	urlo.retrieve(url , output)