#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
#PS1='[\u@\h \W]\$ '

#PS1="\[\033[0;37m\]\342\224\214\342\224\200\$([[ \$? != 0 ]] && echo \"[\[\033[0;31m\]\342\234\227\[\033[0;37m\]]\342\224\200\")[$(if [[ ${EUID} == 0 ]]; then echo '\[\033[0;31m\]\h'; else echo '\[\033[0;33m\]\u\[\033[0;37m\]@\[\033[0;96m\]\h'; fi)\[\033[0;37m\]]\342\224\200[\[\033[0;32m\]\w\[\033[0;37m\]]\n\[\033[0;37m\]\342\224\224\342\224\200\342\224\200\342\225\274 \[\033[0m\]"

RED="\[\033[0;31m\]"
YELLOW="\[\033[1;33m\]"
LIGHT_GREEN="\[\033[1;32m\]"
NO_COLOR="\[\033[0m\]"
LIGHT_GRAY="\[\033[0;37m\]"
WHITE="\[\033[1;37m\]"
Current_Directory="\w"

PS1="$WHITE\342\224\214\342\224\200\$([[ \$? != 0 ]] && echo \"[$RED]\342\234\227\[\033[0;31m\]]\342\224\200\")[$(if [[ ${EUID} == 0 ]]; then echo '\[\033[0;31m\]\h'; else echo '\[\033[1;33m\]\u\[\033[1;37m\]@\[\033[0;34m\]\h'; fi)$WHITE]\342\224\200[$LIGHT_GREEN $Current_Directory $WHITE]\n$WHITE\342\224\224\342\224\200\342\224\200\342\225\274 $RED"



if [ -f /etc/bash_completion ]; then
    /etc/bash_completion
fi

