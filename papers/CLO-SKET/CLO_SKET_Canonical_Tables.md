# CLO-SKET — Canonical Results Tables


## Table 1 — Exact grouped-fold audit

| fold | train_rows | test_rows | train_identities | test_identities | overlapping_identities | test_categories | test_identities_per_category_min | test_identities_per_category_max | test_images_per_category_min | test_images_per_category_max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1839 | 461 | 184 | 46 | 0 | 23 | 2 | 2 | 20 | 21 |
| 2 | 1840 | 460 | 184 | 46 | 0 | 23 | 2 | 2 | 20 | 20 |
| 3 | 1841 | 459 | 184 | 46 | 0 | 23 | 2 | 2 | 19 | 20 |
| 4 | 1840 | 460 | 184 | 46 | 0 | 23 | 2 | 2 | 19 | 21 |
| 5 | 1840 | 460 | 184 | 46 | 0 | 23 | 2 | 2 | 20 | 20 |



## Table 2 — Classification results

| split_design | representation | accuracy | balanced_accuracy | macro_f1 |
| --- | --- | --- | --- | --- |
| Original StratifiedKFold | Morphology | 0.342174 | 0.342174 | 0.342322 |
| Original StratifiedKFold | Morphology + RA | 0.415652 | 0.415652 | 0.414257 |
| Unseen garment identity | Morphology | 0.307826 | 0.307826 | 0.306847 |
| Unseen garment identity | Morphology + RA | 0.342174 | 0.342174 | 0.341445 |



## Table 3 — Primary grouped fold effects

| split_design | fold | morphology_macro_f1 | combined_macro_f1 | delta_macro_f1 | morphology_balanced_accuracy | combined_balanced_accuracy | delta_balanced_accuracy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Original StratifiedKFold | 1 | 0.328726 | 0.417483 | 0.088757 | 0.326087 | 0.419565 | 0.093478 |
| Original StratifiedKFold | 2 | 0.343118 | 0.425692 | 0.082574 | 0.343478 | 0.428261 | 0.084783 |
| Original StratifiedKFold | 3 | 0.360832 | 0.403813 | 0.04298 | 0.363043 | 0.408696 | 0.045652 |
| Original StratifiedKFold | 4 | 0.324048 | 0.35617 | 0.032122 | 0.323913 | 0.358696 | 0.034783 |
| Original StratifiedKFold | 5 | 0.34893 | 0.458502 | 0.109572 | 0.354348 | 0.463043 | 0.108696 |



## Table 4 — Identity-aware integration intervals

| metric | observed_delta | bootstrap_mean | bootstrap_median | ci_2.5_percent | ci_97.5_percent | fraction_delta_le_zero | bootstrap_replicates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Macro-F1 | 0.034598 | 0.034582 | 0.034395 | 0.015783 | 0.053962 | 0.0004 | 5000 |
| Balanced accuracy | 0.034348 | 0.034458 | 0.034348 | 0.015612 | 0.054268 | 0.0004 | 5000 |



## Table 5 — Within-category alignment control

| metric | morphology_only | aligned_combined | observed_gain_vs_morphology | permuted_mean | permuted_median | permuted_2.5_percent | permuted_97.5_percent | aligned_minus_permuted_mean | empirical_alignment_p | permutations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Macro-F1 | 0.306847 | 0.341445 | 0.034598 | 0.335293 | 0.335451 | 0.324199 | 0.345944 | 0.006153 | 0.141929 | 2000 |
| Balanced accuracy | 0.307826 | 0.342174 | 0.034348 | 0.335332 | 0.335652 | 0.323913 | 0.346087 | 0.006842 | 0.122939 | 2000 |



## Table 6 — Repeated grouped partitions

| repeat | seed | morphology_pooled_macro_f1 | combined_pooled_macro_f1 | pooled_delta_macro_f1 | morphology_pooled_ba | combined_pooled_ba | pooled_delta_ba | mean_fold_delta_macro_f1 | mean_fold_delta_ba | positive_macro_f1_folds | positive_ba_folds | convergence_warnings |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 20260820 | 0.306847 | 0.341445 | 0.034598 | 0.307826 | 0.342174 | 0.034348 | 0.031263 | 0.034451 | 5 | 5 | 0 |
| 2 | 20260821 | 0.31391 | 0.347484 | 0.033574 | 0.315217 | 0.346522 | 0.031304 | 0.029268 | 0.031346 | 5 | 5 | 0 |
| 3 | 20260822 | 0.308628 | 0.344077 | 0.035449 | 0.309565 | 0.342609 | 0.033043 | 0.033188 | 0.033108 | 4 | 4 | 0 |
| 4 | 20260823 | 0.298983 | 0.351735 | 0.052752 | 0.300435 | 0.351304 | 0.05087 | 0.050252 | 0.050901 | 5 | 5 | 0 |
| 5 | 20260824 | 0.299648 | 0.343379 | 0.043731 | 0.302609 | 0.343043 | 0.040435 | 0.04352 | 0.040458 | 5 | 5 | 0 |
| 6 | 20260825 | 0.307112 | 0.347248 | 0.040136 | 0.308261 | 0.347826 | 0.039565 | 0.042196 | 0.039843 | 5 | 5 | 0 |
| 7 | 20260826 | 0.305941 | 0.352957 | 0.047016 | 0.306957 | 0.352174 | 0.045217 | 0.045657 | 0.04529 | 5 | 5 | 0 |
| 8 | 20260827 | 0.299075 | 0.351956 | 0.052882 | 0.29913 | 0.35087 | 0.051739 | 0.052348 | 0.051791 | 5 | 5 | 0 |
| 9 | 20260828 | 0.317837 | 0.361226 | 0.04339 | 0.31913 | 0.362174 | 0.043043 | 0.042899 | 0.043154 | 5 | 5 | 0 |
| 10 | 20260829 | 0.304125 | 0.343642 | 0.039517 | 0.305652 | 0.342174 | 0.036522 | 0.036808 | 0.036673 | 5 | 5 | 0 |



