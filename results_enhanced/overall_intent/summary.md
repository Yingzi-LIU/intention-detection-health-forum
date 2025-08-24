# Experiment Results Summary

**Labels:** fonction_phatique, partage_experience, recherche_information

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7914
- **Accuracy:** 0.8261
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "0": {
        "precision": 1.0,
        "recall": 0.6666666666666666,
        "f1-score": 0.8,
        "support": 12.0
    },
    "1": {
        "precision": 0.8271604938271605,
        "recall": 0.9710144927536232,
        "f1-score": 0.8933333333333333,
        "support": 69.0
    },
    "2": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "accuracy": 0.8260869565217391,
    "macro avg": {
        "precision": 0.720164609053498,
        "recall": 0.5761967501097935,
        "f1-score": 0.6120634920634921,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7906602254428342,
        "recall": 0.8260869565217391,
        "f1-score": 0.7914285714285715,
        "support": 92.0
    }
}
```

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.7996
- **Accuracy:** 0.8370
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.9,
        "recall": 0.75,
        "f1-score": 0.8181818181818182,
        "support": 12.0
    },
    "1": {
        "precision": 0.8375,
        "recall": 0.9710144927536232,
        "f1-score": 0.8993288590604027,
        "support": 69.0
    },
    "2": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "accuracy": 0.8369565217391305,
    "macro avg": {
        "precision": 0.7458333333333332,
        "recall": 0.6039745278875713,
        "f1-score": 0.6237856103627916,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8052989130434783,
        "recall": 0.8369565217391305,
        "f1-score": 0.7996106607136663,
        "support": 92.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7383
- **Accuracy:** 0.7500
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "0": {
        "precision": 0.6666666666666666,
        "recall": 0.5,
        "f1-score": 0.5714285714285714,
        "support": 12.0
    },
    "1": {
        "precision": 0.8243243243243243,
        "recall": 0.8840579710144928,
        "f1-score": 0.8531468531468531,
        "support": 69.0
    },
    "2": {
        "precision": 0.2222222222222222,
        "recall": 0.18181818181818182,
        "f1-score": 0.2,
        "support": 11.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.5710710710710711,
        "recall": 0.5219587176108915,
        "f1-score": 0.5415251415251415,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7317698132915524,
        "recall": 0.75,
        "f1-score": 0.738307344829084,
        "support": 92.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.7301
- **Accuracy:** 0.7065
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "0": {
        "precision": 0.47368421052631576,
        "recall": 0.75,
        "f1-score": 0.5806451612903226,
        "support": 12.0
    },
    "1": {
        "precision": 0.9090909090909091,
        "recall": 0.7246376811594203,
        "f1-score": 0.8064516129032258,
        "support": 69.0
    },
    "2": {
        "precision": 0.3333333333333333,
        "recall": 0.5454545454545454,
        "f1-score": 0.41379310344827586,
        "support": 11.0
    },
    "accuracy": 0.7065217391304348,
    "macro avg": {
        "precision": 0.5720361509835193,
        "recall": 0.6733640755379886,
        "f1-score": 0.6002966258806081,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7834581513071216,
        "recall": 0.7065217391304348,
        "f1-score": 0.7300502974319292,
        "support": 92.0
    }
}
```

