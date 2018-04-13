# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

### Necessary on login

module load miniconda/python2
export TMPDIR=~/qiime_tmp
source activate qiime1

### Aliases

alias la="ls -lha"
alias st="qstat -u ilsenato"

### Env

export SOURCETRACKER_PATH='/lustre/home/d411/ilsenato/sourcetracker'
PATH=$PATH:~/ChimeraSlayer
