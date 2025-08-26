# Experiment Results Summary

**Labels:** negatif, non, positif

## BoW_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.8112
- **Accuracy:** 0.8276
- **Best Parameters:** {'classifier__alpha': 0.5}
```json
{
    "negatif": {
        "precision": 0.5714285714285714,
        "recall": 0.36363636363636365,
        "f1-score": 0.4444444444444444,
        "support": 11.0
    },
    "non": {
        "precision": 0.868421052631579,
        "recall": 0.9428571428571428,
        "f1-score": 0.9041095890410958,
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
        "precision": 0.6466165413533834,
        "recall": 0.5466089466089465,
        "f1-score": 0.5828513444951801,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8054619306887909,
        "recall": 0.8275862068965517,
        "f1-score": 0.8112248289858116,
        "support": 87.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.8043
- **Accuracy:** 0.8506
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.8,
        "recall": 0.36363636363636365,
        "f1-score": 0.5,
        "support": 11.0
    },
    "non": {
        "precision": 0.8536585365853658,
        "recall": 1.0,
        "f1-score": 0.9210526315789473,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8505747126436781,
        "recall": 0.9135802469135802,
        "f1-score": 0.8809523809523809,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.826829268292683,
        "recall": 0.6818181818181819,
        "f1-score": 0.7105263157894737,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8463715748268594,
        "recall": 0.9135802469135802,
        "f1-score": 0.8638726445743989,
        "support": 81.0
    }
}
```

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

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7779
- **Accuracy:** 0.8276
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.6,
        "recall": 0.2727272727272727,
        "f1-score": 0.375,
        "support": 11.0
    },
    "non": {
        "precision": 0.8414634146341463,
        "recall": 0.9857142857142858,
        "f1-score": 0.9078947368421053,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8275862068965517,
        "recall": 0.8888888888888888,
        "f1-score": 0.8571428571428571,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.7207317073170731,
        "recall": 0.6292207792207792,
        "f1-score": 0.6414473684210527,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8086720867208672,
        "recall": 0.8888888888888888,
        "f1-score": 0.8355263157894737,
        "support": 81.0
    }
}
```

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7779
- **Accuracy:** 0.8276
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.6,
        "recall": 0.2727272727272727,
        "f1-score": 0.375,
        "support": 11.0
    },
    "non": {
        "precision": 0.8414634146341463,
        "recall": 0.9857142857142858,
        "f1-score": 0.9078947368421053,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8275862068965517,
        "recall": 0.8888888888888888,
        "f1-score": 0.8571428571428571,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.7207317073170731,
        "recall": 0.6292207792207792,
        "f1-score": 0.6414473684210527,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8086720867208672,
        "recall": 0.8888888888888888,
        "f1-score": 0.8355263157894737,
        "support": 81.0
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

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7461
- **Accuracy:** 0.7356
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
        "precision": 0.8656716417910447,
        "recall": 0.8285714285714286,
        "f1-score": 0.8467153284671532,
        "support": 70.0
    },
    "positif": {
        "precision": 0.125,
        "recall": 0.16666666666666666,
        "f1-score": 0.14285714285714285,
        "support": 6.0
    },
    "accuracy": 0.735632183908046,
    "macro avg": {
        "precision": 0.4691127694859038,
        "recall": 0.4832611832611833,
        "f1-score": 0.47478502667331607,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7578200949276604,
        "recall": 0.735632183908046,
        "f1-score": 0.7460899373045491,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.7394
- **Accuracy:** 0.7816
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "negatif": {
        "precision": 0.25,
        "recall": 0.18181818181818182,
        "f1-score": 0.21052631578947367,
        "support": 11.0
    },
    "non": {
        "precision": 0.8354430379746836,
        "recall": 0.9428571428571428,
        "f1-score": 0.8859060402684564,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.7816091954022989,
        "recall": 0.8395061728395061,
        "f1-score": 0.8095238095238095,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.5427215189873418,
        "recall": 0.5623376623376624,
        "f1-score": 0.548216178028965,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7559384278793562,
        "recall": 0.8395061728395061,
        "f1-score": 0.7941878060799525,
        "support": 81.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.7289
- **Accuracy:** 0.7816
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "negatif": {
        "precision": 0.16666666666666666,
        "recall": 0.09090909090909091,
        "f1-score": 0.11764705882352941,
        "support": 11.0
    },
    "non": {
        "precision": 0.8271604938271605,
        "recall": 0.9571428571428572,
        "f1-score": 0.8874172185430463,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.7816091954022989,
        "recall": 0.8395061728395061,
        "f1-score": 0.8095238095238095,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.49691358024691357,
        "recall": 0.5240259740259741,
        "f1-score": 0.5025321386832878,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7374638012498095,
        "recall": 0.8395061728395061,
        "f1-score": 0.782880530186075,
        "support": 81.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'classifier__n_neighbors': 5}
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

## TF-IDF_ngram_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.7001
- **Accuracy:** 0.7701
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.7976190476190477,
        "recall": 0.9571428571428572,
        "f1-score": 0.8701298701298701,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.7701149425287356,
    "macro avg": {
        "precision": 0.26587301587301587,
        "recall": 0.3190476190476191,
        "f1-score": 0.29004329004329005,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6417624521072797,
        "recall": 0.7701149425287356,
        "f1-score": 0.7001044932079414,
        "support": 87.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.7654
- **Accuracy:** 0.7701
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "negatif": {
        "precision": 0.16666666666666666,
        "recall": 0.18181818181818182,
        "f1-score": 0.17391304347826086,
        "support": 11.0
    },
    "non": {
        "precision": 0.863013698630137,
        "recall": 0.9,
        "f1-score": 0.8811188811188811,
        "support": 70.0
    },
    "positif": {
        "precision": 1.0,
        "recall": 0.3333333333333333,
        "f1-score": 0.5,
        "support": 6.0
    },
    "accuracy": 0.7701149425287356,
    "macro avg": {
        "precision": 0.6765601217656011,
        "recall": 0.4717171717171717,
        "f1-score": 0.518343974865714,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7844171521545164,
        "recall": 0.7701149425287356,
        "f1-score": 0.7654179903055466,
        "support": 87.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7635
- **Accuracy:** 0.8161
- **Best Parameters:** {'max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "non": {
        "precision": 0.8313253012048193,
        "recall": 0.9857142857142858,
        "f1-score": 0.9019607843137255,
        "support": 70.0
    },
    "positif": {
        "precision": 1.0,
        "recall": 0.16666666666666666,
        "f1-score": 0.2857142857142857,
        "support": 6.0
    },
    "accuracy": 0.8160919540229885,
    "macro avg": {
        "precision": 0.7215528781793843,
        "recall": 0.4144300144300144,
        "f1-score": 0.4435107376283847,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7799935373678621,
        "recall": 0.8160919540229885,
        "f1-score": 0.7634824044560352,
        "support": 87.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7530
- **Accuracy:** 0.8046
- **Best Parameters:** {'max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "non": {
        "precision": 0.8192771084337349,
        "recall": 0.9714285714285714,
        "f1-score": 0.8888888888888888,
        "support": 70.0
    },
    "positif": {
        "precision": 1.0,
        "recall": 0.16666666666666666,
        "f1-score": 0.2857142857142857,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.7175368139223561,
        "recall": 0.4096681096681097,
        "f1-score": 0.4391534391534391,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7702995891612426,
        "recall": 0.8045977011494253,
        "f1-score": 0.752964787447546,
        "support": 87.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.7337
- **Accuracy:** 0.7816
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8271604938271605,
        "recall": 0.9571428571428572,
        "f1-score": 0.8874172185430463,
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
        "precision": 0.6090534979423868,
        "recall": 0.3746031746031746,
        "f1-score": 0.39104383475244403,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.734496949056336,
        "recall": 0.7816091954022989,
        "f1-score": 0.7337182874976892,
        "support": 87.0
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

