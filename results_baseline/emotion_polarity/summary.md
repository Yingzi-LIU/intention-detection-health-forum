# Experiment Results Summary

**Labels:** NA_CATEGORY, negatif, positif

## BoW_MultinomialNB

- **Weighted F1 Score:** 0.7705
- **Accuracy:** 0.8152
- **Best Parameters:** {'alpha': 1.0}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8275862068965517,
        "recall": 0.972972972972973,
        "f1-score": 0.8944099378881988,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.6666666666666666,
        "recall": 0.18181818181818182,
        "f1-score": 0.2857142857142857,
        "support": 11.0
    },
    "positif": {
        "precision": 0.5,
        "recall": 0.14285714285714285,
        "f1-score": 0.2222222222222222,
        "support": 7.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.6647509578544061,
        "recall": 0.43254943254943257,
        "f1-score": 0.4674488152749022,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7834207896051973,
        "recall": 0.8152173913043478,
        "f1-score": 0.7704863924145589,
        "support": 92.0
    }
}
```

## BoW_LogisticRegression

- **Weighted F1 Score:** 0.7703
- **Accuracy:** 0.8152
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8275862068965517,
        "recall": 0.972972972972973,
        "f1-score": 0.8944099378881988,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.5,
        "recall": 0.18181818181818182,
        "f1-score": 0.26666666666666666,
        "support": 11.0
    },
    "positif": {
        "precision": 1.0,
        "recall": 0.14285714285714285,
        "f1-score": 0.25,
        "support": 7.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.7758620689655172,
        "recall": 0.43254943254943257,
        "f1-score": 0.47035886818495515,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8015367316341829,
        "recall": 0.8152173913043478,
        "f1-score": 0.7703224862723919,
        "support": 92.0
    }
}
```

## BoW_SVM

- **Weighted F1 Score:** 0.7644
- **Accuracy:** 0.7935
- **Best Parameters:** {'C': 1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8313253012048193,
        "recall": 0.9324324324324325,
        "f1-score": 0.8789808917197452,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.5,
        "recall": 0.2727272727272727,
        "f1-score": 0.35294117647058826,
        "support": 11.0
    },
    "positif": {
        "precision": 0.3333333333333333,
        "recall": 0.14285714285714285,
        "f1-score": 0.2,
        "support": 7.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.5548862115127176,
        "recall": 0.4493389493389493,
        "f1-score": 0.4773073560634445,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7538196263314126,
        "recall": 0.7934782608695652,
        "f1-score": 0.764423249222148,
        "support": 92.0
    }
}
```

## TF-IDF_LogisticRegression

- **Weighted F1 Score:** 0.7553
- **Accuracy:** 0.7935
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8235294117647058,
        "recall": 0.9459459459459459,
        "f1-score": 0.8805031446540881,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.5,
        "recall": 0.18181818181818182,
        "f1-score": 0.26666666666666666,
        "support": 11.0
    },
    "positif": {
        "precision": 0.3333333333333333,
        "recall": 0.14285714285714285,
        "f1-score": 0.2,
        "support": 7.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.5522875816993463,
        "recall": 0.4235404235404235,
        "f1-score": 0.44905660377358486,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.747549019607843,
        "recall": 0.7934782608695652,
        "f1-score": 0.7553322395406071,
        "support": 92.0
    }
}
```

## TF-IDF_SVM

- **Weighted F1 Score:** 0.7515
- **Accuracy:** 0.7717
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8375,
        "recall": 0.9054054054054054,
        "f1-score": 0.8701298701298701,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.375,
        "recall": 0.2727272727272727,
        "f1-score": 0.3157894736842105,
        "support": 11.0
    },
    "positif": {
        "precision": 0.25,
        "recall": 0.14285714285714285,
        "f1-score": 0.18181818181818182,
        "support": 7.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.4875,
        "recall": 0.44032994032994033,
        "f1-score": 0.45591250854408744,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7374999999999999,
        "recall": 0.7717391304347826,
        "f1-score": 0.7514784986180866,
        "support": 92.0
    }
}
```

## Bert_DecisionTree

- **Weighted F1 Score:** 0.7510
- **Accuracy:** 0.7717
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.8918918918918919,
        "f1-score": 0.8741721854304636,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.35714285714285715,
        "recall": 0.45454545454545453,
        "f1-score": 0.4,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.4047619047619047,
        "recall": 0.4488124488124488,
        "f1-score": 0.4247240618101545,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.732142857142857,
        "recall": 0.7717391304347826,
        "f1-score": 0.7509645839331991,
        "support": 92.0
    }
}
```

## TF-IDF_MultinomialNB

