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

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.8459
- **Accuracy:** 0.8621
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
        "precision": 0.88,
        "recall": 0.9565217391304348,
        "f1-score": 0.9166666666666666,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.2727272727272727,
        "f1-score": 0.35294117647058826,
        "support": 11.0
    },
    "accuracy": 0.8620689655172413,
    "macro avg": {
        "precision": 0.7933333333333333,
        "recall": 0.6954639563335215,
        "f1-score": 0.7308949220713927,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8416091954022988,
        "recall": 0.8620689655172413,
        "f1-score": 0.8459067977323557,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.8459
- **Accuracy:** 0.8621
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
        "precision": 0.88,
        "recall": 0.9565217391304348,
        "f1-score": 0.9166666666666666,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.2727272727272727,
        "f1-score": 0.35294117647058826,
        "support": 11.0
    },
    "accuracy": 0.8620689655172413,
    "macro avg": {
        "precision": 0.7933333333333333,
        "recall": 0.6954639563335215,
        "f1-score": 0.7308949220713927,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8416091954022988,
        "recall": 0.8620689655172413,
        "f1-score": 0.8459067977323557,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_MultinomialNB_Enhanced

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

## TF-IDF_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.8346
- **Accuracy:** 0.8506
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "fonction_phatique": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8783783783783784,
        "recall": 0.9420289855072463,
        "f1-score": 0.9090909090909091,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.2727272727272727,
        "f1-score": 0.35294117647058826,
        "support": 11.0
    },
    "accuracy": 0.8505747126436781,
    "macro avg": {
        "precision": 0.7451737451737452,
        "recall": 0.6906330384591254,
        "f1-score": 0.7063916475681181,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8288288288288289,
        "recall": 0.8505747126436781,
        "f1-score": 0.8345933984879217,
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

- **Weighted F1 Score:** 0.8086
- **Accuracy:** 0.8161
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
    "accuracy": 0.8160919540229885,
    "macro avg": {
        "precision": 0.6805555555555557,
        "recall": 0.6333521550912855,
        "f1-score": 0.6542825968357884,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8031609195402298,
        "recall": 0.8160919540229885,
        "f1-score": 0.808553906352879,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.8086
- **Accuracy:** 0.8161
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.8333333333333334,
        "recall": 0.7142857142857143,
        "f1-score": 0.7692307692307693,
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
    "accuracy": 0.8160919540229885,
    "macro avg": {
        "precision": 0.6805555555555557,
        "recall": 0.6333521550912855,
        "f1-score": 0.6542825968357884,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8031609195402298,
        "recall": 0.8160919540229885,
        "f1-score": 0.808553906352879,
        "support": 87.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.7898
- **Accuracy:** 0.8276
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8375,
        "recall": 0.9710144927536232,
        "f1-score": 0.8993288590604027,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.7236111111111111,
        "recall": 0.5444507183637618,
        "f1-score": 0.5898195763967576,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7868295019157088,
        "recall": 0.8275862068965517,
        "f1-score": 0.7898394130747752,
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
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.6104417670682731,
        "recall": 0.5238095238095238,
        "f1-score": 0.5450558213716109,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7397867331394543,
        "recall": 0.8390804597701149,
        "f1-score": 0.778570642908211,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.7670
- **Accuracy:** 0.8161
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8271604938271605,
        "recall": 0.9710144927536232,
        "f1-score": 0.8933333333333333,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8160919540229885,
    "macro avg": {
        "precision": 0.6090534979423868,
        "recall": 0.5141476880607315,
        "f1-score": 0.5402020202020202,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7364836100468285,
        "recall": 0.8160919540229885,
        "f1-score": 0.7670219435736677,
        "support": 87.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.7575
- **Accuracy:** 0.7701
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 0.75,
        "recall": 0.8571428571428571,
        "f1-score": 0.8,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8450704225352113,
        "recall": 0.8695652173913043,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.125,
        "recall": 0.09090909090909091,
        "f1-score": 0.10526315789473684,
        "support": 11.0
    },
    "accuracy": 0.7701149425287356,
    "macro avg": {
        "precision": 0.5733568075117371,
        "recall": 0.605872388481084,
        "f1-score": 0.5874686716791979,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7463776914359721,
        "recall": 0.7701149425287356,
        "f1-score": 0.7574799066632096,
        "support": 87.0
    }
}
```

## GloVe_KNN_Enhanced

- **Weighted F1 Score:** 0.8114
- **Accuracy:** 0.8506
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8589743589743589,
        "recall": 0.9710144927536232,
        "f1-score": 0.9115646258503401,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "accuracy": 0.8505747126436781,
    "macro avg": {
        "precision": 0.7387057387057387,
        "recall": 0.639688813601857,
        "f1-score": 0.6408512122797837,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8134394341290894,
        "recall": 0.8505747126436781,
        "f1-score": 0.8113823778848409,
        "support": 87.0
    }
}
```

## GloVe_SVM_Enhanced

- **Weighted F1 Score:** 0.8039
- **Accuracy:** 0.8621
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
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
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8620689655172413,
    "macro avg": {
        "precision": 0.6172839506172839,
        "recall": 0.6190476190476191,
        "f1-score": 0.6143589743589745,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.756066411238825,
        "recall": 0.8620689655172413,
        "f1-score": 0.8039257294429709,
        "support": 87.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.8035
- **Accuracy:** 0.8621
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8625,
        "recall": 1.0,
        "f1-score": 0.9261744966442953,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8620689655172413,
    "macro avg": {
        "precision": 0.5732142857142857,
        "recall": 0.6190476190476191,
        "f1-score": 0.5944391179290508,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7530172413793104,
        "recall": 0.8620689655172413,
        "f1-score": 0.8035177042351307,
        "support": 87.0
    }
}
```

## GloVe_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.8011
- **Accuracy:** 0.8276
- **Best Parameters:** {'C': 1, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8552631578947368,
        "recall": 0.9420289855072463,
        "f1-score": 0.896551724137931,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.2,
        "recall": 0.09090909090909091,
        "f1-score": 0.125,
        "support": 11.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.6850877192982456,
        "recall": 0.6300269778530647,
        "f1-score": 0.6482095490716181,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7840592861464006,
        "recall": 0.8275862068965517,
        "f1-score": 0.8011334187017897,
        "support": 87.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7822
- **Accuracy:** 0.7701
- **Best Parameters:** {'max_depth': 10}
```json
{
    "fonction_phatique": {
        "precision": 0.6,
        "recall": 0.8571428571428571,
        "f1-score": 0.7058823529411765,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.9047619047619048,
        "recall": 0.8260869565217391,
        "f1-score": 0.8636363636363636,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.2857142857142857,
        "recall": 0.36363636363636365,
        "f1-score": 0.32,
        "support": 11.0
    },
    "accuracy": 0.7701149425287356,
    "macro avg": {
        "precision": 0.5968253968253968,
        "recall": 0.6822887257669866,
        "f1-score": 0.6298395721925134,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8019704433497538,
        "recall": 0.7701149425287356,
        "f1-score": 0.7822078800172106,
        "support": 87.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7786
- **Accuracy:** 0.8391
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
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
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.6104417670682731,
        "recall": 0.5238095238095238,
        "f1-score": 0.5450558213716109,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7397867331394543,
        "recall": 0.8390804597701149,
        "f1-score": 0.778570642908211,
        "support": 87.0
    }
}
```

## Word2Vec_SVM_Enhanced

- **Weighted F1 Score:** 0.7786
- **Accuracy:** 0.8391
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
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
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.6104417670682731,
        "recall": 0.5238095238095238,
        "f1-score": 0.5450558213716109,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7397867331394543,
        "recall": 0.8390804597701149,
        "f1-score": 0.778570642908211,
        "support": 87.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.7786
- **Accuracy:** 0.8391
- **Best Parameters:** {'n_neighbors': 7}
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
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.6104417670682731,
        "recall": 0.5238095238095238,
        "f1-score": 0.5450558213716109,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7397867331394543,
        "recall": 0.8390804597701149,
        "f1-score": 0.778570642908211,
        "support": 87.0
    }
}
```

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7786
- **Accuracy:** 0.8391
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
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
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.6104417670682731,
        "recall": 0.5238095238095238,
        "f1-score": 0.5450558213716109,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7397867331394543,
        "recall": 0.8390804597701149,
        "f1-score": 0.778570642908211,
        "support": 87.0
    }
}
```

## FastText_SVM_Enhanced

- **Weighted F1 Score:** 0.7786
- **Accuracy:** 0.8391
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
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
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.6104417670682731,
        "recall": 0.5238095238095238,
        "f1-score": 0.5450558213716109,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7397867331394543,
        "recall": 0.8390804597701149,
        "f1-score": 0.778570642908211,
        "support": 87.0
    }
}
```

