# Experiment Results Summary

**Labels:** negatif, non, positif

## TF-IDF_ngram_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.8035
- **Accuracy:** 0.8276
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "negatif": {
        "precision": 0.6,
        "recall": 0.2727272727272727,
        "f1-score": 0.375,
        "support": 11.0
    },
    "non": {
        "precision": 0.8589743589743589,
        "recall": 0.9571428571428572,
        "f1-score": 0.9054054054054054,
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
        "precision": 0.652991452991453,
        "recall": 0.521067821067821,
        "f1-score": 0.560135135135135,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8014736221632772,
        "recall": 0.8275862068965517,
        "f1-score": 0.8034871077974528,
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
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.5061728395061729,
        "recall": 0.44978354978354984,
        "f1-score": 0.46149850668744313,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7696892294593444,
        "recall": 0.8390804597701149,
        "f1-score": 0.7948273623219555,
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
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.4845528455284553,
        "recall": 0.42424242424242425,
        "f1-score": 0.43201754385964913,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7627137650686852,
        "recall": 0.8390804597701149,
        "f1-score": 0.7884906231094979,
        "support": 87.0
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
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.4535864978902954,
        "recall": 0.44502164502164504,
        "f1-score": 0.44460143647709877,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7557835006547359,
        "recall": 0.8275862068965517,
        "f1-score": 0.7876344413452052,
        "support": 87.0
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
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.47380952380952374,
        "recall": 0.44502164502164504,
        "f1-score": 0.4503703703703703,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7561576354679803,
        "recall": 0.8275862068965517,
        "f1-score": 0.7856960408684547,
        "support": 87.0
    }
}
```

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7798
- **Accuracy:** 0.8161
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.5714285714285714,
        "recall": 0.36363636363636365,
        "f1-score": 0.4444444444444444,
        "support": 11.0
    },
    "non": {
        "precision": 0.8481012658227848,
        "recall": 0.9571428571428572,
        "f1-score": 0.8993288590604027,
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
        "precision": 0.47317661241711867,
        "recall": 0.4402597402597403,
        "f1-score": 0.44792443450161573,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7546299183138991,
        "recall": 0.8160919540229885,
        "f1-score": 0.779792057736978,
        "support": 87.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7779
- **Accuracy:** 0.8276
- **Best Parameters:** {'classifier__max_depth': 10}
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
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.48048780487804876,
        "recall": 0.4194805194805195,
        "f1-score": 0.4276315789473684,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.752901597981497,
        "recall": 0.8275862068965517,
        "f1-score": 0.7779038112522686,
        "support": 87.0
    }
}
```

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.7676
- **Accuracy:** 0.8276
- **Best Parameters:** {'classifier__C': 0.1, 'classifier__kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.6666666666666666,
        "recall": 0.18181818181818182,
        "f1-score": 0.2857142857142857,
        "support": 11.0
    },
    "non": {
        "precision": 0.8333333333333334,
        "recall": 1.0,
        "f1-score": 0.9090909090909091,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.5,
        "recall": 0.393939393939394,
        "f1-score": 0.39826839826839827,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7547892720306514,
        "recall": 0.8275862068965517,
        "f1-score": 0.767577250335871,
        "support": 87.0
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

## BoW_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.7547
- **Accuracy:** 0.8046
- **Best Parameters:** {'classifier__alpha': 1.0}
```json
{
    "negatif": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "non": {
        "precision": 0.8292682926829268,
        "recall": 0.9714285714285714,
        "f1-score": 0.8947368421052632,
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
        "precision": 0.55420054200542,
        "recall": 0.4096681096681097,
        "f1-score": 0.4236017393912131,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7534342584805158,
        "recall": 0.8045977011494253,
        "f1-score": 0.7546806893449362,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7535
- **Accuracy:** 0.7471
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "negatif": {
        "precision": 0.29411764705882354,
        "recall": 0.45454545454545453,
        "f1-score": 0.35714285714285715,
        "support": 11.0
    },
    "non": {
        "precision": 0.8805970149253731,
        "recall": 0.8428571428571429,
        "f1-score": 0.8613138686131386,
        "support": 70.0
    },
    "positif": {
        "precision": 0.3333333333333333,
        "recall": 0.16666666666666666,
        "f1-score": 0.2222222222222222,
        "support": 6.0
    },
    "accuracy": 0.7471264367816092,
    "macro avg": {
        "precision": 0.5026826651058433,
        "recall": 0.488023088023088,
        "f1-score": 0.4802263159927393,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7687021283037148,
        "recall": 0.7471264367816092,
        "f1-score": 0.7534928225841893,
        "support": 87.0
    }
}
```

## TF-IDF_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.7316
- **Accuracy:** 0.7931
- **Best Parameters:** {'classifier__alpha': 0.5}
```json
{
    "negatif": {
        "precision": 1.0,
        "recall": 0.09090909090909091,
        "f1-score": 0.16666666666666666,
        "support": 11.0
    },
    "non": {
        "precision": 0.8095238095238095,
        "recall": 0.9714285714285714,
        "f1-score": 0.8831168831168831,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.7931034482758621,
    "macro avg": {
        "precision": 0.6031746031746031,
        "recall": 0.3541125541125541,
        "f1-score": 0.3499278499278499,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7777777777777777,
        "recall": 0.7931034482758621,
        "f1-score": 0.7316266109369557,
        "support": 87.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.7221
- **Accuracy:** 0.7701
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "negatif": {
        "precision": 0.14285714285714285,
        "recall": 0.09090909090909091,
        "f1-score": 0.1111111111111111,
        "support": 11.0
    },
    "non": {
        "precision": 0.825,
        "recall": 0.9428571428571428,
        "f1-score": 0.88,
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
        "precision": 0.3226190476190476,
        "recall": 0.34458874458874456,
        "f1-score": 0.33037037037037037,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6818555008210181,
        "recall": 0.7701149425287356,
        "f1-score": 0.7220945083014049,
        "support": 87.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.7221
- **Accuracy:** 0.7701
- **Best Parameters:** {'classifier__n_neighbors': 5}
```json
{
    "negatif": {
        "precision": 0.14285714285714285,
        "recall": 0.09090909090909091,
        "f1-score": 0.1111111111111111,
        "support": 11.0
    },
    "non": {
        "precision": 0.825,
        "recall": 0.9428571428571428,
        "f1-score": 0.88,
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
        "precision": 0.3226190476190476,
        "recall": 0.34458874458874456,
        "f1-score": 0.33037037037037037,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6818555008210181,
        "recall": 0.7701149425287356,
        "f1-score": 0.7220945083014049,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.7085
- **Accuracy:** 0.7471
- **Best Parameters:** {'classifier__n_neighbors': 5}
```json
{
    "negatif": {
        "precision": 0.1111111111111111,
        "recall": 0.09090909090909091,
        "f1-score": 0.1,
        "support": 11.0
    },
    "non": {
        "precision": 0.8205128205128205,
        "recall": 0.9142857142857143,
        "f1-score": 0.8648648648648649,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.7471264367816092,
    "macro avg": {
        "precision": 0.31054131054131057,
        "recall": 0.33506493506493507,
        "f1-score": 0.3216216216216216,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.674231260438157,
        "recall": 0.7471264367816092,
        "f1-score": 0.7085119602360983,
        "support": 87.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.7969
- **Accuracy:** 0.8161
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "negatif": {
        "precision": 0.375,
        "recall": 0.2727272727272727,
        "f1-score": 0.3157894736842105,
        "support": 11.0
    },
    "non": {
        "precision": 0.8571428571428571,
        "recall": 0.9428571428571428,
        "f1-score": 0.8979591836734694,
        "support": 70.0
    },
    "positif": {
        "precision": 1.0,
        "recall": 0.3333333333333333,
        "f1-score": 0.5,
        "support": 6.0
    },
    "accuracy": 0.8160919540229885,
    "macro avg": {
        "precision": 0.7440476190476191,
        "recall": 0.5163059163059163,
        "f1-score": 0.5712495524525599,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8060344827586207,
        "recall": 0.8160919540229885,
        "f1-score": 0.796906058249071,
        "support": 87.0
    }
}
```

## GloVe_KNN_Enhanced

- **Weighted F1 Score:** 0.7602
- **Accuracy:** 0.7816
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "negatif": {
        "precision": 0.2,
        "recall": 0.18181818181818182,
        "f1-score": 0.19047619047619047,
        "support": 11.0
    },
    "non": {
        "precision": 0.8552631578947368,
        "recall": 0.9285714285714286,
        "f1-score": 0.8904109589041096,
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
        "precision": 0.6850877192982456,
        "recall": 0.4256854256854257,
        "f1-score": 0.4555338116981953,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7823956442831216,
        "recall": 0.7816091954022989,
        "f1-score": 0.7602102406070285,
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

- **Weighted F1 Score:** 0.7454
- **Accuracy:** 0.7701
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
        "precision": 0.8421052631578947,
        "recall": 0.9142857142857143,
        "f1-score": 0.8767123287671232,
        "support": 70.0
    },
    "positif": {
        "precision": 0.4,
        "recall": 0.3333333333333333,
        "f1-score": 0.36363636363636365,
        "support": 6.0
    },
    "accuracy": 0.7701149425287356,
    "macro avg": {
        "precision": 0.46959064327485384,
        "recall": 0.44617604617604617,
        "f1-score": 0.45266525040900546,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7262149626940916,
        "recall": 0.7701149425287356,
        "f1-score": 0.7453540096847774,
        "support": 87.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.7447
- **Accuracy:** 0.7931
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
        "precision": 0.8271604938271605,
        "recall": 0.9571428571428572,
        "f1-score": 0.8874172185430463,
        "support": 70.0
    },
    "positif": {
        "precision": 0.6666666666666666,
        "recall": 0.3333333333333333,
        "f1-score": 0.4444444444444444,
        "support": 6.0
    },
    "accuracy": 0.7931034482758621,
    "macro avg": {
        "precision": 0.49794238683127573,
        "recall": 0.4301587301587302,
        "f1-score": 0.4439538876624969,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7115084433092096,
        "recall": 0.7931034482758621,
        "f1-score": 0.7446651949963209,
        "support": 87.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7225
- **Accuracy:** 0.7586
- **Best Parameters:** {'max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.25,
        "recall": 0.18181818181818182,
        "f1-score": 0.21052631578947367,
        "support": 11.0
    },
    "non": {
        "precision": 0.8205128205128205,
        "recall": 0.9142857142857143,
        "f1-score": 0.8648648648648649,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.7586206896551724,
    "macro avg": {
        "precision": 0.35683760683760685,
        "recall": 0.36536796536796534,
        "f1-score": 0.3584637268847795,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6917919245505452,
        "recall": 0.7586206896551724,
        "f1-score": 0.7224865518876409,
        "support": 87.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7185
- **Accuracy:** 0.7816
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
        "precision": 0.8072289156626506,
        "recall": 0.9571428571428572,
        "f1-score": 0.8758169934640523,
        "support": 70.0
    },
    "positif": {
        "precision": 0.25,
        "recall": 0.16666666666666666,
        "f1-score": 0.2,
        "support": 6.0
    },
    "accuracy": 0.7816091954022989,
    "macro avg": {
        "precision": 0.35240963855421686,
        "recall": 0.3746031746031746,
        "f1-score": 0.3586056644880174,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6667359091538568,
        "recall": 0.7816091954022989,
        "f1-score": 0.7184734430170536,
        "support": 87.0
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
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.2681992337164751,
        "recall": 0.3333333333333333,
        "f1-score": 0.29723991507430997,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.64737746069494,
        "recall": 0.8045977011494253,
        "f1-score": 0.7174756570759206,
        "support": 87.0
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
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.2681992337164751,
        "recall": 0.3333333333333333,
        "f1-score": 0.29723991507430997,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.64737746069494,
        "recall": 0.8045977011494253,
        "f1-score": 0.7174756570759206,
        "support": 87.0
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
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.2681992337164751,
        "recall": 0.3333333333333333,
        "f1-score": 0.29723991507430997,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.64737746069494,
        "recall": 0.8045977011494253,
        "f1-score": 0.7174756570759206,
        "support": 87.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7060
- **Accuracy:** 0.7816
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8,
        "recall": 0.9714285714285714,
        "f1-score": 0.8774193548387097,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.7816091954022989,
    "macro avg": {
        "precision": 0.26666666666666666,
        "recall": 0.3238095238095238,
        "f1-score": 0.2924731182795699,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6436781609195402,
        "recall": 0.7816091954022989,
        "f1-score": 0.7059695958472377,
        "support": 87.0
    }
}
```

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7060
- **Accuracy:** 0.7816
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8,
        "recall": 0.9714285714285714,
        "f1-score": 0.8774193548387097,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.7816091954022989,
    "macro avg": {
        "precision": 0.26666666666666666,
        "recall": 0.3238095238095238,
        "f1-score": 0.2924731182795699,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6436781609195402,
        "recall": 0.7816091954022989,
        "f1-score": 0.7059695958472377,
        "support": 87.0
    }
}
```

