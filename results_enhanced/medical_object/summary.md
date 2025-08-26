# Experiment Results Summary

**Labels:** NA_CATEGORY, diagnostique, symptome, traitement

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.6640
- **Accuracy:** 0.6667
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.7692307692307693,
        "recall": 0.5,
        "f1-score": 0.6060606060606061,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6190476190476191,
        "recall": 0.7878787878787878,
        "f1-score": 0.6933333333333334,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6153846153846154,
        "recall": 0.5925925925925926,
        "f1-score": 0.6037735849056604,
        "support": 27.0
    },
    "accuracy": 0.6666666666666666,
    "macro avg": {
        "precision": 0.7509157509157509,
        "recall": 0.6844035594035593,
        "f1-score": 0.7065611118441307,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6830870279146142,
        "recall": 0.6666666666666666,
        "f1-score": 0.6639613491402692,
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
        "precision": 0.75,
        "recall": 0.45,
        "f1-score": 0.5625,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6363636363636364,
        "recall": 0.8484848484848485,
        "f1-score": 0.7272727272727273,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6,
        "recall": 0.5555555555555556,
        "f1-score": 0.5769230769230769,
        "support": 27.0
    },
    "accuracy": 0.6666666666666666,
    "macro avg": {
        "precision": 0.7465909090909091,
        "recall": 0.6777958152958152,
        "f1-score": 0.6974431818181819,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6804597701149425,
        "recall": 0.6666666666666666,
        "f1-score": 0.6584880636604774,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.6505
- **Accuracy:** 0.6552
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

- **Weighted F1 Score:** 0.6490
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
        "precision": 0.675,
        "recall": 0.8181818181818182,
        "f1-score": 0.7397260273972602,
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
        "precision": 0.7183531746031746,
        "recall": 0.6702200577200577,
        "f1-score": 0.6869425676839054,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6566912972085386,
        "recall": 0.6551724137931034,
        "f1-score": 0.6489739386179965,
        "support": 87.0
    }
}
```

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.6342
- **Accuracy:** 0.6322
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
        "precision": 0.5789473684210527,
        "recall": 0.55,
        "f1-score": 0.5641025641025641,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6666666666666666,
        "recall": 0.6666666666666666,
        "f1-score": 0.6666666666666666,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5517241379310345,
        "recall": 0.5925925925925926,
        "f1-score": 0.5714285714285714,
        "support": 27.0
    },
    "accuracy": 0.632183908045977,
    "macro avg": {
        "precision": 0.6993345432546885,
        "recall": 0.666600529100529,
        "f1-score": 0.6813186813186813,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6376494148569998,
        "recall": 0.632183908045977,
        "f1-score": 0.6341627720938066,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6247
- **Accuracy:** 0.6322
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
        "precision": 0.6341463414634146,
        "recall": 0.7878787878787878,
        "f1-score": 0.7027027027027027,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5555555555555556,
        "recall": 0.5555555555555556,
        "f1-score": 0.5555555555555556,
        "support": 27.0
    },
    "accuracy": 0.632183908045977,
    "macro avg": {
        "precision": 0.7012716281008964,
        "recall": 0.6501443001443001,
        "f1-score": 0.6665459165459167,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.634879558344655,
        "recall": 0.632183908045977,
        "f1-score": 0.6246861764103143,
        "support": 87.0
    }
}
```

