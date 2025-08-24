# Experiment Results Summary

**Labels:** NA_CATEGORY, diagnostique, symptome, traitement

## TF-IDF_MultinomialNB

- **Weighted F1 Score:** 0.6381
- **Accuracy:** 0.6413
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8888888888888888,
        "recall": 0.6666666666666666,
        "f1-score": 0.7619047619047619,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.5833333333333334,
        "recall": 0.3684210526315789,
        "f1-score": 0.45161290322580644,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.7428571428571429,
        "recall": 0.7878787878787878,
        "f1-score": 0.7647058823529411,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5,
        "recall": 0.6428571428571429,
        "f1-score": 0.5625,
        "support": 28.0
    },
    "accuracy": 0.6413043478260869,
    "macro avg": {
        "precision": 0.6787698412698413,
        "recall": 0.616455912508544,
        "f1-score": 0.6351808868708774,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6550465838509317,
        "recall": 0.6413043478260869,
        "f1-score": 0.6381390915412448,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_MultinomialNB

- **Weighted F1 Score:** 0.6306
- **Accuracy:** 0.6413
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8888888888888888,
        "recall": 0.6666666666666666,
        "f1-score": 0.7619047619047619,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.5454545454545454,
        "recall": 0.3157894736842105,
        "f1-score": 0.4,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.6923076923076923,
        "recall": 0.8181818181818182,
        "f1-score": 0.75,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5454545454545454,
        "recall": 0.6428571428571429,
        "f1-score": 0.5901639344262295,
        "support": 28.0
    },
    "accuracy": 0.6413043478260869,
    "macro avg": {
        "precision": 0.668026418026418,
        "recall": 0.6108737753474596,
        "f1-score": 0.6255171740827479,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6429259146650451,
        "recall": 0.6413043478260869,
        "f1-score": 0.6306244272477345,
        "support": 92.0
    }
}
```

## BoW_MultinomialNB

- **Weighted F1 Score:** 0.6216
- **Accuracy:** 0.6304
- **Best Parameters:** {'alpha': 1.0}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5833333333333334,
        "f1-score": 0.7368421052631579,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.5833333333333334,
        "recall": 0.3684210526315789,
        "f1-score": 0.45161290322580644,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.6511627906976745,
        "recall": 0.8484848484848485,
        "f1-score": 0.7368421052631579,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5333333333333333,
        "recall": 0.5714285714285714,
        "f1-score": 0.5517241379310345,
        "support": 28.0
    },
    "accuracy": 0.6304347826086957,
    "macro avg": {
        "precision": 0.6919573643410852,
        "recall": 0.5929169514695831,
        "f1-score": 0.6192553129207892,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.646793899561847,
        "recall": 0.6304347826086957,
        "f1-score": 0.62159582348045,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_LogisticRegression

- **Weighted F1 Score:** 0.6201
- **Accuracy:** 0.6304
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5833333333333334,
        "f1-score": 0.7368421052631579,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.75,
        "recall": 0.3157894736842105,
        "f1-score": 0.4444444444444444,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.6428571428571429,
        "recall": 0.8181818181818182,
        "f1-score": 0.72,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5142857142857142,
        "recall": 0.6428571428571429,
        "f1-score": 0.5714285714285714,
        "support": 28.0
    },
    "accuracy": 0.6304347826086957,
    "macro avg": {
        "precision": 0.7267857142857143,
        "recall": 0.5900404420141262,
        "f1-score": 0.6181787802840434,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6724378881987577,
        "recall": 0.6304347826086957,
        "f1-score": 0.6200711924739385,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_SVM

- **Weighted F1 Score:** 0.5933
- **Accuracy:** 0.5978
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.875,
        "recall": 0.5833333333333334,
        "f1-score": 0.7,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.5833333333333334,
        "recall": 0.3684210526315789,
        "f1-score": 0.45161290322580644,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.6410256410256411,
        "recall": 0.7575757575757576,
        "f1-score": 0.6944444444444444,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.48484848484848486,
        "recall": 0.5714285714285714,
        "f1-score": 0.5245901639344263,
        "support": 28.0
    },
    "accuracy": 0.5978260869565217,
    "macro avg": {
        "precision": 0.6460518648018648,
        "recall": 0.5701896787423103,
        "f1-score": 0.5926618779011693,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6120971419884463,
        "recall": 0.5978260869565217,
        "f1-score": 0.5933243088926187,
        "support": 92.0
    }
}
```

