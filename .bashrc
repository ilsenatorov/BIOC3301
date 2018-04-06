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
alias errout="cat parallel_benchmarking_3301.*"
alias rmout="rm parallel_benchmarking_3301.*"
export TMPDIR=~/qiime_tmp/
alias la="ls -la"
