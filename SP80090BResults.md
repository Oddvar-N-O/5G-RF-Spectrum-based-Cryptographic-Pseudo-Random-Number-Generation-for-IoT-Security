# Data collection 
It is done using methods in the generateEntropies.ipynb and according to the speciications SP 800-90B.

# Determining the track 
This is based on steps in NIST SP 800-90B (Section 3.1.2)
## Step 1:
The data is IID based on tables created from samples created. 
## Step 2 (Test Raw dataset):
Loaded 1000000 samples of 11 distinct 8-bit-wide symbols
Number of Binary samples: 8000000

Samples have been translated
Calculating baseline statistics...
        Raw Mean: 78.641169
        Median: 4.000000
        Binary: false

Literal MCV Estimate: mode = 302630, p-hat = 0.30263000000000001, p_u = 0.30381332738698391
Bitstring MCV Estimate: mode = 4269152, p-hat = 0.53364400000000001, p_u = 0.5340983146201812
H_original: 1.718743
H_bitstring: 0.904823
min(H_original, 8 X H_bitstring): 1.718743
Chi square independence
        score = 98.589350
        degrees of freedom = 90
        p-value = 0.251351

Chi square goodness of fit
        score = 78.193929
        degrees of freedom = 90
        p-value = 0.808235

** Passed chi square tests

Literal Longest Repeated Substring results
        P_col: 0.227811
        Length of LRS: 18
        Pr(X >= 1): 0.744763
** Passed length of longest repeated substring test

Beginning initial tests...

Initial test results
              excursion: 41926.9
     numDirectionalRuns: 625969
     lenDirectionalRuns: 13
  numIncreasesDecreases: 614093
          numRunsMedian: 500116
          lenRunsMedian: 23
           avgCollision: 3.43486
           maxCollision: 9
         periodicity(1): 227920
         periodicity(2): 228157
         periodicity(8): 227430
        periodicity(16): 227617
        periodicity(32): 228150
          covariance(1): 6.17972e+09
          covariance(2): 6.18222e+09
          covariance(8): 6.18164e+09
         covariance(16): 6.18406e+09
         covariance(32): 6.19078e+09
            compression: 344526

Beginning permutation tests... these may take some time
 75.29% of Permutation test rounds, 100.00% of Permutation tests

                statistic  C[i][0]  C[i][1]  C[i][2]
----------------------------------------------------
                excursion      19       0       6
       numDirectionalRuns       6       0       7
       lenDirectionalRuns       4       6       0
    numIncreasesDecreases       6       0      15
            numRunsMedian       6       0      30
            lenRunsMedian       2       4      28
             avgCollision      36       0       6
             maxCollision       0       6       0
           periodicity(1)       6       0       8
           periodicity(2)       6       0      11
           periodicity(8)      14       0       6
          periodicity(16)      21       0       6
          periodicity(32)       6       0      22
            covariance(1)      82       0       6
            covariance(2)      16       0       6
            covariance(8)      13       0       6
           covariance(16)      12       0       6
           covariance(32)       6       0     106
              compression       6       0       7
(* denotes failed test)

** Passed IID permutation tests

## Step 3 (Tested Restart dataset):
Loaded 1000000 samples of 11 distinct 8-bit-wide symbols
Number of Binary samples: 8000000

Samples have been translated
Calculating baseline statistics...
        Raw Mean: 78.684066
        Median: 4.000000
        Binary: false

Bitstring MCV Estimate: mode = 4268377, p-hat = 0.53354712500000001, p_u = 0.53400144556143769
h': 0.905084
Chi square independence
        score = 90.502888
        degrees of freedom = 90
        p-value = 0.465293

Chi square goodness of fit
        score = 83.491411
        degrees of freedom = 90
        p-value = 0.672675

** Passed chi square tests

Literal Longest Repeated Substring results
        P_col: 0.227704
        Length of LRS: 18
        Pr(X >= 1): 0.741792
** Passed length of longest repeated substring test

Beginning initial tests...