- **Weighted F1 Score:** 0.7507
- **Accuracy:** 0.7826
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8313253012048193,
        "recall": 0.9324324324324325,
        "f1-score": 0.8789808917197452,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.4,
        "recall": 0.18181818181818182,
        "f1-score": 0.25,
        "support": 11.0
    },
    "positif": {
        "precision": 0.25,
        "recall": 0.14285714285714285,
        "f1-score": 0.18181818181818182,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.49377510040160644,
        "recall": 0.419035919035919,
        "f1-score": 0.4369330245126424,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7355225248821372,
        "recall": 0.782608695652174,
        "f1-score": 0.7507316658694393,
        "support": 92.0
    }
}
```

## Bert_LogisticRegression

- **Weighted F1 Score:** 0.7496
- **Accuracy:** 0.7609
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.8918918918918919,
        "f1-score": 0.8741721854304636,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.2727272727272727,
        "recall": 0.2727272727272727,
        "f1-score": 0.2727272727272727,
        "support": 11.0
    },
    "positif": {
        "precision": 0.25,
        "recall": 0.14285714285714285,
        "f1-score": 0.18181818181818182,
        "support": 7.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.4599567099567099,
        "recall": 0.4358254358254358,
        "f1-score": 0.44290587999197273,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7410714285714285,
        "recall": 0.7608695652173914,
        "f1-score": 0.7495811847237128,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_SVM

- **Weighted F1 Score:** 0.7476
- **Accuracy:** 0.7826
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8214285714285714,
        "recall": 0.9324324324324325,
        "f1-score": 0.8734177215189873,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.4,
        "recall": 0.18181818181818182,
        "f1-score": 0.25,
        "support": 11.0
    },
    "positif": {
        "precision": 0.3333333333333333,
        "recall": 0.14285714285714285,
        "f1-score": 0.2,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.5182539682539683,
        "recall": 0.419035919035919,
        "f1-score": 0.4411392405063291,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7339026915113871,
        "recall": 0.782608695652174,
        "f1-score": 0.7476403412217942,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN

- **Weighted F1 Score:** 0.7361
- **Accuracy:** 0.7826
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.813953488372093,
        "recall": 0.9459459459459459,
        "f1-score": 0.875,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "positif": {
        "precision": 0.3333333333333333,
        "recall": 0.14285714285714285,
        "f1-score": 0.2,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.49354005167958653,
        "recall": 0.3932373932373932,
        "f1-score": 0.4059523809523809,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7199191102123356,
        "recall": 0.782608695652174,
        "f1-score": 0.7361024844720497,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_LogisticRegression

- **Weighted F1 Score:** 0.7351
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8111111111111111,
        "recall": 0.9864864864864865,
        "f1-score": 0.8902439024390244,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 1.0,
        "recall": 0.14285714285714285,
        "f1-score": 0.25,
        "support": 7.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.6037037037037037,
        "recall": 0.3764478764478765,
        "f1-score": 0.3800813008130081,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7285024154589372,
        "recall": 0.8043478260869565,
        "f1-score": 0.7350874867444326,
        "support": 92.0
    }
}
```

## TF-IDF_KNN

- **Weighted F1 Score:** 0.7284
- **Accuracy:** 0.7500
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.825,
        "recall": 0.8918918918918919,
        "f1-score": 0.8571428571428571,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.25,
        "recall": 0.18181818181818182,
        "f1-score": 0.21052631578947367,
        "support": 11.0
    },
    "positif": {
        "precision": 0.25,
        "recall": 0.14285714285714285,
        "f1-score": 0.18181818181818182,
        "support": 7.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.44166666666666665,
        "recall": 0.40552240552240554,
        "f1-score": 0.41649578491683753,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7125,
        "recall": 0.75,
        "f1-score": 0.7284466105976403,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.7275
- **Accuracy:** 0.7935
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8089887640449438,
        "recall": 0.972972972972973,
        "f1-score": 0.8834355828220859,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 0.5,
        "recall": 0.14285714285714285,
        "f1-score": 0.2222222222222222,
        "support": 7.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.4363295880149813,
        "recall": 0.37194337194337196,
        "f1-score": 0.368552601681436,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.688751831949194,
        "recall": 0.7934782608695652,
        "f1-score": 0.7274977030911948,
        "support": 92.0
    }
}
```

## Bert_KNN

- **Weighted F1 Score:** 0.7194
- **Accuracy:** 0.7500
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8170731707317073,
        "recall": 0.9054054054054054,
        "f1-score": 0.8589743589743589,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.14285714285714285,
        "recall": 0.09090909090909091,
        "f1-score": 0.1111111111111111,
        "support": 11.0
    },
    "positif": {
        "precision": 0.3333333333333333,
        "recall": 0.14285714285714285,
        "f1-score": 0.2,
        "support": 7.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.4310878823073945,
        "recall": 0.3797238797238797,
        "f1-score": 0.39002849002849,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6996540928142201,
        "recall": 0.75,
        "f1-score": 0.7194165737643999,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_MultinomialNB

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'alpha': 0.5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "micro avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "macro avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "weighted avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.8915662650602411,
        "support": 74.0
    }
}
```

