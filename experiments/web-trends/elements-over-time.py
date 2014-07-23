import json
from pprint import pprint

def to_a_map(html):
    num_years = len(html)/2
    by_year = {}
    for i in range(0,22):
        by_year[html[i*2]] = html[i*2+1]
    return by_year

#basedir = '2014-06-30-JISC4-Analysis'
#year_field = 'crawl_year'

basedir = '2014-07-22-JISC5-Analysis'
year_field = 'crawl_years'

with open(basedir+'/select-format-tika-html.json') as data_file:    
    data = json.load(data_file)
html = to_a_map(data['facet_counts']['facet_fields'][year_field])

with open(basedir+'/select-format-tika-xhtml.json') as data_file:    
    data = json.load(data_file)
xhtml = to_a_map(data['facet_counts']['facet_fields'][year_field])

elements = ['applet' ,'b' ,'basefont' ,'blink' ,'dir' ,'div' ,
            'em' ,'embed' ,'emph' ,'font' ,'form' ,'frame' ,'frameset' ,
            'i' ,'iframe' ,'link' ,'listing' ,'map' ,'marquee' ,'object' ,
            'script' ,'span' ,'strong' ,'style']

elem = {}
for e in elements:
    with open(basedir+'/select-element-'+e+'.json') as data_file:    
        data = json.load(data_file)
    elem[e] = to_a_map(data['facet_counts']['facet_fields'][year_field])

print("year\t"+"\t".join(elements))
for y in sorted(html.keys()):
    tots = []
    for e in elements:
        if xhtml.has_key(y):
            total = html[y] + xhtml[y]
        else:
            total = html[y]
        if total > 0 and elem[e].has_key(y):
            tots.append(str(100.0*elem[e][y]/total))
        else:
            tots.append("0")
    print(y+"\t"+"\t".join(tots))
