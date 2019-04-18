#!/usr/bin/python

import requests, sys, os

print """
###########################
# TrD0n - File Downloader #
# Coded By Afrizal F.A    #
# From : ICWR-TECH        #
###########################
"""
url = sys.argv[1]
request = requests.get(sys.argv[1],stream=True)
if request.status_code == int(200):
    print "[+] Downloading : " + url
    byte = request.headers.get("content-length")
    print "[+] Size : " + str(byte)
    nama_file = os.getcwd() + "/download/" + sys.argv[2]
    print "[+] Proccessing : " + sys.argv[2]
    save = open(nama_file, "w")
    write = save.write(request.content)
    if not request.content:
        print "[-] Status : Failed"
        exit()

print "[+] Status : Success "
print "[+] Saved : " + nama_file
save.close()