## TF-IDF_LogisticRegression

- **Weighted F1 Score:** 0.5815
- **Accuracy:** 0.5870
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.875,
        "recall": 0.5833333333333334,
        "f1-score": 0.7,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.6,
        "recall": 0.3157894736842105,
        "f1-score": 0.41379310344827586,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.6578947368421053,
        "recall": 0.7575757575757576,
        "f1-score": 0.704225352112676,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.4444444444444444,
        "recall": 0.5714285714285714,
        "f1-score": 0.5,
        "support": 28.0
    },
    "accuracy": 0.5869565217391305,
    "macro avg": {
        "precision": 0.6443347953216374,
        "recall": 0.5570317840054682,
        "f1-score": 0.579504613890238,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6092931604373252,
        "recall": 0.5869565217391305,
        "f1-score": 0.581538104187343,
        "support": 92.0
    }
}
```

## TF-IDF_KNN

- **Weighted F1 Score:** 0.5654
- **Accuracy:** 0.5761
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6111111111111112,
        "recall": 0.9166666666666666,
        "f1-score": 0.7333333333333333,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.5384615384615384,
        "recall": 0.3684210526315789,
        "f1-score": 0.4375,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.6470588235294118,
        "recall": 0.6666666666666666,
        "f1-score": 0.6567164179104478,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.48148148148148145,
        "recall": 0.4642857142857143,
        "f1-score": 0.4727272727272727,
        "support": 28.0
    },
    "accuracy": 0.5760869565217391,
    "macro avg": {
        "precision": 0.5695282386458856,
        "recall": 0.6040100250626567,
        "f1-score": 0.5750692559927635,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.569549187196246,
        "recall": 0.5760869565217391,
        "f1-score": 0.565440276384874,
        "support": 92.0
    }
}
```

## Bert_LogisticRegression

- **Weighted F1 Score:** 0.5576
- **Accuracy:** 0.5652
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8,
        "recall": 0.6666666666666666,
        "f1-score": 0.7272727272727273,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.5454545454545454,
        "recall": 0.3157894736842105,
        "f1-score": 0.4,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.5454545454545454,
        "recall": 0.5454545454545454,
        "f1-score": 0.5454545454545454,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5263157894736842,
        "recall": 0.7142857142857143,
        "f1-score": 0.6060606060606061,
        "support": 28.0
    },
    "accuracy": 0.5652173913043478,
    "macro avg": {
        "precision": 0.6043062200956938,
        "recall": 0.5605491000227842,
        "f1-score": 0.5696969696969697,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5728312877054297,
        "recall": 0.5652173913043478,
        "f1-score": 0.5575757575757576,
        "support": 92.0
    }
}
```

## Bert_SVM

- **Weighted F1 Score:** 0.5544
- **Accuracy:** 0.5543
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.5333333333333333,
        "recall": 0.6666666666666666,
        "f1-score": 0.5925925925925926,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.5882352941176471,
        "recall": 0.5263157894736842,
        "f1-score": 0.5555555555555556,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.6,
        "recall": 0.5454545454545454,
        "f1-score": 0.5714285714285714,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5,
        "recall": 0.5357142857142857,
        "f1-score": 0.5172413793103449,
        "support": 28.0
    },
    "accuracy": 0.5543478260869565,
    "macro avg": {
        "precision": 0.5553921568627451,
        "recall": 0.5685378218272955,
        "f1-score": 0.5592045247217661,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5584398976982097,
        "recall": 0.5543478260869565,
        "f1-score": 0.5544192189619476,
        "support": 92.0
    }
}
```

## BoW_LogisticRegression

