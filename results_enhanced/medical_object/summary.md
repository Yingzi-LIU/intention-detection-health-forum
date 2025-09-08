# Experiment Results Summary

**Labels:** NA_CATEGORY, diagnostique, symptome, traitement

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.6883
- **Accuracy:** 0.6897
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6666666666666666,
        "recall": 0.5,
        "f1-score": 0.5714285714285714,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.7428571428571429,
        "recall": 0.7878787878787878,
        "f1-score": 0.7647058823529411,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5806451612903226,
        "recall": 0.6666666666666666,
        "f1-score": 0.6206896551724138,
        "support": 27.0
    },
    "accuracy": 0.6896551724137931,
    "macro avg": {
        "precision": 0.747542242703533,
        "recall": 0.7029220779220778,
        "f1-score": 0.7199752580077123,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6956900965799743,
        "recall": 0.6896551724137931,
        "f1-score": 0.68832212295876,
        "support": 87.0
    }
}
```

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.6668
- **Accuracy:** 0.6667
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6111111111111112,
        "recall": 0.55,
        "f1-score": 0.5789473684210527,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.7142857142857143,
        "recall": 0.7575757575757576,
        "f1-score": 0.7352941176470589,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5714285714285714,
        "recall": 0.5925925925925926,
        "f1-score": 0.5818181818181818,
        "support": 27.0
    },
    "accuracy": 0.6666666666666666,
    "macro avg": {
        "precision": 0.7242063492063493,
        "recall": 0.6893278018278017,
        "f1-score": 0.7047841477408041,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6692209450830141,
        "recall": 0.6666666666666666,
        "f1-score": 0.6668308347287744,
        "support": 87.0
    }
}
```

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6585
- **Accuracy:** 0.6667
- **Best Parameters:** {'classifier__C': 1, 'classifier__solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6923076923076923,
        "recall": 0.45,
        "f1-score": 0.5454545454545454,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6666666666666666,
        "recall": 0.8484848484848485,
        "f1-score": 0.7466666666666667,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5769230769230769,
        "recall": 0.5555555555555556,
        "f1-score": 0.5660377358490566,
        "support": 27.0
    },
    "accuracy": 0.6666666666666666,
    "macro avg": {
        "precision": 0.733974358974359,
        "recall": 0.6777958152958152,
        "f1-score": 0.695308967761798,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6715296198054819,
        "recall": 0.6666666666666666,
        "f1-score": 0.6585476809029184,
        "support": 87.0
    }
}
```

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.6520
- **Accuracy:** 0.6552
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.7692307692307693,
        "recall": 0.5,
        "f1-score": 0.6060606060606061,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.625,
        "recall": 0.7575757575757576,
        "f1-score": 0.684931506849315,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5925925925925926,
        "recall": 0.5925925925925926,
        "f1-score": 0.5925925925925926,
        "support": 27.0
    },
    "accuracy": 0.6551724137931034,
    "macro avg": {
        "precision": 0.7109915547415547,
        "recall": 0.6768278018278018,
        "f1-score": 0.6851818906613427,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6667771883289125,
        "recall": 0.6551724137931034,
        "f1-score": 0.6519994465199944,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6505
- **Accuracy:** 0.6552
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6428571428571429,
        "recall": 0.45,
        "f1-score": 0.5294117647058824,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6666666666666666,
        "recall": 0.7878787878787878,
        "f1-score": 0.7222222222222222,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5714285714285714,
        "recall": 0.5925925925925926,
        "f1-score": 0.5818181818181818,
        "support": 27.0
    },
    "accuracy": 0.6551724137931034,
    "macro avg": {
        "precision": 0.7202380952380951,
        "recall": 0.6719035594035594,
        "f1-score": 0.6891322729558025,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.658456486042693,
        "recall": 0.6551724137931034,
        "f1-score": 0.6504850344606937,
        "support": 87.0
    }
}
```

