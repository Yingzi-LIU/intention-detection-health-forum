# Experiment Results Summary

**Labels:** diagnostique, nan, symptome, traitement

## BoW_LogisticRegression

- **Weighted F1 Score:** 0.5527
- **Accuracy:** 0.5543
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "0": {
        "precision": 0.5384615384615384,
        "recall": 0.3684210526315789,
        "f1-score": 0.4375,
        "support": 19.0
    },
    "1": {
        "precision": 0.8,
        "recall": 0.6666666666666666,
        "f1-score": 0.7272727272727273,
        "support": 12.0
    },
    "2": {
        "precision": 0.5945945945945946,
        "recall": 0.6666666666666666,
        "f1-score": 0.6285714285714286,
        "support": 33.0
    },
    "3": {
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

## BoW_SVM

- **Weighted F1 Score:** 0.5236
- **Accuracy:** 0.5217
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.5,
        "recall": 0.42105263157894735,
        "f1-score": 0.45714285714285713,
        "support": 19.0
    },
    "1": {
        "precision": 0.7272727272727273,
        "recall": 0.6666666666666666,
        "f1-score": 0.6956521739130435,
        "support": 12.0
    },
    "2": {
        "precision": 0.5757575757575758,
        "recall": 0.5757575757575758,
        "f1-score": 0.5757575757575758,
        "support": 33.0
    },
    "3": {
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

## BoW_MultinomialNB

- **Weighted F1 Score:** 0.6216
- **Accuracy:** 0.6304
- **Best Parameters:** {'alpha': 1.0}
```json
{
    "0": {
        "precision": 0.5833333333333334,
        "recall": 0.3684210526315789,
        "f1-score": 0.45161290322580644,
        "support": 19.0
    },
    "1": {
        "precision": 1.0,
        "recall": 0.5833333333333334,
        "f1-score": 0.7368421052631579,
        "support": 12.0
    },
    "2": {
        "precision": 0.6511627906976745,
        "recall": 0.8484848484848485,
        "f1-score": 0.7368421052631579,
        "support": 33.0
    },
    "3": {
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

## BoW_DecisionTree

- **Weighted F1 Score:** 0.5153
- **Accuracy:** 0.5217
- **Best Parameters:** {'max_depth': None}
```json
{
    "0": {
        "precision": 0.4375,
        "recall": 0.3684210526315789,
        "f1-score": 0.4,
        "support": 19.0
    },
    "1": {
        "precision": 0.7777777777777778,
        "recall": 0.5833333333333334,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "2": {
        "precision": 0.48936170212765956,
        "recall": 0.696969696969697,
        "f1-score": 0.575,
        "support": 33.0
    },
    "3": {
        "precision": 0.55,
        "recall": 0.39285714285714285,
        "f1-score": 0.4583333333333333,
        "support": 28.0
    },
    "accuracy": 0.5217391304347826,
    "macro avg": {
        "precision": 0.5636598699763593,
        "recall": 0.5103953064479381,
        "f1-score": 0.525,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5347257554733271,
        "recall": 0.5217391304347826,
        "f1-score": 0.5153079710144928,
        "support": 92.0
    }
}
```

## BoW_KNN

- **Weighted F1 Score:** 0.3813
- **Accuracy:** 0.4457
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "0": {
        "precision": 0.42105263157894735,
        "recall": 0.42105263157894735,
        "f1-score": 0.42105263157894735,
        "support": 19.0
    },
    "1": {
        "precision": 0.4090909090909091,
        "recall": 0.75,
        "f1-score": 0.5294117647058824,
        "support": 12.0
    },
    "2": {
        "precision": 0.48936170212765956,
        "recall": 0.696969696969697,
        "f1-score": 0.575,
        "support": 33.0
    },
    "3": {
        "precision": 0.25,
        "recall": 0.03571428571428571,
        "f1-score": 0.0625,
        "support": 28.0
    },
    "accuracy": 0.44565217391304346,
    "macro avg": {
        "precision": 0.392376310699379,
        "recall": 0.47593415356573254,
        "f1-score": 0.39699109907120744,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.39193507694895297,
        "recall": 0.44565217391304346,
        "f1-score": 0.3812819693094629,
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
    "0": {
        "precision": 0.6,
        "recall": 0.3157894736842105,
        "f1-score": 0.41379310344827586,
        "support": 19.0
    },
    "1": {
        "precision": 0.875,
        "recall": 0.5833333333333334,
        "f1-score": 0.7,
        "support": 12.0
    },
    "2": {
        "precision": 0.6578947368421053,
        "recall": 0.7575757575757576,
        "f1-score": 0.704225352112676,
        "support": 33.0
    },
    "3": {
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

## TF-IDF_SVM

- **Weighted F1 Score:** 0.5281
- **Accuracy:** 0.5217
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.4117647058823529,
        "recall": 0.3684210526315789,
        "f1-score": 0.3888888888888889,
        "support": 19.0
    },
    "1": {
        "precision": 0.8888888888888888,
        "recall": 0.6666666666666666,
        "f1-score": 0.7619047619047619,
        "support": 12.0
    },
    "2": {
        "precision": 0.625,
        "recall": 0.6060606060606061,
        "f1-score": 0.6153846153846154,
        "support": 33.0
    },
    "3": {
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

## TF-IDF_MultinomialNB

- **Weighted F1 Score:** 0.6381
- **Accuracy:** 0.6413
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "0": {
        "precision": 0.5833333333333334,
        "recall": 0.3684210526315789,
        "f1-score": 0.45161290322580644,
        "support": 19.0
    },
    "1": {
        "precision": 0.8888888888888888,
        "recall": 0.6666666666666666,
        "f1-score": 0.7619047619047619,
        "support": 12.0
    },
    "2": {
        "precision": 0.7428571428571429,
        "recall": 0.7878787878787878,
        "f1-score": 0.7647058823529411,
        "support": 33.0
    },
    "3": {
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

## TF-IDF_DecisionTree

- **Weighted F1 Score:** 0.4787
- **Accuracy:** 0.4783
- **Best Parameters:** {'max_depth': None}
```json
{
    "0": {
        "precision": 0.3684210526315789,
        "recall": 0.3684210526315789,
        "f1-score": 0.3684210526315789,
        "support": 19.0
    },
    "1": {
        "precision": 0.8571428571428571,
        "recall": 0.5,
        "f1-score": 0.631578947368421,
        "support": 12.0
    },
    "2": {
        "precision": 0.4878048780487805,
        "recall": 0.6060606060606061,
        "f1-score": 0.5405405405405406,
        "support": 33.0
    },
    "3": {
        "precision": 0.44,
        "recall": 0.39285714285714285,
        "f1-score": 0.41509433962264153,
        "support": 28.0
    },
    "accuracy": 0.4782608695652174,
    "macro avg": {
        "precision": 0.5383421969558041,
        "recall": 0.466834700387332,
        "f1-score": 0.48890872004079555,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.4967747311013483,
        "recall": 0.4782608695652174,
        "f1-score": 0.4786894208227484,
        "support": 92.0
    }
}
```

## TF-IDF_KNN

- **Weighted F1 Score:** 0.5576
- **Accuracy:** 0.5652
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "0": {
        "precision": 0.4666666666666667,
        "recall": 0.3684210526315789,
        "f1-score": 0.4117647058823529,
        "support": 19.0
    },
    "1": {
        "precision": 0.625,
        "recall": 0.8333333333333334,
        "f1-score": 0.7142857142857143,
        "support": 12.0
    },
    "2": {
        "precision": 0.6470588235294118,
        "recall": 0.6666666666666666,
        "f1-score": 0.6567164179104478,
        "support": 33.0
    },
    "3": {
        "precision": 0.48148148148148145,
        "recall": 0.4642857142857143,
        "f1-score": 0.4727272727272727,
        "support": 28.0
    },
    "accuracy": 0.5652173913043478,
    "macro avg": {
        "precision": 0.55505174291939,
        "recall": 0.5831766917293233,
        "f1-score": 0.5638735277014469,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.556533579615421,
        "recall": 0.5652173913043478,
        "f1-score": 0.5576409066369749,
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
    "0": {
        "precision": 0.75,
        "recall": 0.3157894736842105,
        "f1-score": 0.4444444444444444,
        "support": 19.0
    },
    "1": {
        "precision": 1.0,
        "recall": 0.5833333333333334,
        "f1-score": 0.7368421052631579,
        "support": 12.0
    },
    "2": {
        "precision": 0.6428571428571429,
        "recall": 0.8181818181818182,
        "f1-score": 0.72,
        "support": 33.0
    },
    "3": {
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
    "0": {
        "precision": 0.5833333333333334,
        "recall": 0.3684210526315789,
        "f1-score": 0.45161290322580644,
        "support": 19.0
    },
    "1": {
        "precision": 0.875,
        "recall": 0.5833333333333334,
        "f1-score": 0.7,
        "support": 12.0
    },
    "2": {
        "precision": 0.6410256410256411,
        "recall": 0.7575757575757576,
        "f1-score": 0.6944444444444444,
        "support": 33.0
    },
    "3": {
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

## TF-IDF_ngram_MultinomialNB

- **Weighted F1 Score:** 0.6306
- **Accuracy:** 0.6413
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "0": {
        "precision": 0.5454545454545454,
        "recall": 0.3157894736842105,
        "f1-score": 0.4,
        "support": 19.0
    },
    "1": {
        "precision": 0.8888888888888888,
        "recall": 0.6666666666666666,
        "f1-score": 0.7619047619047619,
        "support": 12.0
    },
    "2": {
        "precision": 0.6923076923076923,
        "recall": 0.8181818181818182,
        "f1-score": 0.75,
        "support": 33.0
    },
    "3": {
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

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.4529
- **Accuracy:** 0.4565
- **Best Parameters:** {'max_depth': None}
```json
{
    "0": {
        "precision": 0.5454545454545454,
        "recall": 0.3157894736842105,
        "f1-score": 0.4,
        "support": 19.0
    },
    "1": {
        "precision": 0.75,
        "recall": 0.5,
        "f1-score": 0.6,
        "support": 12.0
    },
    "2": {
        "precision": 0.40816326530612246,
        "recall": 0.6060606060606061,
        "f1-score": 0.4878048780487805,
        "support": 33.0
    },
    "3": {
        "precision": 0.4166666666666667,
        "recall": 0.35714285714285715,
        "f1-score": 0.38461538461538464,
        "support": 28.0
    },
    "accuracy": 0.45652173913043476,
    "macro avg": {
        "precision": 0.5300711193568336,
        "recall": 0.44474823422191845,
        "f1-score": 0.46810506566604126,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.4836922911457074,
        "recall": 0.45652173913043476,
        "f1-score": 0.4528999102700057,
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
    "0": {
        "precision": 0.4,
        "recall": 0.3157894736842105,
        "f1-score": 0.35294117647058826,
        "support": 19.0
    },
    "1": {
        "precision": 0.55,
        "recall": 0.9166666666666666,
        "f1-score": 0.6875,
        "support": 12.0
    },
    "2": {
        "precision": 0.6111111111111112,
        "recall": 0.6666666666666666,
        "f1-score": 0.6376811594202898,
        "support": 33.0
    },
    "3": {
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

## Word2Vec_LogisticRegression

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "2": {
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
    "2": {
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

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.3942
- **Accuracy:** 0.4022
- **Best Parameters:** {'max_depth': 5}
```json
{
    "0": {
        "precision": 0.375,
        "recall": 0.47368421052631576,
        "f1-score": 0.4186046511627907,
        "support": 19.0
    },
    "1": {
        "precision": 0.6,
        "recall": 0.75,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "2": {
        "precision": 0.41379310344827586,
        "recall": 0.36363636363636365,
        "f1-score": 0.3870967741935484,
        "support": 33.0
    },
    "3": {
        "precision": 0.2916666666666667,
        "recall": 0.25,
        "f1-score": 0.2692307692307692,
        "support": 28.0
    },
    "accuracy": 0.40217391304347827,
    "macro avg": {
        "precision": 0.42011494252873566,
        "recall": 0.4593301435406698,
        "f1-score": 0.4353997153134437,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.3929004247876062,
        "recall": 0.40217391304347827,
        "f1-score": 0.3941972115102354,
        "support": 92.0
    }
}
```

## Word2Vec_KNN

- **Weighted F1 Score:** 0.3768
- **Accuracy:** 0.4022
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "0": {
        "precision": 0.3076923076923077,
        "recall": 0.42105263157894735,
        "f1-score": 0.35555555555555557,
        "support": 19.0
    },
    "1": {
        "precision": 0.875,
        "recall": 0.5833333333333334,
        "f1-score": 0.7,
        "support": 12.0
    },
    "2": {
        "precision": 0.43478260869565216,
        "recall": 0.6060606060606061,
        "f1-score": 0.5063291139240507,
        "support": 33.0
    },
    "3": {
        "precision": 0.16666666666666666,
        "recall": 0.07142857142857142,
        "f1-score": 0.1,
        "support": 28.0
    },
    "accuracy": 0.40217391304347827,
    "macro avg": {
        "precision": 0.44603539576365664,
        "recall": 0.42046878560036455,
        "f1-score": 0.4154711673699016,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.38435485434540256,
        "recall": 0.40217391304347827,
        "f1-score": 0.3767871338592307,
        "support": 92.0
    }
}
```

## FastText_LogisticRegression

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "2": {
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
    "2": {
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

## FastText_DecisionTree

- **Weighted F1 Score:** 0.3538
- **Accuracy:** 0.3478
- **Best Parameters:** {'max_depth': 10}
```json
{
    "0": {
        "precision": 0.3333333333333333,
        "recall": 0.3157894736842105,
        "f1-score": 0.32432432432432434,
        "support": 19.0
    },
    "1": {
        "precision": 0.7,
        "recall": 0.5833333333333334,
        "f1-score": 0.6363636363636364,
        "support": 12.0
    },
    "2": {
        "precision": 0.36666666666666664,
        "recall": 0.3333333333333333,
        "f1-score": 0.3492063492063492,
        "support": 33.0
    },
    "3": {
        "precision": 0.23529411764705882,
        "recall": 0.2857142857142857,
        "f1-score": 0.25806451612903225,
        "support": 28.0
    },
    "accuracy": 0.34782608695652173,
    "macro avg": {
        "precision": 0.4088235294117647,
        "recall": 0.3795426065162907,
        "f1-score": 0.39198970650583553,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.36327791986359753,
        "recall": 0.34782608695652173,
        "f1-score": 0.35378414971682853,
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
    "0": {
        "precision": 0.2978723404255319,
        "recall": 0.7368421052631579,
        "f1-score": 0.42424242424242425,
        "support": 19.0
    },
    "1": {
        "precision": 1.0,
        "recall": 0.4166666666666667,
        "f1-score": 0.5882352941176471,
        "support": 12.0
    },
    "2": {
        "precision": 0.4482758620689655,
        "recall": 0.3939393939393939,
        "f1-score": 0.41935483870967744,
        "support": 33.0
    },
    "3": {
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

## Bert_LogisticRegression

- **Weighted F1 Score:** 0.5576
- **Accuracy:** 0.5652
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "0": {
        "precision": 0.5454545454545454,
        "recall": 0.3157894736842105,
        "f1-score": 0.4,
        "support": 19.0
    },
    "1": {
        "precision": 0.8,
        "recall": 0.6666666666666666,
        "f1-score": 0.7272727272727273,
        "support": 12.0
    },
    "2": {
        "precision": 0.5454545454545454,
        "recall": 0.5454545454545454,
        "f1-score": 0.5454545454545454,
        "support": 33.0
    },
    "3": {
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
    "0": {
        "precision": 0.5882352941176471,
        "recall": 0.5263157894736842,
        "f1-score": 0.5555555555555556,
        "support": 19.0
    },
    "1": {
        "precision": 0.5333333333333333,
        "recall": 0.6666666666666666,
        "f1-score": 0.5925925925925926,
        "support": 12.0
    },
    "2": {
        "precision": 0.6,
        "recall": 0.5454545454545454,
        "f1-score": 0.5714285714285714,
        "support": 33.0
    },
    "3": {
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

## Bert_DecisionTree

- **Weighted F1 Score:** 0.4135
- **Accuracy:** 0.4130
- **Best Parameters:** {'max_depth': 5}
```json
{
    "0": {
        "precision": 0.4444444444444444,
        "recall": 0.42105263157894735,
        "f1-score": 0.43243243243243246,
        "support": 19.0
    },
    "1": {
        "precision": 0.5,
        "recall": 0.4166666666666667,
        "f1-score": 0.45454545454545453,
        "support": 12.0
    },
    "2": {
        "precision": 0.45714285714285713,
        "recall": 0.48484848484848486,
        "f1-score": 0.47058823529411764,
        "support": 33.0
    },
    "3": {
        "precision": 0.3103448275862069,
        "recall": 0.32142857142857145,
        "f1-score": 0.3157894736842105,
        "support": 28.0
    },
    "accuracy": 0.41304347826086957,
    "macro avg": {
        "precision": 0.4279830322933771,
        "recall": 0.4109990886306676,
        "f1-score": 0.41833889898905385,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.41543275981057093,
        "recall": 0.41304347826086957,
        "f1-score": 0.41350302933288535,
        "support": 92.0
    }
}
```

## Bert_KNN

- **Weighted F1 Score:** 0.5410
- **Accuracy:** 0.5435
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "0": {
        "precision": 0.5,
        "recall": 0.42105263157894735,
        "f1-score": 0.45714285714285713,
        "support": 19.0
    },
    "1": {
        "precision": 0.7692307692307693,
        "recall": 0.8333333333333334,
        "f1-score": 0.8,
        "support": 12.0
    },
    "2": {
        "precision": 0.5588235294117647,
        "recall": 0.5757575757575758,
        "f1-score": 0.5671641791044776,
        "support": 33.0
    },
    "3": {
        "precision": 0.4482758620689655,
        "recall": 0.4642857142857143,
        "f1-score": 0.45614035087719296,
        "support": 28.0
    },
    "accuracy": 0.5434782608695652,
    "macro avg": {
        "precision": 0.5690825401778749,
        "recall": 0.5736073137388927,
        "f1-score": 0.5701118467811319,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5404746721661794,
        "recall": 0.5434782608695652,
        "f1-score": 0.5410224132687331,
        "support": 92.0
    }
}
```

