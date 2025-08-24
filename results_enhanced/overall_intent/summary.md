# Experiment Results Summary

**Labels:** fonction_phatique, partage_experience, recherche_information

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

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.7977
- **Accuracy:** 0.8261
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.875,
        "recall": 0.5833333333333334,
        "f1-score": 0.7,
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
        "recall": 0.18181818181818182,
        "f1-score": 0.26666666666666666,
        "support": 11.0
    },
    "accuracy": 0.8260869565217391,
    "macro avg": {
        "precision": 0.7374999999999999,
        "recall": 0.5787220026350461,
        "f1-score": 0.6219985085756897,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8020380434782608,
        "recall": 0.8260869565217391,
        "f1-score": 0.7976850500924035,
        "support": 92.0
    }
}
```

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.7954
- **Accuracy:** 0.8152
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
        "precision": 0.8552631578947368,
        "recall": 0.9420289855072463,
        "f1-score": 0.896551724137931,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.3333333333333333,
        "recall": 0.18181818181818182,
        "f1-score": 0.23529411764705882,
        "support": 11.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.6628654970760234,
        "recall": 0.5968379446640316,
        "f1-score": 0.6197061896859057,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7856502669717773,
        "recall": 0.8152173913043478,
        "f1-score": 0.7954084455098654,
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

- **Weighted F1 Score:** 0.7809
- **Accuracy:** 0.8152
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 0.8,
        "recall": 0.6666666666666666,
        "f1-score": 0.7272727272727273,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8354430379746836,
        "recall": 0.9565217391304348,
        "f1-score": 0.8918918918918919,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.6562587904360057,
        "recall": 0.5713658322353975,
        "f1-score": 0.5873405873405874,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7707851770317373,
        "recall": 0.8152173913043478,
        "f1-score": 0.7808613243395852,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.7754
- **Accuracy:** 0.8152
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 0.7777777777777778,
        "recall": 0.5833333333333334,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8271604938271605,
        "recall": 0.9710144927536232,
        "f1-score": 0.8933333333333333,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.7016460905349794,
        "recall": 0.5484189723320158,
        "f1-score": 0.5712820512820512,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7816022544283413,
        "recall": 0.8152173913043478,
        "f1-score": 0.7753511705685618,
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

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.7580
- **Accuracy:** 0.8152
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 0.7777777777777778,
        "recall": 0.5833333333333334,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8192771084337349,
        "recall": 0.9855072463768116,
        "f1-score": 0.8947368421052632,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.5323516287371709,
        "recall": 0.5229468599033816,
        "f1-score": 0.52046783625731,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.71590710668762,
        "recall": 0.8152173913043478,
        "f1-score": 0.7580091533180777,
        "support": 92.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7513
- **Accuracy:** 0.7609
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "fonction_phatique": {
        "precision": 0.7,
        "recall": 0.5833333333333334,
        "f1-score": 0.6363636363636364,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8356164383561644,
        "recall": 0.8840579710144928,
        "f1-score": 0.8591549295774648,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.2222222222222222,
        "recall": 0.18181818181818182,
        "f1-score": 0.2,
        "support": 11.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.5859462201927955,
        "recall": 0.5497364953886693,
        "f1-score": 0.5651728553137004,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.744586724902389,
        "recall": 0.7608695652173914,
        "f1-score": 0.7512831932305294,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7322
- **Accuracy:** 0.7500
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.75,
        "recall": 0.5,
        "f1-score": 0.6,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8157894736842105,
        "recall": 0.8985507246376812,
        "f1-score": 0.8551724137931035,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.125,
        "recall": 0.09090909090909091,
        "f1-score": 0.10526315789473684,
        "support": 11.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.5635964912280702,
        "recall": 0.49648660518225735,
        "f1-score": 0.5201451905626134,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7246138443935927,
        "recall": 0.75,
        "f1-score": 0.7322259922670245,
        "support": 92.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.7302
- **Accuracy:** 0.7174
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 0.6666666666666666,
        "recall": 0.6666666666666666,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8461538461538461,
        "recall": 0.7971014492753623,
        "f1-score": 0.8208955223880597,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.2,
        "recall": 0.2727272727272727,
        "f1-score": 0.23076923076923078,
        "support": 11.0
    },
    "accuracy": 0.717391304347826,
    "macro avg": {
        "precision": 0.5709401709401709,
        "recall": 0.5788317962231005,
        "f1-score": 0.5727771399413191,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.745484949832776,
        "recall": 0.717391304347826,
        "f1-score": 0.7302201367743223,
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
    "fonction_phatique": {
        "precision": 0.75,
        "recall": 0.5,
        "f1-score": 0.6,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8108108108108109,
        "recall": 0.8695652173913043,
        "f1-score": 0.8391608391608392,
        "support": 69.0
    },
    "recherche_information": {
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

- **Weighted F1 Score:** 0.7751
- **Accuracy:** 0.8152
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.5833333333333334,
        "recall": 0.5833333333333334,
        "f1-score": 0.5833333333333334,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8481012658227848,
        "recall": 0.9710144927536232,
        "f1-score": 0.9054054054054054,
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
        "precision": 0.8104781997187059,
        "recall": 0.5484189723320158,
        "f1-score": 0.5518018018018018,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.831728123280132,
        "recall": 0.8152173913043478,
        "f1-score": 0.7750685468076771,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7408
- **Accuracy:** 0.7391
- **Best Parameters:** {'max_depth': 10}
```json
{
    "fonction_phatique": {
        "precision": 0.42857142857142855,
        "recall": 0.5,
        "f1-score": 0.46153846153846156,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8529411764705882,
        "recall": 0.8405797101449275,
        "f1-score": 0.8467153284671532,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.4,
        "recall": 0.36363636363636365,
        "f1-score": 0.38095238095238093,
        "support": 11.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.5605042016806722,
        "recall": 0.5680720245937637,
        "f1-score": 0.5630687236526652,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7434325904274754,
        "recall": 0.7391304347826086,
        "f1-score": 0.7407858194909924,
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

