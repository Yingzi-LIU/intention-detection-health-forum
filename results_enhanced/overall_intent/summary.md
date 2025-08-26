# Experiment Results Summary

**Labels:** fonction_phatique, partage_experience, recherche_information

## TF-IDF_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.8730
- **Accuracy:** 0.8966
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8846153846153846,
        "recall": 1.0,
        "f1-score": 0.9387755102040817,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 1.0,
        "recall": 0.2727272727272727,
        "f1-score": 0.42857142857142855,
        "support": 11.0
    },
    "accuracy": 0.896551724137931,
    "macro avg": {
        "precision": 0.9615384615384616,
        "recall": 0.70995670995671,
        "f1-score": 0.7634746206174777,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.9084880636604774,
        "recall": 0.896551724137931,
        "f1-score": 0.8730038434471933,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.8546
- **Accuracy:** 0.8736
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.881578947368421,
        "recall": 0.9710144927536232,
        "f1-score": 0.9241379310344827,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.6,
        "recall": 0.2727272727272727,
        "f1-score": 0.375,
        "support": 11.0
    },
    "accuracy": 0.8735632183908046,
    "macro avg": {
        "precision": 0.8271929824561403,
        "recall": 0.7002948742079177,
        "f1-score": 0.7407382847038019,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.855505142165759,
        "recall": 0.8735632183908046,
        "f1-score": 0.8546213299185951,
        "support": 87.0
    }
}
```

## TF-IDF_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.8359
- **Accuracy:** 0.8621
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8701298701298701,
        "recall": 0.9710144927536232,
        "f1-score": 0.9178082191780822,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.18181818181818182,
        "f1-score": 0.26666666666666666,
        "support": 11.0
    },
    "accuracy": 0.8620689655172413,
    "macro avg": {
        "precision": 0.79004329004329,
        "recall": 0.6699918439048873,
        "f1-score": 0.7025172696405573,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8337811613673682,
        "recall": 0.8620689655172413,
        "f1-score": 0.8359038956110283,
        "support": 87.0
    }
}
```

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.8299
- **Accuracy:** 0.8736
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8625,
        "recall": 1.0,
        "f1-score": 0.9261744966442953,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 1.0,
        "recall": 0.09090909090909091,
        "f1-score": 0.16666666666666666,
        "support": 11.0
    },
    "accuracy": 0.8735632183908046,
    "macro avg": {
        "precision": 0.9541666666666666,
        "recall": 0.6493506493506493,
        "f1-score": 0.6719726954626283,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.890948275862069,
        "recall": 0.8735632183908046,
        "f1-score": 0.8298955409577949,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.8299
- **Accuracy:** 0.8736
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8625,
        "recall": 1.0,
        "f1-score": 0.9261744966442953,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 1.0,
        "recall": 0.09090909090909091,
        "f1-score": 0.16666666666666666,
        "support": 11.0
    },
    "accuracy": 0.8735632183908046,
    "macro avg": {
        "precision": 0.9541666666666666,
        "recall": 0.6493506493506493,
        "f1-score": 0.6719726954626283,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.890948275862069,
        "recall": 0.8735632183908046,
        "f1-score": 0.8298955409577949,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.8295
- **Accuracy:** 0.8276
- **Best Parameters:** {'classifier__max_depth': 10}
```json
{
    "fonction_phatique": {
        "precision": 0.8333333333333334,
        "recall": 0.7142857142857143,
        "f1-score": 0.7692307692307693,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8985507246376812,
        "recall": 0.8985507246376812,
        "f1-score": 0.8985507246376812,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.4166666666666667,
        "recall": 0.45454545454545453,
        "f1-score": 0.43478260869565216,
        "support": 11.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.716183574879227,
        "recall": 0.68912729782295,
        "f1-score": 0.7008547008547009,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.832375478927203,
        "recall": 0.8275862068965517,
        "f1-score": 0.8295083227616961,
        "support": 87.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.8271
- **Accuracy:** 0.8621
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8518518518518519,
        "recall": 1.0,
        "f1-score": 0.92,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 1.0,
        "recall": 0.18181818181818182,
        "f1-score": 0.3076923076923077,
        "support": 11.0
    },
    "accuracy": 0.8620689655172413,
    "macro avg": {
        "precision": 0.9506172839506174,
        "recall": 0.5844155844155844,
        "f1-score": 0.6516550116550117,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8825031928480204,
        "recall": 0.8620689655172413,
        "f1-score": 0.8270749939715458,
        "support": 87.0
    }
}
```

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.8225
- **Accuracy:** 0.8621
- **Best Parameters:** {'classifier__C': 1, 'classifier__solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8607594936708861,
        "recall": 0.9855072463768116,
        "f1-score": 0.918918918918919,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "accuracy": 0.8620689655172413,
    "macro avg": {
        "precision": 0.7869198312236287,
        "recall": 0.6445197314762532,
        "f1-score": 0.6652806652806653,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.826349483486105,
        "recall": 0.8620689655172413,
        "f1-score": 0.8225201328649605,
        "support": 87.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.8225
- **Accuracy:** 0.8621
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8607594936708861,
        "recall": 0.9855072463768116,
        "f1-score": 0.918918918918919,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "accuracy": 0.8620689655172413,
    "macro avg": {
        "precision": 0.7869198312236287,
        "recall": 0.6445197314762532,
        "f1-score": 0.6652806652806653,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.826349483486105,
        "recall": 0.8620689655172413,
        "f1-score": 0.8225201328649605,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.8225
- **Accuracy:** 0.8621
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8607594936708861,
        "recall": 0.9855072463768116,
        "f1-score": 0.918918918918919,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "accuracy": 0.8620689655172413,
    "macro avg": {
        "precision": 0.7869198312236287,
        "recall": 0.6445197314762532,
        "f1-score": 0.6652806652806653,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.826349483486105,
        "recall": 0.8620689655172413,
        "f1-score": 0.8225201328649605,
        "support": 87.0
    }
}
```

## BoW_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.8209
- **Accuracy:** 0.8276
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.875,
        "recall": 0.9130434782608695,
        "f1-score": 0.8936170212765957,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.3333333333333333,
        "recall": 0.2727272727272727,
        "f1-score": 0.3,
        "support": 11.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.7361111111111112,
        "recall": 0.6809712027103331,
        "f1-score": 0.7055646481178396,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8165708812260537,
        "recall": 0.8275862068965517,
        "f1-score": 0.8209323325244088,
        "support": 87.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.8001
- **Accuracy:** 0.8161
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.7142857142857143,
        "f1-score": 0.8333333333333334,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8533333333333334,
        "recall": 0.927536231884058,
        "f1-score": 0.8888888888888888,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.2857142857142857,
        "recall": 0.18181818181818182,
        "f1-score": 0.2222222222222222,
        "support": 11.0
    },
    "accuracy": 0.8160919540229885,
    "macro avg": {
        "precision": 0.713015873015873,
        "recall": 0.6078800426626514,
        "f1-score": 0.6481481481481483,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7933661740558291,
        "recall": 0.8160919540229885,
        "f1-score": 0.8001277139208173,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.7982
- **Accuracy:** 0.8506
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.85,
        "recall": 0.9855072463768116,
        "f1-score": 0.912751677852349,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8505747126436781,
    "macro avg": {
        "precision": 0.6166666666666667,
        "recall": 0.6142167011732229,
        "f1-score": 0.6119428669764241,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7545977011494254,
        "recall": 0.8505747126436781,
        "f1-score": 0.7981770601534545,
        "support": 87.0
    }
}
```

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.7786
- **Accuracy:** 0.8391
- **Best Parameters:** {'classifier__C': 0.1, 'classifier__kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8313253012048193,
        "recall": 1.0,
        "f1-score": 0.9078947368421053,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.8390804597701149,
        "recall": 0.9605263157894737,
        "f1-score": 0.8957055214723927,
        "support": 76.0
    },
    "macro avg": {
        "precision": 0.9156626506024097,
        "recall": 0.7857142857142857,
        "f1-score": 0.8175837320574163,
        "support": 76.0
    },
    "weighted avg": {
        "precision": 0.846861128725428,
        "recall": 0.9605263157894737,
        "f1-score": 0.8912584991186099,
        "support": 76.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.7567
- **Accuracy:** 0.7816
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 0.5454545454545454,
        "recall": 0.8571428571428571,
        "f1-score": 0.6666666666666666,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8472222222222222,
        "recall": 0.8840579710144928,
        "f1-score": 0.8652482269503546,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.25,
        "recall": 0.09090909090909091,
        "f1-score": 0.13333333333333333,
        "support": 11.0
    },
    "accuracy": 0.7816091954022989,
    "macro avg": {
        "precision": 0.5475589225589226,
        "recall": 0.6107033063554802,
        "f1-score": 0.5550827423167849,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7474312086381052,
        "recall": 0.7816091954022989,
        "f1-score": 0.7567294367000897,
        "support": 87.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.8039
- **Accuracy:** 0.8621
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8518518518518519,
        "recall": 1.0,
        "f1-score": 0.92,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.8620689655172413,
        "recall": 0.9868421052631579,
        "f1-score": 0.9202453987730062,
        "support": 76.0
    },
    "macro avg": {
        "precision": 0.9259259259259259,
        "recall": 0.9285714285714286,
        "f1-score": 0.9215384615384616,
        "support": 76.0
    },
    "weighted avg": {
        "precision": 0.8654970760233918,
        "recall": 0.9868421052631579,
        "f1-score": 0.9202834008097167,
        "support": 76.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.7800
- **Accuracy:** 0.8276
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "fonction_phatique": {
        "precision": 0.8333333333333334,
        "recall": 0.7142857142857143,
        "f1-score": 0.7692307692307693,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8481012658227848,
        "recall": 0.9710144927536232,
        "f1-score": 0.9054054054054054,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.560478199718706,
        "recall": 0.5617667356797792,
        "f1-score": 0.5582120582120582,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7396818468402929,
        "recall": 0.8275862068965517,
        "f1-score": 0.7799722799722799,
        "support": 87.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7786
- **Accuracy:** 0.8391
- **Best Parameters:** {'C': 1, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8313253012048193,
        "recall": 1.0,
        "f1-score": 0.9078947368421053,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.8390804597701149,
        "recall": 0.9605263157894737,
        "f1-score": 0.8957055214723927,
        "support": 76.0
    },
    "macro avg": {
        "precision": 0.9156626506024097,
        "recall": 0.7857142857142857,
        "f1-score": 0.8175837320574163,
        "support": 76.0
    },
    "weighted avg": {
        "precision": 0.846861128725428,
        "recall": 0.9605263157894737,
        "f1-score": 0.8912584991186099,
        "support": 76.0
    }
}
```

## Word2Vec_SVM_Enhanced

- **Weighted F1 Score:** 0.7786
- **Accuracy:** 0.8391
- **Best Parameters:** {'C': 1, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8313253012048193,
        "recall": 1.0,
        "f1-score": 0.9078947368421053,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.8390804597701149,
        "recall": 0.9605263157894737,
        "f1-score": 0.8957055214723927,
        "support": 76.0
    },
    "macro avg": {
        "precision": 0.9156626506024097,
        "recall": 0.7857142857142857,
        "f1-score": 0.8175837320574163,
        "support": 76.0
    },
    "weighted avg": {
        "precision": 0.846861128725428,
        "recall": 0.9605263157894737,
        "f1-score": 0.8912584991186099,
        "support": 76.0
    }
}
```

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7786
- **Accuracy:** 0.8391
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8313253012048193,
        "recall": 1.0,
        "f1-score": 0.9078947368421053,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.8390804597701149,
        "recall": 0.9605263157894737,
        "f1-score": 0.8957055214723927,
        "support": 76.0
    },
    "macro avg": {
        "precision": 0.9156626506024097,
        "recall": 0.7857142857142857,
        "f1-score": 0.8175837320574163,
        "support": 76.0
    },
    "weighted avg": {
        "precision": 0.846861128725428,
        "recall": 0.9605263157894737,
        "f1-score": 0.8912584991186099,
        "support": 76.0
    }
}
```

## FastText_SVM_Enhanced

- **Weighted F1 Score:** 0.7786
- **Accuracy:** 0.8391
- **Best Parameters:** {'C': 1, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8313253012048193,
        "recall": 1.0,
        "f1-score": 0.9078947368421053,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.8390804597701149,
        "recall": 0.9605263157894737,
        "f1-score": 0.8957055214723927,
        "support": 76.0
    },
    "macro avg": {
        "precision": 0.9156626506024097,
        "recall": 0.7857142857142857,
        "f1-score": 0.8175837320574163,
        "support": 76.0
    },
    "weighted avg": {
        "precision": 0.846861128725428,
        "recall": 0.9605263157894737,
        "f1-score": 0.8912584991186099,
        "support": 76.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7262
- **Accuracy:** 0.7701
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.6,
        "recall": 0.42857142857142855,
        "f1-score": 0.5,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.810126582278481,
        "recall": 0.927536231884058,
        "f1-score": 0.8648648648648649,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.7701149425287356,
    "macro avg": {
        "precision": 0.470042194092827,
        "recall": 0.4520358868184955,
        "f1-score": 0.45495495495495497,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6907900480139677,
        "recall": 0.7701149425287356,
        "f1-score": 0.726157191674433,
        "support": 87.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7007
- **Accuracy:** 0.7011
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.75,
        "recall": 0.42857142857142855,
        "f1-score": 0.5454545454545454,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8028169014084507,
        "recall": 0.8260869565217391,
        "f1-score": 0.8142857142857143,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.08333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.08695652173913043,
        "support": 11.0
    },
    "accuracy": 0.7011494252873564,
    "macro avg": {
        "precision": 0.5453834115805947,
        "recall": 0.44852249200075284,
        "f1-score": 0.48223226049313,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.707598078894825,
        "recall": 0.7011494252873564,
        "f1-score": 0.7006944579658223,
        "support": 87.0
    }
}
```

