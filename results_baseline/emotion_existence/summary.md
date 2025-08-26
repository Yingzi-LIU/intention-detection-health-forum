# Experiment Results Summary

**Labels:** non, oui

## BoW_LogisticRegression

- **Weighted F1 Score:** 0.7971
- **Accuracy:** 0.8152
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
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

## Bert_LogisticRegression

- **Weighted F1 Score:** 0.7729
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 1, 'solver': 'liblinear'}
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

## Bert_SVM

- **Weighted F1 Score:** 0.7729
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
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

## BoW_MultinomialNB

- **Weighted F1 Score:** 0.7651
- **Accuracy:** 0.7826
- **Best Parameters:** {'alpha': 1.0}
```json
{
    "non": {
        "precision": 0.8375,
        "recall": 0.9054054054054054,
        "f1-score": 0.8701298701298701,
        "support": 74.0
    },
    "oui": {
        "precision": 0.4166666666666667,
        "recall": 0.2777777777777778,
        "f1-score": 0.3333333333333333,
        "support": 18.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.6270833333333333,
        "recall": 0.5915915915915916,
        "f1-score": 0.6017316017316017,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7551630434782608,
        "recall": 0.782608695652174,
        "f1-score": 0.7651044607566346,
        "support": 92.0
    }
}
```

## TF-IDF_LogisticRegression

- **Weighted F1 Score:** 0.7650
- **Accuracy:** 0.7935
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.8313253012048193,
        "recall": 0.9324324324324325,
        "f1-score": 0.8789808917197452,
        "support": 74.0
    },
    "oui": {
        "precision": 0.4444444444444444,
        "recall": 0.2222222222222222,
        "f1-score": 0.2962962962962963,
        "support": 18.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.6378848728246318,
        "recall": 0.5773273273273274,
        "f1-score": 0.5876385940080208,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7556312205343112,
        "recall": 0.7934782608695652,
        "f1-score": 0.7649773839195051,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree

- **Weighted F1 Score:** 0.7650
- **Accuracy:** 0.7935
- **Best Parameters:** {'max_depth': 10}
```json
{
    "non": {
        "precision": 0.8313253012048193,
        "recall": 0.9324324324324325,
        "f1-score": 0.8789808917197452,
        "support": 74.0
    },
    "oui": {
        "precision": 0.4444444444444444,
        "recall": 0.2222222222222222,
        "f1-score": 0.2962962962962963,
        "support": 18.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.6378848728246318,
        "recall": 0.5773273273273274,
        "f1-score": 0.5876385940080208,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7556312205343112,
        "recall": 0.7934782608695652,
        "f1-score": 0.7649773839195051,
        "support": 92.0
    }
}
```

## Bert_KNN

- **Weighted F1 Score:** 0.7650
- **Accuracy:** 0.7935
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "non": {
        "precision": 0.8313253012048193,
        "recall": 0.9324324324324325,
        "f1-score": 0.8789808917197452,
        "support": 74.0
    },
    "oui": {
        "precision": 0.4444444444444444,
        "recall": 0.2222222222222222,
        "f1-score": 0.2962962962962963,
        "support": 18.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.6378848728246318,
        "recall": 0.5773273273273274,
        "f1-score": 0.5876385940080208,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7556312205343112,
        "recall": 0.7934782608695652,
        "f1-score": 0.7649773839195051,
        "support": 92.0
    }
}
```

## BoW_SVM

- **Weighted F1 Score:** 0.7636
- **Accuracy:** 0.7717
- **Best Parameters:** {'C': 1, 'kernel': 'linear'}
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

## TF-IDF_SVM

- **Weighted F1 Score:** 0.7636
- **Accuracy:** 0.7717
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
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

## TF-IDF_MultinomialNB

- **Weighted F1 Score:** 0.7571
- **Accuracy:** 0.7717
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "non": {
        "precision": 0.8354430379746836,
        "recall": 0.8918918918918919,
        "f1-score": 0.8627450980392157,
        "support": 74.0
    },
    "oui": {
        "precision": 0.38461538461538464,
        "recall": 0.2777777777777778,
        "f1-score": 0.3225806451612903,
        "support": 18.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.6100292112950341,
        "recall": 0.5848348348348349,
        "f1-score": 0.592662871600253,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7472376275348208,
        "recall": 0.7717391304347826,
        "f1-score": 0.7570607485630999,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_SVM

- **Weighted F1 Score:** 0.7416
- **Accuracy:** 0.7609
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.825,
        "recall": 0.8918918918918919,
        "f1-score": 0.8571428571428571,
        "support": 74.0
    },
    "oui": {
        "precision": 0.3333333333333333,
        "recall": 0.2222222222222222,
        "f1-score": 0.26666666666666666,
        "support": 18.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.5791666666666666,
        "recall": 0.557057057057057,
        "f1-score": 0.5619047619047619,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7288043478260869,
        "recall": 0.7608695652173914,
        "f1-score": 0.7416149068322981,
        "support": 92.0
    }
}
```

