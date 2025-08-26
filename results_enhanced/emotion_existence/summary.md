# Experiment Results Summary

**Labels:** non, oui

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7971
- **Accuracy:** 0.8152
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.8518518518518519,
        "recall": 0.9324324324324325,
        "f1-score": 0.8903225806451613,
        "support": 74.0
    },
    "oui": {
        "precision": 0.5454545454545454,
        "recall": 0.3333333333333333,
        "f1-score": 0.41379310344827586,
        "support": 18.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.6986531986531986,
        "recall": 0.6328828828828829,
        "f1-score": 0.6520578420467186,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.791904552774118,
        "recall": 0.8152173913043478,
        "f1-score": 0.7970885524979446,
        "support": 92.0
    }
}
```

## BoW_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.7777
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__alpha': 0.5}
```json
{
    "non": {
        "precision": 0.8552631578947368,
        "recall": 0.8783783783783784,
        "f1-score": 0.8666666666666667,
        "support": 74.0
    },
    "oui": {
        "precision": 0.4375,
        "recall": 0.3888888888888889,
        "f1-score": 0.4117647058823529,
        "support": 18.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.6463815789473684,
        "recall": 0.6336336336336337,
        "f1-score": 0.6392156862745098,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7735268878718535,
        "recall": 0.782608695652174,
        "f1-score": 0.7776641091219096,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7729
- **Accuracy:** 0.8043
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "non": {
        "precision": 0.8333333333333334,
        "recall": 0.9459459459459459,
        "f1-score": 0.8860759493670886,
        "support": 74.0
    },
    "oui": {
        "precision": 0.5,
        "recall": 0.2222222222222222,
        "f1-score": 0.3076923076923077,
        "support": 18.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.6666666666666667,
        "recall": 0.5840840840840841,
        "f1-score": 0.5968841285296982,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7681159420289856,
        "recall": 0.8043478260869565,
        "f1-score": 0.7729139325176749,
        "support": 92.0
    }
}
```

## TF-IDF_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.7719
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "non": {
        "precision": 0.8461538461538461,
        "recall": 0.8918918918918919,
        "f1-score": 0.868421052631579,
        "support": 74.0
    },
    "oui": {
        "precision": 0.42857142857142855,
        "recall": 0.3333333333333333,
        "f1-score": 0.375,
        "support": 18.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.6373626373626373,
        "recall": 0.6126126126126126,
        "f1-score": 0.6217105263157895,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7644529383659817,
        "recall": 0.782608695652174,
        "f1-score": 0.7718821510297483,
        "support": 92.0
    }
}
```

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.7636
- **Accuracy:** 0.7717
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.8441558441558441,
        "recall": 0.8783783783783784,
        "f1-score": 0.8609271523178808,
        "support": 74.0
    },
    "oui": {
        "precision": 0.4,
        "recall": 0.3333333333333333,
        "f1-score": 0.36363636363636365,
        "support": 18.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.622077922077922,
        "recall": 0.6058558558558559,
        "f1-score": 0.6122817579771223,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7572557876905703,
        "recall": 0.7717391304347826,
        "f1-score": 0.76363112844541,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7628
- **Accuracy:** 0.8043
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "non": {
        "precision": 0.8255813953488372,
        "recall": 0.9594594594594594,
        "f1-score": 0.8875,
        "support": 74.0
    },
    "oui": {
        "precision": 0.5,
        "recall": 0.16666666666666666,
        "f1-score": 0.25,
        "support": 18.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.6627906976744187,
        "recall": 0.5630630630630631,
        "f1-score": 0.56875,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7618806875631953,
        "recall": 0.8043478260869565,
        "f1-score": 0.7627717391304347,
        "support": 92.0
    }
}
```

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.7491
- **Accuracy:** 0.7609
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.8333333333333334,
        "recall": 0.8783783783783784,
        "f1-score": 0.8552631578947368,
        "support": 74.0
    },
    "oui": {
        "precision": 0.35714285714285715,
        "recall": 0.2777777777777778,
        "f1-score": 0.3125,
        "support": 18.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.5952380952380952,
        "recall": 0.5780780780780781,
        "f1-score": 0.5838815789473684,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7401656314699794,
        "recall": 0.7608695652173914,
        "f1-score": 0.749070366132723,
        "support": 92.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7435
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__max_depth': None}
```json
{
    "non": {
        "precision": 0.8160919540229885,
        "recall": 0.9594594594594594,
        "f1-score": 0.8819875776397516,
        "support": 74.0
    },
    "oui": {
        "precision": 0.4,
        "recall": 0.1111111111111111,
        "f1-score": 0.17391304347826086,
        "support": 18.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.6080459770114943,
        "recall": 0.5352852852852853,
        "f1-score": 0.5279503105590062,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7346826586706647,
        "recall": 0.7934782608695652,
        "f1-score": 0.7434512557385903,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.7328
- **Accuracy:** 0.7609
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.8170731707317073,
        "recall": 0.9054054054054054,
        "f1-score": 0.8589743589743589,
        "support": 74.0
    },
    "oui": {
        "precision": 0.3,
        "recall": 0.16666666666666666,
        "f1-score": 0.21428571428571427,
        "support": 18.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.5585365853658536,
        "recall": 0.536036036036036,
        "f1-score": 0.5366300366300366,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7159066808059384,
        "recall": 0.7608695652173914,
        "f1-score": 0.732839624143972,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.7255
- **Accuracy:** 0.7500
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "non": {
        "precision": 0.8148148148148148,
        "recall": 0.8918918918918919,
        "f1-score": 0.8516129032258064,
        "support": 74.0
    },
    "oui": {
        "precision": 0.2727272727272727,
        "recall": 0.16666666666666666,
        "f1-score": 0.20689655172413793,
        "support": 18.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.5437710437710437,
        "recall": 0.5292792792792793,
        "f1-score": 0.5292547274749722,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7087542087542087,
        "recall": 0.75,
        "f1-score": 0.725472747497219,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.7225
- **Accuracy:** 0.7609
- **Best Parameters:** {'classifier__n_neighbors': 5}
```json
{
    "non": {
        "precision": 0.8095238095238095,
        "recall": 0.918918918918919,
        "f1-score": 0.8607594936708861,
        "support": 74.0
    },
    "oui": {
        "precision": 0.25,
        "recall": 0.1111111111111111,
        "f1-score": 0.15384615384615385,
        "support": 18.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.5297619047619048,
        "recall": 0.515015015015015,
        "f1-score": 0.50730282375852,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7000517598343684,
        "recall": 0.7608695652173914,
        "f1-score": 0.7224503619660472,
        "support": 92.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.7186
- **Accuracy:** 0.7283
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "non": {
        "precision": 0.8181818181818182,
        "recall": 0.8513513513513513,
        "f1-score": 0.8344370860927153,
        "support": 74.0
    },
    "oui": {
        "precision": 0.26666666666666666,
        "recall": 0.2222222222222222,
        "f1-score": 0.24242424242424243,
        "support": 18.0
    },
    "accuracy": 0.7282608695652174,
    "macro avg": {
        "precision": 0.5424242424242425,
        "recall": 0.5367867867867868,
        "f1-score": 0.5384306642584789,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7102766798418972,
        "recall": 0.7282608695652174,
        "f1-score": 0.7186084862445358,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7101
- **Accuracy:** 0.7609
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.8023255813953488,
        "recall": 0.9324324324324325,
        "f1-score": 0.8625,
        "support": 74.0
    },
    "oui": {
        "precision": 0.16666666666666666,
        "recall": 0.05555555555555555,
        "f1-score": 0.08333333333333333,
        "support": 18.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.4844961240310077,
        "recall": 0.493993993993994,
        "f1-score": 0.4729166666666667,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6779575328614762,
        "recall": 0.7608695652173914,
        "f1-score": 0.710054347826087,
        "support": 92.0
    }
}
```

## TF-IDF_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7036
- **Accuracy:** 0.7500
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.8,
        "recall": 0.918918918918919,
        "f1-score": 0.8553459119496856,
        "support": 74.0
    },
    "oui": {
        "precision": 0.14285714285714285,
        "recall": 0.05555555555555555,
        "f1-score": 0.08,
        "support": 18.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.4714285714285714,
        "recall": 0.4872372372372373,
        "f1-score": 0.46767295597484276,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6714285714285715,
        "recall": 0.75,
        "f1-score": 0.7036477987421385,
        "support": 92.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.6894
- **Accuracy:** 0.7500
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "non": {
        "precision": 0.7931034482758621,
        "recall": 0.9324324324324325,
        "f1-score": 0.8571428571428571,
        "support": 74.0
    },
    "oui": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 18.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.39655172413793105,
        "recall": 0.46621621621621623,
        "f1-score": 0.42857142857142855,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6379310344827587,
        "recall": 0.75,
        "f1-score": 0.6894409937888198,
        "support": 92.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.7255
- **Accuracy:** 0.7500
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "non": {
        "precision": 0.8148148148148148,
        "recall": 0.8918918918918919,
        "f1-score": 0.8516129032258064,
        "support": 74.0
    },
    "oui": {
        "precision": 0.2727272727272727,
        "recall": 0.16666666666666666,
        "f1-score": 0.20689655172413793,
        "support": 18.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.5437710437710437,
        "recall": 0.5292792792792793,
        "f1-score": 0.5292547274749722,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7087542087542087,
        "recall": 0.75,
        "f1-score": 0.725472747497219,
        "support": 92.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7255
- **Accuracy:** 0.7500
- **Best Parameters:** {'max_depth': 5}
```json
{
    "non": {
        "precision": 0.8148148148148148,
        "recall": 0.8918918918918919,
        "f1-score": 0.8516129032258064,
        "support": 74.0
    },
    "oui": {
        "precision": 0.2727272727272727,
        "recall": 0.16666666666666666,
        "f1-score": 0.20689655172413793,
        "support": 18.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.5437710437710437,
        "recall": 0.5292792792792793,
        "f1-score": 0.5292547274749722,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7087542087542087,
        "recall": 0.75,
        "f1-score": 0.725472747497219,
        "support": 92.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.7225
- **Accuracy:** 0.7609
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "non": {
        "precision": 0.8095238095238095,
        "recall": 0.918918918918919,
        "f1-score": 0.8607594936708861,
        "support": 74.0
    },
    "oui": {
        "precision": 0.25,
        "recall": 0.1111111111111111,
        "f1-score": 0.15384615384615385,
        "support": 18.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.5297619047619048,
        "recall": 0.515015015015015,
        "f1-score": 0.50730282375852,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7000517598343684,
        "recall": 0.7608695652173914,
        "f1-score": 0.7224503619660472,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7108
- **Accuracy:** 0.7283
- **Best Parameters:** {'max_depth': 5}
```json
{
    "non": {
        "precision": 0.810126582278481,
        "recall": 0.8648648648648649,
        "f1-score": 0.8366013071895425,
        "support": 74.0
    },
    "oui": {
        "precision": 0.23076923076923078,
        "recall": 0.16666666666666666,
        "f1-score": 0.1935483870967742,
        "support": 18.0
    },
    "accuracy": 0.7282608695652174,
    "macro avg": {
        "precision": 0.5204479065238559,
        "recall": 0.5157657657657658,
        "f1-score": 0.5150748471431583,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.696774056983193,
        "recall": 0.7282608695652174,
        "f1-score": 0.7107866054322617,
        "support": 92.0
    }
}
```

## Word2Vec_SVM_Enhanced

- **Weighted F1 Score:** 0.7063
- **Accuracy:** 0.7826
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.8,
        "recall": 0.972972972972973,
        "f1-score": 0.8780487804878049,
        "support": 74.0
    },
    "oui": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 18.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.4,
        "recall": 0.4864864864864865,
        "f1-score": 0.43902439024390244,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6434782608695653,
        "recall": 0.782608695652174,
        "f1-score": 0.706256627783669,
        "support": 92.0
    }
}
```

## FastText_SVM_Enhanced

- **Weighted F1 Score:** 0.7063
- **Accuracy:** 0.7826
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.8,
        "recall": 0.972972972972973,
        "f1-score": 0.8780487804878049,
        "support": 74.0
    },
    "oui": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 18.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.4,
        "recall": 0.4864864864864865,
        "f1-score": 0.43902439024390244,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6434782608695653,
        "recall": 0.782608695652174,
        "f1-score": 0.706256627783669,
        "support": 92.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6837
- **Accuracy:** 0.7391
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.7906976744186046,
        "recall": 0.918918918918919,
        "f1-score": 0.85,
        "support": 74.0
    },
    "oui": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 18.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.3953488372093023,
        "recall": 0.4594594594594595,
        "f1-score": 0.425,
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

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6837
- **Accuracy:** 0.7391
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.7906976744186046,
        "recall": 0.918918918918919,
        "f1-score": 0.85,
        "support": 74.0
    },
    "oui": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 18.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.3953488372093023,
        "recall": 0.4594594594594595,
        "f1-score": 0.425,
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

