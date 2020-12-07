#!/usr/bin/env zsh
# This is a little helper library of data and functions that help with general
# shell scripting and providing a consistent TUI.
#
# NOTE: Some useful docs / resources for reference
#   built-ins  -- http://zsh.sourceforge.net/Doc/Release/Shell-Builtin-Commands.html#Shell-Builtin-Commands
#   redirects  -- http://zsh.sourceforge.net/Doc/Release/Redirection.html#Redirection
#   arithmetic -- http://zsh.sourceforge.net/Doc/Release/Arithmetic-Evaluation.html#Arithmetic-Evaluation
#   expansion  -- http://zsh.sourceforge.net/Doc/Release/Expansion.html#Expansion

typeset -AH C
C=(
  red    '\033[1;31m' green '\033[1;32m' yellow  '\033[1;33m' blue '\033[1;34m'
  purple '\033[1;35m' cyan  '\033[1;36m' white   '\033[1;37m' nc   '\033[0m'
)
C_HEADING="$C[purple]"
C_WARN="$C[yellow]"
C_ERR="$C[red]"

# Arithmetic reducers
function sum { awk '{ T+=$1 }; END { print T }' }
function product { awk 'BEGIN { T=1 }; { T*=$1 }; END { print T }' }

# utility
function mapstdin {
  local func=$1 line
  while read line; do
    $func $line
  done
}

# Formatting
function cecho { echo -e "$C[$1]$2$C[nc]" }
function warn { echo -e "${C_WARN}::$C[nc] $*" }
function heading { echo -e "${C_HEADING}:: $C[white]$1$C[nc]" }
function warn_and_exit { echo -e "${C_WARN}::$C[nc] $*" && exit 0 }
function error_and_exit { echo -e "${C_ERR}error:$C[nc] $*" && exit 1 }

# strip surrounding whitespace without messing up quotes like xargs does
alias trim="sed 's/^[[:space:]]*//; s/[[:space:]]*$//'"

# Misc
function continue_or_exit {
  local confirm prompt=${1:-"continue?"}
  echo; heading "$prompt [Y/n]"
  read -q confirm; echo # read -q doesn't drop to the next line
  [ "$confirm" = "y" ] || exit 0
}

function require_external {
  for prog in $*; do
    if ! [ -x "$(command -v $prog)" ]; then
      error_and_exit "'$prog' is required for zayoure to run"
    fi
  done
}

function require_dirs {
  for d in $*; do
    [ -d "$d" ] || error_and_exit "$d is a required directory"
  done
}

function require_env_vars {
  for v in $*; do
    if ! [[ -v "$v" ]]; then
      error_and_exit "$v is a required env var: please set it"
    fi
  done
}

function poll_long_running {
  local tick i pid=$1 message=$2 ticks=(".  " ".. " "..." "   ")

  while [ "$(ps a | awk "!/awk/ && /$pid/")" ]; do
    ((i++))
    tick=$ticks[$((i % 4))]
    sleep 0.2
    echo -ne "${C_HEADING}:: $C[white]$message $tick$C[nc]" "\r"
  done
  echo -n "$(echo "$message" | sed 's/./ /')             " "\r"
  wait "$pid" >/dev/null 2>&1 && cecho green "done     " || cecho red "failed     "
}

function txt_from_editor {
  local default_body=$1

  fname=$(mktemp) || exit 1
  echo "$default_body" >$fname
  $EDITOR $fname </dev/tty >/dev/tty  # make sure that we have a TTY to work with for the editor
  cat $fname
  rm $fname
}
