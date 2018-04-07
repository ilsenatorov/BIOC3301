# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
module load miniconda/python2
source activate qiime1
export TMPDIR=~/qiime_tmp/
alias la="ls -lha"
alias st="qstat -u ilsenato"

