#!/bin/bash
while read line; do (echo "Valid trans found: $line" && sudo ike-scan -M $line $1) | grep -B14 "1 returned handshake" | grep "Valid trans found" ; done < ike-dict.txt
