#!/usr/bin/env bash

# common
function cdl()
{
    if [ -n "$1" ] ; then
        cd "$1"
        ls
    else
        cd
        ls
    fi
}
alias l='ls -lah'
alias la='ls -lAh'
alias ll='ls -lh'
alias ls='ls --color=tty'
alias lsa='ls -lah'
alias md='mkdir -p'



# podman
alias docker='podman'
alias pm-il='podman images'
alias pm-cl='podman ps -a'
alias pm-ra='podman rm --all'
alias pm-ri='podman rmi'
alias pm-clean='podman container prune && podman volume prune'
alias pm-cdl='podman rmi $(podman images -f "dangling=true" -q)'

# git
alias gs="git status"
alias gpm='git push origin main'
alias ga='git add'
alias gcmsg='git commit -m'
alias gf='git fetch'
alias gd='git diff'
alias glg='git log --graph'