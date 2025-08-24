# Experiment Results Summary

**Labels:** fonction_phatique, partage_experience, recherche_information

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.8145
- **Accuracy:** 0.8261
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.6666666666666666,
        "f1-score": 0.8,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8552631578947368,
        "recall": 0.9420289855072463,
        "f1-score": 0.896551724137931,
        "support": 69.0
    },
    "recherche_information": {
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

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.8081
- **Accuracy:** 0.8370
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.8,
        "recall": 0.6666666666666666,
        "f1-score": 0.7272727272727273,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8481012658227848,
        "recall": 0.9710144927536232,
        "f1-score": 0.9054054054054054,
        "support": 69.0
    },
    "recherche_information": {
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

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.7996
- **Accuracy:** 0.8370
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.9,
        "recall": 0.75,
        "f1-score": 0.8181818181818182,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8375,
        "recall": 0.9710144927536232,
        "f1-score": 0.8993288590604027,
        "support": 69.0
    },
    "recherche_information": {
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

## TF-IDF_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7922
- **Accuracy:** 0.8370
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 0.875,
        "recall": 0.5833333333333334,
        "f1-score": 0.7,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8313253012048193,
        "recall": 1.0,
        "f1-score": 0.9078947368421053,
        "support": 69.0
    },
    "recherche_information": {
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

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7914
- **Accuracy:** 0.8261
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.6666666666666666,
        "f1-score": 0.8,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8271604938271605,
        "recall": 0.9710144927536232,
        "f1-score": 0.8933333333333333,
        "support": 69.0
    },
    "recherche_information": {
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

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.7692
- **Accuracy:** 0.8152
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 0.75,
        "recall": 0.5,
        "f1-score": 0.6,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8192771084337349,
        "recall": 0.9855072463768116,
        "f1-score": 0.8947368421052632,
        "support": 69.0
    },
    "recherche_information": {
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
    "fonction_phatique": {
        "precision": 0.875,
        "recall": 0.5833333333333334,
        "f1-score": 0.7,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8214285714285714,
        "recall": 1.0,
        "f1-score": 0.9019607843137255,
        "support": 69.0
    },
    "recherche_information": {
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

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7525
- **Accuracy:** 0.8043
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.7777777777777778,
        "recall": 0.5833333333333334,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8170731707317073,
        "recall": 0.9710144927536232,
        "f1-score": 0.8874172185430463,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.5316169828364951,
        "recall": 0.5181159420289855,
        "f1-score": 0.518027961736571,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7142541534110992,
        "recall": 0.8043478260869565,
        "f1-score": 0.7525194356464151,
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
    "fonction_phatique": {
        "precision": 0.75,
        "recall": 0.5,
        "f1-score": 0.6,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8072289156626506,
        "recall": 0.9710144927536232,
        "f1-score": 0.881578947368421,
        "support": 69.0
    },
    "recherche_information": {
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

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7357
- **Accuracy:** 0.7500
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.8571428571428571,
        "recall": 0.5,
        "f1-score": 0.631578947368421,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8157894736842105,
        "recall": 0.8985507246376812,
        "f1-score": 0.8551724137931035,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.1111111111111111,
        "recall": 0.09090909090909091,
        "f1-score": 0.1,
        "support": 11.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.5946811473127263,
        "recall": 0.49648660518225735,
        "f1-score": 0.5289171203871749,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7369283716537722,
        "recall": 0.75,
        "f1-score": 0.7357156947841869,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7321
- **Accuracy:** 0.7391
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "fonction_phatique": {
        "precision": 0.7777777777777778,
        "recall": 0.5833333333333334,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.821917808219178,
        "recall": 0.8695652173913043,
        "f1-score": 0.8450704225352113,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.1,
        "recall": 0.09090909090909091,
        "f1-score": 0.09523809523809523,
        "support": 11.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.5665651953323186,
        "recall": 0.5146025472112429,
        "f1-score": 0.5356583948133244,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7298441532658326,
        "recall": 0.7391304347826086,
        "f1-score": 0.7321465022016155,
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
    "fonction_phatique": {
        "precision": 0.47368421052631576,
        "recall": 0.75,
        "f1-score": 0.5806451612903226,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.9090909090909091,
        "recall": 0.7246376811594203,
        "f1-score": 0.8064516129032258,
        "support": 69.0
    },
    "recherche_information": {
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

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.7856
- **Accuracy:** 0.8261
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.4166666666666667,
        "f1-score": 0.5882352941176471,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8117647058823529,
        "recall": 1.0,
        "f1-score": 0.8961038961038961,
        "support": 69.0
    },
    "recherche_information": {
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

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7664
- **Accuracy:** 0.8043
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.5384615384615384,
        "recall": 0.5833333333333334,
        "f1-score": 0.56,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8461538461538461,
        "recall": 0.9565217391304348,
        "f1-score": 0.8979591836734694,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 1.0,
        "recall": 0.09090909090909091,
        "f1-score": 0.16666666666666666,
        "support": 11.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.7948717948717948,
        "recall": 0.5435880544576196,
        "f1-score": 0.5415419501133788,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8244147157190637,
        "recall": 0.8043478260869565,
        "f1-score": 0.7664404022478557,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7436
- **Accuracy:** 0.7717
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.5,
        "recall": 0.5833333333333334,
        "f1-score": 0.5384615384615384,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.84,
        "recall": 0.9130434782608695,
        "f1-score": 0.875,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.5577777777777777,
        "recall": 0.5290953008344312,
        "f1-score": 0.5187728937728937,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.735072463768116,
        "recall": 0.7717391304347826,
        "f1-score": 0.7435648590539895,
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
    "fonction_phatique": {
        "precision": 0.6666666666666666,
        "recall": 0.5,
        "f1-score": 0.5714285714285714,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8051948051948052,
        "recall": 0.8985507246376812,
        "f1-score": 0.8493150684931506,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "micro avg": {
        "precision": 0.7640449438202247,
        "recall": 0.7391304347826086,
        "f1-score": 0.7513812154696132,
        "support": 92.0
    },
    "macro avg": {
        "precision": 0.49062049062049057,
        "recall": 0.46618357487922707,
        "f1-score": 0.47358121330724073,
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

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6429
- **Accuracy:** 0.7500
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "recherche_information": {
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
    "fonction_phatique": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "recherche_information": {
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

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6429
- **Accuracy:** 0.7500
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "recherche_information": {
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
    "fonction_phatique": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "recherche_information": {
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

