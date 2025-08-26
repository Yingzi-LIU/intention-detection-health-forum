# Experiment Results Summary

**Labels:** fonction_phatique, partage_experience, recherche_information

## TF-IDF_LogisticRegression

- **Weighted F1 Score:** 0.8608
- **Accuracy:** 0.8851
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
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

## TF-IDF_ngram_SVM

- **Weighted F1 Score:** 0.8434
- **Accuracy:** 0.8621
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
        "precision": 0.88,
        "recall": 0.9565217391304348,
        "f1-score": 0.9166666666666666,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.6,
        "recall": 0.2727272727272727,
        "f1-score": 0.375,
        "support": 11.0
    },
    "accuracy": 0.8620689655172413,
    "macro avg": {
        "precision": 0.7790476190476191,
        "recall": 0.6954639563335215,
        "f1-score": 0.7162698412698413,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8427586206896551,
        "recall": 0.8620689655172413,
        "f1-score": 0.8433908045977011,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_KNN

- **Weighted F1 Score:** 0.8328
- **Accuracy:** 0.8506
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
        "precision": 0.8783783783783784,
        "recall": 0.9420289855072463,
        "f1-score": 0.9090909090909091,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.6,
        "recall": 0.2727272727272727,
        "f1-score": 0.375,
        "support": 11.0
    },
    "accuracy": 0.8505747126436781,
    "macro avg": {
        "precision": 0.7427927927927929,
        "recall": 0.6906330384591254,
        "f1-score": 0.6946969696969697,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8328518173345759,
        "recall": 0.8505747126436781,
        "f1-score": 0.8327847439916406,
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

## TF-IDF_SVM

- **Weighted F1 Score:** 0.8225
- **Accuracy:** 0.8391
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.8333333333333334,
        "recall": 0.7142857142857143,
        "f1-score": 0.7692307692307693,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8666666666666667,
        "recall": 0.9420289855072463,
        "f1-score": 0.9027777777777778,
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
        "precision": 0.7333333333333334,
        "recall": 0.6430139908400777,
        "f1-score": 0.6749832411597118,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.817624521072797,
        "recall": 0.8390804597701149,
        "f1-score": 0.8225130458903277,
        "support": 87.0
    }
}
```

## Word2Vec_KNN

- **Weighted F1 Score:** 0.8185
- **Accuracy:** 0.8506
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.85,
        "recall": 0.9855072463768116,
        "f1-score": 0.912751677852349,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.6666666666666666,
        "recall": 0.18181818181818182,
        "f1-score": 0.2857142857142857,
        "support": 11.0
    },
    "accuracy": 0.8505747126436781,
    "macro avg": {
        "precision": 0.8388888888888889,
        "recall": 0.5795846665411883,
        "f1-score": 0.641912896946454,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8388888888888889,
        "recall": 0.8505747126436781,
        "f1-score": 0.818547494316992,
        "support": 87.0
    }
}
```

## BoW_SVM

- **Weighted F1 Score:** 0.8166
- **Accuracy:** 0.8391
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
        "precision": 0.8666666666666667,
        "recall": 0.9420289855072463,
        "f1-score": 0.9027777777777778,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.4,
        "recall": 0.18181818181818182,
        "f1-score": 0.25,
        "support": 11.0
    },
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.707936507936508,
        "recall": 0.6603300081560951,
        "f1-score": 0.669973544973545,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8068965517241381,
        "recall": 0.8390804597701149,
        "f1-score": 0.8165708812260535,
        "support": 87.0
    }
}
```

## TF-IDF_KNN

- **Weighted F1 Score:** 0.8137
- **Accuracy:** 0.8276
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
        "precision": 0.875,
        "recall": 0.9130434782608695,
        "f1-score": 0.8936170212765957,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.2727272727272727,
        "f1-score": 0.35294117647058826,
        "support": 11.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.6805555555555555,
        "recall": 0.6809712027103331,
        "f1-score": 0.6655193992490613,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.810823754789272,
        "recall": 0.8275862068965517,
        "f1-score": 0.8137003150489837,
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

## BoW_LogisticRegression

- **Weighted F1 Score:** 0.8104
- **Accuracy:** 0.8506
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
        "precision": 0.85,
        "recall": 0.9855072463768116,
        "f1-score": 0.912751677852349,
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
        "precision": 0.7833333333333333,
        "recall": 0.5969006838572056,
        "f1-score": 0.6333103883439454,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.817816091954023,
        "recall": 0.8505747126436781,
        "f1-score": 0.8104081241086564,
        "support": 87.0
    }
}
```

## BoW_DecisionTree

- **Weighted F1 Score:** 0.8044
- **Accuracy:** 0.8506
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
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
        "recall": 0.09090909090909091,
        "f1-score": 0.16666666666666666,
        "support": 11.0
    },
    "accuracy": 0.8505747126436781,
    "macro avg": {
        "precision": 0.9471544715447154,
        "recall": 0.5541125541125541,
        "f1-score": 0.602615559569202,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.874264087468461,
        "recall": 0.8505747126436781,
        "f1-score": 0.8044120123361959,
        "support": 87.0
    }
}
```

## Bert_LogisticRegression

- **Weighted F1 Score:** 0.7922
- **Accuracy:** 0.8161
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 0.6666666666666666,
        "recall": 0.5714285714285714,
        "f1-score": 0.6153846153846154,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8552631578947368,
        "recall": 0.9420289855072463,
        "f1-score": 0.896551724137931,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.4,
        "recall": 0.18181818181818182,
        "f1-score": 0.25,
        "support": 11.0
    },
    "accuracy": 0.8160919540229885,
    "macro avg": {
        "precision": 0.6406432748538012,
        "recall": 0.5650919129179999,
        "f1-score": 0.5873121131741822,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7825267190965921,
        "recall": 0.8160919540229885,
        "f1-score": 0.79218116405988,
        "support": 87.0
    }
}
```