## TF-IDF_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6476
- **Accuracy:** 0.6552
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6153846153846154,
        "recall": 0.4,
        "f1-score": 0.48484848484848486,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6923076923076923,
        "recall": 0.8181818181818182,
        "f1-score": 0.75,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5517241379310345,
        "recall": 0.5925925925925926,
        "f1-score": 0.5714285714285714,
        "support": 27.0
    },
    "accuracy": 0.6551724137931034,
    "macro avg": {
        "precision": 0.7148541114058355,
        "recall": 0.666979316979317,
        "f1-score": 0.6823384948384947,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6557516997469435,
        "recall": 0.6551724137931034,
        "f1-score": 0.6475526389319493,
        "support": 87.0
    }
}
```

## BoW_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.6458
- **Accuracy:** 0.6552
- **Best Parameters:** {'classifier__alpha': 1.0}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5714285714285714,
        "recall": 0.4,
        "f1-score": 0.47058823529411764,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.7,
        "recall": 0.8484848484848485,
        "f1-score": 0.7671232876712328,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5555555555555556,
        "recall": 0.5555555555555556,
        "f1-score": 0.5555555555555556,
        "support": 27.0
    },
    "accuracy": 0.6551724137931034,
    "macro avg": {
        "precision": 0.7067460317460317,
        "recall": 0.6652958152958153,
        "f1-score": 0.6790860003994572,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6497536945812807,
        "recall": 0.6551724137931034,
        "f1-score": 0.6458433524203621,
        "support": 87.0
    }
}
```

