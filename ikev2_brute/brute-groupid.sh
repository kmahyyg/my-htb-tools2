#!/bin/bash

# Try fakeID
sudo ike-scan -P -M -A -n fakeID $1


# Try BF

while read line; do (echo "Found ID: $line" && sudo ike-scan -M -A -n $line $1) | grep -B14 "1 returned handshake" | grep "Found ID:"; done < vpnIDs.txt
