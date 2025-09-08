# Experiment Results Summary

**Labels:** fonction_phatique, partage_experience, recherche_information

## TF-IDF_LogisticRegression

- **Weighted F1 Score:** 0.8730
- **Accuracy:** 0.8966
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
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

## TF-IDF_MultinomialNB

- **Weighted F1 Score:** 0.8608
- **Accuracy:** 0.8851
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.7142857142857143,
        "f1-score": 0.8333333333333334,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8734177215189873,
        "recall": 1.0,
        "f1-score": 0.9324324324324325,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 1.0,
        "recall": 0.2727272727272727,
        "f1-score": 0.42857142857142855,
        "support": 11.0
    },
    "accuracy": 0.8850574712643678,
    "macro avg": {
        "precision": 0.9578059071729959,
        "recall": 0.6623376623376623,
        "f1-score": 0.7314457314457314,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8996071584460934,
        "recall": 0.8850574712643678,
        "f1-score": 0.8607523779937571,
        "support": 87.0
    }
}
```

## BoW_LogisticRegression

- **Weighted F1 Score:** 0.8346
- **Accuracy:** 0.8506
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
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

## TF-IDF_SVM

- **Weighted F1 Score:** 0.8346
- **Accuracy:** 0.8506
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
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

## TF-IDF_ngram_SVM

- **Weighted F1 Score:** 0.8346
- **Accuracy:** 0.8506
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
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

## TF-IDF_ngram_LogisticRegression

- **Weighted F1 Score:** 0.8299
- **Accuracy:** 0.8736
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
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

## BoW_DecisionTree

- **Weighted F1 Score:** 0.8271
- **Accuracy:** 0.8621
- **Best Parameters:** {'max_depth': 10}
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

## BoW_SVM

- **Weighted F1 Score:** 0.8247
- **Accuracy:** 0.8506
- **Best Parameters:** {'C': 1, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.868421052631579,
        "recall": 0.9565217391304348,
        "f1-score": 0.9103448275862069,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.18181818181818182,
        "f1-score": 0.26666666666666666,
        "support": 11.0
    },
    "accuracy": 0.8505747126436781,
    "macro avg": {
        "precision": 0.7418546365914787,
        "recall": 0.6651609260304913,
        "f1-score": 0.6780514504652436,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8209316394434363,
        "recall": 0.8505747126436781,
        "f1-score": 0.8246796142158807,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_KNN

- **Weighted F1 Score:** 0.8239
- **Accuracy:** 0.8391
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.75,
        "recall": 0.8571428571428571,
        "f1-score": 0.8,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8767123287671232,
        "recall": 0.927536231884058,
        "f1-score": 0.9014084507042254,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.2727272727272727,
        "f1-score": 0.35294117647058826,
        "support": 11.0
    },
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.708904109589041,
        "recall": 0.6858021205847292,
        "f1-score": 0.6847832090582712,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8188867894819714,
        "recall": 0.8390804597701149,
        "f1-score": 0.8239027131007817,
        "support": 87.0
    }
}
```

## BoW_MultinomialNB

- **Weighted F1 Score:** 0.8120
- **Accuracy:** 0.8506
- **Best Parameters:** {'alpha': 1.0}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.42857142857142855,
        "f1-score": 0.6,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8414634146341463,
        "recall": 1.0,
        "f1-score": 0.9139072847682119,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 1.0,
        "recall": 0.18181818181818182,
        "f1-score": 0.3076923076923077,
        "support": 11.0
    },
    "accuracy": 0.8505747126436781,
    "macro avg": {
        "precision": 0.9471544715447154,
        "recall": 0.5367965367965368,
        "f1-score": 0.6071998641535065,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.874264087468461,
        "recall": 0.8505747126436781,
        "f1-score": 0.8120025061335864,
        "support": 87.0
    }
}
```

## TF-IDF_KNN

- **Weighted F1 Score:** 0.8050
- **Accuracy:** 0.8161
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.6666666666666666,
        "recall": 0.8571428571428571,
        "f1-score": 0.75,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8732394366197183,
        "recall": 0.8985507246376812,
        "f1-score": 0.8857142857142857,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.42857142857142855,
        "recall": 0.2727272727272727,
        "f1-score": 0.3333333333333333,
        "support": 11.0
    },
    "accuracy": 0.8160919540229885,
    "macro avg": {
        "precision": 0.6561591772859379,
        "recall": 0.6761402848359369,
        "f1-score": 0.6563492063492063,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8003962472150913,
        "recall": 0.8160919540229885,
        "f1-score": 0.8049534756431309,
        "support": 87.0
    }
}
```

