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

with open('2014-06-30-JISC4-Analysis/select-format-tika-xhtml.json') as data_file:    
    data = json.load(data_file)
xhtml = to_a_map(data['facet_counts']['facet_fields']['crawl_year'])

elems = ['applet', 'b', 'basefont', 'blink', 'dir', 'div', 'embed', 'em', 'font', 'form', 'frame', 'frameset', 'i', 'iframe', 'link', 'listing', 'map', 'marquee', 'object', 'script', 'span', 'strong', 'style']

elem = {}
for e in elems:
    with open('2014-06-30-JISC4-Analysis/select-element-'+e+'.json') as data_file:    
        data = json.load(data_file)
    elem[e] = to_a_map(data['facet_counts']['facet_fields']['crawl_year'])

print("year\t"+"\t".join(elems))
for y in sorted(html.keys()):
    tots = []
    for e in elems:
        total = html[y] + xhtml[y]
        if total > 0:
            tots.append(str(100.0*elem[e][y]/total))
        else:
            tots.append("0")
    print(y+"\t"+"\t".join(tots))
