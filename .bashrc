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
alias errout="cat _2017_cr_nojoin_no_golay_parallel.*"
alias rmout="rm _2017_cr_nojoin_no_golay_parallel.*"
export TMPDIR=~/qiime_tmp/
