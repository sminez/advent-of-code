#!/usr/bin/env zsh
FNAME="../inputs/02.txt"

function validCharCount {
  local total=0

  cat $FNAME | tr -d ':' | tr '-' ' ' | while read -r min max char password; do
    count=${#password//[^$char]/}

    if (( min <= count )) && (( count <= max )); then
      (( total += 1 ))
    fi
  done
  echo $total
}

function validCharPositions {
  local total=0

  cat $FNAME | tr -d ':' | tr '-' ' ' | while read -r pos1 pos2 char password; do
    c1=${password[pos1]}
    c2=${password[pos2]}

    [[ $c1 == $char ]] && [[ $c2 != $char ]] && (( total += 1 ))
    [[ $c1 != $char ]] && [[ $c2 == $char ]] && (( total += 1 ))
  done
  echo $total
}


# part 1
validCharCount

# part2
validCharPositions
