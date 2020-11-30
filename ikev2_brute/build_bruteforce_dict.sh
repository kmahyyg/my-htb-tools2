#!/bin/bash
for ENC in 1 2 3 4 5 6 7/128 7/192 7/256 8; do for HASH in 1 2 3 4 5 6; do for AUTH in 1 2 3 4 5 6 7 8 64221 64222 64223 64224 65001 65002 65003 65004 65005 65006 65007 65008 65009 65010; do for GROUP in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18; do echo "--trans=$ENC,$HASH,$AUTH,$GROUP" >> ike-dict.txt ;done ;done ;done ;done