## TF-IDF_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7922
- **Accuracy:** 0.8370
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "0": {
        "precision": 0.875,
        "recall": 0.5833333333333334,
        "f1-score": 0.7,
        "support": 12.0
    },
    "1": {
        "precision": 0.8313253012048193,
        "recall": 1.0,
        "f1-score": 0.9078947368421053,
        "support": 69.0
    },
    "2": {
        "precision": 1.0,
        "recall": 0.09090909090909091,
        "f1-score": 0.16666666666666666,
        "support": 11.0
    },
    "accuracy": 0.8369565217391305,
    "macro avg": {
        "precision": 0.9021084337349398,
        "recall": 0.5580808080808081,
        "f1-score": 0.5915204678362573,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8571896280775274,
        "recall": 0.8369565217391305,
        "f1-score": 0.7921529366895499,
        "support": 92.0
    }
}
```

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.8145
- **Accuracy:** 0.8261
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "0": {
        "precision": 1.0,
        "recall": 0.6666666666666666,
        "f1-score": 0.8,
        "support": 12.0
    },
    "1": {
        "precision": 0.8552631578947368,
        "recall": 0.9420289855072463,
        "f1-score": 0.896551724137931,
        "support": 69.0
    },
    "2": {
        "precision": 0.375,
        "recall": 0.2727272727272727,
        "f1-score": 0.3157894736842105,
        "support": 11.0
    },
    "accuracy": 0.8260869565217391,
    "macro avg": {
        "precision": 0.7434210526315789,
        "recall": 0.6271409749670619,
        "f1-score": 0.6707803992740472,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8167191075514875,
        "recall": 0.8260869565217391,
        "f1-score": 0.814519056261343,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7182
- **Accuracy:** 0.7391
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "0": {
        "precision": 0.7142857142857143,
        "recall": 0.4166666666666667,
        "f1-score": 0.5263157894736842,
        "support": 12.0
    },
    "1": {
        "precision": 0.8051948051948052,
        "recall": 0.8985507246376812,
        "f1-score": 0.8493150684931506,
        "support": 69.0
    },
    "2": {
        "precision": 0.125,
        "recall": 0.09090909090909091,
        "f1-score": 0.10526315789473684,
        "support": 11.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.5481601731601732,
        "recall": 0.46870882740447956,
        "f1-score": 0.49363133862052394,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.712009457933371,
        "recall": 0.7391304347826086,
        "f1-score": 0.7182219993103665,
        "support": 92.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.7692
- **Accuracy:** 0.8152
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "0": {
        "precision": 0.75,
        "recall": 0.5,
        "f1-score": 0.6,
        "support": 12.0
    },
    "1": {
        "precision": 0.8192771084337349,
        "recall": 0.9855072463768116,
        "f1-score": 0.8947368421052632,
        "support": 69.0
    },
    "2": {
        "precision": 1.0,
        "recall": 0.09090909090909091,
        "f1-score": 0.16666666666666666,
        "support": 11.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.856425702811245,
        "recall": 0.5254721124286341,
        "f1-score": 0.5538011695906433,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8318491356731272,
        "recall": 0.8152173913043478,
        "f1-score": 0.7692410373760488,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7678
- **Accuracy:** 0.8261
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "0": {
        "precision": 0.875,
        "recall": 0.5833333333333334,
        "f1-score": 0.7,
        "support": 12.0
    },
    "1": {
        "precision": 0.8214285714285714,
        "recall": 1.0,
        "f1-score": 0.9019607843137255,
        "support": 69.0
    },
    "2": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8260869565217391,
    "macro avg": {
        "precision": 0.5654761904761905,
        "recall": 0.5277777777777778,
        "f1-score": 0.5339869281045752,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7302018633540371,
        "recall": 0.8260869565217391,
        "f1-score": 0.7677749360613809,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.8081
- **Accuracy:** 0.8370
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.8,
        "recall": 0.6666666666666666,
        "f1-score": 0.7272727272727273,
        "support": 12.0
    },
    "1": {
        "precision": 0.8481012658227848,
        "recall": 0.9710144927536232,
        "f1-score": 0.9054054054054054,
        "support": 69.0
    },
    "2": {
        "precision": 0.6666666666666666,
        "recall": 0.18181818181818182,
        "f1-score": 0.2857142857142857,
        "support": 11.0
    },
    "accuracy": 0.8369565217391305,
    "macro avg": {
        "precision": 0.7715893108298171,
        "recall": 0.6064997804128239,
        "f1-score": 0.6394641394641395,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8201339203815813,
        "recall": 0.8369565217391305,
        "f1-score": 0.808077204816335,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7190
- **Accuracy:** 0.7283
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "0": {
        "precision": 0.75,
        "recall": 0.5,
        "f1-score": 0.6,
        "support": 12.0
    },
    "1": {
        "precision": 0.8108108108108109,
        "recall": 0.8695652173913043,
        "f1-score": 0.8391608391608392,
        "support": 69.0
    },
    "2": {
        "precision": 0.1,
        "recall": 0.09090909090909091,
        "f1-score": 0.09523809523809523,
        "support": 11.0
    },
    "accuracy": 0.7282608695652174,
    "macro avg": {
        "precision": 0.5536036036036037,
        "recall": 0.48682476943346503,
        "f1-score": 0.5114663114663115,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7178907168037603,
        "recall": 0.7282608695652174,
        "f1-score": 0.7190186624969234,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.7394
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "0": {
        "precision": 0.75,
        "recall": 0.5,
        "f1-score": 0.6,
        "support": 12.0
    },
    "1": {
        "precision": 0.8072289156626506,
        "recall": 0.9710144927536232,
        "f1-score": 0.881578947368421,
        "support": 69.0
    },
    "2": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.5190763052208835,
        "recall": 0.4903381642512077,
        "f1-score": 0.49385964912280694,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7032477737035098,
        "recall": 0.7934782608695652,
        "f1-score": 0.7394450800915331,
        "support": 92.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6429
- **Accuracy:** 0.7500
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "0": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 12.0
    },
    "1": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "2": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.25,
        "recall": 0.3333333333333333,
        "f1-score": 0.2857142857142857,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5625,
        "recall": 0.75,
        "f1-score": 0.6428571428571428,
        "support": 92.0
    }
}
```