## TF-IDF_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.6312
- **Accuracy:** 0.6322
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5,
        "recall": 0.5,
        "f1-score": 0.5,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6944444444444444,
        "recall": 0.7575757575757576,
        "f1-score": 0.7246376811594203,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.56,
        "recall": 0.5185185185185185,
        "f1-score": 0.5384615384615384,
        "support": 27.0
    },
    "accuracy": 0.632183908045977,
    "macro avg": {
        "precision": 0.6886111111111112,
        "recall": 0.6583092833092833,
        "f1-score": 0.6715440356744704,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6326053639846743,
        "recall": 0.632183908045977,
        "f1-score": 0.631184407796102,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.6167
- **Accuracy:** 0.6207
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5,
        "recall": 0.4,
        "f1-score": 0.4444444444444444,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6756756756756757,
        "recall": 0.7575757575757576,
        "f1-score": 0.7142857142857143,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5357142857142857,
        "recall": 0.5555555555555556,
        "f1-score": 0.5454545454545454,
        "support": 27.0
    },
    "accuracy": 0.6206896551724138,
    "macro avg": {
        "precision": 0.6778474903474903,
        "recall": 0.6425685425685426,
        "f1-score": 0.6568154068154068,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6179492300181956,
        "recall": 0.6206896551724138,
        "f1-score": 0.6166566511394097,
        "support": 87.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.6129
- **Accuracy:** 0.6207
- **Best Parameters:** {'classifier__max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6875,
        "recall": 0.55,
        "f1-score": 0.6111111111111112,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5652173913043478,
        "recall": 0.7878787878787878,
        "f1-score": 0.6582278481012658,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5789473684210527,
        "recall": 0.4074074074074074,
        "f1-score": 0.4782608695652174,
        "support": 27.0
    },
    "accuracy": 0.6206896551724138,
    "macro avg": {
        "precision": 0.7079161899313501,
        "recall": 0.650607263107263,
        "f1-score": 0.6676691879636293,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6325718719587574,
        "recall": 0.6206896551724138,
        "f1-score": 0.6128542890731417,
        "support": 87.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.6076
- **Accuracy:** 0.6092
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5,
        "recall": 0.5,
        "f1-score": 0.5,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6571428571428571,
        "recall": 0.696969696969697,
        "f1-score": 0.6764705882352942,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.56,
        "recall": 0.5185185185185185,
        "f1-score": 0.5384615384615384,
        "support": 27.0
    },
    "accuracy": 0.6091954022988506,
    "macro avg": {
        "precision": 0.6435714285714286,
        "recall": 0.6431577681577682,
        "f1-score": 0.6430187459599224,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6069622331691298,
        "recall": 0.6091954022988506,
        "f1-score": 0.6076090913819109,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.5621
- **Accuracy:** 0.5747
- **Best Parameters:** {'classifier__max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.7142857142857143,
        "recall": 0.7142857142857143,
        "f1-score": 0.7142857142857143,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.75,
        "recall": 0.3,
        "f1-score": 0.42857142857142855,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5217391304347826,
        "recall": 0.7272727272727273,
        "f1-score": 0.6075949367088608,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5769230769230769,
        "recall": 0.5555555555555556,
        "f1-score": 0.5660377358490566,
        "support": 27.0
    },
    "accuracy": 0.5747126436781609,
    "macro avg": {
        "precision": 0.6407369804108936,
        "recall": 0.5742784992784993,
        "f1-score": 0.579122453853765,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.606831199784723,
        "recall": 0.5747126436781609,
        "f1-score": 0.5621273603533965,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.5495
- **Accuracy:** 0.5517
- **Best Parameters:** {'classifier__n_neighbors': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6666666666666666,
        "recall": 0.8571428571428571,
        "f1-score": 0.75,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.391304347826087,
        "recall": 0.45,
        "f1-score": 0.4186046511627907,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6176470588235294,
        "recall": 0.6363636363636364,
        "f1-score": 0.6268656716417911,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5714285714285714,
        "recall": 0.4444444444444444,
        "f1-score": 0.5,
        "support": 27.0
    },
    "accuracy": 0.5517241379310345,
    "macro avg": {
        "precision": 0.5617616611862136,
        "recall": 0.5969877344877346,
        "f1-score": 0.5738675807011455,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5552146895739805,
        "recall": 0.5517241379310345,
        "f1-score": 0.5495248297406313,
        "support": 87.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.5478
- **Accuracy:** 0.5632
- **Best Parameters:** {'classifier__max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.4166666666666667,
        "recall": 0.25,
        "f1-score": 0.3125,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5853658536585366,
        "recall": 0.7272727272727273,
        "f1-score": 0.6486486486486487,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5185185185185185,
        "recall": 0.5185185185185185,
        "f1-score": 0.5185185185185185,
        "support": 27.0
    },
    "accuracy": 0.5632183908045977,
    "macro avg": {
        "precision": 0.5944234739966447,
        "recall": 0.5882335257335257,
        "f1-score": 0.5842025060775061,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5477058218858051,
        "recall": 0.5632183908045977,
        "f1-score": 0.5477632805219012,
        "support": 87.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.4071
- **Accuracy:** 0.4483
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.4,
        "recall": 0.8571428571428571,
        "f1-score": 0.5454545454545454,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.4,
        "recall": 0.3,
        "f1-score": 0.34285714285714286,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4791666666666667,
        "recall": 0.696969696969697,
        "f1-score": 0.5679012345679012,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.4444444444444444,
        "recall": 0.14814814814814814,
        "f1-score": 0.2222222222222222,
        "support": 27.0
    },
    "accuracy": 0.4482758620689655,
    "macro avg": {
        "precision": 0.4309027777777778,
        "recall": 0.5005651755651755,
        "f1-score": 0.41960878627545295,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.44382183908045975,
        "recall": 0.4482758620689655,
        "f1-score": 0.4070812116789128,
        "support": 87.0
    }
}
```

## GloVe_SVM_Enhanced

- **Weighted F1 Score:** 0.6269
- **Accuracy:** 0.6437
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.75,
        "recall": 0.3,
        "f1-score": 0.42857142857142855,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6176470588235294,
        "recall": 0.6363636363636364,
        "f1-score": 0.6268656716417911,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5897435897435898,
        "recall": 0.8518518518518519,
        "f1-score": 0.696969696969697,
        "support": 27.0
    },
    "accuracy": 0.6436781609195402,
    "macro avg": {
        "precision": 0.7393476621417798,
        "recall": 0.6613395863395863,
        "f1-score": 0.66887093006496,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6701773547615333,
        "recall": 0.6436781609195402,
        "f1-score": 0.6268702990267582,
        "support": 87.0
    }
}
```

## GloVe_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.5878
- **Accuracy:** 0.5977
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.75,
        "recall": 0.3,
        "f1-score": 0.42857142857142855,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5227272727272727,
        "recall": 0.696969696969697,
        "f1-score": 0.5974025974025974,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5862068965517241,
        "recall": 0.6296296296296297,
        "f1-score": 0.6071428571428571,
        "support": 27.0
    },
    "accuracy": 0.5977011494252874,
    "macro avg": {
        "precision": 0.7147335423197492,
        "recall": 0.6209355459355459,
        "f1-score": 0.6390484515484516,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6330757035275465,
        "recall": 0.5977011494252874,
        "f1-score": 0.5878173550587343,
        "support": 87.0
    }
}
```

## GloVe_KNN_Enhanced

- **Weighted F1 Score:** 0.5521
- **Accuracy:** 0.5517
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.3783783783783784,
        "recall": 0.7,
        "f1-score": 0.49122807017543857,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6129032258064516,
        "recall": 0.5757575757575758,
        "f1-score": 0.59375,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6923076923076923,
        "recall": 0.3333333333333333,
        "f1-score": 0.45,
        "support": 27.0
    },
    "accuracy": 0.5517241379310345,
    "macro avg": {
        "precision": 0.6708973241231306,
        "recall": 0.6165584415584415,
        "f1-score": 0.6145137483130905,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6147779507067606,
        "recall": 0.5517241379310345,
        "f1-score": 0.5520672398281291,
        "support": 87.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.5281
- **Accuracy:** 0.5287
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.38235294117647056,
        "recall": 0.65,
        "f1-score": 0.48148148148148145,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5454545454545454,
        "recall": 0.5454545454545454,
        "f1-score": 0.5454545454545454,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6428571428571429,
        "recall": 0.3333333333333333,
        "f1-score": 0.43902439024390244,
        "support": 27.0
    },
    "accuracy": 0.5287356321839081,
    "macro avg": {
        "precision": 0.6426661573720397,
        "recall": 0.596482683982684,
        "f1-score": 0.5972593350642131,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5747609388583019,
        "recall": 0.5287356321839081,
        "f1-score": 0.5281014554914191,
        "support": 87.0
    }
}
```

## GloVe_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.4630
- **Accuracy:** 0.4598
- **Best Parameters:** {'max_depth': 10}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8333333333333334,
        "recall": 0.7142857142857143,
        "f1-score": 0.7692307692307693,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.38461538461538464,
        "recall": 0.5,
        "f1-score": 0.43478260869565216,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5185185185185185,
        "recall": 0.42424242424242425,
        "f1-score": 0.4666666666666667,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.39285714285714285,
        "recall": 0.4074074074074074,
        "f1-score": 0.4,
        "support": 27.0
    },
    "accuracy": 0.45977011494252873,
    "macro avg": {
        "precision": 0.5323310948310949,
        "recall": 0.5114838864838865,
        "f1-score": 0.517670011148272,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.4740677585505172,
        "recall": 0.45977011494252873,
        "f1-score": 0.46299158113251065,
        "support": 87.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.4475
- **Accuracy:** 0.4483
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.75,
        "recall": 0.8571428571428571,
        "f1-score": 0.8,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.3076923076923077,
        "recall": 0.6,
        "f1-score": 0.4067796610169492,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5,
        "recall": 0.36363636363636365,
        "f1-score": 0.42105263157894735,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5625,
        "recall": 0.3333333333333333,
        "f1-score": 0.4186046511627907,
        "support": 27.0
    },
    "accuracy": 0.4482758620689655,
    "macro avg": {
        "precision": 0.5300480769230769,
        "recall": 0.5385281385281385,
        "f1-score": 0.5116092359396718,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.4953028293545535,
        "recall": 0.4482758620689655,
        "f1-score": 0.44750178900965054,
        "support": 87.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.4170
- **Accuracy:** 0.4368
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.2857142857142857,
        "recall": 0.1,
        "f1-score": 0.14814814814814814,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4523809523809524,
        "recall": 0.5757575757575758,
        "f1-score": 0.5066666666666667,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.38235294117647056,
        "recall": 0.48148148148148145,
        "f1-score": 0.4262295081967213,
        "support": 27.0
    },
    "accuracy": 0.4367816091954023,
    "macro avg": {
        "precision": 0.5301120448179271,
        "recall": 0.43216690716690714,
        "f1-score": 0.4520792625710659,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.43639524775427413,
        "recall": 0.4367816091954023,
        "f1-score": 0.41703527327797163,
        "support": 87.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.3845
- **Accuracy:** 0.4713
- **Best Parameters:** {'C': 1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4626865671641791,
        "recall": 0.9393939393939394,
        "f1-score": 0.62,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.42857142857142855,
        "recall": 0.2222222222222222,
        "f1-score": 0.2926829268292683,
        "support": 27.0
    },
    "accuracy": 0.47126436781609193,
    "macro avg": {
        "precision": 0.4728144989339019,
        "recall": 0.43326118326118324,
        "f1-score": 0.4099889135254989,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.38896649756145374,
        "recall": 0.47126436781609193,
        "f1-score": 0.38452124270459004,
        "support": 87.0
    }
}
```

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.3845
- **Accuracy:** 0.4713
- **Best Parameters:** {'C': 1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4626865671641791,
        "recall": 0.9393939393939394,
        "f1-score": 0.62,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.42857142857142855,
        "recall": 0.2222222222222222,
        "f1-score": 0.2926829268292683,
        "support": 27.0
    },
    "accuracy": 0.47126436781609193,
    "macro avg": {
        "precision": 0.4728144989339019,
        "recall": 0.43326118326118324,
        "f1-score": 0.4099889135254989,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.38896649756145374,
        "recall": 0.47126436781609193,
        "f1-score": 0.38452124270459004,
        "support": 87.0
    }
}
```