- **Weighted F1 Score:** 0.5527
- **Accuracy:** 0.5543
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8,
        "recall": 0.6666666666666666,
        "f1-score": 0.7272727272727273,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.5384615384615384,
        "recall": 0.3684210526315789,
        "f1-score": 0.4375,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.5945945945945946,
        "recall": 0.6666666666666666,
        "f1-score": 0.6285714285714286,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.4375,
        "recall": 0.5,
        "f1-score": 0.4666666666666667,
        "support": 28.0
    },
    "accuracy": 0.5543478260869565,
    "macro avg": {
        "precision": 0.5926390332640333,
        "recall": 0.5504385964912281,
        "f1-score": 0.5650027056277056,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.561982509265118,
        "recall": 0.5543478260869565,
        "f1-score": 0.5527097449651797,
        "support": 92.0
    }
}
```

## Bert_KNN

- **Weighted F1 Score:** 0.5398
- **Accuracy:** 0.5435
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.7142857142857143,
        "recall": 0.8333333333333334,
        "f1-score": 0.7692307692307693,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.5333333333333333,
        "recall": 0.42105263157894735,
        "f1-score": 0.47058823529411764,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.5588235294117647,
        "recall": 0.5757575757575758,
        "f1-score": 0.5671641791044776,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.4482758620689655,
        "recall": 0.4642857142857143,
        "f1-score": 0.45614035087719296,
        "support": 28.0
    },
    "accuracy": 0.5434782608695652,
    "macro avg": {
        "precision": 0.5636796097749445,
        "recall": 0.5736073137388927,
        "f1-score": 0.5657808836266394,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5401919838400128,
        "recall": 0.5434782608695652,
        "f1-score": 0.5397857982213764,
        "support": 92.0
    }
}
```

## TF-IDF_SVM

- **Weighted F1 Score:** 0.5281
- **Accuracy:** 0.5217
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8888888888888888,
        "recall": 0.6666666666666666,
        "f1-score": 0.7619047619047619,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.4117647058823529,
        "recall": 0.3684210526315789,
        "f1-score": 0.3888888888888889,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.625,
        "recall": 0.6060606060606061,
        "f1-score": 0.6153846153846154,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.38235294117647056,
        "recall": 0.4642857142857143,
        "f1-score": 0.41935483870967744,
        "support": 28.0
    },
    "accuracy": 0.5217391304347826,
    "macro avg": {
        "precision": 0.577001633986928,
        "recall": 0.5263585099111415,
        "f1-score": 0.5463832762219859,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5415334612105711,
        "recall": 0.5217391304347826,
        "f1-score": 0.5280584111229273,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN

- **Weighted F1 Score:** 0.5279
- **Accuracy:** 0.5435
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.55,
        "recall": 0.9166666666666666,
        "f1-score": 0.6875,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.4,
        "recall": 0.3157894736842105,
        "f1-score": 0.35294117647058826,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.6111111111111112,
        "recall": 0.6666666666666666,
        "f1-score": 0.6376811594202898,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5238095238095238,
        "recall": 0.39285714285714285,
        "f1-score": 0.4489795918367347,
        "support": 28.0
    },
    "accuracy": 0.5434782608695652,
    "macro avg": {
        "precision": 0.5212301587301588,
        "recall": 0.5729949874686716,
        "f1-score": 0.5317754819319032,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5329710144927536,
        "recall": 0.5434782608695652,
        "f1-score": 0.5279433607091228,
        "support": 92.0
    }
}
```

## BoW_DecisionTree

- **Weighted F1 Score:** 0.5273
- **Accuracy:** 0.5326
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.7777777777777778,
        "recall": 0.5833333333333334,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.4444444444444444,
        "recall": 0.42105263157894735,
        "f1-score": 0.43243243243243246,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.5111111111111111,
        "recall": 0.696969696969697,
        "f1-score": 0.5897435897435898,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.55,
        "recall": 0.39285714285714285,
        "f1-score": 0.4583333333333333,
        "support": 28.0
    },
    "accuracy": 0.532608695652174,
    "macro avg": {
        "precision": 0.5708333333333333,
        "recall": 0.5235532011847802,
        "f1-score": 0.5367940055440056,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.543961352657005,
        "recall": 0.532608695652174,
        "f1-score": 0.5272944349031305,
        "support": 92.0
    }
}
```