Initial test results
              excursion: 67862.5
     numDirectionalRuns: 625223
     lenDirectionalRuns: 14
  numIncreasesDecreases: 614071
          numRunsMedian: 498838
          lenRunsMedian: 19
           avgCollision: 3.43919
           maxCollision: 9
         periodicity(1): 227533
         periodicity(2): 227518
         periodicity(8): 227885
        periodicity(16): 228205
        periodicity(32): 227069
          covariance(1): 6.19783e+09
          covariance(2): 6.19284e+09
          covariance(8): 6.19379e+09
         covariance(16): 6.19607e+09
         covariance(32): 6.19147e+09
            compression: 344847

Beginning permutation tests... these may take some time
 75.47% of Permutation test rounds, 100.00% of Permutation tests

                statistic  C[i][0]  C[i][1]  C[i][2]
----------------------------------------------------
                excursion       6       0      19
       numDirectionalRuns      99       0       6
       lenDirectionalRuns       1       5       4
    numIncreasesDecreases       6       0      16
            numRunsMedian     104       0       6
            lenRunsMedian       7       5       1
             avgCollision       6       0      11
             maxCollision       0       6       0
           periodicity(1)      24       0       6
           periodicity(2)       9       0       6
           periodicity(8)       6       0      15
          periodicity(16)       6       0      61
          periodicity(32)      25       0       6
            covariance(1)       6       0     129
            covariance(2)       6       0      11
            covariance(8)       6       0      37
           covariance(16)       6       0      41
           covariance(32)       6       0       6
              compression       6       0     179
(* denotes failed test)

** Passed IID permutation tests

## Step 4 (Tested conditioned dataset):
Loaded 1000000 samples of 246 distinct 8-bit-wide symbols
Number of Binary samples: 8000000

Samples have been translated
Calculating baseline statistics...
        Raw Mean: 95.115113
        Median: 92.000000
        Binary: false

Literal MCV Estimate: mode = 121592, p-hat = 0.12159200000000001, p_u = 0.12243381747897834
Bitstring MCV Estimate: mode = 5424355, p-hat = 0.67804437500000003, p_u = 0.67846987462390618
H_original: 3.029926
H_bitstring: 0.559643
min(H_original, 8 X H_bitstring): 3.029926
Chi square independence
        score = 2885.901277
        degrees of freedom = 2692
        p-value = 0.004789

Chi square goodness of fit
        score = 971.261797
        degrees of freedom = 1008
        p-value = 0.792031

** Passed chi square tests

Literal Longest Repeated Substring results
        P_col: 0.063618
        Length of LRS: 9
        Pr(X >= 1): 0.999803
** Passed length of longest repeated substring test

Beginning initial tests...

Initial test results
              excursion: 96439
     numDirectionalRuns: 663559
     lenDirectionalRuns: 9
  numIncreasesDecreases: 531811
          numRunsMedian: 499946
          lenRunsMedian: 22
           avgCollision: 5.80362
           maxCollision: 18
         periodicity(1): 63645
         periodicity(2): 63825
         periodicity(8): 63605
        periodicity(16): 63523
        periodicity(32): 63589
          covariance(1): 9.04056e+09
          covariance(2): 9.04447e+09
          covariance(8): 9.04845e+09
         covariance(16): 9.05087e+09
         covariance(32): 9.05645e+09
            compression: 630790

Beginning permutation tests... these may take some time
 76.23% of Permutation test rounds, 100.00% of Permutation tests

                statistic  C[i][0]  C[i][1]  C[i][2]
----------------------------------------------------
                excursion       6       0      78
       numDirectionalRuns       6       0      23
       lenDirectionalRuns       1       6       0
    numIncreasesDecreases      10       0       6
            numRunsMedian       6       0      88
            lenRunsMedian       1       5       8
             avgCollision      10       0       6
             maxCollision      15       6       0
           periodicity(1)       6       0      10
           periodicity(2)       6       0      25
           periodicity(8)       6       0      10
          periodicity(16)       6       0       6
          periodicity(32)      11       0       6
            covariance(1)      54       0       6
            covariance(2)       9       0       6
            covariance(8)       6       0       7
           covariance(16)       6       0      29
           covariance(32)       6       0     488
              compression       7       0       6
(* denotes failed test)

** Passed IID permutation tests

# Restart tests
Loaded 1000000 samples made up of 245 distinct 8-bit-wide symbols.

Symbols have been translated.

H_I: 3.025890
ALPHA: 5.0251553006530614e-06, X_cutoff: 176
X_max: 159

