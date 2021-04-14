# flake8: noqa
import sys

if sys.version_info[0] >= 3:
    from sparse_dot_topn.awesome_cossim_topn import awesome_cossim_topn, awesome_cossim_true_minmax_topn_only
else:
    from awesome_cossim_topn import awesome_cossim_topn, awesome_cossim_true_minmax_topn_only