## GloVe_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7448
- **Accuracy:** 0.7816
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.6666666666666666,
        "recall": 0.5714285714285714,
        "f1-score": 0.6153846153846154,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8311688311688312,
        "recall": 0.927536231884058,
        "f1-score": 0.8767123287671232,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.7816091954022989,
    "macro avg": {
        "precision": 0.4992784992784993,
        "recall": 0.4996549344375431,
        "f1-score": 0.49736564805057953,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7128427128427128,
        "recall": 0.7816091954022989,
        "f1-score": 0.7448372757772852,
        "support": 87.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.6973
- **Accuracy:** 0.6667
- **Best Parameters:** {'max_depth': None}
```json
{
    "fonction_phatique": {
        "precision": 0.625,
        "recall": 0.7142857142857143,
        "f1-score": 0.6666666666666666,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8448275862068966,
        "recall": 0.7101449275362319,
        "f1-score": 0.7716535433070866,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.19047619047619047,
        "recall": 0.36363636363636365,
        "f1-score": 0.25,
        "support": 11.0
    },
    "accuracy": 0.6666666666666666,
    "macro avg": {
        "precision": 0.5534345922276956,
        "recall": 0.59602233515277,
        "f1-score": 0.5627734033245844,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7444062246380915,
        "recall": 0.6666666666666666,
        "f1-score": 0.6972501282167315,
        "support": 87.0
    }
}
```