## Word2Vec_LogisticRegression

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "micro avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "macro avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "weighted avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.8915662650602411,
        "support": 74.0
    }
}
```

## Word2Vec_SVM

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "micro avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "macro avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "weighted avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.8915662650602411,
        "support": 74.0
    }
}
```

## FastText_LogisticRegression

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "micro avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "macro avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "weighted avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.8915662650602411,
        "support": 74.0
    }
}
```

## FastText_SVM

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "micro avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "macro avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "weighted avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.8915662650602411,
        "support": 74.0
    }
}
```

## FastText_KNN

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "micro avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "macro avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "weighted avg": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.8915662650602411,
        "support": 74.0
    }
}
```

## Bert_SVM

- **Weighted F1 Score:** 0.7167
- **Accuracy:** 0.7391
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8354430379746836,
        "recall": 0.8918918918918919,
        "f1-score": 0.8627450980392157,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.2,
        "recall": 0.18181818181818182,
        "f1-score": 0.19047619047619047,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.3451476793248945,
        "recall": 0.3579033579033579,
        "f1-score": 0.35107376283846875,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6958998348926803,
        "recall": 0.7391304347826086,
        "f1-score": 0.7167214711971746,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree

- **Weighted F1 Score:** 0.7133
- **Accuracy:** 0.7717
- **Best Parameters:** {'max_depth': 10}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8045977011494253,
        "recall": 0.9459459459459459,
        "f1-score": 0.8695652173913043,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 0.25,
        "recall": 0.14285714285714285,
        "f1-score": 0.18181818181818182,
        "support": 7.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.35153256704980845,
        "recall": 0.36293436293436293,
        "f1-score": 0.3504611330698287,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6661981509245377,
        "recall": 0.7717391304347826,
        "f1-score": 0.7132668843443889,
        "support": 92.0
    }
}
```

## BoW_DecisionTree

- **Weighted F1 Score:** 0.7128
- **Accuracy:** 0.7391
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8148148148148148,
        "recall": 0.8918918918918919,
        "f1-score": 0.8516129032258064,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.125,
        "recall": 0.09090909090909091,
        "f1-score": 0.10526315789473684,
        "support": 11.0
    },
    "positif": {
        "precision": 0.3333333333333333,
        "recall": 0.14285714285714285,
        "f1-score": 0.2,
        "support": 7.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.4243827160493827,
        "recall": 0.37521937521937526,
        "f1-score": 0.38562535370684775,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.695702495974235,
        "recall": 0.7391304347826086,
        "f1-score": 0.7127961910386064,
        "support": 92.0
    }
}
```

## Word2Vec_KNN

- **Weighted F1 Score:** 0.7106
- **Accuracy:** 0.7826
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8089887640449438,
        "recall": 0.972972972972973,
        "f1-score": 0.8834355828220859,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.2696629213483146,
        "recall": 0.32432432432432434,
        "f1-score": 0.294478527607362,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6507083536883244,
        "recall": 0.782608695652174,
        "f1-score": 0.7105894905308083,
        "support": 92.0
    }
}
```

## BoW_KNN

- **Weighted F1 Score:** 0.7007
- **Accuracy:** 0.7717
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.797752808988764,
        "recall": 0.9594594594594594,
        "f1-score": 0.8711656441717791,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.26591760299625467,
        "recall": 0.31981981981981983,
        "f1-score": 0.2903885480572597,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6416707376648754,
        "recall": 0.7717391304347826,
        "f1-score": 0.7007201920512136,
        "support": 92.0
    }
}
```

## FastText_DecisionTree

- **Weighted F1 Score:** 0.6837
- **Accuracy:** 0.7391
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.7906976744186046,
        "recall": 0.918918918918919,
        "f1-score": 0.85,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.2635658914728682,
        "recall": 0.30630630630630634,
        "f1-score": 0.2833333333333333,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6359959555106167,
        "recall": 0.7391304347826086,
        "f1-score": 0.683695652173913,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.6499
- **Accuracy:** 0.6630
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.7922077922077922,
        "recall": 0.8243243243243243,
        "f1-score": 0.8079470198675497,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.6630434782608695,
    "macro avg": {
        "precision": 0.26406926406926406,
        "recall": 0.2747747747747748,
        "f1-score": 0.2693156732891832,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.637210615471485,
        "recall": 0.6630434782608695,
        "f1-score": 0.6498704290238987,
        "support": 92.0
    }
}
```

