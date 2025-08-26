# Experiment Results Summary

**Labels:** negatif, non, positif

## TF-IDF_DecisionTree

- **Weighted F1 Score:** 0.8043
- **Accuracy:** 0.8506
- **Best Parameters:** {'max_depth': 5}
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

## TF-IDF_SVM

- **Weighted F1 Score:** 0.7967
- **Accuracy:** 0.8276
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.5555555555555556,
        "recall": 0.45454545454545453,
        "f1-score": 0.5,
        "support": 11.0
    },
    "non": {
        "precision": 0.8701298701298701,
        "recall": 0.9571428571428572,
        "f1-score": 0.9115646258503401,
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
        "precision": 0.4752284752284752,
        "recall": 0.47056277056277057,
        "f1-score": 0.4705215419501134,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7703471496574945,
        "recall": 0.8275862068965517,
        "f1-score": 0.7966611932129174,
        "support": 87.0
    }
}
```

## Bert_LogisticRegression

- **Weighted F1 Score:** 0.7957
- **Accuracy:** 0.8276
- **Best Parameters:** {'C': 1, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.5,
        "recall": 0.18181818181818182,
        "f1-score": 0.26666666666666666,
        "support": 11.0
    },
    "non": {
        "precision": 0.8607594936708861,
        "recall": 0.9714285714285714,
        "f1-score": 0.912751677852349,
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
        "precision": 0.6202531645569621,
        "recall": 0.4955266955266955,
        "f1-score": 0.5264727815063385,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7902662592754255,
        "recall": 0.8275862068965517,
        "f1-score": 0.7957005837126181,
        "support": 87.0
    }
}
```

## Bert_SVM

- **Weighted F1 Score:** 0.7945
- **Accuracy:** 0.8391
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.5,
        "recall": 0.18181818181818182,
        "f1-score": 0.26666666666666666,
        "support": 11.0
    },
    "non": {
        "precision": 0.8536585365853658,
        "recall": 1.0,
        "f1-score": 0.9210526315789473,
        "support": 70.0
    },
    "positif": {
        "precision": 1.0,
        "recall": 0.16666666666666666,
        "f1-score": 0.2857142857142857,
        "support": 6.0
    },
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.7845528455284553,
        "recall": 0.44949494949494956,
        "f1-score": 0.49114452798663316,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8190356041491449,
        "recall": 0.8390804597701149,
        "f1-score": 0.794497738599372,
        "support": 87.0
    }
}
```

## BoW_DecisionTree

- **Weighted F1 Score:** 0.7779
- **Accuracy:** 0.8276
- **Best Parameters:** {'max_depth': 5}
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

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.7670
- **Accuracy:** 0.7701
- **Best Parameters:** {'max_depth': 10}
```json
{
    "negatif": {
        "precision": 0.35714285714285715,
        "recall": 0.45454545454545453,
        "f1-score": 0.4,
        "support": 11.0
    },
    "non": {
        "precision": 0.8714285714285714,
        "recall": 0.8714285714285714,
        "f1-score": 0.8714285714285714,
        "support": 70.0
    },
    "positif": {
        "precision": 0.3333333333333333,
        "recall": 0.16666666666666666,
        "f1-score": 0.2222222222222222,
        "support": 6.0
    },
    "accuracy": 0.7701149425287356,
    "macro avg": {
        "precision": 0.5206349206349207,
        "recall": 0.49754689754689757,
        "f1-score": 0.4978835978835979,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7692939244663383,
        "recall": 0.7701149425287356,
        "f1-score": 0.7670498084291187,
        "support": 87.0
    }
}
```

## BoW_LogisticRegression

- **Weighted F1 Score:** 0.7571
- **Accuracy:** 0.8161
- **Best Parameters:** {'C': 1, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.6666666666666666,
        "recall": 0.18181818181818182,
        "f1-score": 0.2857142857142857,
        "support": 11.0
    },
    "non": {
        "precision": 0.8214285714285714,
        "recall": 0.9857142857142858,
        "f1-score": 0.8961038961038961,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8160919540229885,
        "recall": 0.8765432098765432,
        "f1-score": 0.8452380952380952,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.7440476190476191,
        "recall": 0.5837662337662338,
        "f1-score": 0.5909090909090908,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8004115226337448,
        "recall": 0.8765432098765432,
        "f1-score": 0.8132114798781466,
        "support": 81.0
    }
}
```

## Word2Vec_KNN