## BoW_SVM

- **Weighted F1 Score:** 0.5236
- **Accuracy:** 0.5217
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.7272727272727273,
        "recall": 0.6666666666666666,
        "f1-score": 0.6956521739130435,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.5,
        "recall": 0.42105263157894735,
        "f1-score": 0.45714285714285713,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.5757575757575758,
        "recall": 0.5757575757575758,
        "f1-score": 0.5757575757575758,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.40625,
        "recall": 0.4642857142857143,
        "f1-score": 0.43333333333333335,
        "support": 28.0
    },
    "accuracy": 0.5217391304347826,
    "macro avg": {
        "precision": 0.5523200757575758,
        "recall": 0.531940647072226,
        "f1-score": 0.5404714850367025,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5282855731225297,
        "recall": 0.5217391304347826,
        "f1-score": 0.5235529750652624,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.4722
- **Accuracy:** 0.4783
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6,
        "recall": 0.75,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.5,
        "recall": 0.42105263157894735,
        "f1-score": 0.45714285714285713,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.46153846153846156,
        "recall": 0.36363636363636365,
        "f1-score": 0.4067796610169492,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.42857142857142855,
        "recall": 0.5357142857142857,
        "f1-score": 0.47619047619047616,
        "support": 28.0
    },
    "accuracy": 0.4782608695652174,
    "macro avg": {
        "precision": 0.4975274725274726,
        "recall": 0.5176008202323992,
        "f1-score": 0.5016949152542373,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.47750836120401335,
        "recall": 0.4782608695652174,
        "f1-score": 0.47220409165877103,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree

- **Weighted F1 Score:** 0.4712
- **Accuracy:** 0.4783
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6666666666666666,
        "recall": 0.6666666666666666,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.38461538461538464,
        "recall": 0.2631578947368421,
        "f1-score": 0.3125,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.48717948717948717,
        "recall": 0.5757575757575758,
        "f1-score": 0.5277777777777778,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.42857142857142855,
        "recall": 0.42857142857142855,
        "f1-score": 0.42857142857142855,
        "support": 28.0
    },
    "accuracy": 0.4782608695652174,
    "macro avg": {
        "precision": 0.4917582417582418,
        "recall": 0.4835383914331283,
        "f1-score": 0.48387896825396826,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.47157190635451507,
        "recall": 0.4782608695652174,
        "f1-score": 0.47124094202898553,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.4611
- **Accuracy:** 0.4674
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.75,
        "recall": 0.5,
        "f1-score": 0.6,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.42857142857142855,
        "recall": 0.3157894736842105,
        "f1-score": 0.36363636363636365,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.45652173913043476,
        "recall": 0.6363636363636364,
        "f1-score": 0.5316455696202531,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.4166666666666667,
        "recall": 0.35714285714285715,
        "f1-score": 0.38461538461538464,
        "support": 28.0
    },
    "accuracy": 0.4673913043478261,
    "macro avg": {
        "precision": 0.5129399585921325,
        "recall": 0.452323991797676,
        "f1-score": 0.46997432946800033,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.4768993608785669,
        "recall": 0.4673913043478261,
        "f1-score": 0.4611154943020655,
        "support": 92.0
    }
}
```

## Bert_DecisionTree

- **Weighted F1 Score:** 0.4362
- **Accuracy:** 0.4348
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.5,
        "recall": 0.4166666666666667,
        "f1-score": 0.45454545454545453,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.45,
        "recall": 0.47368421052631576,
        "f1-score": 0.46153846153846156,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.4838709677419355,
        "recall": 0.45454545454545453,
        "f1-score": 0.46875,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.3548387096774194,
        "recall": 0.39285714285714285,
        "f1-score": 0.3728813559322034,
        "support": 28.0
    },
    "accuracy": 0.43478260869565216,
    "macro avg": {
        "precision": 0.4471774193548387,
        "recall": 0.43443836864889496,
        "f1-score": 0.4394288180040299,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.43970897615708276,
        "recall": 0.43478260869565216,
        "f1-score": 0.43623048032476,
        "support": 92.0
    }
}
```

