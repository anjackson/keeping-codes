import json
from pprint import pprint

def to_a_map(html):
    num_years = len(html)/2
    by_year = {}
    for i in range(0,22):
        by_year[html[i*2]] = html[i*2+1]
    return by_year



with open('2014-06-30-JISC4-Analysis/select-all-facet-crawl-year.json') as data_file:    
    data = json.load(data_file)
html = to_a_map(data['facet_counts']['facet_fields']['crawl_year'])

with open('2014-06-30-JISC4-Analysis/select-octet-stream-faceted-years-and-extensions.json') as data_file:    
    data = json.load(data_file)
unknown = to_a_map(data['facet_counts']['facet_fields']['crawl_year'])

for y in sorted(html.keys()):
    if html[y] > 0:
        print('\t'.join((y, str(html[y]), str(unknown[y]), str(100.0*unknown[y]/html[y]))))
