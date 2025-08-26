# Experiment Results Summary

**Labels:** fonction_phatique, partage_experience, recherche_information

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.8293
- **Accuracy:** 0.8478
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.6,
        "f1-score": 0.75,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.85,
        "recall": 0.9714285714285714,
        "f1-score": 0.9066666666666666,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.6666666666666666,
        "recall": 0.3333333333333333,
        "f1-score": 0.4444444444444444,
        "support": 12.0
    },
    "accuracy": 0.8478260869565217,
    "macro avg": {
        "precision": 0.8388888888888889,
        "recall": 0.6349206349206349,
        "f1-score": 0.7003703703703703,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.842391304347826,
        "recall": 0.8478260869565217,
        "f1-score": 0.8293478260869565,
        "support": 92.0
    }
}
```

## TF-IDF_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.8105
- **Accuracy:** 0.8478
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.6,
        "f1-score": 0.75,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8333333333333334,
        "recall": 1.0,
        "f1-score": 0.9090909090909091,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 1.0,
        "recall": 0.16666666666666666,
        "f1-score": 0.2857142857142857,
        "support": 12.0
    },
    "accuracy": 0.8478260869565217,
    "macro avg": {
        "precision": 0.9444444444444445,
        "recall": 0.5888888888888889,
        "f1-score": 0.6482683982683982,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8731884057971016,
        "recall": 0.8478260869565217,
        "f1-score": 0.8104884246188593,
        "support": 92.0
    }
}
```

