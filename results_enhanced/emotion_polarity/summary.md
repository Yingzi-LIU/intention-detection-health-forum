# Experiment Results Summary

**Labels:** NA_CATEGORY, negatif, positif

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7703
- **Accuracy:** 0.8152
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
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

## TF-IDF_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.7592
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8395061728395061,
        "recall": 0.918918918918919,
        "f1-score": 0.8774193548387097,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.18181818181818182,
        "f1-score": 0.23529411764705882,
        "support": 11.0
    },
    "positif": {
        "precision": 0.4,
        "recall": 0.2857142857142857,
        "f1-score": 0.3333333333333333,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.5242798353909465,
        "recall": 0.4621504621504622,
        "f1-score": 0.4820156019397006,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7455448201825013,
        "recall": 0.782608695652174,
        "f1-score": 0.7592456617990816,
        "support": 92.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7509
- **Accuracy:** 0.8152
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8202247191011236,
        "recall": 0.9864864864864865,
        "f1-score": 0.8957055214723927,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.6666666666666666,
        "recall": 0.2857142857142857,
        "f1-score": 0.4,
        "support": 7.0
    },
    "micro avg": {
        "precision": 0.8152173913043478,
        "recall": 0.9259259259259259,
        "f1-score": 0.8670520231213873,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.7434456928838951,
        "recall": 0.6361003861003861,
        "f1-score": 0.6478527607361964,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8069542701253064,
        "recall": 0.9259259259259259,
        "f1-score": 0.8528667727031736,
        "support": 81.0
    }
}
```

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.7483
- **Accuracy:** 0.7717
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8271604938271605,
        "recall": 0.9054054054054054,
        "f1-score": 0.864516129032258,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.375,
        "recall": 0.2727272727272727,
        "f1-score": 0.3157894736842105,
        "support": 11.0
    },
    "positif": {
        "precision": 0.3333333333333333,
        "recall": 0.14285714285714285,
        "f1-score": 0.2,
        "support": 7.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.5118312757201646,
        "recall": 0.44032994032994033,
        "f1-score": 0.46010186757215615,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7355240203972088,
        "recall": 0.7717391304347826,
        "f1-score": 0.7483464973794938,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.7476
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
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

## TF-IDF_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7367
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.813953488372093,
        "recall": 0.9459459459459459,
        "f1-score": 0.875,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.25,
        "recall": 0.09090909090909091,
        "f1-score": 0.13333333333333333,
        "support": 11.0
    },
    "positif": {
        "precision": 0.5,
        "recall": 0.14285714285714285,
        "f1-score": 0.2222222222222222,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.5213178294573644,
        "recall": 0.3932373932373932,
        "f1-score": 0.4101851851851852,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7226365015166836,
        "recall": 0.782608695652174,
        "f1-score": 0.7366545893719807,
        "support": 92.0
    }
}
```

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.7351
- **Accuracy:** 0.8043
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
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

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7330
- **Accuracy:** 0.8043
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8111111111111111,
        "recall": 0.9864864864864865,
        "f1-score": 0.8902439024390244,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.5,
        "recall": 0.14285714285714285,
        "f1-score": 0.2222222222222222,
        "support": 7.0
    },
    "micro avg": {
        "precision": 0.8043478260869565,
        "recall": 0.9135802469135802,
        "f1-score": 0.8554913294797688,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.6555555555555556,
        "recall": 0.5646718146718147,
        "f1-score": 0.5562330623306233,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7842249657064473,
        "recall": 0.9135802469135802,
        "f1-score": 0.8325136337783131,
        "support": 81.0
    }
}
```

## BoW_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.7318
- **Accuracy:** 0.7391
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8421052631578947,
        "recall": 0.8648648648648649,
        "f1-score": 0.8533333333333334,
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
        "recall": 0.2857142857142857,
        "f1-score": 0.26666666666666666,
        "support": 7.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.4473684210526316,
        "recall": 0.4441324441324442,
        "f1-score": 0.4435087719298245,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7262585812356979,
        "recall": 0.7391304347826086,
        "f1-score": 0.7318382913806254,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7296
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
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
        "precision": 1.0,
        "recall": 0.14285714285714285,
        "f1-score": 0.25,
        "support": 7.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.602996254681648,
        "recall": 0.37194337194337196,
        "f1-score": 0.3778118609406953,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7267953102100636,
        "recall": 0.7934782608695652,
        "f1-score": 0.729611229661243,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.7290
- **Accuracy:** 0.7717
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8117647058823529,
        "recall": 0.9324324324324325,
        "f1-score": 0.8679245283018868,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
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
        "precision": 0.46503267973856205,
        "recall": 0.3887328887328887,
        "f1-score": 0.39753328432573715,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7118179880647911,
        "recall": 0.7717391304347826,
        "f1-score": 0.7290279449836463,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7258
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8089887640449438,
        "recall": 0.972972972972973,
        "f1-score": 0.8834355828220859,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.14285714285714285,
        "f1-score": 0.2,
        "support": 7.0
    },
    "micro avg": {
        "precision": 0.7934782608695652,
        "recall": 0.9012345679012346,
        "f1-score": 0.8439306358381503,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.5711610486891385,
        "recall": 0.5579150579150579,
        "f1-score": 0.5417177914110429,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7678827391686318,
        "recall": 0.9012345679012346,
        "f1-score": 0.824373248504128,
        "support": 81.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.7107
- **Accuracy:** 0.7609
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8023255813953488,
        "recall": 0.9324324324324325,
        "f1-score": 0.8625,
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
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.434108527131783,
        "recall": 0.3584298584298584,
        "f1-score": 0.36157407407407405,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6833923154701719,
        "recall": 0.7608695652173914,
        "f1-score": 0.7106582125603865,
        "support": 92.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.7007
- **Accuracy:** 0.7717
- **Best Parameters:** {'classifier__n_neighbors': 3}
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

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.6991
- **Accuracy:** 0.7391
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.7976190476190477,
        "recall": 0.9054054054054054,
        "f1-score": 0.8481012658227848,
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
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.43253968253968256,
        "recall": 0.34942084942084944,
        "f1-score": 0.35677449601500233,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6796066252587992,
        "recall": 0.7391304347826086,
        "f1-score": 0.6990766220265394,
        "support": 92.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7367
- **Accuracy:** 0.7826
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.813953488372093,
        "recall": 0.9459459459459459,
        "f1-score": 0.875,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.25,
        "recall": 0.09090909090909091,
        "f1-score": 0.13333333333333333,
        "support": 11.0
    },
    "positif": {
        "precision": 0.5,
        "recall": 0.14285714285714285,
        "f1-score": 0.2222222222222222,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.5213178294573644,
        "recall": 0.3932373932373932,
        "f1-score": 0.4101851851851852,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7226365015166836,
        "recall": 0.782608695652174,
        "f1-score": 0.7366545893719807,
        "support": 92.0
    }
}
```