## GloVe_DecisionTree

- **Weighted F1 Score:** 0.8016
- **Accuracy:** 0.8161
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.5,
        "recall": 0.42857142857142855,
        "f1-score": 0.46153846153846156,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8533333333333334,
        "recall": 0.927536231884058,
        "f1-score": 0.8888888888888888,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.6666666666666666,
        "recall": 0.36363636363636365,
        "f1-score": 0.47058823529411764,
        "support": 11.0
    },
    "accuracy": 0.8160919540229885,
    "macro avg": {
        "precision": 0.6733333333333333,
        "recall": 0.5732480080306167,
        "f1-score": 0.6070051952404895,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8013026819923372,
        "recall": 0.8160919540229885,
        "f1-score": 0.8016157833602051,
        "support": 87.0
    }
}
```

## GloVe_SVM

- **Weighted F1 Score:** 0.7992
- **Accuracy:** 0.7931
- **Best Parameters:** {'C': 1, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8805970149253731,
        "recall": 0.855072463768116,
        "f1-score": 0.8676470588235294,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.3076923076923077,
        "recall": 0.36363636363636365,
        "f1-score": 0.3333333333333333,
        "support": 11.0
    },
    "accuracy": 0.7931034482758621,
    "macro avg": {
        "precision": 0.6818107265868459,
        "recall": 0.6919505615157789,
        "f1-score": 0.6860410830999067,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8062736714306452,
        "recall": 0.7931034482758621,
        "f1-score": 0.7992449853504622,
        "support": 87.0
    }
}
```

## GloVe_LogisticRegression

- **Weighted F1 Score:** 0.7961
- **Accuracy:** 0.8276
- **Best Parameters:** {'C': 1, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.7142857142857143,
        "f1-score": 0.8333333333333334,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8461538461538461,
        "recall": 0.9565217391304348,
        "f1-score": 0.8979591836734694,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.25,
        "recall": 0.09090909090909091,
        "f1-score": 0.13333333333333333,
        "support": 11.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.6987179487179488,
        "recall": 0.5872388481084133,
        "f1-score": 0.6215419501133786,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.78315649867374,
        "recall": 0.8275862068965517,
        "f1-score": 0.7960825709594184,
        "support": 87.0
    }
}
```

## Word2Vec_KNN

- **Weighted F1 Score:** 0.7894
- **Accuracy:** 0.8391
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.42857142857142855,
        "f1-score": 0.6,
        "support": 7.0
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
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.9437751004016065,
        "recall": 0.5064935064935064,
        "f1-score": 0.558187134502924,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8662235147486497,
        "recall": 0.8390804597701149,
        "f1-score": 0.7894031054648114,
        "support": 87.0
    }
}
```

## GloVe_KNN

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

## TF-IDF_DecisionTree

