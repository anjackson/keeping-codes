import urllib

urlo=urllib.URLopener()

solr_server = "http://192.168.1.181:8983/solr/jisc5"
solr_year_facet_query = solr_server+"/select?q=%s&rows=0&wt=json&indent=true&facet=true&facet.field=crawl_years"

# ALL
#urlo.retrieve( solr_year_facet_query % ("*:*") , "select-all.json")

# Tika v. DROID HTML and XHTML
#urlo.retrieve( solr_year_facet_query % ("content_type_tika:text\\/html*") , "select-format-tika-html.json")
#urlo.retrieve( solr_year_facet_query % ("content_type_droid:\"application/octet-stream\" AND content_type_tika:text\\/html*") , "select-format-tika-html-droid-missed.json")
#urlo.retrieve( solr_year_facet_query % ("content_type_tika:application\\/xhtml*") , "select-format-tika-xhtml.json")
#urlo.retrieve( solr_year_facet_query % ("content_type_droid:\"application/octet-stream\" AND content_type_tika:application\\/xhtml*") , "select-format-tika-xhtml-droid-missed.json")

# Other format cases:
urlo.retrieve( solr_year_facet_query % ("content_type_droid:\"application/octet-stream\"") , "select-format-droid-missed.json")
urlo.retrieve( solr_year_facet_query % ("content_type_tika:\"application/octet-stream\"") , "select-format-tika-missed.json")
urlo.retrieve( solr_year_facet_query % ("content_type_droid:\"application/octet-stream\" AND content_type_tika:\"application/octet-stream\"") , "select-format-tika-and-droid-missed.json")



# elements
#elements = ['script', 'form']
elements = ['applet' ,'b' ,'basefont' ,'blink' ,'dir' ,'div' ,
            'em' ,'embed' ,'emph' ,'font' ,'form' ,'frame' ,'frameset' ,
            'i' ,'iframe' ,'link' ,'listing' ,'map' ,'marquee' ,'object' ,
            'script' ,'span' ,'strong' ,'style']
for element in elements:
    query = "elements_used:\"%s\"" % element
    url = solr_year_facet_query % (query)
    output = "select-element-%s.json" % element
    #urlo.retrieve(url , output)

