#!/bin/bash

# Disable several commands by creating dummy functions
function cat() {
  echo "The 'cat' command is disabled."
}
function less() {
  echo "The 'less' command is disabled."
}
function more() {
  echo "The 'more' command is disabled."
}
function head() {
  echo "The 'head' command is disabled."
}
function tail() {
  echo "The 'tail' command is disabled."
}
function grep() {
  echo "The 'grep' command is disabled."
}
function awk() {
  echo "The 'awk' command is disabled."
}
function sed() {
  echo "The 'sed' command is disabled."
}


# Set a secure PATH
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin


# ... (the rest of your command overrides)# Prevent changes to functions
readonly -f $(compgen -A function)

# Disable history file to prevent storing commands
unset HISTFILE

# Keep the shell interactive and trap the exit command to prevent exiting the shell
trap '' EXIT

# Make sure to clear aliases just in case
unalias -a

# Start the shell in restricted mode
set -r

# Display a message or shell prompt
echo "Restricted shell. Some commands have been disabled."
PS1='restricted $ '

# Keep the script running and handle commands
while true; do
  read -p "$PS1" -r CMD
  eval "$CMD"
done



# Call restricted bash
exec /bin/bash --norc --noprofile