## Word2Vec_SVM_Enhanced

- **Weighted F1 Score:** 0.3664
- **Accuracy:** 0.4598
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4305555555555556,
        "recall": 0.9393939393939394,
        "f1-score": 0.5904761904761905,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5,
        "recall": 0.18518518518518517,
        "f1-score": 0.2702702702702703,
        "support": 27.0
    },
    "accuracy": 0.45977011494252873,
    "macro avg": {
        "precision": 0.4826388888888889,
        "recall": 0.424001924001924,
        "f1-score": 0.39700479700479696,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.39894636015325674,
        "recall": 0.45977011494252873,
        "f1-score": 0.3663669042979388,
        "support": 87.0
    }
}
```

## FastText_SVM_Enhanced

- **Weighted F1 Score:** 0.3664
- **Accuracy:** 0.4598
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4305555555555556,
        "recall": 0.9393939393939394,
        "f1-score": 0.5904761904761905,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5,
        "recall": 0.18518518518518517,
        "f1-score": 0.2702702702702703,
        "support": 27.0
    },
    "accuracy": 0.45977011494252873,
    "macro avg": {
        "precision": 0.4826388888888889,
        "recall": 0.424001924001924,
        "f1-score": 0.39700479700479696,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.39894636015325674,
        "recall": 0.45977011494252873,
        "f1-score": 0.3663669042979388,
        "support": 87.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.3265
- **Accuracy:** 0.3563
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.5,
        "recall": 0.2857142857142857,
        "f1-score": 0.36363636363636365,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.14285714285714285,
        "recall": 0.1,
        "f1-score": 0.11764705882352941,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4444444444444444,
        "recall": 0.24242424242424243,
        "f1-score": 0.3137254901960784,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.37254901960784315,
        "recall": 0.7037037037037037,
        "f1-score": 0.48717948717948717,
        "support": 27.0
    },
    "accuracy": 0.3563218390804598,
    "macro avg": {
        "precision": 0.3649626517273576,
        "recall": 0.33296055796055796,
        "f1-score": 0.32054709995886466,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.3572716442898998,
        "recall": 0.3563218390804598,
        "f1-score": 0.3264963569223204,
        "support": 87.0
    }
}
```

