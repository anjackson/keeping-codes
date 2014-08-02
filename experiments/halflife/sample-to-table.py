import json, sys
from pprint import pprint
from checkurl import checkUrl
import dateutil.parser

def mapStatusToKey( status, reason ):
    if status / 100 == 2:
        if reason.endswith("VIA-REDIRECT+"):
            return "MOVED"
        else:
            return "OK"
    elif status / 100 == 3:
        return "REDIRECT"
    elif status / 100 == 4:
        return "MISSING"
    elif status / 100 == 5:
        return "ERROR"
    elif status / 100 == 9:
        return "GONE"
    else:
        return "UNKNOWN"

file_template = "2014-08-01-Selective-Sample/random-sample-for-%s.json"

for y in range(2004,2015):
    with open( file_template % y ) as data_file:    
        data = json.load(data_file)
    for doc in data['response']['docs']:
        url = doc['wct_url']

        timestamp = dateutil.parser.parse(doc['timestamp'])

        status, reason = checkUrl( url )
        key = mapStatusToKey(status, reason )

        try:
            ascii_reason = reason.encode('ascii','replace')
        except:
            ascii_reason = "UNKNOWN REASON"

        month = timestamp.strftime("%m")
        quarter = 1 + (int(month)-1)/3

        try:
            print( "%s\t%s\t%s\t%s\t%s\t%s\t%s" % ( y, quarter, month, key, status, ascii_reason, url ) )
        except:
            print("ERROR", y, url, key, status, ascii_reason)
            sys.exit(1)
        # FLUSH:
        sys.stdout.flush()

