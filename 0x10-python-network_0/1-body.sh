#!/bin/bash
#script that displays the body of the response
curl -s "$1" | awk 'BEGIN{RS="\r\n\r\n"} NR==1{if($0 ~ /HTTP\/1.1 200 OK/){print $0}}'
