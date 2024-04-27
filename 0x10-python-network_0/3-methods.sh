#!/bin/bash
#will displays all the http methods in the server
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