## Bert_DecisionTree

- **Weighted F1 Score:** 0.7789
- **Accuracy:** 0.7816
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.4,
        "recall": 0.5714285714285714,
        "f1-score": 0.47058823529411764,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8840579710144928,
        "recall": 0.8840579710144928,
        "f1-score": 0.8840579710144928,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.375,
        "recall": 0.2727272727272727,
        "f1-score": 0.3157894736842105,
        "support": 11.0
    },
    "accuracy": 0.7816091954022989,
    "macro avg": {
        "precision": 0.5530193236714976,
        "recall": 0.5760712717234456,
        "f1-score": 0.5568118933309404,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7807471264367816,
        "recall": 0.7816091954022989,
        "f1-score": 0.7789402512366108,
        "support": 87.0
    }
}
```

## TF-IDF_DecisionTree

- **Weighted F1 Score:** 0.7712
- **Accuracy:** 0.7471
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
        "precision": 0.9137931034482759,
        "recall": 0.7681159420289855,
        "f1-score": 0.8346456692913385,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.3,
        "recall": 0.5454545454545454,
        "f1-score": 0.3870967741935484,
        "support": 11.0
    },
    "accuracy": 0.7471264367816092,
    "macro avg": {
        "precision": 0.6268199233716475,
        "recall": 0.7235711148754627,
        "f1-score": 0.657247481161629,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8163033425815828,
        "recall": 0.7471264367816092,
        "f1-score": 0.771248456290016,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.7593
- **Accuracy:** 0.7356
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
        "precision": 0.8983050847457628,
        "recall": 0.7681159420289855,
        "f1-score": 0.828125,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.2631578947368421,
        "recall": 0.45454545454545453,
        "f1-score": 0.3333333333333333,
        "support": 11.0
    },
    "accuracy": 0.735632183908046,
    "macro avg": {
        "precision": 0.6093765487164239,
        "recall": 0.6932680845724324,
        "f1-score": 0.6371527777777778,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7993615443244778,
        "recall": 0.735632183908046,
        "f1-score": 0.7592792145593871,
        "support": 87.0
    }
}
```

## Bert_KNN

- **Weighted F1 Score:** 0.7535
- **Accuracy:** 0.8161
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 0.75,
        "recall": 0.42857142857142855,
        "f1-score": 0.5454545454545454,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8192771084337349,
        "recall": 0.9855072463768116,
        "f1-score": 0.8947368421052632,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.8160919540229885,
        "recall": 0.9342105263157895,
        "f1-score": 0.8711656441717791,
        "support": 76.0
    },
    "macro avg": {
        "precision": 0.7846385542168675,
        "recall": 0.7070393374741201,
        "f1-score": 0.7200956937799043,
        "support": 76.0
    },
    "weighted avg": {
        "precision": 0.8128963221306278,
        "recall": 0.9342105263157895,
        "f1-score": 0.862566104255855,
        "support": 76.0
    }
}
```

## FastText_DecisionTree

- **Weighted F1 Score:** 0.7410
- **Accuracy:** 0.7816
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.6666666666666666,
        "recall": 0.2857142857142857,
        "f1-score": 0.4,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8125,
        "recall": 0.9420289855072463,
        "f1-score": 0.87248322147651,
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
        "precision": 0.5763888888888888,
        "recall": 0.4395507873768743,
        "f1-score": 0.4686055182699478,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7296455938697318,
        "recall": 0.7816091954022989,
        "f1-score": 0.7410115971097225,
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

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.7231
- **Accuracy:** 0.7471
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.3,
        "recall": 0.42857142857142855,
        "f1-score": 0.35294117647058826,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8243243243243243,
        "recall": 0.8840579710144928,
        "f1-score": 0.8531468531468531,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "accuracy": 0.7471264367816092,
    "macro avg": {
        "precision": 0.4858858858858859,
        "recall": 0.46784616349833735,
        "f1-score": 0.4496483908248614,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7200579890235063,
        "recall": 0.7471264367816092,
        "f1-score": 0.7230936744121328,
        "support": 87.0
    }
}
```

## Bert_SVM

- **Weighted F1 Score:** 0.7229
- **Accuracy:** 0.7356
- **Best Parameters:** {'C': 1, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.45454545454545453,
        "recall": 0.7142857142857143,
        "f1-score": 0.5555555555555556,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.855072463768116,
        "recall": 0.855072463768116,
        "f1-score": 0.855072463768116,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.735632183908046,
    "macro avg": {
        "precision": 0.4365393061045235,
        "recall": 0.52311939268461,
        "f1-score": 0.4702093397745572,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7147335423197492,
        "recall": 0.735632183908046,
        "f1-score": 0.722860791826309,
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

## BoW_KNN

- **Weighted F1 Score:** 0.7015
- **Accuracy:** 0.7011
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.3,
        "recall": 0.8571428571428571,
        "f1-score": 0.4444444444444444,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8571428571428571,
        "recall": 0.782608695652174,
        "f1-score": 0.8181818181818182,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.25,
        "recall": 0.09090909090909091,
        "f1-score": 0.13333333333333333,
        "support": 11.0
    },
    "accuracy": 0.7011494252873564,
    "macro avg": {
        "precision": 0.469047619047619,
        "recall": 0.5768868812347073,
        "f1-score": 0.4653198653198653,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7355500821018062,
        "recall": 0.7011494252873564,
        "f1-score": 0.7015209566933706,
        "support": 87.0
    }
}
```

