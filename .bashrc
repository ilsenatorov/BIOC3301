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

export PATH=$PATH:~/microbiomeutils/ChimeraSlayer