## FastText_DecisionTree

- **Weighted F1 Score:** 0.4142
- **Accuracy:** 0.4130
- **Best Parameters:** {'max_depth': 10}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6666666666666666,
        "recall": 0.6666666666666666,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.32,
        "recall": 0.42105263157894735,
        "f1-score": 0.36363636363636365,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.4444444444444444,
        "recall": 0.36363636363636365,
        "f1-score": 0.4,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.35714285714285715,
        "recall": 0.35714285714285715,
        "f1-score": 0.35714285714285715,
        "support": 28.0
    },
    "accuracy": 0.41304347826086957,
    "macro avg": {
        "precision": 0.44706349206349205,
        "recall": 0.4521246297562087,
        "f1-score": 0.44686147186147185,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.4211594202898551,
        "recall": 0.41304347826086957,
        "f1-score": 0.4142292490118577,
        "support": 92.0
    }
}
```

## FastText_KNN

- **Weighted F1 Score:** 0.3616
- **Accuracy:** 0.3804
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.4166666666666667,
        "f1-score": 0.5882352941176471,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.2978723404255319,
        "recall": 0.7368421052631579,
        "f1-score": 0.42424242424242425,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.4482758620689655,
        "recall": 0.3939393939393939,
        "f1-score": 0.41935483870967744,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.2727272727272727,
        "recall": 0.10714285714285714,
        "f1-score": 0.15384615384615385,
        "support": 28.0
    },
    "accuracy": 0.3804347826086957,
    "macro avg": {
        "precision": 0.5047188688054425,
        "recall": 0.41364775575301893,
        "f1-score": 0.3964196777289757,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.43575045166005,
        "recall": 0.3804347826086957,
        "f1-score": 0.3615851258166249,
        "support": 92.0
    }
}
```

## BoW_KNN

- **Weighted F1 Score:** 0.3606
- **Accuracy:** 0.4239
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.3333333333333333,
        "recall": 0.75,
        "f1-score": 0.46153846153846156,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.42857142857142855,
        "recall": 0.3157894736842105,
        "f1-score": 0.36363636363636365,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.48936170212765956,
        "recall": 0.696969696969697,
        "f1-score": 0.575,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.25,
        "recall": 0.03571428571428571,
        "f1-score": 0.0625,
        "support": 28.0
    },
    "accuracy": 0.42391304347826086,
    "macro avg": {
        "precision": 0.37531661600810534,
        "recall": 0.44961836409204836,
        "f1-score": 0.3656687062937063,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.38360644905510766,
        "recall": 0.42391304347826086,
        "f1-score": 0.36057122225600485,
        "support": 92.0
    }
}
```

## Word2Vec_KNN

- **Weighted F1 Score:** 0.3595
- **Accuracy:** 0.3913
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6666666666666666,
        "recall": 0.6666666666666666,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "diagnostique": {
        "precision": 0.2727272727272727,
        "recall": 0.3157894736842105,
        "f1-score": 0.2926829268292683,
        "support": 19.0
    },
    "symptome": {
        "precision": 0.43478260869565216,
        "recall": 0.6060606060606061,
        "f1-score": 0.5063291139240507,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.16666666666666666,
        "recall": 0.07142857142857142,
        "f1-score": 0.1,
        "support": 28.0
    },
    "accuracy": 0.391304347826087,
    "macro avg": {
        "precision": 0.3852108036890646,
        "recall": 0.4149863294600136,
        "f1-score": 0.3914196768549964,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.34995990147218875,
        "recall": 0.391304347826087,
        "f1-score": 0.35945474314401915,
        "support": 92.0
    }
}
```

## Word2Vec_LogisticRegression

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "micro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "macro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "weighted avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    }
}
```

## Word2Vec_SVM

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "micro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "macro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "weighted avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    }
}
```

## FastText_LogisticRegression

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "micro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "macro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "weighted avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    }
}
```

## FastText_SVM

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "micro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "macro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "weighted avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    }
}
```

