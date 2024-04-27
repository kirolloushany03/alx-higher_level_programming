#!/bin/bash
# will send delete request for to the url
curl -X DELETE "$1" -s | awk 'BEGIN{RS="\r\n\r\n"} NR==1{print $0}'