## TF-IDF_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.8105
- **Accuracy:** 0.8478
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.6,
        "f1-score": 0.75,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8333333333333334,
        "recall": 1.0,
        "f1-score": 0.9090909090909091,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 1.0,
        "recall": 0.16666666666666666,
        "f1-score": 0.2857142857142857,
        "support": 12.0
    },
    "accuracy": 0.8478260869565217,
    "macro avg": {
        "precision": 0.9444444444444445,
        "recall": 0.5888888888888889,
        "f1-score": 0.6482683982683982,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8731884057971016,
        "recall": 0.8478260869565217,
        "f1-score": 0.8104884246188593,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.8105
- **Accuracy:** 0.8478
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.6,
        "f1-score": 0.75,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8333333333333334,
        "recall": 1.0,
        "f1-score": 0.9090909090909091,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 1.0,
        "recall": 0.16666666666666666,
        "f1-score": 0.2857142857142857,
        "support": 12.0
    },
    "accuracy": 0.8478260869565217,
    "macro avg": {
        "precision": 0.9444444444444445,
        "recall": 0.5888888888888889,
        "f1-score": 0.6482683982683982,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8731884057971016,
        "recall": 0.8478260869565217,
        "f1-score": 0.8104884246188593,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.8025
- **Accuracy:** 0.8261
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.8571428571428571,
        "recall": 0.6,
        "f1-score": 0.7058823529411765,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8375,
        "recall": 0.9571428571428572,
        "f1-score": 0.8933333333333333,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.6,
        "recall": 0.25,
        "f1-score": 0.35294117647058826,
        "support": 12.0
    },
    "accuracy": 0.8260869565217391,
    "macro avg": {
        "precision": 0.7648809523809524,
        "recall": 0.6023809523809524,
        "f1-score": 0.650718954248366,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8086568322981367,
        "recall": 0.8260869565217391,
        "f1-score": 0.8024722932651321,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.7933
- **Accuracy:** 0.8152
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.6,
        "f1-score": 0.75,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8481012658227848,
        "recall": 0.9571428571428572,
        "f1-score": 0.8993288590604027,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.2857142857142857,
        "recall": 0.16666666666666666,
        "f1-score": 0.21052631578947367,
        "support": 12.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.7112718505123569,
        "recall": 0.5746031746031747,
        "f1-score": 0.6199517249499588,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7912571743061562,
        "recall": 0.8152173913043478,
        "f1-score": 0.7932536513445855,
        "support": 92.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.7902
- **Accuracy:** 0.8152
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.6,
        "f1-score": 0.75,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8375,
        "recall": 0.9571428571428572,
        "f1-score": 0.8933333333333333,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.3333333333333333,
        "recall": 0.16666666666666666,
        "f1-score": 0.2222222222222222,
        "support": 12.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.7236111111111111,
        "recall": 0.5746031746031747,
        "f1-score": 0.6218518518518518,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7894021739130435,
        "recall": 0.8152173913043478,
        "f1-score": 0.7902173913043479,
        "support": 92.0
    }
}
```

## BoW_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.7888
- **Accuracy:** 0.8370
- **Best Parameters:** {'classifier__alpha': 0.5}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.6,
        "f1-score": 0.75,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8235294117647058,
        "recall": 1.0,
        "f1-score": 0.9032258064516129,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 1.0,
        "recall": 0.08333333333333333,
        "f1-score": 0.15384615384615385,
        "support": 12.0
    },
    "accuracy": 0.8369565217391305,
    "macro avg": {
        "precision": 0.9411764705882352,
        "recall": 0.5611111111111111,
        "f1-score": 0.6023573200992556,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8657289002557544,
        "recall": 0.8369565217391305,
        "f1-score": 0.788825655410508,
        "support": 92.0
    }
}
```

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.7784
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.8571428571428571,
        "recall": 0.6,
        "f1-score": 0.7058823529411765,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8311688311688312,
        "recall": 0.9142857142857143,
        "f1-score": 0.8707482993197279,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.375,
        "recall": 0.25,
        "f1-score": 0.3,
        "support": 12.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.6877705627705627,
        "recall": 0.5880952380952381,
        "f1-score": 0.6255435507536348,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7744918125352909,
        "recall": 0.7934782608695652,
        "f1-score": 0.7783826574107904,
        "support": 92.0
    }
}
```

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7717
- **Accuracy:** 0.8152
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 0.8571428571428571,
        "recall": 0.6,
        "f1-score": 0.7058823529411765,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8192771084337349,
        "recall": 0.9714285714285714,
        "f1-score": 0.8888888888888888,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.08333333333333333,
        "f1-score": 0.14285714285714285,
        "support": 12.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.725473321858864,
        "recall": 0.5515873015873015,
        "f1-score": 0.5792094615624027,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7817481104542393,
        "recall": 0.8152173913043478,
        "f1-score": 0.7716883854991271,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7652
- **Accuracy:** 0.7717
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "fonction_phatique": {
        "precision": 0.6666666666666666,
        "recall": 0.6,
        "f1-score": 0.631578947368421,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8356164383561644,
        "recall": 0.8714285714285714,
        "f1-score": 0.8531468531468531,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.4,
        "recall": 0.3333333333333333,
        "f1-score": 0.36363636363636365,
        "support": 12.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.6340943683409437,
        "recall": 0.6015873015873016,
        "f1-score": 0.6161207213838793,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7604327972999801,
        "recall": 0.7717391304347826,
        "f1-score": 0.7652141908434814,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.7644
- **Accuracy:** 0.8261
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.6,
        "f1-score": 0.75,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.813953488372093,
        "recall": 1.0,
        "f1-score": 0.8974358974358975,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8260869565217391,
        "recall": 0.95,
        "f1-score": 0.8837209302325582,
        "support": 80.0
    },
    "macro avg": {
        "precision": 0.9069767441860466,
        "recall": 0.8,
        "f1-score": 0.8237179487179487,
        "support": 80.0
    },
    "weighted avg": {
        "precision": 0.8372093023255814,
        "recall": 0.95,
        "f1-score": 0.8790064102564102,
        "support": 80.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.7632
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 0.6666666666666666,
        "recall": 0.6,
        "f1-score": 0.631578947368421,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8421052631578947,
        "recall": 0.9142857142857143,
        "f1-score": 0.8767123287671232,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.2857142857142857,
        "recall": 0.16666666666666666,
        "f1-score": 0.21052631578947367,
        "support": 12.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.5981620718462822,
        "recall": 0.5603174603174603,
        "f1-score": 0.5729391973083393,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.750463114307508,
        "recall": 0.782608695652174,
        "f1-score": 0.7631735682267013,
        "support": 92.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7260
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "fonction_phatique": {
        "precision": 0.7142857142857143,
        "recall": 0.5,
        "f1-score": 0.5882352941176471,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.7976190476190477,
        "recall": 0.9571428571428572,
        "f1-score": 0.8701298701298701,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 12.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.503968253968254,
        "recall": 0.48571428571428577,
        "f1-score": 0.48612172141583904,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6845238095238095,
        "recall": 0.782608695652174,
        "f1-score": 0.7259939548942106,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7238
- **Accuracy:** 0.7391
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.45454545454545453,
        "recall": 0.5,
        "f1-score": 0.47619047619047616,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8243243243243243,
        "recall": 0.8714285714285714,
        "f1-score": 0.8472222222222222,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.2857142857142857,
        "recall": 0.16666666666666666,
        "f1-score": 0.21052631578947367,
        "support": 12.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.5215280215280216,
        "recall": 0.5126984126984128,
        "f1-score": 0.5113130047340574,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.713877485616616,
        "recall": 0.7391304347826086,
        "f1-score": 0.7238453924666739,
        "support": 92.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.8415
- **Accuracy:** 0.8478
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.7,
        "f1-score": 0.8235294117647058,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.88,
        "recall": 0.9428571428571428,
        "f1-score": 0.9103448275862069,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.4166666666666667,
        "f1-score": 0.45454545454545453,
        "support": 12.0
    },
    "accuracy": 0.8478260869565217,
    "macro avg": {
        "precision": 0.7933333333333333,
        "recall": 0.6865079365079364,
        "f1-score": 0.729473231298789,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8434782608695651,
        "recall": 0.8478260869565217,
        "f1-score": 0.8414562772089892,
        "support": 92.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.7776
- **Accuracy:** 0.8043
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "fonction_phatique": {
        "precision": 0.875,
        "recall": 0.7,
        "f1-score": 0.7777777777777778,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8461538461538461,
        "recall": 0.9428571428571428,
        "f1-score": 0.8918918918918919,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.16666666666666666,
        "recall": 0.08333333333333333,
        "f1-score": 0.1111111111111111,
        "support": 12.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.6292735042735044,
        "recall": 0.5753968253968254,
        "f1-score": 0.5935935935935936,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7606605351170568,
        "recall": 0.8043478260869565,
        "f1-score": 0.777647212429821,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7582
- **Accuracy:** 0.7935
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.8571428571428571,
        "recall": 0.6,
        "f1-score": 0.7058823529411765,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8148148148148148,
        "recall": 0.9428571428571428,
        "f1-score": 0.8741721854304636,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.25,
        "recall": 0.08333333333333333,
        "f1-score": 0.125,
        "support": 12.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.640652557319224,
        "recall": 0.542063492063492,
        "f1-score": 0.5683515127905467,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7457441913963653,
        "recall": 0.7934782608695652,
        "f1-score": 0.7581617011906979,
        "support": 92.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7363
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.4,
        "f1-score": 0.5714285714285714,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.7954545454545454,
        "recall": 1.0,
        "f1-score": 0.8860759493670886,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8043478260869565,
        "recall": 0.925,
        "f1-score": 0.8604651162790697,
        "support": 80.0
    },
    "macro avg": {
        "precision": 0.8977272727272727,
        "recall": 0.7,
        "f1-score": 0.72875226039783,
        "support": 80.0
    },
    "weighted avg": {
        "precision": 0.8210227272727273,
        "recall": 0.925,
        "f1-score": 0.8467450271247738,
        "support": 80.0
    }
}
```

