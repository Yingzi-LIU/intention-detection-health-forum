# Experiment Results Summary

**Labels:** negatif, non, positif

## TF-IDF_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.8018
- **Accuracy:** 0.8276
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "negatif": {
        "precision": 0.75,
        "recall": 0.2727272727272727,
        "f1-score": 0.4,
        "support": 11.0
    },
    "non": {
        "precision": 0.8481012658227848,
        "recall": 0.9571428571428572,
        "f1-score": 0.8993288590604027,
        "support": 70.0
    },
    "positif": {
        "precision": 0.5,
        "recall": 0.3333333333333333,
        "f1-score": 0.4,
        "support": 6.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.699367088607595,
        "recall": 0.521067821067821,
        "f1-score": 0.5664429530201343,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8116906736505165,
        "recall": 0.8275862068965517,
        "f1-score": 0.8017588521175655,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7948
- **Accuracy:** 0.8391
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.6666666666666666,
        "recall": 0.36363636363636365,
        "f1-score": 0.47058823529411764,
        "support": 11.0
    },
    "non": {
        "precision": 0.8518518518518519,
        "recall": 0.9857142857142858,
        "f1-score": 0.9139072847682119,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8390804597701149,
        "recall": 0.9012345679012346,
        "f1-score": 0.8690476190476191,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.7592592592592593,
        "recall": 0.6746753246753248,
        "f1-score": 0.6922477600311647,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8267032464563329,
        "recall": 0.9012345679012346,
        "f1-score": 0.8537034632346929,
        "support": 81.0
    }
}
```

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.7885
- **Accuracy:** 0.8391
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.6,
        "recall": 0.2727272727272727,
        "f1-score": 0.375,
        "support": 11.0
    },
    "non": {
        "precision": 0.8536585365853658,
        "recall": 1.0,
        "f1-score": 0.9210526315789473,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8390804597701149,
        "recall": 0.9012345679012346,
        "f1-score": 0.8690476190476191,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.7268292682926829,
        "recall": 0.6363636363636364,
        "f1-score": 0.6480263157894737,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.819211080999699,
        "recall": 0.9012345679012346,
        "f1-score": 0.8468973359324237,
        "support": 81.0
    }
}
```

## TF-IDF_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7876
- **Accuracy:** 0.8276
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.5,
        "recall": 0.36363636363636365,
        "f1-score": 0.42105263157894735,
        "support": 11.0
    },
    "non": {
        "precision": 0.8607594936708861,
        "recall": 0.9714285714285714,
        "f1-score": 0.912751677852349,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8275862068965517,
        "recall": 0.8888888888888888,
        "f1-score": 0.8571428571428571,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.6803797468354431,
        "recall": 0.6675324675324675,
        "f1-score": 0.6669021547156482,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8117674636661978,
        "recall": 0.8888888888888888,
        "f1-score": 0.8459777332967019,
        "support": 81.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7857
- **Accuracy:** 0.8276
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "negatif": {
        "precision": 0.5714285714285714,
        "recall": 0.36363636363636365,
        "f1-score": 0.4444444444444444,
        "support": 11.0
    },
    "non": {
        "precision": 0.85,
        "recall": 0.9714285714285714,
        "f1-score": 0.9066666666666666,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8275862068965517,
        "recall": 0.8888888888888888,
        "f1-score": 0.8571428571428571,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.7107142857142856,
        "recall": 0.6675324675324675,
        "f1-score": 0.6755555555555555,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8121693121693122,
        "recall": 0.8888888888888888,
        "f1-score": 0.8438957475994513,
        "support": 81.0
    }
}
```

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.7857
- **Accuracy:** 0.8276
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.5714285714285714,
        "recall": 0.36363636363636365,
        "f1-score": 0.4444444444444444,
        "support": 11.0
    },
    "non": {
        "precision": 0.85,
        "recall": 0.9714285714285714,
        "f1-score": 0.9066666666666666,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8275862068965517,
        "recall": 0.8888888888888888,
        "f1-score": 0.8571428571428571,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.7107142857142856,
        "recall": 0.6675324675324675,
        "f1-score": 0.6755555555555555,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8121693121693122,
        "recall": 0.8888888888888888,
        "f1-score": 0.8438957475994513,
        "support": 81.0
    }
}
```

