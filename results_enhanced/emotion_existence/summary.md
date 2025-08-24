# Experiment Results Summary

**Labels:** non, oui

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.7813
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.8461538461538461,
        "recall": 0.9041095890410958,
        "f1-score": 0.8741721854304636,
        "support": 73.0
    },
    "oui": {
        "precision": 0.5,
        "recall": 0.3684210526315789,
        "f1-score": 0.42424242424242425,
        "support": 19.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.6730769230769231,
        "recall": 0.6362653208363374,
        "f1-score": 0.649207304836444,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.774665551839465,
        "recall": 0.7934782608695652,
        "f1-score": 0.7812519086633686,
        "support": 92.0
    }
}
```

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7636
- **Accuracy:** 0.8152
- **Best Parameters:** {'classifier__C': 1, 'classifier__solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.8181818181818182,
        "recall": 0.9863013698630136,
        "f1-score": 0.8944099378881988,
        "support": 73.0
    },
    "oui": {
        "precision": 0.75,
        "recall": 0.15789473684210525,
        "f1-score": 0.2608695652173913,
        "support": 19.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.7840909090909092,
        "recall": 0.5720980533525595,
        "f1-score": 0.577639751552795,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8041007905138341,
        "recall": 0.8152173913043478,
        "f1-score": 0.7635700783148799,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7586
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "non": {
        "precision": 0.8214285714285714,
        "recall": 0.9452054794520548,
        "f1-score": 0.8789808917197452,
        "support": 73.0
    },
    "oui": {
        "precision": 0.5,
        "recall": 0.21052631578947367,
        "f1-score": 0.2962962962962963,
        "support": 19.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.6607142857142857,
        "recall": 0.5778658976207642,
        "f1-score": 0.5876385940080208,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7550465838509318,
        "recall": 0.7934782608695652,
        "f1-score": 0.7586438557083809,
        "support": 92.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7482
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "non": {
        "precision": 0.813953488372093,
        "recall": 0.958904109589041,
        "f1-score": 0.8805031446540881,
        "support": 73.0
    },
    "oui": {
        "precision": 0.5,
        "recall": 0.15789473684210525,
        "f1-score": 0.24,
        "support": 19.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.6569767441860466,
        "recall": 0.5583994232155731,
        "f1-score": 0.560251572327044,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7491152679474216,
        "recall": 0.7934782608695652,
        "f1-score": 0.7482253213016135,
        "support": 92.0
    }
}
```