## Word2Vec_SVM_Enhanced

- **Weighted F1 Score:** 0.7363
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.4,
        "f1-score": 0.5714285714285714,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.7954545454545454,
        "recall": 1.0,
        "f1-score": 0.8860759493670886,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8043478260869565,
        "recall": 0.925,
        "f1-score": 0.8604651162790697,
        "support": 80.0
    },
    "macro avg": {
        "precision": 0.8977272727272727,
        "recall": 0.7,
        "f1-score": 0.72875226039783,
        "support": 80.0
    },
    "weighted avg": {
        "precision": 0.8210227272727273,
        "recall": 0.925,
        "f1-score": 0.8467450271247738,
        "support": 80.0
    }
}
```

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7363
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.4,
        "f1-score": 0.5714285714285714,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.7954545454545454,
        "recall": 1.0,
        "f1-score": 0.8860759493670886,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8043478260869565,
        "recall": 0.925,
        "f1-score": 0.8604651162790697,
        "support": 80.0
    },
    "macro avg": {
        "precision": 0.8977272727272727,
        "recall": 0.7,
        "f1-score": 0.72875226039783,
        "support": 80.0
    },
    "weighted avg": {
        "precision": 0.8210227272727273,
        "recall": 0.925,
        "f1-score": 0.8467450271247738,
        "support": 80.0
    }
}
```

## FastText_SVM_Enhanced

- **Weighted F1 Score:** 0.7363
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.4,
        "f1-score": 0.5714285714285714,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.7954545454545454,
        "recall": 1.0,
        "f1-score": 0.8860759493670886,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8043478260869565,
        "recall": 0.925,
        "f1-score": 0.8604651162790697,
        "support": 80.0
    },
    "macro avg": {
        "precision": 0.8977272727272727,
        "recall": 0.7,
        "f1-score": 0.72875226039783,
        "support": 80.0
    },
    "weighted avg": {
        "precision": 0.8210227272727273,
        "recall": 0.925,
        "f1-score": 0.8467450271247738,
        "support": 80.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7294
- **Accuracy:** 0.7500
- **Best Parameters:** {'max_depth': 10}
```json
{
    "fonction_phatique": {
        "precision": 0.5714285714285714,
        "recall": 0.4,
        "f1-score": 0.47058823529411764,
        "support": 10.0
    },
    "partage_experience": {
        "precision": 0.8181818181818182,
        "recall": 0.9,
        "f1-score": 0.8571428571428571,
        "support": 70.0
    },
    "recherche_information": {
        "precision": 0.25,
        "recall": 0.16666666666666666,
        "f1-score": 0.2,
        "support": 12.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.5465367965367965,
        "recall": 0.48888888888888893,
        "f1-score": 0.5092436974789916,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7172501411631846,
        "recall": 0.75,
        "f1-score": 0.7294117647058824,
        "support": 92.0
    }
}
```