## BoW_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.7776
- **Accuracy:** 0.8046
- **Best Parameters:** {'classifier__alpha': 0.5}
```json
{
    "negatif": {
        "precision": 0.5,
        "recall": 0.2727272727272727,
        "f1-score": 0.35294117647058826,
        "support": 11.0
    },
    "non": {
        "precision": 0.8461538461538461,
        "recall": 0.9428571428571428,
        "f1-score": 0.8918918918918919,
        "support": 70.0
    },
    "positif": {
        "precision": 0.3333333333333333,
        "recall": 0.16666666666666666,
        "f1-score": 0.2222222222222222,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.5598290598290598,
        "recall": 0.46075036075036074,
        "f1-score": 0.48901843019490077,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7670203359858532,
        "recall": 0.8045977011494253,
        "f1-score": 0.7775645828384166,
        "support": 87.0
    }
}
```

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.7705
- **Accuracy:** 0.8161
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.75,
        "recall": 0.2727272727272727,
        "f1-score": 0.4,
        "support": 11.0
    },
    "non": {
        "precision": 0.8292682926829268,
        "recall": 0.9714285714285714,
        "f1-score": 0.8947368421052632,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8160919540229885,
    "macro avg": {
        "precision": 0.5264227642276422,
        "recall": 0.41471861471861465,
        "f1-score": 0.43157894736842106,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7620549481356882,
        "recall": 0.8160919540229885,
        "f1-score": 0.7704779189352693,
        "support": 87.0
    }
}
```

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7693
- **Accuracy:** 0.8161
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.5,
        "recall": 0.2727272727272727,
        "f1-score": 0.35294117647058826,
        "support": 11.0
    },
    "non": {
        "precision": 0.8395061728395061,
        "recall": 0.9714285714285714,
        "f1-score": 0.9006622516556292,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8160919540229885,
        "recall": 0.8765432098765432,
        "f1-score": 0.8452380952380952,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.6697530864197531,
        "recall": 0.622077922077922,
        "f1-score": 0.6268017140631087,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7934003962810547,
        "recall": 0.8765432098765432,
        "f1-score": 0.8262803772477841,
        "support": 81.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7611
- **Accuracy:** 0.7586
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "negatif": {
        "precision": 0.4166666666666667,
        "recall": 0.45454545454545453,
        "f1-score": 0.43478260869565216,
        "support": 11.0
    },
    "non": {
        "precision": 0.8695652173913043,
        "recall": 0.8571428571428571,
        "f1-score": 0.8633093525179856,
        "support": 70.0
    },
    "positif": {
        "precision": 0.16666666666666666,
        "recall": 0.16666666666666666,
        "f1-score": 0.16666666666666666,
        "support": 6.0
    },
    "accuracy": 0.7586206896551724,
    "macro avg": {
        "precision": 0.48429951690821255,
        "recall": 0.49278499278499277,
        "f1-score": 0.4882528759601015,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7638264201232717,
        "recall": 0.7586206896551724,
        "f1-score": 0.7610834870334616,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7551
- **Accuracy:** 0.7471
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "negatif": {
        "precision": 0.35714285714285715,
        "recall": 0.45454545454545453,
        "f1-score": 0.4,
        "support": 11.0
    },
    "non": {
        "precision": 0.8805970149253731,
        "recall": 0.8428571428571429,
        "f1-score": 0.8613138686131386,
        "support": 70.0
    },
    "positif": {
        "precision": 0.16666666666666666,
        "recall": 0.16666666666666666,
        "f1-score": 0.16666666666666666,
        "support": 6.0
    },
    "accuracy": 0.7471264367816092,
    "macro avg": {
        "precision": 0.4681355129116323,
        "recall": 0.488023088023088,
        "f1-score": 0.47599351175993515,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.76517658015342,
        "recall": 0.7471264367816092,
        "f1-score": 0.755080124171491,
        "support": 87.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.7462
- **Accuracy:** 0.8161
- **Best Parameters:** {'classifier__n_neighbors': 5}
```json
{
    "negatif": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "non": {
        "precision": 0.8235294117647058,
        "recall": 1.0,
        "f1-score": 0.9032258064516129,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8160919540229885,
        "recall": 0.8765432098765432,
        "f1-score": 0.8452380952380952,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.6617647058823529,
        "recall": 0.5454545454545454,
        "f1-score": 0.5285359801488834,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7795933188090051,
        "recall": 0.8765432098765432,
        "f1-score": 0.8014581993076616,
        "support": 81.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.7320
- **Accuracy:** 0.7701
- **Best Parameters:** {'classifier__n_neighbors': 5}
```json
{
    "negatif": {
        "precision": 0.2222222222222222,
        "recall": 0.18181818181818182,
        "f1-score": 0.2,
        "support": 11.0
    },
    "non": {
        "precision": 0.8333333333333334,
        "recall": 0.9285714285714286,
        "f1-score": 0.8783783783783784,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.7701149425287356,
        "recall": 0.8271604938271605,
        "f1-score": 0.7976190476190477,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.5277777777777778,
        "recall": 0.5551948051948052,
        "f1-score": 0.5391891891891892,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7503429355281207,
        "recall": 0.8271604938271605,
        "f1-score": 0.786252919586253,
        "support": 81.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.7247
- **Accuracy:** 0.7586
- **Best Parameters:** {'classifier__n_neighbors': 5}
```json
{
    "negatif": {
        "precision": 0.2,
        "recall": 0.18181818181818182,
        "f1-score": 0.19047619047619047,
        "support": 11.0
    },
    "non": {
        "precision": 0.8311688311688312,
        "recall": 0.9142857142857143,
        "f1-score": 0.8707482993197279,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.7586206896551724,
        "recall": 0.8148148148148148,
        "f1-score": 0.7857142857142857,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.5155844155844156,
        "recall": 0.548051948051948,
        "f1-score": 0.5306122448979591,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7454545454545456,
        "recall": 0.8148148148148148,
        "f1-score": 0.7783656672545561,
        "support": 81.0
    }
}
```

## TF-IDF_ngram_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.7060
- **Accuracy:** 0.7816
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "negatif": {
        "precision": 0.8,
        "recall": 0.9714285714285714,
        "f1-score": 0.8774193548387097,
        "support": 70.0
    },
    "non": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "micro avg": {
        "precision": 0.7816091954022989,
        "recall": 0.8947368421052632,
        "f1-score": 0.8343558282208589,
        "support": 76.0
    },
    "macro avg": {
        "precision": 0.4,
        "recall": 0.4857142857142857,
        "f1-score": 0.43870967741935485,
        "support": 76.0
    },
    "weighted avg": {
        "precision": 0.7368421052631579,
        "recall": 0.8947368421052632,
        "f1-score": 0.8081494057724958,
        "support": 76.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.8051
- **Accuracy:** 0.8276
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "negatif": {
        "precision": 0.42857142857142855,
        "recall": 0.2727272727272727,
        "f1-score": 0.3333333333333333,
        "support": 11.0
    },
    "non": {
        "precision": 0.8589743589743589,
        "recall": 0.9571428571428572,
        "f1-score": 0.9054054054054054,
        "support": 70.0
    },
    "positif": {
        "precision": 1.0,
        "recall": 0.3333333333333333,
        "f1-score": 0.5,
        "support": 6.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.7625152625152625,
        "recall": 0.521067821067821,
        "f1-score": 0.5795795795795796,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8142815039366762,
        "recall": 0.8275862068965517,
        "f1-score": 0.8051154602878741,
        "support": 87.0
    }
}
```

## GloVe_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7582
- **Accuracy:** 0.7816
- **Best Parameters:** {'max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.2727272727272727,
        "f1-score": 0.3,
        "support": 11.0
    },
    "non": {
        "precision": 0.8311688311688312,
        "recall": 0.9142857142857143,
        "f1-score": 0.8707482993197279,
        "support": 70.0
    },
    "positif": {
        "precision": 1.0,
        "recall": 0.16666666666666666,
        "f1-score": 0.2857142857142857,
        "support": 6.0
    },
    "accuracy": 0.7816091954022989,
    "macro avg": {
        "precision": 0.7215007215007215,
        "recall": 0.45122655122655125,
        "f1-score": 0.4854875283446711,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7798676419366074,
        "recall": 0.7816091954022989,
        "f1-score": 0.7582375478927201,
        "support": 87.0
    }
}
```

## GloVe_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7540
- **Accuracy:** 0.7816
- **Best Parameters:** {'C': 1, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.16666666666666666,
        "recall": 0.09090909090909091,
        "f1-score": 0.11764705882352941,
        "support": 11.0
    },
    "non": {
        "precision": 0.8441558441558441,
        "recall": 0.9285714285714286,
        "f1-score": 0.8843537414965986,
        "support": 70.0
    },
    "positif": {
        "precision": 0.5,
        "recall": 0.3333333333333333,
        "f1-score": 0.4,
        "support": 6.0
    },
    "accuracy": 0.7816091954022989,
    "macro avg": {
        "precision": 0.5036075036075036,
        "recall": 0.4509379509379509,
        "f1-score": 0.4673336001067094,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7347614071752002,
        "recall": 0.7816091954022989,
        "f1-score": 0.7540101097910429,
        "support": 87.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.7506
- **Accuracy:** 0.8046
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8292682926829268,
        "recall": 0.9714285714285714,
        "f1-score": 0.8947368421052632,
        "support": 70.0
    },
    "positif": {
        "precision": 0.6666666666666666,
        "recall": 0.3333333333333333,
        "f1-score": 0.4444444444444444,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.4986449864498645,
        "recall": 0.43492063492063493,
        "f1-score": 0.44639376218323584,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7132043734230445,
        "recall": 0.8045977011494253,
        "f1-score": 0.7505545472877597,
        "support": 87.0
    }
}
```

## GloVe_KNN_Enhanced

- **Weighted F1 Score:** 0.7353
- **Accuracy:** 0.7586
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "negatif": {
        "precision": 0.1111111111111111,
        "recall": 0.09090909090909091,
        "f1-score": 0.1,
        "support": 11.0
    },
    "non": {
        "precision": 0.8421052631578947,
        "recall": 0.9142857142857143,
        "f1-score": 0.8767123287671232,
        "support": 70.0
    },
    "positif": {
        "precision": 0.5,
        "recall": 0.16666666666666666,
        "f1-score": 0.25,
        "support": 6.0
    },
    "accuracy": 0.7586206896551724,
    "macro avg": {
        "precision": 0.4844054580896686,
        "recall": 0.39062049062049065,
        "f1-score": 0.4089041095890411,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7260872487732741,
        "recall": 0.7586206896551724,
        "f1-score": 0.7352857817666509,
        "support": 87.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7221
- **Accuracy:** 0.8046
- **Best Parameters:** {'max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.813953488372093,
        "recall": 1.0,
        "f1-score": 0.8974358974358975,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 0.8641975308641975,
        "f1-score": 0.8333333333333334,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.4069767441860465,
        "recall": 0.5,
        "f1-score": 0.44871794871794873,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7034165948894631,
        "recall": 0.8641975308641975,
        "f1-score": 0.7755618866729979,
        "support": 81.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7212
- **Accuracy:** 0.7586
- **Best Parameters:** {'max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.2222222222222222,
        "recall": 0.18181818181818182,
        "f1-score": 0.2,
        "support": 11.0
    },
    "non": {
        "precision": 0.8205128205128205,
        "recall": 0.9142857142857143,
        "f1-score": 0.8648648648648649,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.7586206896551724,
        "recall": 0.8148148148148148,
        "f1-score": 0.7857142857142857,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.5213675213675213,
        "recall": 0.548051948051948,
        "f1-score": 0.5324324324324324,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7392634800042207,
        "recall": 0.8148148148148148,
        "f1-score": 0.7745745745745747,
        "support": 81.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "macro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "weighted avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    }
}
```

## Word2Vec_SVM_Enhanced

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "macro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "weighted avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    }
}
```

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "macro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "weighted avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    }
}
```

## FastText_SVM_Enhanced

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "macro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "weighted avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    }
}
```

## GloVe_SVM_Enhanced

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "macro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "weighted avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    }
}
```