## Table 7 — Grouped radial–angular recovery intervals

| target | observed_r2 | r2_ci_low | r2_ci_high | r2_fraction_le_zero | observed_spearman | spearman_ci_low | spearman_ci_high | spearman_fraction_le_zero | observed_mae | mae_ci_low | mae_ci_high | observed_rmse | rmse_ci_low | rmse_ci_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F2_peak_magnitude | 0.302221 | 0.266905 | 0.33387 | 0.0 | 0.631055 | 0.602427 | 0.658446 | 0.0 | 0.013196 | 0.012721 | 0.013686 | 0.017027 | 0.016362 | 0.017707 |
| F2_peak_radius | 0.014269 | -0.042301 | 0.066573 | 0.2974 | 0.324874 | 0.28408 | 0.366127 | 0.0 | 4.080491 | 3.939184 | 4.2164 | 5.128389 | 4.940123 | 5.304208 |
| R2_at_F2_peak | 0.190971 | 0.121399 | 0.253892 | 0.0 | 0.521587 | 0.479772 | 0.563474 | 0.0 | 0.127284 | 0.122482 | 0.132113 | 0.162518 | 0.155809 | 0.16939 |
| axial_error | 0.206346 | 0.148195 | 0.260074 | 0.0 | 0.442901 | 0.396301 | 0.488413 | 0.0 | 20.041103 | 19.303544 | 20.79766 | 26.323096 | 25.389361 | 27.251001 |



## Supplementary Table S1 — Category-level effects

| category | support | morphology_f1 | ra_only_f1 | combined_f1 | combined_minus_morphology | combined_minus_ra |
| --- | --- | --- | --- | --- | --- | --- |
| Sarong | 100 | 0.2755 | 0.3755 | 0.3923 | 0.1168 | 0.0169 |
| Suit | 100 | 0.2128 | 0.3415 | 0.3269 | 0.1142 | -0.0145 |
| Blouse | 100 | 0.5027 | 0.3368 | 0.5949 | 0.0922 | 0.258 |
| Vest | 100 | 0.3033 | 0.3282 | 0.3838 | 0.0805 | 0.0556 |
| Skinny | 100 | 0.1111 | 0.1914 | 0.191 | 0.0798 | -0.0004 |
| Mini | 100 | 0.2451 | 0.3092 | 0.3085 | 0.0634 | -0.0007 |
| Circle | 100 | 0.3707 | 0.2632 | 0.419 | 0.0483 | 0.1559 |
| Jumpsuit | 100 | 0.3861 | 0.347 | 0.4299 | 0.0438 | 0.0829 |
| Cardigan | 100 | 0.1415 | 0.113 | 0.1759 | 0.0344 | 0.0629 |
| T-shirt | 100 | 0.4909 | 0.5094 | 0.5171 | 0.0262 | 0.0076 |
| Straight | 100 | 0.2938 | 0.2743 | 0.3178 | 0.0239 | 0.0434 |
| Hoodie | 100 | 0.2512 | 0.2132 | 0.2745 | 0.0233 | 0.0613 |
| A-Line | 100 | 0.4731 | 0.33 | 0.4948 | 0.0217 | 0.1648 |
| Jacket | 100 | 0.1991 | 0.2011 | 0.2176 | 0.0186 | 0.0165 |
| Mermaid | 100 | 0.3053 | 0.0915 | 0.3209 | 0.0156 | 0.2294 |
| Flare | 100 | 0.4059 | 0.2376 | 0.4138 | 0.0079 | 0.1762 |
| Harem | 100 | 0.1326 | 0.0578 | 0.14 | 0.0074 | 0.0822 |
| Wide-Leg | 100 | 0.5479 | 0.4055 | 0.5534 | 0.0055 | 0.1479 |
| Bermuda | 100 | 0.6316 | 0.4811 | 0.6316 | 0.0 | 0.1504 |
| Shirt | 100 | 0.2077 | 0.2793 | 0.2073 | -0.0004 | -0.072 |
| Dress | 100 | 0.2245 | 0.2198 | 0.2211 | -0.0034 | 0.0013 |
| Tunic | 100 | 0.1872 | 0.0694 | 0.1791 | -0.0081 | 0.1097 |
| Pencil | 100 | 0.1579 | 0.1266 | 0.1421 | -0.0158 | 0.0155 |



## Supplementary Table S2 — Direct axial-orientation effects

| metric | observed_effect | bootstrap_mean | ci_2.5_percent | ci_97.5_percent | fraction_le_zero | positive_ci | negative_ci | bootstrap_replicates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean_error_reduction_deg | 1.447897 | 1.459367 | 0.425764 | 2.525118 | 0.0024 | True | False | 5000 |
| median_error_reduction_deg | -1.348916 | -1.332023 | -1.811536 | -0.88967 | 1.0 | False | True | 5000 |
| r2_weighted_mean_error_reduction_deg | 1.024246 | 1.039112 | -0.113484 | 2.231822 | 0.0394 | False | False | 5000 |
| within_10_increase | -0.051304 | -0.051155 | -0.069285 | -0.033101 | 1.0 | False | True | 5000 |
| within_15_increase | -0.014348 | -0.014196 | -0.030435 | 0.002606 | 0.9572 | False | False | 5000 |
| within_30_increase | 0.017826 | 0.017964 | 0.004778 | 0.031767 | 0.0046 | True | False | 5000 |
| axial_agreement_increase | 0.048157 | 0.048449 | 0.023101 | 0.075019 | 0.0 | True | False | 5000 |