- **Weighted F1 Score:** 0.7595
- **Accuracy:** 0.7241
- **Best Parameters:** {'max_depth': None}
```json
{
    "fonction_phatique": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.9107142857142857,
        "recall": 0.7391304347826086,
        "f1-score": 0.816,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.25,
        "recall": 0.5454545454545454,
        "f1-score": 0.34285714285714286,
        "support": 11.0
    },
    "accuracy": 0.7241379310344828,
    "macro avg": {
        "precision": 0.6726190476190476,
        "recall": 0.7139092791266703,
        "f1-score": 0.672,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.822865353037767,
        "recall": 0.7241379310344828,
        "f1-score": 0.7594876847290639,
        "support": 87.0
    }
}
```

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.7568
- **Accuracy:** 0.7471
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
        "precision": 0.8636363636363636,
        "recall": 0.8260869565217391,
        "f1-score": 0.8444444444444444,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.3125,
        "recall": 0.45454545454545453,
        "f1-score": 0.37037037037037035,
        "support": 11.0
    },
    "accuracy": 0.7471264367816092,
    "macro avg": {
        "precision": 0.5920454545454545,
        "recall": 0.5697346132128741,
        "f1-score": 0.571604938271605,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7727403343782655,
        "recall": 0.7471264367816092,
        "f1-score": 0.7567901234567901,
        "support": 87.0
    }
}
```

## BoW_KNN

- **Weighted F1 Score:** 0.7515
- **Accuracy:** 0.7356
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 0.3,
        "recall": 0.8571428571428571,
        "f1-score": 0.4444444444444444,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.9016393442622951,
        "recall": 0.7971014492753623,
        "f1-score": 0.8461538461538461,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.2727272727272727,
        "f1-score": 0.35294117647058826,
        "support": 11.0
    },
    "accuracy": 0.735632183908046,
    "macro avg": {
        "precision": 0.5672131147540983,
        "recall": 0.642323859715164,
        "f1-score": 0.5478464890229596,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8024495948746938,
        "recall": 0.735632183908046,
        "f1-score": 0.7514721774356663,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.7385
- **Accuracy:** 0.7126
- **Best Parameters:** {'max_depth': None}
```json
{
    "fonction_phatique": {
        "precision": 0.6666666666666666,
        "recall": 0.8571428571428571,
        "f1-score": 0.75,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8813559322033898,
        "recall": 0.7536231884057971,
        "f1-score": 0.8125,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.21052631578947367,
        "recall": 0.36363636363636365,
        "f1-score": 0.26666666666666666,
        "support": 11.0
    },
    "accuracy": 0.7126436781609196,
    "macro avg": {
        "precision": 0.5861829715531767,
        "recall": 0.658134136395006,
        "f1-score": 0.6097222222222222,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7792645455446525,
        "recall": 0.7126436781609196,
        "f1-score": 0.7384578544061303,
        "support": 87.0
    }
}
```

## FastText_KNN

- **Weighted F1 Score:** 0.7372
- **Accuracy:** 0.8046
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 0.6666666666666666,
        "recall": 0.2857142857142857,
        "f1-score": 0.4,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8095238095238095,
        "recall": 0.9855072463768116,
        "f1-score": 0.8888888888888888,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 0.9210526315789473,
        "f1-score": 0.8588957055214724,
        "support": 76.0
    },
    "macro avg": {
        "precision": 0.7380952380952381,
        "recall": 0.6356107660455487,
        "f1-score": 0.6444444444444444,
        "support": 76.0
    },
    "weighted avg": {
        "precision": 0.7963659147869674,
        "recall": 0.9210526315789473,
        "f1-score": 0.8438596491228069,
        "support": 76.0
    }
}
```

## TF-IDF_ngram_MultinomialNB

- **Weighted F1 Score:** 0.7262
- **Accuracy:** 0.8046
- **Best Parameters:** {'alpha': 0.5}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.14285714285714285,
        "f1-score": 0.25,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8023255813953488,
        "recall": 1.0,
        "f1-score": 0.8903225806451613,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 0.9210526315789473,
        "f1-score": 0.8588957055214724,
        "support": 76.0
    },
    "macro avg": {
        "precision": 0.9011627906976745,
        "recall": 0.5714285714285714,
        "f1-score": 0.5701612903225807,
        "support": 76.0
    },
    "weighted avg": {
        "precision": 0.820532435740514,
        "recall": 0.9210526315789473,
        "f1-score": 0.8313455008488965,
        "support": 76.0
    }
}
```

## FastText_DecisionTree

- **Weighted F1 Score:** 0.7184
- **Accuracy:** 0.7356
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.3333333333333333,
        "recall": 0.2857142857142857,
        "f1-score": 0.3076923076923077,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8108108108108109,
        "recall": 0.8695652173913043,
        "f1-score": 0.8391608391608392,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.2857142857142857,
        "recall": 0.18181818181818182,
        "f1-score": 0.2222222222222222,
        "support": 11.0
    },
    "accuracy": 0.735632183908046,
    "macro avg": {
        "precision": 0.4766194766194767,
        "recall": 0.44569922830792397,
        "f1-score": 0.45635845635845634,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7060015680705337,
        "recall": 0.735632183908046,
        "f1-score": 0.718395270119408,
        "support": 87.0
    }
}
```

## Word2Vec_LogisticRegression

- **Weighted F1 Score:** 0.7016
- **Accuracy:** 0.7931
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    },
    "macro avg": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    },
    "weighted avg": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    }
}
```

## Word2Vec_SVM

- **Weighted F1 Score:** 0.7016
- **Accuracy:** 0.7931
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    },
    "macro avg": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    },
    "weighted avg": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    }
}
```

## FastText_LogisticRegression

- **Weighted F1 Score:** 0.7016
- **Accuracy:** 0.7931
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    },
    "macro avg": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    },
    "weighted avg": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    }
}
```

## FastText_SVM

- **Weighted F1 Score:** 0.7016
- **Accuracy:** 0.7931
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    },
    "macro avg": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    },
    "weighted avg": {
        "precision": 0.7931034482758621,
        "recall": 1.0,
        "f1-score": 0.8846153846153846,
        "support": 69.0
    }
}
```

