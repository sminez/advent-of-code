#!/usr/bin/env zsh
# NOTE: The $1=$1 in pass_per_line rebuilds the current record using OFS
#
# NOTE: For the eye color check, see this SO answer on checking zsh arrays:
#   https://unix.stackexchange.com/questions/411304/how-do-i-check-whether-a-zsh-array-contains-a-given-value

FNAME="../inputs/04.txt"
FIELDS=("byr" "ecl" "eyr" "hcl" "hgt" "iyr" "pid")
EYE_COLORS=("amb" "blu" "brn" "gry" "grn" "hzl" "oth")
typeset -AH passport

function passport_kv { tr ':' ' ' }
function passport_keys { sed 's/:[a-zA-Z0-9#]*//g' }
function pass_per_line { awk 'BEGIN { RS="\n\n" }; { $1=$1; print }' $FNAME }
function in_range { (( $1 >= $2 )) && (( $1 <= $3 )) && echo $1 }

function valid_height {
  local height=$1
  len=${#height}
  val=$height[1,(( len -2 ))]
  units=$height[(( len - 1)),$len]

  case $units in
    "cm") [[ -n $(in_range $val 150 193) ]] && echo $1;;
    "in") [[ -n $(in_range $val 59 76) ]] && echo $1;;
  esac
}

function has_required {
  keys=$(echo $1 | passport_keys | tr ' ' '\n')
  found=($(sort <(echo $FIELDS | tr ' ' '\n') <(echo $keys) | uniq -d))
  [[ $found == $FIELDS ]] && echo $1
}

function has_valid {
  passport=($(echo $1 | passport_kv))

  (( ${EYE_COLORS[(Ie)${passport[ecl]}]} )) || return
  [[ ${#passport[pid]} == 9 ]] || return
  [[ $passport[pid] =~ "^[0-9]+$" ]] || return
  [[ $passport[hcl] =~ "^#[a-fA-F0-9]{6}$" ]] || return
  [[ -n $(in_range $passport[byr] 1920 2002) ]] || return
  [[ -n $(in_range $passport[iyr] 2010 2020) ]] || return
  [[ -n $(in_range $passport[eyr] 2020 2030) ]] || return
  [[ -n $(valid_height $passport[hgt]) ]] || return

  echo $1
}

# part 1
WITH_REQUIRED=$(
  pass_per_line | while read -r line; do
    has_required $line
  done
)
echo $WITH_REQUIRED | wc -l

# part2
echo $WITH_REQUIRED | while read -r line; do
  has_valid $line
done | wc -l