## TF-IDF_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7407
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.8117647058823529,
        "recall": 0.9452054794520548,
        "f1-score": 0.8734177215189873,
        "support": 73.0
    },
    "oui": {
        "precision": 0.42857142857142855,
        "recall": 0.15789473684210525,
        "f1-score": 0.23076923076923078,
        "support": 19.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.6201680672268908,
        "recall": 0.55155010814708,
        "f1-score": 0.5520934761441091,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7326269638290099,
        "recall": 0.782608695652174,
        "f1-score": 0.7406968375597984,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7407
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "non": {
        "precision": 0.8117647058823529,
        "recall": 0.9452054794520548,
        "f1-score": 0.8734177215189873,
        "support": 73.0
    },
    "oui": {
        "precision": 0.42857142857142855,
        "recall": 0.15789473684210525,
        "f1-score": 0.23076923076923078,
        "support": 19.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.6201680672268908,
        "recall": 0.55155010814708,
        "f1-score": 0.5520934761441091,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7326269638290099,
        "recall": 0.782608695652174,
        "f1-score": 0.7406968375597984,
        "support": 92.0
    }
}
```

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.7198
- **Accuracy:** 0.7391
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.810126582278481,
        "recall": 0.8767123287671232,
        "f1-score": 0.8421052631578947,
        "support": 73.0
    },
    "oui": {
        "precision": 0.3076923076923077,
        "recall": 0.21052631578947367,
        "f1-score": 0.25,
        "support": 19.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.5589094449853944,
        "recall": 0.5436193222782985,
        "f1-score": 0.5460526315789473,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.706362982092206,
        "recall": 0.7391304347826086,
        "f1-score": 0.7198226544622426,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.7079
- **Accuracy:** 0.7717
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.7954545454545454,
        "recall": 0.958904109589041,
        "f1-score": 0.8695652173913043,
        "support": 73.0
    },
    "oui": {
        "precision": 0.25,
        "recall": 0.05263157894736842,
        "f1-score": 0.08695652173913043,
        "support": 19.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.5227272727272727,
        "recall": 0.5057678442682048,
        "f1-score": 0.4782608695652174,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6828063241106719,
        "recall": 0.7717391304347826,
        "f1-score": 0.7079395085066164,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7016
- **Accuracy:** 0.7609
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.7931034482758621,
        "recall": 0.9452054794520548,
        "f1-score": 0.8625,
        "support": 73.0
    },
    "oui": {
        "precision": 0.2,
        "recall": 0.05263157894736842,
        "f1-score": 0.08333333333333333,
        "support": 19.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.496551724137931,
        "recall": 0.4989185291997116,
        "f1-score": 0.4729166666666667,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6706146926536732,
        "recall": 0.7608695652173914,
        "f1-score": 0.7015851449275362,
        "support": 92.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.6888
- **Accuracy:** 0.7391
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "non": {
        "precision": 0.788235294117647,
        "recall": 0.9178082191780822,
        "f1-score": 0.8481012658227848,
        "support": 73.0
    },
    "oui": {
        "precision": 0.14285714285714285,
        "recall": 0.05263157894736842,
        "f1-score": 0.07692307692307693,
        "support": 19.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.46554621848739497,
        "recall": 0.48521989906272533,
        "f1-score": 0.4625121713729309,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.654950675922543,
        "recall": 0.7391304347826086,
        "f1-score": 0.6888362050717581,
        "support": 92.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.6871
- **Accuracy:** 0.7174
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "non": {
        "precision": 0.7901234567901234,
        "recall": 0.8767123287671232,
        "f1-score": 0.8311688311688312,
        "support": 73.0
    },
    "oui": {
        "precision": 0.18181818181818182,
        "recall": 0.10526315789473684,
        "f1-score": 0.13333333333333333,
        "support": 19.0
    },
    "accuracy": 0.717391304347826,
    "macro avg": {
        "precision": 0.48597081930415265,
        "recall": 0.49098774333093004,
        "f1-score": 0.48225108225108226,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6644951934807007,
        "recall": 0.717391304347826,
        "f1-score": 0.6870506305288915,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.6871
- **Accuracy:** 0.7174
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "non": {
        "precision": 0.7901234567901234,
        "recall": 0.8767123287671232,
        "f1-score": 0.8311688311688312,
        "support": 73.0
    },
    "oui": {
        "precision": 0.18181818181818182,
        "recall": 0.10526315789473684,
        "f1-score": 0.13333333333333333,
        "support": 19.0
    },
    "accuracy": 0.717391304347826,
    "macro avg": {
        "precision": 0.48597081930415265,
        "recall": 0.49098774333093004,
        "f1-score": 0.48225108225108226,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6644951934807007,
        "recall": 0.717391304347826,
        "f1-score": 0.6870506305288915,
        "support": 92.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.7336
- **Accuracy:** 0.7391
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "non": {
        "precision": 0.8266666666666667,
        "recall": 0.8493150684931506,
        "f1-score": 0.8378378378378378,
        "support": 73.0
    },
    "oui": {
        "precision": 0.35294117647058826,
        "recall": 0.3157894736842105,
        "f1-score": 0.3333333333333333,
        "support": 19.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.5898039215686275,
        "recall": 0.5825522710886806,
        "f1-score": 0.5855855855855856,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7288320545609548,
        "recall": 0.7391304347826086,
        "f1-score": 0.7336466901684292,
        "support": 92.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7115
- **Accuracy:** 0.7174
- **Best Parameters:** {'max_depth': 10}
```json
{
    "non": {
        "precision": 0.8133333333333334,
        "recall": 0.8356164383561644,
        "f1-score": 0.8243243243243243,
        "support": 73.0
    },
    "oui": {
        "precision": 0.29411764705882354,
        "recall": 0.2631578947368421,
        "f1-score": 0.2777777777777778,
        "support": 19.0
    },
    "accuracy": 0.717391304347826,
    "macro avg": {
        "precision": 0.5537254901960784,
        "recall": 0.5493871665465032,
        "f1-score": 0.5510510510510511,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7061040068201194,
        "recall": 0.717391304347826,
        "f1-score": 0.7114505810157984,
        "support": 92.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7021
- **Accuracy:** 0.7935
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "oui": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 19.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.3967391304347826,
        "recall": 0.5,
        "f1-score": 0.44242424242424244,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6296077504725898,
        "recall": 0.7934782608695652,
        "f1-score": 0.7021080368906456,
        "support": 92.0
    }
}
```

## Word2Vec_SVM_Enhanced

- **Weighted F1 Score:** 0.7021
- **Accuracy:** 0.7935
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "oui": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 19.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.3967391304347826,
        "recall": 0.5,
        "f1-score": 0.44242424242424244,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6296077504725898,
        "recall": 0.7934782608695652,
        "f1-score": 0.7021080368906456,
        "support": 92.0
    }
}
```

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7021
- **Accuracy:** 0.7935
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "oui": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 19.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.3967391304347826,
        "recall": 0.5,
        "f1-score": 0.44242424242424244,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6296077504725898,
        "recall": 0.7934782608695652,
        "f1-score": 0.7021080368906456,
        "support": 92.0
    }
}
```

## FastText_SVM_Enhanced

- **Weighted F1 Score:** 0.7021
- **Accuracy:** 0.7935
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "oui": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 19.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.3967391304347826,
        "recall": 0.5,
        "f1-score": 0.44242424242424244,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6296077504725898,
        "recall": 0.7934782608695652,
        "f1-score": 0.7021080368906456,
        "support": 92.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.7016
- **Accuracy:** 0.7609
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "non": {
        "precision": 0.7931034482758621,
        "recall": 0.9452054794520548,
        "f1-score": 0.8625,
        "support": 73.0
    },
    "oui": {
        "precision": 0.2,
        "recall": 0.05263157894736842,
        "f1-score": 0.08333333333333333,
        "support": 19.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.496551724137931,
        "recall": 0.4989185291997116,
        "f1-score": 0.4729166666666667,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6706146926536732,
        "recall": 0.7608695652173914,
        "f1-score": 0.7015851449275362,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.6661
- **Accuracy:** 0.6848
- **Best Parameters:** {'max_depth': 5}
```json
{
    "non": {
        "precision": 0.782051282051282,
        "recall": 0.8356164383561644,
        "f1-score": 0.8079470198675497,
        "support": 73.0
    },
    "oui": {
        "precision": 0.14285714285714285,
        "recall": 0.10526315789473684,
        "f1-score": 0.12121212121212122,
        "support": 19.0
    },
    "accuracy": 0.6847826086956522,
    "macro avg": {
        "precision": 0.4624542124542125,
        "recall": 0.4704397981254506,
        "f1-score": 0.46457957053983545,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6500437967829272,
        "recall": 0.6847826086956522,
        "f1-score": 0.6661213342756678,
        "support": 92.0
    }
}
```

