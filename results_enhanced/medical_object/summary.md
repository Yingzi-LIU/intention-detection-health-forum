# Experiment Results Summary

**Labels:** diagnostique, nan, symptome, traitement

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.5516
- **Accuracy:** 0.5543
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "0": {
        "precision": 0.5454545454545454,
        "recall": 0.3157894736842105,
        "f1-score": 0.4,
        "support": 19.0
    },
    "1": {
        "precision": 0.8,
        "recall": 0.6666666666666666,
        "f1-score": 0.7272727272727273,
        "support": 12.0
    },
    "2": {
        "precision": 0.6060606060606061,
        "recall": 0.6060606060606061,
        "f1-score": 0.6060606060606061,
        "support": 33.0
    },
    "3": {
        "precision": 0.4473684210526316,
        "recall": 0.6071428571428571,
        "f1-score": 0.5151515151515151,
        "support": 28.0
    },
    "accuracy": 0.5543478260869565,
    "macro avg": {
        "precision": 0.5997208931419458,
        "recall": 0.5489149008885851,
        "f1-score": 0.5621212121212121,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5705429581859789,
        "recall": 0.5543478260869565,
        "f1-score": 0.5516469038208168,
        "support": 92.0
    }
}
```

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.5652
- **Accuracy:** 0.5652
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.5333333333333333,
        "recall": 0.42105263157894735,
        "f1-score": 0.47058823529411764,
        "support": 19.0
    },
    "1": {
        "precision": 0.7272727272727273,
        "recall": 0.6666666666666666,
        "f1-score": 0.6956521739130435,
        "support": 12.0
    },
    "2": {
        "precision": 0.6129032258064516,
        "recall": 0.5757575757575758,
        "f1-score": 0.59375,
        "support": 33.0
    },
    "3": {
        "precision": 0.4857142857142857,
        "recall": 0.6071428571428571,
        "f1-score": 0.5396825396825397,
        "support": 28.0
    },
    "accuracy": 0.5652173913043478,
    "macro avg": {
        "precision": 0.5898058930316995,
        "recall": 0.5676549327865117,
        "f1-score": 0.5749182372224252,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5726783968719452,
        "recall": 0.5652173913043478,
        "f1-score": 0.5651506920506072,
        "support": 92.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.5069
- **Accuracy:** 0.5109
- **Best Parameters:** {'classifier__max_depth': None}
```json
{
    "0": {
        "precision": 0.35714285714285715,
        "recall": 0.2631578947368421,
        "f1-score": 0.30303030303030304,
        "support": 19.0
    },
    "1": {
        "precision": 0.8,
        "recall": 0.6666666666666666,
        "f1-score": 0.7272727272727273,
        "support": 12.0
    },
    "2": {
        "precision": 0.5,
        "recall": 0.5454545454545454,
        "f1-score": 0.5217391304347826,
        "support": 33.0
    },
    "3": {
        "precision": 0.5,
        "recall": 0.5714285714285714,
        "f1-score": 0.5333333333333333,
        "support": 28.0
    },
    "accuracy": 0.5108695652173914,
    "macro avg": {
        "precision": 0.5392857142857144,
        "recall": 0.5116769195716564,
        "f1-score": 0.5213438735177865,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5096273291925466,
        "recall": 0.5108695652173914,
        "f1-score": 0.5069084035057569,
        "support": 92.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.4451
- **Accuracy:** 0.5000
- **Best Parameters:** {'classifier__n_neighbors': 5}
```json
{
    "0": {
        "precision": 0.5,
        "recall": 0.21052631578947367,
        "f1-score": 0.2962962962962963,
        "support": 19.0
    },
    "1": {
        "precision": 0.5,
        "recall": 0.8333333333333334,
        "f1-score": 0.625,
        "support": 12.0
    },
    "2": {
        "precision": 0.4909090909090909,
        "recall": 0.8181818181818182,
        "f1-score": 0.6136363636363636,
        "support": 33.0
    },
    "3": {
        "precision": 0.5555555555555556,
        "recall": 0.17857142857142858,
        "f1-score": 0.2702702702702703,
        "support": 28.0
    },
    "accuracy": 0.5,
    "macro avg": {
        "precision": 0.5116161616161616,
        "recall": 0.5101532239690134,
        "f1-score": 0.45130073255073255,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5136473429951691,
        "recall": 0.5,
        "f1-score": 0.4450782304043174,
        "support": 92.0
    }
}
```

## TF-IDF_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.5981
- **Accuracy:** 0.5978
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "0": {
        "precision": 0.5,
        "recall": 0.3157894736842105,
        "f1-score": 0.3870967741935484,
        "support": 19.0
    },
    "1": {
        "precision": 1.0,
        "recall": 0.6666666666666666,
        "f1-score": 0.8,
        "support": 12.0
    },
    "2": {
        "precision": 0.7058823529411765,
        "recall": 0.7272727272727273,
        "f1-score": 0.7164179104477612,
        "support": 33.0
    },
    "3": {
        "precision": 0.4473684210526316,
        "recall": 0.6071428571428571,
        "f1-score": 0.5151515151515151,
        "support": 28.0
    },
    "accuracy": 0.5978260869565217,
    "macro avg": {
        "precision": 0.663312693498452,
        "recall": 0.5792179311916154,
        "f1-score": 0.6046665499482061,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6230481895275273,
        "recall": 0.5978260869565217,
        "f1-score": 0.5980529584640866,
        "support": 92.0
    }
}
```

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.5526
- **Accuracy:** 0.5435
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.42105263157894735,
        "recall": 0.42105263157894735,
        "f1-score": 0.42105263157894735,
        "support": 19.0
    },
    "1": {
        "precision": 1.0,
        "recall": 0.6666666666666666,
        "f1-score": 0.8,
        "support": 12.0
    },
    "2": {
        "precision": 0.6333333333333333,
        "recall": 0.5757575757575758,
        "f1-score": 0.6031746031746031,
        "support": 33.0
    },
    "3": {
        "precision": 0.42857142857142855,
        "recall": 0.5357142857142857,
        "f1-score": 0.47619047619047616,
        "support": 28.0
    },
    "accuracy": 0.5434782608695652,
    "macro avg": {
        "precision": 0.6207393483709273,
        "recall": 0.5497977899293688,
        "f1-score": 0.5751044277360067,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.575,
        "recall": 0.5434782608695652,
        "f1-score": 0.5525879917184264,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.4825
- **Accuracy:** 0.4783
- **Best Parameters:** {'classifier__max_depth': None}
```json
{
    "0": {
        "precision": 0.35,
        "recall": 0.3684210526315789,
        "f1-score": 0.358974358974359,
        "support": 19.0
    },
    "1": {
        "precision": 0.875,
        "recall": 0.5833333333333334,
        "f1-score": 0.7,
        "support": 12.0
    },
    "2": {
        "precision": 0.5277777777777778,
        "recall": 0.5757575757575758,
        "f1-score": 0.5507246376811594,
        "support": 33.0
    },
    "3": {
        "precision": 0.39285714285714285,
        "recall": 0.39285714285714285,
        "f1-score": 0.39285714285714285,
        "support": 28.0
    },
    "accuracy": 0.4782608695652174,
    "macro avg": {
        "precision": 0.5364087301587301,
        "recall": 0.4800922761449077,
        "f1-score": 0.5006390348781653,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.4952898550724637,
        "recall": 0.4782608695652174,
        "f1-score": 0.48254810721729435,
        "support": 92.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.4915
- **Accuracy:** 0.4891
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "0": {
        "precision": 0.35294117647058826,
        "recall": 0.3157894736842105,
        "f1-score": 0.3333333333333333,
        "support": 19.0
    },
    "1": {
        "precision": 0.75,
        "recall": 0.5,
        "f1-score": 0.6,
        "support": 12.0
    },
    "2": {
        "precision": 0.5806451612903226,
        "recall": 0.5454545454545454,
        "f1-score": 0.5625,
        "support": 33.0
    },
    "3": {
        "precision": 0.4166666666666667,
        "recall": 0.5357142857142857,
        "f1-score": 0.46875,
        "support": 28.0
    },
    "accuracy": 0.4891304347826087,
    "macro avg": {
        "precision": 0.5250632511068943,
        "recall": 0.4742395762132604,
        "f1-score": 0.49114583333333334,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5058026015455271,
        "recall": 0.4891304347826087,
        "f1-score": 0.49153079710144926,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6173
- **Accuracy:** 0.6413
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "0": {
        "precision": 0.8,
        "recall": 0.21052631578947367,
        "f1-score": 0.3333333333333333,
        "support": 19.0
    },
    "1": {
        "precision": 0.8888888888888888,
        "recall": 0.6666666666666666,
        "f1-score": 0.7619047619047619,
        "support": 12.0
    },
    "2": {
        "precision": 0.6585365853658537,
        "recall": 0.8181818181818182,
        "f1-score": 0.7297297297297297,
        "support": 33.0
    },
    "3": {
        "precision": 0.5405405405405406,
        "recall": 0.7142857142857143,
        "f1-score": 0.6153846153846154,
        "support": 28.0
    },
    "accuracy": 0.6413043478260869,
    "macro avg": {
        "precision": 0.7219915036988207,
        "recall": 0.6024151287309182,
        "f1-score": 0.61008811008811,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6818859686834237,
        "recall": 0.6413043478260869,
        "f1-score": 0.6172613129134868,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.5396
- **Accuracy:** 0.5435
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.4166666666666667,
        "recall": 0.2631578947368421,
        "f1-score": 0.3225806451612903,
        "support": 19.0
    },
    "1": {
        "precision": 0.875,
        "recall": 0.5833333333333334,
        "f1-score": 0.7,
        "support": 12.0
    },
    "2": {
        "precision": 0.6176470588235294,
        "recall": 0.6363636363636364,
        "f1-score": 0.6268656716417911,
        "support": 33.0
    },
    "3": {
        "precision": 0.4473684210526316,
        "recall": 0.6071428571428571,
        "f1-score": 0.5151515151515151,
        "support": 28.0
    },
    "accuracy": 0.5434782608695652,
    "macro avg": {
        "precision": 0.589170536635707,
        "recall": 0.5224994303941672,
        "f1-score": 0.5411494579886491,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5578840804056177,
        "recall": 0.5434782608695652,
        "f1-score": 0.5395634983313701,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.4401
- **Accuracy:** 0.4457
- **Best Parameters:** {'classifier__max_depth': None}
```json
{
    "0": {
        "precision": 0.35294117647058826,
        "recall": 0.3157894736842105,
        "f1-score": 0.3333333333333333,
        "support": 19.0
    },
    "1": {
        "precision": 0.7777777777777778,
        "recall": 0.5833333333333334,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "2": {
        "precision": 0.46511627906976744,
        "recall": 0.6060606060606061,
        "f1-score": 0.5263157894736842,
        "support": 33.0
    },
    "3": {
        "precision": 0.34782608695652173,
        "recall": 0.2857142857142857,
        "f1-score": 0.3137254901960784,
        "support": 28.0
    },
    "accuracy": 0.44565217391304346,
    "macro avg": {
        "precision": 0.4859153300686638,
        "recall": 0.4477244246981089,
        "f1-score": 0.4600103199174406,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.44703460141695045,
        "recall": 0.44565217391304346,
        "f1-score": 0.4400659577332077,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.4957
- **Accuracy:** 0.5000
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "0": {
        "precision": 0.4166666666666667,
        "recall": 0.2631578947368421,
        "f1-score": 0.3225806451612903,
        "support": 19.0
    },
    "1": {
        "precision": 0.75,
        "recall": 0.5,
        "f1-score": 0.6,
        "support": 12.0
    },
    "2": {
        "precision": 0.5625,
        "recall": 0.5454545454545454,
        "f1-score": 0.5538461538461539,
        "support": 33.0
    },
    "3": {
        "precision": 0.425,
        "recall": 0.6071428571428571,
        "f1-score": 0.5,
        "support": 28.0
    },
    "accuracy": 0.5,
    "macro avg": {
        "precision": 0.5385416666666667,
        "recall": 0.47893882433356116,
        "f1-score": 0.49410669975186106,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5149909420289855,
        "recall": 0.5,
        "f1-score": 0.4957169058150826,
        "support": 92.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "0": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 19.0
    },
    "1": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 12.0
    },
    "2": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "3": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 28.0
    },
    "accuracy": 0.358695652173913,
    "macro avg": {
        "precision": 0.08967391304347826,
        "recall": 0.25,
        "f1-score": 0.132,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.1286625708884688,
        "recall": 0.358695652173913,
        "f1-score": 0.18939130434782608,
        "support": 92.0
    }
}
```

## Word2Vec_SVM_Enhanced

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 19.0
    },
    "1": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 12.0
    },
    "2": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "3": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 28.0
    },
    "accuracy": 0.358695652173913,
    "macro avg": {
        "precision": 0.08967391304347826,
        "recall": 0.25,
        "f1-score": 0.132,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.1286625708884688,
        "recall": 0.358695652173913,
        "f1-score": 0.18939130434782608,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.2817
- **Accuracy:** 0.2826
- **Best Parameters:** {'max_depth': None}
```json
{
    "0": {
        "precision": 0.25,
        "recall": 0.21052631578947367,
        "f1-score": 0.22857142857142856,
        "support": 19.0
    },
    "1": {
        "precision": 0.35714285714285715,
        "recall": 0.4166666666666667,
        "f1-score": 0.38461538461538464,
        "support": 12.0
    },
    "2": {
        "precision": 0.3225806451612903,
        "recall": 0.30303030303030304,
        "f1-score": 0.3125,
        "support": 33.0
    },
    "3": {
        "precision": 0.22580645161290322,
        "recall": 0.25,
        "f1-score": 0.23728813559322035,
        "support": 28.0
    },
    "accuracy": 0.2826086956521739,
    "macro avg": {
        "precision": 0.2888824884792627,
        "recall": 0.29505582137161085,
        "f1-score": 0.2907437371950084,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.28264626327389303,
        "recall": 0.2826086956521739,
        "f1-score": 0.28168271255273836,
        "support": 92.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.4379
- **Accuracy:** 0.4783
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "0": {
        "precision": 0.3181818181818182,
        "recall": 0.3684210526315789,
        "f1-score": 0.34146341463414637,
        "support": 19.0
    },
    "1": {
        "precision": 0.8333333333333334,
        "recall": 0.4166666666666667,
        "f1-score": 0.5555555555555556,
        "support": 12.0
    },
    "2": {
        "precision": 0.5185185185185185,
        "recall": 0.8484848484848485,
        "f1-score": 0.6436781609195402,
        "support": 33.0
    },
    "3": {
        "precision": 0.4,
        "recall": 0.14285714285714285,
        "f1-score": 0.21052631578947367,
        "support": 28.0
    },
    "accuracy": 0.4782608695652174,
    "macro avg": {
        "precision": 0.5175084175084175,
        "recall": 0.44410742766005923,
        "f1-score": 0.437805861724679,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.4821365832235398,
        "recall": 0.4782608695652174,
        "f1-score": 0.4379411706213645,
        "support": 92.0
    }
}
```

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "0": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 19.0
    },
    "1": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 12.0
    },
    "2": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "3": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 28.0
    },
    "accuracy": 0.358695652173913,
    "macro avg": {
        "precision": 0.08967391304347826,
        "recall": 0.25,
        "f1-score": 0.132,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.1286625708884688,
        "recall": 0.358695652173913,
        "f1-score": 0.18939130434782608,
        "support": 92.0
    }
}
```

## FastText_SVM_Enhanced

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 19.0
    },
    "1": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 12.0
    },
    "2": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "3": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 28.0
    },
    "accuracy": 0.358695652173913,
    "macro avg": {
        "precision": 0.08967391304347826,
        "recall": 0.25,
        "f1-score": 0.132,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.1286625708884688,
        "recall": 0.358695652173913,
        "f1-score": 0.18939130434782608,
        "support": 92.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.3597
- **Accuracy:** 0.3587
- **Best Parameters:** {'max_depth': None}
```json
{
    "0": {
        "precision": 0.18181818181818182,
        "recall": 0.21052631578947367,
        "f1-score": 0.1951219512195122,
        "support": 19.0
    },
    "1": {
        "precision": 0.5,
        "recall": 0.6666666666666666,
        "f1-score": 0.5714285714285714,
        "support": 12.0
    },
    "2": {
        "precision": 0.5185185185185185,
        "recall": 0.42424242424242425,
        "f1-score": 0.4666666666666667,
        "support": 33.0
    },
    "3": {
        "precision": 0.25925925925925924,
        "recall": 0.25,
        "f1-score": 0.2545454545454545,
        "support": 28.0
    },
    "accuracy": 0.358695652173913,
    "macro avg": {
        "precision": 0.3648989898989899,
        "recall": 0.3878588516746411,
        "f1-score": 0.3719406609650512,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.3676621285316938,
        "recall": 0.358695652173913,
        "f1-score": 0.3596927462781121,
        "support": 92.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.3948
- **Accuracy:** 0.4239
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "0": {
        "precision": 0.28205128205128205,
        "recall": 0.5789473684210527,
        "f1-score": 0.3793103448275862,
        "support": 19.0
    },
    "1": {
        "precision": 0.8571428571428571,
        "recall": 0.5,
        "f1-score": 0.631578947368421,
        "support": 12.0
    },
    "2": {
        "precision": 0.5128205128205128,
        "recall": 0.6060606060606061,
        "f1-score": 0.5555555555555556,
        "support": 33.0
    },
    "3": {
        "precision": 0.2857142857142857,
        "recall": 0.07142857142857142,
        "f1-score": 0.11428571428571428,
        "support": 28.0
    },
    "accuracy": 0.42391304347826086,
    "macro avg": {
        "precision": 0.4844322344322344,
        "recall": 0.4391091364775575,
        "f1-score": 0.42018264050931925,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.44095397356266913,
        "recall": 0.42391304347826086,
        "f1-score": 0.3947736657986797,
        "support": 92.0
    }
}
```

