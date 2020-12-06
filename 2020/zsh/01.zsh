#!/usr/bin/env zsh
FNAME="../inputs/01.txt"

function product { awk 'BEGIN { T=1 }; { T*=$1 }; END { print T }' }

function matchingCompliment {
  cat $FNAME | while read n; do
    echo "$n\n$(( $1 - n ))"
  done | sort | uniq -d
}

# part 1
matchingCompliment 2020 | product

# part2
cat $FNAME | while read n; do
  res=$(matchingCompliment $(( 2020 - n )))
  [[ -n $res ]] && echo "$n\n$res" | product && return
done
