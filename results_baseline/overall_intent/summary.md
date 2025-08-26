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

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.8410
- **Accuracy:** 0.8391
- **Best Parameters:** {'max_depth': 10}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.7142857142857143,
        "f1-score": 0.8333333333333334,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.9,
        "recall": 0.9130434782608695,
        "f1-score": 0.9064748201438849,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.4166666666666667,
        "recall": 0.45454545454545453,
        "f1-score": 0.43478260869565216,
        "support": 11.0
    },
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.7722222222222221,
        "recall": 0.6939582156973461,
        "f1-score": 0.7248635873909568,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.846934865900383,
        "recall": 0.8390804597701149,
        "f1-score": 0.8409506278036042,
        "support": 87.0
    }
}
```

## TF-IDF_DecisionTree

- **Weighted F1 Score:** 0.8361
- **Accuracy:** 0.8391
- **Best Parameters:** {'max_depth': 10}
```json
{
    "fonction_phatique": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.9,
        "recall": 0.9130434782608695,
        "f1-score": 0.9064748201438849,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.4,
        "recall": 0.36363636363636365,
        "f1-score": 0.38095238095238093,
        "support": 11.0
    },
    "accuracy": 0.8390804597701149,
    "macro avg": {
        "precision": 0.719047619047619,
        "recall": 0.7112742330133633,
        "f1-score": 0.7148566860797075,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.8333333333333334,
        "recall": 0.8390804597701149,
        "f1-score": 0.8360602158667154,
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

- **Weighted F1 Score:** 0.7616
- **Accuracy:** 0.7701
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.36363636363636365,
        "recall": 0.5714285714285714,
        "f1-score": 0.4444444444444444,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8714285714285714,
        "recall": 0.8840579710144928,
        "f1-score": 0.8776978417266187,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.3333333333333333,
        "recall": 0.18181818181818182,
        "f1-score": 0.23529411764705882,
        "support": 11.0
    },
    "accuracy": 0.7701149425287356,
    "macro avg": {
        "precision": 0.5227994227994228,
        "recall": 0.5457682414204154,
        "f1-score": 0.519145467939374,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7625366970194556,
        "recall": 0.7701149425287356,
        "f1-score": 0.7616149136133961,
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

- **Weighted F1 Score:** 0.7393
- **Accuracy:** 0.7816
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.5,
        "recall": 0.2857142857142857,
        "f1-score": 0.36363636363636365,
        "support": 7.0
    },
    "partage_experience": {
        "precision": 0.8125,
        "recall": 0.9420289855072463,
        "f1-score": 0.87248322147651,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "accuracy": 0.7816091954022989,
    "macro avg": {
        "precision": 0.548611111111111,
        "recall": 0.4395507873768743,
        "f1-score": 0.4596589093233388,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.726772030651341,
        "recall": 0.7816091954022989,
        "f1-score": 0.7392899471122104,
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

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.7003
- **Accuracy:** 0.7356
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
        "precision": 0.8133333333333334,
        "recall": 0.8840579710144928,
        "f1-score": 0.8472222222222222,
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
        "precision": 0.3711111111111111,
        "recall": 0.4375431331953071,
        "f1-score": 0.4000544662309368,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6691954022988507,
        "recall": 0.735632183908046,
        "f1-score": 0.7003324318233041,
        "support": 87.0
    }
}
```