- **Weighted F1 Score:** 0.7527
- **Accuracy:** 0.7931
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
        "precision": 0.8354430379746836,
        "recall": 0.9428571428571428,
        "f1-score": 0.8859060402684564,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.7931034482758621,
        "recall": 0.8518518518518519,
        "f1-score": 0.8214285714285714,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.6052215189873418,
        "recall": 0.6077922077922078,
        "f1-score": 0.6008477569763335,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7729137365213314,
        "recall": 0.8518518518518519,
        "f1-score": 0.8084828028310898,
        "support": 81.0
    }
}
```

## TF-IDF_LogisticRegression

- **Weighted F1 Score:** 0.7515
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.4,
        "recall": 0.18181818181818182,
        "f1-score": 0.25,
        "support": 11.0
    },
    "non": {
        "precision": 0.8292682926829268,
        "recall": 0.9714285714285714,
        "f1-score": 0.8947368421052632,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 0.8641975308641975,
        "f1-score": 0.8333333333333334,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.6146341463414634,
        "recall": 0.5766233766233766,
        "f1-score": 0.5723684210526316,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.770972598614875,
        "recall": 0.8641975308641975,
        "f1-score": 0.8071799870045484,
        "support": 81.0
    }
}
```

## Bert_DecisionTree

- **Weighted F1 Score:** 0.7445
- **Accuracy:** 0.7701
- **Best Parameters:** {'max_depth': 10}
```json
{
    "negatif": {
        "precision": 0.25,
        "recall": 0.18181818181818182,
        "f1-score": 0.21052631578947367,
        "support": 11.0
    },
    "non": {
        "precision": 0.8311688311688312,
        "recall": 0.9142857142857143,
        "f1-score": 0.8707482993197279,
        "support": 70.0
    },
    "positif": {
        "precision": 0.5,
        "recall": 0.16666666666666666,
        "f1-score": 0.25,
        "support": 6.0
    },
    "accuracy": 0.7701149425287356,
    "macro avg": {
        "precision": 0.5270562770562771,
        "recall": 0.4209235209235209,
        "f1-score": 0.44375820503640045,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7348484848484849,
        "recall": 0.7701149425287356,
        "f1-score": 0.7444617290352317,
        "support": 87.0
    }
}
```

## BoW_MultinomialNB

- **Weighted F1 Score:** 0.7431
- **Accuracy:** 0.8161
- **Best Parameters:** {'alpha': 1.0}
```json
{
    "negatif": {
        "precision": 1.0,
        "recall": 0.09090909090909091,
        "f1-score": 0.16666666666666666,
        "support": 11.0
    },
    "non": {
        "precision": 0.813953488372093,
        "recall": 1.0,
        "f1-score": 0.8974358974358975,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8160919540229885,
        "recall": 0.8765432098765432,
        "f1-score": 0.8452380952380952,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.9069767441860466,
        "recall": 0.5454545454545454,
        "f1-score": 0.532051282051282,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8392190640252657,
        "recall": 0.8765432098765432,
        "f1-score": 0.7981956315289649,
        "support": 81.0
    }
}
```

## BoW_KNN

- **Weighted F1 Score:** 0.7431
- **Accuracy:** 0.8161
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "negatif": {
        "precision": 1.0,
        "recall": 0.09090909090909091,
        "f1-score": 0.16666666666666666,
        "support": 11.0
    },
    "non": {
        "precision": 0.813953488372093,
        "recall": 1.0,
        "f1-score": 0.8974358974358975,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8160919540229885,
        "recall": 0.8765432098765432,
        "f1-score": 0.8452380952380952,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.9069767441860466,
        "recall": 0.5454545454545454,
        "f1-score": 0.532051282051282,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8392190640252657,
        "recall": 0.8765432098765432,
        "f1-score": 0.7981956315289649,
        "support": 81.0
    }
}
```

## TF-IDF_MultinomialNB

- **Weighted F1 Score:** 0.7431
- **Accuracy:** 0.8161
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "negatif": {
        "precision": 1.0,
        "recall": 0.09090909090909091,
        "f1-score": 0.16666666666666666,
        "support": 11.0
    },
    "non": {
        "precision": 0.813953488372093,
        "recall": 1.0,
        "f1-score": 0.8974358974358975,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8160919540229885,
        "recall": 0.8765432098765432,
        "f1-score": 0.8452380952380952,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.9069767441860466,
        "recall": 0.5454545454545454,
        "f1-score": 0.532051282051282,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8392190640252657,
        "recall": 0.8765432098765432,
        "f1-score": 0.7981956315289649,
        "support": 81.0
    }
}
```

## Bert_KNN