Restart Sanity Check Passed...

Running non-IID tests...

Running Most Common Value Estimate...
Literal MCV Estimate: mode = 121934, p-hat = 0.121934, p_u = 0.122776836408199
        Most Common Value Estimate (Rows) = 3.025890 / 8 bit(s)
Literal MCV Estimate: mode = 121934, p-hat = 0.121934, p_u = 0.122776836408199
        Most Common Value Estimate (Cols) = 3.025890 / 8 bit(s)

Running Tuple Estimates...
Literal t-Tuple Estimate: t = 4, p-hat_max = 0.12420656891431511, p_u = 0.12505612180300482
Literal LRS Estimate: u = 5, v = 9, p-hat = 0.06607304039813143, p_u = 0.066712901778700803
Literal t-Tuple Estimate: t = 4, p-hat_max = 0.121934, p_u = 0.122776836408199
Literal LRS Estimate: u = 5, v = 9, p-hat = 0.063994435105186112, p_u = 0.064624851671264194
        T-Tuple Test Estimate (Rows) = 2.999352 / 8 bit(s)
        T-Tuple Test Estimate (Cols) = 3.025890 / 8 bit(s)
        LRS Test Estimate (Rows) = 3.905890 / 8 bit(s)
        LRS Test Estimate (Cols) = 3.951767 / 8 bit(s)

Running Predictor Estimates...
Literal MultiMCW Prediction Estimate: N = 999937, Pglobal' = 0.12256590513957324 (C = 121716) Plocal can't affect result (r = 7)
        Multi Most Common in Window (MultiMCW) Prediction Test Estimate (Rows) = 3.028370 / 8 bit(s)
Literal MultiMCW Prediction Estimate: N = 999937, Pglobal' = 0.12262207553740827 (C = 121772) Plocal can't affect result (r = 7)
        Multi Most Common in Window (MultiMCW) Prediction Test Estimate (Cols) = 3.027709 / 8 bit(s)
Literal Lag Prediction Estimate: N = 999999, Pglobal' = 0.064168390851197146 (C = 63540) Plocal can't affect result (r = 5)
        Lag Prediction Test Estimate (Rows) = 3.961993 / 8 bit(s)
Literal Lag Prediction Estimate: N = 999999, Pglobal' = 0.064036786577938432 (C = 63409) Plocal can't affect result (r = 5)
        Lag Prediction Test Estimate (Cols) = 3.964955 / 8 bit(s)
Literal MultiMMC Prediction Estimate: N = 999998, Pglobal' = 0.12217729759850326 (C = 121336) Plocal can't affect result (r = 7)
        Multi Markov Model with Counting (MultiMMC) Prediction Test Estimate (Rows) = 3.032952 / 8 bit(s)
Literal MultiMMC Prediction Estimate: N = 999998, Pglobal' = 0.12219936335664058 (C = 121358) Plocal can't affect result (r = 7)
        Multi Markov Model with Counting (MultiMMC) Prediction Test Estimate (Cols) = 3.032691 / 8 bit(s)
Literal LZ78Y Prediction Estimate: N = 999983, Pglobal' = 0.12192235972495805 (C = 121080) Plocal can't affect result (r = 7)
        LZ78Y Prediction Test Estimate (Rows) = 3.035965 / 8 bit(s)
Literal LZ78Y Prediction Estimate: N = 999983, Pglobal' = 0.12177491720352983 (C = 120933) Plocal can't affect result (r = 7)
        LZ78Y Prediction Test Estimate (Cols) = 3.037711 / 8 bit(s)

H_r: 2.999352
H_c: 3.025890
H_I: 3.025890

Validation Test Passed...

min(H_r, H_c, H_I): 2.999352

# Conditioning results

./ea_conditioning -n 8 8 8 .214516375 .37823625
n_in = 8
n_out = 8
nw = 8
h_in = 0.2145163749999999999978
h' = 0.3782362499999999999773
Attempting to compute entropy with 106 bits of precision.
Output_Entropy(*) = 0.2136096580726153692825
0.999 * n_out = 7.991999999999999999833
h' * n_out = 3.025889999999999999819
(Non-vetted) h_out = 0.2136096580726153692825