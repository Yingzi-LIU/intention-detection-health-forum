# Experiment Results Summary

**Labels:** non, oui

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

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.7287
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.8045977011494253,
        "recall": 0.958904109589041,
        "f1-score": 0.875,
        "support": 73.0
    },
    "oui": {
        "precision": 0.4,
        "recall": 0.10526315789473684,
        "f1-score": 0.16666666666666666,
        "support": 19.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.6022988505747127,
        "recall": 0.5320836337418889,
        "f1-score": 0.5208333333333334,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7210394802598701,
        "recall": 0.782608695652174,
        "f1-score": 0.7287137681159421,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7217
- **Accuracy:** 0.7717
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "non": {
        "precision": 0.8023255813953488,
        "recall": 0.9452054794520548,
        "f1-score": 0.8679245283018868,
        "support": 73.0
    },
    "oui": {
        "precision": 0.3333333333333333,
        "recall": 0.10526315789473684,
        "f1-score": 0.16,
        "support": 19.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.5678294573643411,
        "recall": 0.5252343186733959,
        "f1-score": 0.5139622641509434,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.705468486686889,
        "recall": 0.7717391304347826,
        "f1-score": 0.7217227235438884,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.7198
- **Accuracy:** 0.7391
- **Best Parameters:** {'classifier__n_neighbors': 3}
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

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.7185
- **Accuracy:** 0.7500
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "non": {
        "precision": 0.8048780487804879,
        "recall": 0.9041095890410958,
        "f1-score": 0.8516129032258064,
        "support": 73.0
    },
    "oui": {
        "precision": 0.3,
        "recall": 0.15789473684210525,
        "f1-score": 0.20689655172413793,
        "support": 19.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.552439024390244,
        "recall": 0.5310021629416005,
        "f1-score": 0.5292547274749722,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7006097560975609,
        "recall": 0.75,
        "f1-score": 0.7184649610678532,
        "support": 92.0
    }
}
```

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.7038
- **Accuracy:** 0.7283
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.8,
        "recall": 0.8767123287671232,
        "f1-score": 0.8366013071895425,
        "support": 73.0
    },
    "oui": {
        "precision": 0.25,
        "recall": 0.15789473684210525,
        "f1-score": 0.1935483870967742,
        "support": 19.0
    },
    "accuracy": 0.7282608695652174,
    "macro avg": {
        "precision": 0.525,
        "recall": 0.5173035328046143,
        "f1-score": 0.5150748471431583,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6864130434782609,
        "recall": 0.7282608695652174,
        "f1-score": 0.7037968997790796,
        "support": 92.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.7016
- **Accuracy:** 0.7609
- **Best Parameters:** {'classifier__n_neighbors': 3}
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

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.6857
- **Accuracy:** 0.7609
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.7865168539325843,
        "recall": 0.958904109589041,
        "f1-score": 0.8641975308641975,
        "support": 73.0
    },
    "oui": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 19.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.39325842696629215,
        "recall": 0.4794520547945205,
        "f1-score": 0.43209876543209874,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6240840254030289,
        "recall": 0.7608695652173914,
        "f1-score": 0.6857219538378958,
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
- **Best Parameters:** {'n_neighbors': 7}
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

- **Weighted F1 Score:** 0.6965
- **Accuracy:** 0.7174
- **Best Parameters:** {'max_depth': 5}
```json
{
    "non": {
        "precision": 0.7974683544303798,
        "recall": 0.863013698630137,
        "f1-score": 0.8289473684210527,
        "support": 73.0
    },
    "oui": {
        "precision": 0.23076923076923078,
        "recall": 0.15789473684210525,
        "f1-score": 0.1875,
        "support": 19.0
    },
    "accuracy": 0.717391304347826,
    "macro avg": {
        "precision": 0.5141187925998053,
        "recall": 0.5104542177361211,
        "f1-score": 0.5082236842105263,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.680432665848186,
        "recall": 0.717391304347826,
        "f1-score": 0.6964745423340962,
        "support": 92.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.6893
- **Accuracy:** 0.6957
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "non": {
        "precision": 0.8,
        "recall": 0.821917808219178,
        "f1-score": 0.8108108108108109,
        "support": 73.0
    },
    "oui": {
        "precision": 0.23529411764705882,
        "recall": 0.21052631578947367,
        "f1-score": 0.2222222222222222,
        "support": 19.0
    },
    "accuracy": 0.6956521739130435,
    "macro avg": {
        "precision": 0.5176470588235295,
        "recall": 0.5162220620043259,
        "f1-score": 0.5165165165165165,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.683375959079284,
        "recall": 0.6956521739130435,
        "f1-score": 0.6892544718631676,
        "support": 92.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.6888
- **Accuracy:** 0.7391
- **Best Parameters:** {'max_depth': 5}
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