- **Weighted F1 Score:** 0.7426
- **Accuracy:** 0.7816
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "negatif": {
        "precision": 0.16666666666666666,
        "recall": 0.09090909090909091,
        "f1-score": 0.11764705882352941,
        "support": 11.0
    },
    "non": {
        "precision": 0.825,
        "recall": 0.9428571428571428,
        "f1-score": 0.88,
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
        "precision": 0.6638888888888889,
        "recall": 0.40014430014430014,
        "f1-score": 0.4277871148459384,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7538314176245212,
        "recall": 0.7816091954022989,
        "f1-score": 0.742625325992466,
        "support": 87.0
    }
}
```

## TF-IDF_KNN

- **Weighted F1 Score:** 0.7409
- **Accuracy:** 0.7931
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "negatif": {
        "precision": 0.4,
        "recall": 0.18181818181818182,
        "f1-score": 0.25,
        "support": 11.0
    },
    "non": {
        "precision": 0.8170731707317073,
        "recall": 0.9571428571428572,
        "f1-score": 0.881578947368421,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.7931034482758621,
        "recall": 0.8518518518518519,
        "f1-score": 0.8214285714285714,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.6085365853658536,
        "recall": 0.5694805194805195,
        "f1-score": 0.5657894736842105,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7604336043360432,
        "recall": 0.8518518518518519,
        "f1-score": 0.7958089668615985,
        "support": 81.0
    }
}
```

## TF-IDF_ngram_KNN

- **Weighted F1 Score:** 0.7391
- **Accuracy:** 0.8046
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "non": {
        "precision": 0.8214285714285714,
        "recall": 0.9857142857142858,
        "f1-score": 0.8961038961038961,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 0.8641975308641975,
        "f1-score": 0.8333333333333334,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.5773809523809523,
        "recall": 0.5383116883116883,
        "f1-score": 0.5194805194805194,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7551440329218106,
        "recall": 0.8641975308641975,
        "f1-score": 0.7938111271444606,
        "support": 81.0
    }
}
```

## BoW_SVM

- **Weighted F1 Score:** 0.7358
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "non": {
        "precision": 0.8117647058823529,
        "recall": 0.9857142857142858,
        "f1-score": 0.8903225806451613,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 0.8641975308641975,
        "f1-score": 0.8333333333333334,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.6558823529411765,
        "recall": 0.5383116883116883,
        "f1-score": 0.5220843672456577,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7694262890341321,
        "recall": 0.8641975308641975,
        "f1-score": 0.790307263425543,
        "support": 81.0
    }
}
```

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.7340
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
        "precision": 0.8148148148148148,
        "recall": 0.9428571428571428,
        "f1-score": 0.8741721854304636,
        "support": 70.0
    },
    "positif": {
        "precision": 0.6666666666666666,
        "recall": 0.3333333333333333,
        "f1-score": 0.4444444444444444,
        "support": 6.0
    },
    "accuracy": 0.7816091954022989,
    "macro avg": {
        "precision": 0.49382716049382713,
        "recall": 0.4253968253968254,
        "f1-score": 0.4395388766249693,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7015751383567475,
        "recall": 0.7816091954022989,
        "f1-score": 0.7340082718022887,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_LogisticRegression

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
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

## TF-IDF_ngram_SVM

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

## TF-IDF_ngram_MultinomialNB

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'alpha': 0.5}
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

## Word2Vec_LogisticRegression

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
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

## Word2Vec_SVM

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

## FastText_LogisticRegression

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
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

## FastText_SVM

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

## FastText_KNN

- **Weighted F1 Score:** 0.7001
- **Accuracy:** 0.7701
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
        "precision": 0.7976190476190477,
        "recall": 0.9571428571428572,
        "f1-score": 0.8701298701298701,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.7701149425287356,
        "recall": 0.8271604938271605,
        "f1-score": 0.7976190476190477,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.39880952380952384,
        "recall": 0.4785714285714286,
        "f1-score": 0.43506493506493504,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.6893004115226338,
        "recall": 0.8271604938271605,
        "f1-score": 0.7519640852974186,
        "support": 81.0
    }
}
```

## FastText_DecisionTree

- **Weighted F1 Score:** 0.6928
- **Accuracy:** 0.7241
- **Best Parameters:** {'max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.14285714285714285,
        "recall": 0.09090909090909091,
        "f1-score": 0.1111111111111111,
        "support": 11.0
    },
    "non": {
        "precision": 0.8051948051948052,
        "recall": 0.8857142857142857,
        "f1-score": 0.8435374149659864,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.7241379310344828,
    "macro avg": {
        "precision": 0.31601731601731603,
        "recall": 0.3255411255411255,
        "f1-score": 0.3182161753590325,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6659202866099418,
        "recall": 0.7241379310344828,
        "f1-score": 0.6927567962050721,
        "support": 87.0
    }
}
```