## Word2Vec_SVM_Enhanced

- **Weighted F1 Score:** 0.6429
- **Accuracy:** 0.7500
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 12.0
    },
    "1": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "2": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.25,
        "recall": 0.3333333333333333,
        "f1-score": 0.2857142857142857,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5625,
        "recall": 0.75,
        "f1-score": 0.6428571428571428,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7521
- **Accuracy:** 0.7500
- **Best Parameters:** {'max_depth': 10}
```json
{
    "0": {
        "precision": 0.46153846153846156,
        "recall": 0.5,
        "f1-score": 0.48,
        "support": 12.0
    },
    "1": {
        "precision": 0.8676470588235294,
        "recall": 0.855072463768116,
        "f1-score": 0.8613138686131386,
        "support": 69.0
    },
    "2": {
        "precision": 0.36363636363636365,
        "recall": 0.36363636363636365,
        "f1-score": 0.36363636363636365,
        "support": 11.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.564273961332785,
        "recall": 0.5729029424681599,
        "f1-score": 0.5683167440831675,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7544142238835334,
        "recall": 0.75,
        "f1-score": 0.7520723579815932,
        "support": 92.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.7115
- **Accuracy:** 0.7391
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "-1": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 0.0
    },
    "0": {
        "precision": 0.6666666666666666,
        "recall": 0.5,
        "f1-score": 0.5714285714285714,
        "support": 12.0
    },
    "1": {
        "precision": 0.8051948051948052,
        "recall": 0.8985507246376812,
        "f1-score": 0.8493150684931506,
        "support": 69.0
    },
    "2": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.36796536796536794,
        "recall": 0.3496376811594203,
        "f1-score": 0.35518590998043054,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6908526256352343,
        "recall": 0.7391304347826086,
        "f1-score": 0.7115204628605463,
        "support": 92.0
    }
}
```

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6429
- **Accuracy:** 0.7500
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "0": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 12.0
    },
    "1": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "2": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.25,
        "recall": 0.3333333333333333,
        "f1-score": 0.2857142857142857,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5625,
        "recall": 0.75,
        "f1-score": 0.6428571428571428,
        "support": 92.0
    }
}
```

## FastText_SVM_Enhanced

- **Weighted F1 Score:** 0.6429
- **Accuracy:** 0.7500
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 12.0
    },
    "1": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "2": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.25,
        "recall": 0.3333333333333333,
        "f1-score": 0.2857142857142857,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5625,
        "recall": 0.75,
        "f1-score": 0.6428571428571428,
        "support": 92.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7680
- **Accuracy:** 0.8043
- **Best Parameters:** {'max_depth': 5}
```json
{
    "0": {
        "precision": 0.5833333333333334,
        "recall": 0.5833333333333334,
        "f1-score": 0.5833333333333334,
        "support": 12.0
    },
    "1": {
        "precision": 0.8461538461538461,
        "recall": 0.9565217391304348,
        "f1-score": 0.8979591836734694,
        "support": 69.0
    },
    "2": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.6431623931623932,
        "recall": 0.5435880544576196,
        "f1-score": 0.5450462236176522,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7704849498327759,
        "recall": 0.8043478260869565,
        "f1-score": 0.7679509931062727,
        "support": 92.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.7856
- **Accuracy:** 0.8261
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "0": {
        "precision": 1.0,
        "recall": 0.4166666666666667,
        "f1-score": 0.5882352941176471,
        "support": 12.0
    },
    "1": {
        "precision": 0.8117647058823529,
        "recall": 1.0,
        "f1-score": 0.8961038961038961,
        "support": 69.0
    },
    "2": {
        "precision": 1.0,
        "recall": 0.18181818181818182,
        "f1-score": 0.3076923076923077,
        "support": 11.0
    },
    "accuracy": 0.8260869565217391,
    "macro avg": {
        "precision": 0.9372549019607842,
        "recall": 0.5328282828282829,
        "f1-score": 0.5973438326379503,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8588235294117648,
        "recall": 0.8260869565217391,
        "f1-score": 0.7855935624477823,
        "support": 92.0
    }
}
```

