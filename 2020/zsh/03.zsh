#!/usr/bin/env zsh
FNAME="../inputs/03.txt"

function check_slope {
  local dx=$1 dy=$2 hits=0

  grid=($(cat $FNAME))
  w=${#grid[1]}
  h=${#grid[@]}

  for step in $(seq 0 $h); do
    x=$(( step * dx ))
    y=$(( step * dy ))
    row=$grid[(( y % h + 1 ))]
    char=$row[(( x % w + 1 ))]

    [[ $char == '#' ]] && (( hits += 1 ));
    (( y >= h )) && break;
  done
  echo $hits
}


# part 1
check_slope 3 1

# part2
total=1
slopes=("11" "31" "51" "71" "12")
for s in $slopes; do
  (( total *= $(check_slope $s[1] $s[2]) ))
done
echo $total
