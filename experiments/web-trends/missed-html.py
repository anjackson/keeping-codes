import json
from pprint import pprint

def to_a_map(html):
    num_years = len(html)/2
    by_year = {}
    for i in range(0,22):
        by_year[html[i*2]] = html[i*2+1]
    return by_year



with open('2014-06-30-JISC4-Analysis/select-format-tika-html.json') as data_file:    
    data = json.load(data_file)
html = to_a_map(data['facet_counts']['facet_fields']['crawl_year'])

with open('2014-06-30-JISC4-Analysis/select-format-tika-html-droid-missed.json') as data_file:    
    data = json.load(data_file)
htmlDM = to_a_map(data['facet_counts']['facet_fields']['crawl_year'])

with open('2014-06-30-JISC4-Analysis/select-format-tika-xhtml.json') as data_file:    
    data = json.load(data_file)
xhtml = to_a_map(data['facet_counts']['facet_fields']['crawl_year'])

with open('2014-06-30-JISC4-Analysis/select-format-tika-xhtml-droid-missed.json') as data_file:    
    data = json.load(data_file)
xhtmlDM = to_a_map(data['facet_counts']['facet_fields']['crawl_year'])

for y in sorted(html.keys()):
    totgood = html[y] + xhtml[y]
    totmissed = htmlDM[y] + xhtmlDM[y]
    if totgood > 0:
        print('\t'.join((y, str(100.0*htmlDM[y]/totgood), str(100.0*xhtmlDM[y]/totgood), str(100.0*totmissed/totgood))))
