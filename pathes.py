from enum import Enum


class Path(Enum):
    path_w2v = 'w2v'  # win 5
    path_w2v_seg = 'w2v-sig'  # win 10
    path_FT = 'fastText'  # win 5
    path_FT_final = 'fastText-final'  # doesnt work
    path_FT_seg = 'fastText-sig'  # win 10
    path_w2v_nn_win3 = 'w2v-nn-win3'  # win 3
    path_w2v_nn_win5 = 'w2v-nn-win5'  # win 5
    path_w2v_nn_win10 = 'w2v-nn-win10'  # win 10
    path_w2v_nn_win5_neg10 = 'w2v-nn-win5-neg10'  # win 10
    path_w2v_multi_pos = 'w2v-multi-pos'
    path_FT_nn = 'fastText-nn'
    path_FT_multi_pos = 'fastText-multi-pos'
    path_FT_nn_filtered = 'fastText-nn-filtered'
    path_w2v_nn_filtered = 'w2v-nn-filtered'
    path_odeds_algo_200 = 'odeds-algo-200dim'
    path_odeds_algo = 'odeds-algo'
    path_w2v_nn_pos_10 = "w2v-nn-pos-10"
    path_w2v_nn_pos_100 = "w2v-nn-pos-100"
    path_w2v_nn_pos_200 = "w2v-nn-pos-200"
    path_w2v_twitter = 'twitter-w2v'
    path_w2v_neg_20 = 'w2v-nn-pos-neg-20'
    path_w2v_neg_20_min_20 = 'w2v-nn-pos-neg-20-min-20'