## Word2Vec_SVM_Enhanced

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
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

## FastText_SVM_Enhanced

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
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

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.7161
- **Accuracy:** 0.7935
- **Best Parameters:** {'n_neighbors': 7}
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
    "micro avg": {
        "precision": 0.7934782608695652,
        "recall": 0.8588235294117647,
        "f1-score": 0.8248587570621468,
        "support": 85.0
    },
    "macro avg": {
        "precision": 0.40555555555555556,
        "recall": 0.49324324324324326,
        "f1-score": 0.4451219512195122,
        "support": 85.0
    },
    "weighted avg": {
        "precision": 0.7061437908496733,
        "recall": 0.8588235294117647,
        "f1-score": 0.7750358680057389,
        "support": 85.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.7032
- **Accuracy:** 0.7500
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8,
        "recall": 0.918918918918919,
        "f1-score": 0.8553459119496856,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
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
        "precision": 0.37777777777777777,
        "recall": 0.35392535392535396,
        "f1-score": 0.3517819706498952,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.668840579710145,
        "recall": 0.75,
        "f1-score": 0.7032130161334428,
        "support": 92.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7007
- **Accuracy:** 0.7717
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
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

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7007
- **Accuracy:** 0.7717
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
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

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.6880
- **Accuracy:** 0.7391
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8,
        "recall": 0.918918918918919,
        "f1-score": 0.8553459119496856,
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
        "precision": 0.26666666666666666,
        "recall": 0.30630630630630634,
        "f1-score": 0.28511530398322854,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6434782608695653,
        "recall": 0.7391304347826086,
        "f1-score": 0.6879956248290949,
        "support": 92.0
    }
}
```

