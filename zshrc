# Path to your oh-my-zsh configuration.
ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
ZSH_THEME="robbyrussell"

# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

# Set to this to use case-sensitive completion
# CASE_SENSITIVE="true"

# Comment this out to disable weekly auto-update checks
# DISABLE_AUTO_UPDATE="true"

# Change this value to set how frequently ZSH updates¬
export UPDATE_ZSH_DAYS=13

# Uncomment following line if you want to disable colors in ls
# DISABLE_LS_COLORS="true"

# Uncomment following line if you want to disable autosetting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment following line if you want red dots to be displayed while waiting for completion
# COMPLETION_WAITING_DOTS="true"

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
plugins=(git)

source $ZSH/oh-my-zsh.sh
source ~/.setup_environment
# Customize to your needs...
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/home/gtiwari/tomcat-base:/home/gtiwari/src/cbs-tools/bin/:/home/gtiwari/src/cbs-tools/bin/solr:/home/gtiwari/src/cbs-tools/bin/analysis:/home/gtiwari/src/cbs-tools/bin/pickgame:/home/gtiwari/src/cbs-tools/bin/poll:/home/gtiwari/src/cbs-tools/bin/infrastructure:/home/gtiwari/src/cbs-tools/bin/migration:/home/gtiwari/src/cbs-tools/bin/workspace_commands:/home/gtiwari/src/cbs-tools/bin/protobuf:/home/gtiwari/src/cbs-tools/bin/prod_utilities:/home/gtiwari/src/cbs-tools/bin/contest:/home/gtiwari/src/cbs-tools/bin/deploy:/home/gtiwari/src/cbs-tools/bin/cbs-mvc-shows:/home/gtiwari/tomcat-base


function repo_char {
    git branch >/dev/null 2>/dev/null && echo '☿' && return
    echo '○'
}

# Display any virtual env stuff with python.
function virtualenv_info {
    [ $VIRTUAL_ENV ] && echo '('`basename $VIRTUAL_ENV`') '
}

# All of my git variables.
ZSH_THEME_GIT_PROMPT_PREFIX=" on %{$fg[magenta]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[green]%}!"
ZSH_THEME_GIT_PROMPT_UNTRACKED="%{$fg[green]%}?"
ZSH_THEME_GIT_PROMPT_CLEAN=""

# I like a new line between my result and the next prompt.  Makes it easier to see
PROMPT='
%{$fg[magenta]%}%n%{$reset_color%} at %{$fg[yellow]%}%m%{$reset_color%} in %{$fg_bold[green]%}${PWD/#$HOME/~}%{$reset_color%}$(git_prompt_info)
$(virtualenv_info)$(repo_char) '

# Display the date.  (My desktop at work uses $(date -u ...) instead, because I use UTC a lot at work.
RPROMPT='$(date "+%x %T %Z")'

alias -g ll='ls -al'
alias -g ...=../..
alias -g ....=../../..
alias -g .....=../../../..
alias -g ......=../../../../..
alias cd..='cd ..'
alias cd...='cd ../..'
alias cd....='cd ../../..'
alias cd.....='cd ../../../..'
alias ..='cd ..'
alias ../..='cd ../..'
alias ../../..='cd ../../..'
alias ../../../..='cd ../../../..'
alias ../../../../..='cd ../../../../..'

alias cd/='cd /'
alias emacs='emacs -nw'
alias 1='cd -'
alias 2='cd +2'
alias 3='cd +3'
alias 4='cd +4'
alias 5='cd +5'
alias 6='cd +6'
alias 7='cd +7'
alias 8='cd +8'
alias 9='cd +9'

alias l='ls -lah'           # Long view, show hidden
alias la='ls -AF'           # Compact view, show hidden
alias ll='ls -lFh'          # Long view, no hidden

alias grep='grep --color=auto' # Always highlight grep search term
alias ping='ping -c 5'      # Pings with 5 packets, not unlimited
alias df='df -h'            # Disk free, in gigabytes, not bytes
alias du='du -h -c'         # Calculate total disk usage for a folder
alias sgi='sudo gem install' # Install ruby stuff
alias clj='clj-env-dir'        # Clojure helper
alias clr='clear;echo "Currently logged in on $(tty), as $(whoami) in directory $(pwd)."'
alias tt='tt++ $HOME/.ttconf'
alias svim="sudo vim" # Run vim as super user
alias emc="emacsclient -n" # no blocking terminal waiting for edit




extract () {
    if [ -f $1 ] ; then
        case $1 in
            *.tar.bz2)        tar xjf $1        ;;
            *.tar.gz)         tar xzf $1        ;;
            *.bz2)            bunzip2 $1        ;;
            *.rar)            unrar x $1        ;;
            *.gz)             gunzip $1         ;;
            *.tar)            tar xf $1         ;;
            *.tbz2)           tar xjf $1        ;;
            *.tgz)            tar xzf $1        ;;
            *.zip)            unzip $1          ;;
            *.Z)              uncompress $1     ;;
            *)                echo "'$1' cannot be extracted via extract()" ;;
        esac
    else
        echo "'$1' is not a valid file"
    fi
}




function props(){
  sudo cp -v $SVN_PROJECTS/api/conf/localhost/properties.xml $TOMCAT_HOME/lib/properties.xml
  sudo cp -v $SVN_PROJECTS/community-base/conf/context.xml $TOMCAT_BASE/conf/context.xml
}

export SVN_ROOT=~/src/cbs/community-trunk
source /home/gtiwari/src/cbs-tools/source_me.sh


export API_USER=cbsadmin@cbsinteractive.com
export API_PASS=3ETUPafr
export HISTCONTROL=erasedups  # Ignore duplicate entries in history
export HISTFILE=~/.histfile
export HISTSIZE=20000         # Increases size of history
export SAVEHIST=20000
export HISTIGNORE="&:ls:ll:la:l.:pwd:exit:clear:clr:[bf]g"

echo ""
fortune
echo ""

export PERL_LOCAL_LIB_ROOT="$PERL_LOCAL_LIB_ROOT:/home/gtiwari/perl5";
export PERL_MB_OPT="--install_base /home/gtiwari/perl5";
export PERL_MM_OPT="INSTALL_BASE=/home/gtiwari/perl5";
export PERL5LIB="/home/gtiwari/perl5/lib/perl5:$PERL5LIB";
export PATH="/home/gtiwari/perl5/bin:/home/gtiwari/bin:$PATH";
source /home/gtiwari/colour-scheme/base16-shell/base16-eighties.dark.sh
export C1=util3021.drt.cbsig.net
export C2=util3022.drt.cbsig.net
export JAVA_CMD=/usr/lib/jvm/java-6-sun/bin/java
export RECOMMENDATION_ROOT=~/cbs-recommendations
#export API_ROOT=~/src/cbs/api-prod-release