## TF-IDF_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.6184
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
        "recall": 0.5,
        "f1-score": 0.5,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6756756756756757,
        "recall": 0.7575757575757576,
        "f1-score": 0.7142857142857143,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5416666666666666,
        "recall": 0.48148148148148145,
        "f1-score": 0.5098039215686274,
        "support": 27.0
    },
    "accuracy": 0.6206896551724138,
    "macro avg": {
        "precision": 0.6793355855855855,
        "recall": 0.649050024050024,
        "f1-score": 0.6617916397328162,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6197965206585896,
        "recall": 0.6206896551724138,
        "f1-score": 0.6183640564979308,
        "support": 87.0
    }
}
```

## BoW_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.6178
- **Accuracy:** 0.6207
- **Best Parameters:** {'classifier__alpha': 0.5}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.47058823529411764,
        "recall": 0.4,
        "f1-score": 0.43243243243243246,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6944444444444444,
        "recall": 0.7575757575757576,
        "f1-score": 0.7246376811594203,
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
        "precision": 0.675186741363212,
        "recall": 0.6425685425685426,
        "f1-score": 0.6564003955308303,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6183070929521234,
        "recall": 0.6206896551724138,
        "f1-score": 0.6178218771921921,
        "support": 87.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.5837
- **Accuracy:** 0.5977
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
        "precision": 0.47058823529411764,
        "recall": 0.4,
        "f1-score": 0.43243243243243246,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6428571428571429,
        "recall": 0.8181818181818182,
        "f1-score": 0.72,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5238095238095238,
        "recall": 0.4074074074074074,
        "f1-score": 0.4583333333333333,
        "support": 27.0
    },
    "accuracy": 0.5977011494252874,
    "macro avg": {
        "precision": 0.6235994397759104,
        "recall": 0.6206830206830207,
        "f1-score": 0.6169771557271558,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.583550661643968,
        "recall": 0.5977011494252874,
        "f1-score": 0.5837200994097546,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.5832
- **Accuracy:** 0.5862
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
        "precision": 0.47058823529411764,
        "recall": 0.4,
        "f1-score": 0.43243243243243246,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6486486486486487,
        "recall": 0.7272727272727273,
        "f1-score": 0.6857142857142857,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.48148148148148145,
        "recall": 0.48148148148148145,
        "f1-score": 0.48148148148148145,
        "support": 27.0
    },
    "accuracy": 0.5862068965517241,
    "macro avg": {
        "precision": 0.650179591356062,
        "recall": 0.6164742664742665,
        "f1-score": 0.6306762806762807,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5841054035780203,
        "recall": 0.5862068965517241,
        "f1-score": 0.5832041211351556,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.5726
- **Accuracy:** 0.5862
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.75,
        "recall": 0.8571428571428571,
        "f1-score": 0.8,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.4444444444444444,
        "recall": 0.4,
        "f1-score": 0.42105263157894735,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6190476190476191,
        "recall": 0.7878787878787878,
        "f1-score": 0.6933333333333334,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5789473684210527,
        "recall": 0.4074074074074074,
        "f1-score": 0.4782608695652174,
        "support": 27.0
    },
    "accuracy": 0.5862068965517241,
    "macro avg": {
        "precision": 0.5981098579782791,
        "recall": 0.6131072631072632,
        "f1-score": 0.5981617086193746,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5770004513198705,
        "recall": 0.5862068965517241,
        "f1-score": 0.5725758173544806,
        "support": 87.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.5310
- **Accuracy:** 0.5402
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
        "precision": 0.42857142857142855,
        "recall": 0.3,
        "f1-score": 0.35294117647058826,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5348837209302325,
        "recall": 0.696969696969697,
        "f1-score": 0.6052631578947368,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5,
        "recall": 0.4444444444444444,
        "f1-score": 0.47058823529411764,
        "support": 27.0
    },
    "accuracy": 0.5402298850574713,
    "macro avg": {
        "precision": 0.6158637873754153,
        "recall": 0.5746392496392496,
        "f1-score": 0.5879673731840915,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5370412800244396,
        "recall": 0.5402298850574713,
        "f1-score": 0.5310336615450312,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.5104
- **Accuracy:** 0.5517
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5714285714285714,
        "recall": 0.2,
        "f1-score": 0.2962962962962963,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5,
        "recall": 0.9393939393939394,
        "f1-score": 0.6526315789473685,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6428571428571429,
        "recall": 0.3333333333333333,
        "f1-score": 0.43902439024390244,
        "support": 27.0
    },
    "accuracy": 0.5517241379310345,
    "macro avg": {
        "precision": 0.6785714285714285,
        "recall": 0.5110389610389611,
        "f1-score": 0.5288062481900736,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6009852216748769,
        "recall": 0.5517241379310345,
        "f1-score": 0.5104291455021097,
        "support": 87.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.4908
- **Accuracy:** 0.5402
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 1.0,
        "recall": 0.15,
        "f1-score": 0.2608695652173913,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.484375,
        "recall": 0.9393939393939394,
        "f1-score": 0.6391752577319587,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5625,
        "recall": 0.3333333333333333,
        "f1-score": 0.4186046511627907,
        "support": 27.0
    },
    "accuracy": 0.5402298850574713,
    "macro avg": {
        "precision": 0.76171875,
        "recall": 0.49853896103896106,
        "f1-score": 0.511480550346217,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6686422413793104,
        "recall": 0.5402298850574713,
        "f1-score": 0.49084378714720583,
        "support": 87.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.4634
- **Accuracy:** 0.4943
- **Best Parameters:** {'classifier__n_neighbors': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.42857142857142855,
        "recall": 0.8571428571428571,
        "f1-score": 0.5714285714285714,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5,
        "recall": 0.35,
        "f1-score": 0.4117647058823529,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.48,
        "recall": 0.7272727272727273,
        "f1-score": 0.5783132530120482,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6666666666666666,
        "recall": 0.2222222222222222,
        "f1-score": 0.3333333333333333,
        "support": 27.0
    },
    "accuracy": 0.4942528735632184,
    "macro avg": {
        "precision": 0.5188095238095238,
        "recall": 0.5391594516594517,
        "f1-score": 0.47370996591407644,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5383908045977012,
        "recall": 0.4942528735632184,
        "f1-score": 0.46344403985108784,
        "support": 87.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.5315
- **Accuracy:** 0.5287
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.375,
        "recall": 0.6,
        "f1-score": 0.46153846153846156,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5625,
        "recall": 0.5454545454545454,
        "f1-score": 0.5538461538461539,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5882352941176471,
        "recall": 0.37037037037037035,
        "f1-score": 0.45454545454545453,
        "support": 27.0
    },
    "accuracy": 0.5287356321839081,
    "macro avg": {
        "precision": 0.6314338235294118,
        "recall": 0.5932419432419431,
        "f1-score": 0.5982517482517482,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5625845165652468,
        "recall": 0.5287356321839081,
        "f1-score": 0.5315167591029661,
        "support": 87.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.5002
- **Accuracy:** 0.4943
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.7142857142857143,
        "f1-score": 0.8333333333333334,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.36363636363636365,
        "recall": 0.6,
        "f1-score": 0.4528301886792453,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5,
        "recall": 0.45454545454545453,
        "f1-score": 0.47619047619047616,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5789473684210527,
        "recall": 0.4074074074074074,
        "f1-score": 0.4782608695652174,
        "support": 27.0
    },
    "accuracy": 0.4942528735632184,
    "macro avg": {
        "precision": 0.6106459330143541,
        "recall": 0.544059644059644,
        "f1-score": 0.5601537169420681,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5333828301160424,
        "recall": 0.4942528735632184,
        "f1-score": 0.5001984632122394,
        "support": 87.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.4482
- **Accuracy:** 0.4483
- **Best Parameters:** {'max_depth': 10}
```json
{
    "NA_CATEGORY": {
        "precision": 0.5714285714285714,
        "recall": 0.5714285714285714,
        "f1-score": 0.5714285714285714,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.38095238095238093,
        "recall": 0.4,
        "f1-score": 0.3902439024390244,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5151515151515151,
        "recall": 0.5151515151515151,
        "f1-score": 0.5151515151515151,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.38461538461538464,
        "recall": 0.37037037037037035,
        "f1-score": 0.37735849056603776,
        "support": 27.0
    },
    "accuracy": 0.4482758620689655,
    "macro avg": {
        "precision": 0.463036963036963,
        "recall": 0.4642376142376142,
        "f1-score": 0.4635456198962872,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.4483179655593449,
        "recall": 0.4482758620689655,
        "f1-score": 0.44820180797774145,
        "support": 87.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.4049
- **Accuracy:** 0.4943
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
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
        "precision": 0.5,
        "recall": 0.2222222222222222,
        "f1-score": 0.3076923076923077,
        "support": 27.0
    },
    "accuracy": 0.4942528735632184,
    "macro avg": {
        "precision": 0.4906716417910448,
        "recall": 0.5046897546897547,
        "f1-score": 0.4626923076923077,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.41113398524618283,
        "recall": 0.4942528735632184,
        "f1-score": 0.4049336870026525,
        "support": 87.0
    }
}
```

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.4049
- **Accuracy:** 0.4943
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
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
        "precision": 0.5,
        "recall": 0.2222222222222222,
        "f1-score": 0.3076923076923077,
        "support": 27.0
    },
    "accuracy": 0.4942528735632184,
    "macro avg": {
        "precision": 0.4906716417910448,
        "recall": 0.5046897546897547,
        "f1-score": 0.4626923076923077,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.41113398524618283,
        "recall": 0.4942528735632184,
        "f1-score": 0.4049336870026525,
        "support": 87.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.3985
- **Accuracy:** 0.3908
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.34782608695652173,
        "recall": 0.4,
        "f1-score": 0.37209302325581395,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.42857142857142855,
        "recall": 0.36363636363636365,
        "f1-score": 0.39344262295081966,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.3125,
        "recall": 0.37037037037037035,
        "f1-score": 0.3389830508474576,
        "support": 27.0
    },
    "accuracy": 0.39080459770114945,
    "macro avg": {
        "precision": 0.5222243788819876,
        "recall": 0.4263588263588264,
        "f1-score": 0.45794785608170463,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.41996412508031694,
        "recall": 0.39080459770114945,
        "f1-score": 0.3984933159342962,
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