## FastText_KNN

- **Weighted F1 Score:** 0.7328
- **Accuracy:** 0.7609
- **Best Parameters:** {'n_neighbors': 3}
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

## Word2Vec_KNN

- **Weighted F1 Score:** 0.7225
- **Accuracy:** 0.7609
- **Best Parameters:** {'n_neighbors': 7}
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

## BoW_KNN

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "non": {
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

## TF-IDF_ngram_MultinomialNB

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'alpha': 0.5}
```json
{
    "non": {
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
    "non": {
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
    "non": {
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
    "non": {
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
    "non": {
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

## TF-IDF_ngram_LogisticRegression

- **Weighted F1 Score:** 0.7164
- **Accuracy:** 0.7717
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.8045977011494253,
        "recall": 0.9459459459459459,
        "f1-score": 0.8695652173913043,
        "support": 74.0
    },
    "oui": {
        "precision": 0.2,
        "recall": 0.05555555555555555,
        "f1-score": 0.08695652173913043,
        "support": 18.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.5022988505747127,
        "recall": 0.5007507507507507,
        "f1-score": 0.4782608695652174,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6863068465767117,
        "recall": 0.7717391304347826,
        "f1-score": 0.716446124763705,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN

- **Weighted F1 Score:** 0.7155
- **Accuracy:** 0.7500
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "non": {
        "precision": 0.8072289156626506,
        "recall": 0.9054054054054054,
        "f1-score": 0.8535031847133758,
        "support": 74.0
    },
    "oui": {
        "precision": 0.2222222222222222,
        "recall": 0.1111111111111111,
        "f1-score": 0.14814814814814814,
        "support": 18.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.5147255689424364,
        "recall": 0.5082582582582582,
        "f1-score": 0.500825666430762,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6927710843373494,
        "recall": 0.75,
        "f1-score": 0.7154989384288747,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.7108
- **Accuracy:** 0.7283
- **Best Parameters:** {'max_depth': None}
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

## BoW_DecisionTree

- **Weighted F1 Score:** 0.7101
- **Accuracy:** 0.7609
- **Best Parameters:** {'max_depth': 10}
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

## FastText_DecisionTree

- **Weighted F1 Score:** 0.7036
- **Accuracy:** 0.7500
- **Best Parameters:** {'max_depth': 5}
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

## TF-IDF_KNN

- **Weighted F1 Score:** 0.6777
- **Accuracy:** 0.7065
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "non": {
        "precision": 0.7901234567901234,
        "recall": 0.8648648648648649,
        "f1-score": 0.8258064516129032,
        "support": 74.0
    },
    "oui": {
        "precision": 0.09090909090909091,
        "recall": 0.05555555555555555,
        "f1-score": 0.06896551724137931,
        "support": 18.0
    },
    "accuracy": 0.7065217391304348,
    "macro avg": {
        "precision": 0.4405162738496072,
        "recall": 0.46021021021021025,
        "f1-score": 0.4473859844271413,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6533206460742692,
        "recall": 0.7065217391304348,
        "f1-score": 0.6777288774967355,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.6665
- **Accuracy:** 0.6739
- **Best Parameters:** {'max_depth': 5}
```json
{
    "non": {
        "precision": 0.7894736842105263,
        "recall": 0.8108108108108109,
        "f1-score": 0.8,
        "support": 74.0
    },
    "oui": {
        "precision": 0.125,
        "recall": 0.1111111111111111,
        "f1-score": 0.11764705882352941,
        "support": 18.0
    },
    "accuracy": 0.6739130434782609,
    "macro avg": {
        "precision": 0.45723684210526316,
        "recall": 0.46096096096096095,
        "f1-score": 0.45882352941176474,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6594679633867276,
        "recall": 0.6739130434782609,
        "f1-score": 0.6664961636828645,
        "support": 92.0
    }
}
```

## Bert_DecisionTree

- **Weighted F1 Score:** 0.6569
- **Accuracy:** 0.6413
- **Best Parameters:** {'max_depth': 10}
```json
{
    "non": {
        "precision": 0.7971014492753623,
        "recall": 0.7432432432432432,
        "f1-score": 0.7692307692307693,
        "support": 74.0
    },
    "oui": {
        "precision": 0.17391304347826086,
        "recall": 0.2222222222222222,
        "f1-score": 0.1951219512195122,
        "support": 18.0
    },
    "accuracy": 0.6413043478260869,
    "macro avg": {
        "precision": 0.4855072463768116,
        "recall": 0.4827327327327327,
        "f1-score": 0.48217636022514077,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6751732829237556,
        "recall": 0.6413043478260869,
        "f1-score": 0.656905130924219,
        "support": 92.0
    }
}
```

