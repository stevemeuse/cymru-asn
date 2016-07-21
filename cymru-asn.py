#!/usr/bin/env python

import cgi, cgitb, sys, socket, dns.resolver

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

try:
        # These two basically grab all the headers from the POST. 
        # Slack puts anything after /slash as the "text" field
        form = cgi.FieldStorage()
        text = form.getvalue("text")
	#
	#  Now submit the query to Cymru and print the results.
	dnshost = "as%s.asn.cymru.com" % text
	answers = dns.resolver.query(dnshost, 'TXT') 
	for rdata in answers:
		str1 = rdata.to_text()
		print str1.strip('"')


#	for rdata in answers:
#	print rdata

except:

        # If Cymru doesn't return anything, send the error message to the user
        error =  "No data found  (%s)\n" % text
	print error


