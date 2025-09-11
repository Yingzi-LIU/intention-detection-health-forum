# Experiment Results Summary

**Labels:** NA_CATEGORY, diagnostique, symptome, traitement

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.6883
- **Accuracy:** 0.6897
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6666666666666666,
        "recall": 0.5,
        "f1-score": 0.5714285714285714,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.7428571428571429,
        "recall": 0.7878787878787878,
        "f1-score": 0.7647058823529411,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5806451612903226,
        "recall": 0.6666666666666666,
        "f1-score": 0.6206896551724138,
        "support": 27.0
    },
    "accuracy": 0.6896551724137931,
    "macro avg": {
        "precision": 0.747542242703533,
        "recall": 0.7029220779220778,
        "f1-score": 0.7199752580077123,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6956900965799743,
        "recall": 0.6896551724137931,
        "f1-score": 0.68832212295876,
        "support": 87.0
    }
}
```

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.6668
- **Accuracy:** 0.6667
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6111111111111112,
        "recall": 0.55,
        "f1-score": 0.5789473684210527,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.7142857142857143,
        "recall": 0.7575757575757576,
        "f1-score": 0.7352941176470589,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5714285714285714,
        "recall": 0.5925925925925926,
        "f1-score": 0.5818181818181818,
        "support": 27.0
    },
    "accuracy": 0.6666666666666666,
    "macro avg": {
        "precision": 0.7242063492063493,
        "recall": 0.6893278018278017,
        "f1-score": 0.7047841477408041,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6692209450830141,
        "recall": 0.6666666666666666,
        "f1-score": 0.6668308347287744,
        "support": 87.0
    }
}
```

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6587
- **Accuracy:** 0.6667
- **Best Parameters:** {'classifier__C': 1, 'classifier__solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.75,
        "recall": 0.45,
        "f1-score": 0.5625,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6511627906976745,
        "recall": 0.8484848484848485,
        "f1-score": 0.7368421052631579,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5769230769230769,
        "recall": 0.5555555555555556,
        "f1-score": 0.5660377358490566,
        "support": 27.0
    },
    "accuracy": 0.6666666666666666,
    "macro avg": {
        "precision": 0.7445214669051878,
        "recall": 0.6777958152958152,
        "f1-score": 0.6971141910472843,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6789114387350154,
        "recall": 0.6666666666666666,
        "f1-score": 0.6587396184269793,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6505
- **Accuracy:** 0.6552
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6428571428571429,
        "recall": 0.45,
        "f1-score": 0.5294117647058824,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6666666666666666,
        "recall": 0.7878787878787878,
        "f1-score": 0.7222222222222222,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5714285714285714,
        "recall": 0.5925925925925926,
        "f1-score": 0.5818181818181818,
        "support": 27.0
    },
    "accuracy": 0.6551724137931034,
    "macro avg": {
        "precision": 0.7202380952380951,
        "recall": 0.6719035594035594,
        "f1-score": 0.6891322729558025,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.658456486042693,
        "recall": 0.6551724137931034,
        "f1-score": 0.6504850344606937,
        "support": 87.0
    }
}
```

## TF-IDF_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.6476
- **Accuracy:** 0.6552
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6153846153846154,
        "recall": 0.4,
        "f1-score": 0.48484848484848486,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6923076923076923,
        "recall": 0.8181818181818182,
        "f1-score": 0.75,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5517241379310345,
        "recall": 0.5925925925925926,
        "f1-score": 0.5714285714285714,
        "support": 27.0
    },
    "accuracy": 0.6551724137931034,
    "macro avg": {
        "precision": 0.7148541114058355,
        "recall": 0.666979316979317,
        "f1-score": 0.6823384948384947,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6557516997469435,
        "recall": 0.6551724137931034,
        "f1-score": 0.6475526389319493,
        "support": 87.0
    }
}
```

## BoW_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.6153
- **Accuracy:** 0.6207
- **Best Parameters:** {'classifier__alpha': 0.5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5,
        "recall": 0.4,
        "f1-score": 0.4444444444444444,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6944444444444444,
        "recall": 0.7575757575757576,
        "f1-score": 0.7246376811594203,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5357142857142857,
        "recall": 0.5555555555555556,
        "f1-score": 0.5454545454545454,
        "support": 27.0
    },
    "accuracy": 0.6206896551724138,
    "macro avg": {
        "precision": 0.6468253968253967,
        "recall": 0.6425685425685426,
        "f1-score": 0.6429198820503168,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6135741652983032,
        "recall": 0.6206896551724138,
        "f1-score": 0.6152782194761205,
        "support": 87.0
    }
}
```

## TF-IDF_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.5964
- **Accuracy:** 0.5977
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.42105263157894735,
        "recall": 0.4,
        "f1-score": 0.41025641025641024,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6666666666666666,
        "recall": 0.7272727272727273,
        "f1-score": 0.6956521739130435,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5384615384615384,
        "recall": 0.5185185185185185,
        "f1-score": 0.5283018867924528,
        "support": 27.0
    },
    "accuracy": 0.5977011494252874,
    "macro avg": {
        "precision": 0.656545209176788,
        "recall": 0.6257335257335257,
        "f1-score": 0.6393218485097074,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5972357950579366,
        "recall": 0.5977011494252874,
        "f1-score": 0.5964061994160152,
        "support": 87.0
    }
}
```

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.5935
- **Accuracy:** 0.6207
- **Best Parameters:** {'classifier__C': 0.1, 'classifier__kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.7142857142857143,
        "recall": 0.25,
        "f1-score": 0.37037037037037035,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6,
        "recall": 0.9090909090909091,
        "f1-score": 0.7228915662650602,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5769230769230769,
        "recall": 0.5555555555555556,
        "f1-score": 0.5660377358490566,
        "support": 27.0
    },
    "accuracy": 0.6206896551724138,
    "macro avg": {
        "precision": 0.7228021978021979,
        "recall": 0.5715187590187589,
        "f1-score": 0.5966430999393036,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6512946823291651,
        "recall": 0.6206896551724138,
        "f1-score": 0.5935259431377932,
        "support": 87.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.5927
- **Accuracy:** 0.5977
- **Best Parameters:** {'classifier__max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6666666666666666,
        "recall": 0.4,
        "f1-score": 0.5,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5581395348837209,
        "recall": 0.7272727272727273,
        "f1-score": 0.631578947368421,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5384615384615384,
        "recall": 0.5185185185185185,
        "f1-score": 0.5283018867924528,
        "support": 27.0
    },
    "accuracy": 0.5977011494252874,
    "macro avg": {
        "precision": 0.6908169350029815,
        "recall": 0.6257335257335257,
        "f1-score": 0.6457394393094492,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6125333278500881,
        "recall": 0.5977011494252874,
        "f1-score": 0.5927332720470412,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_MultinomialNB_Enhanced

- **Weighted F1 Score:** 0.5902
- **Accuracy:** 0.5977
- **Best Parameters:** {'classifier__alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.4375,
        "recall": 0.35,
        "f1-score": 0.3888888888888889,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6756756756756757,
        "recall": 0.7575757575757576,
        "f1-score": 0.7142857142857143,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5185185185185185,
        "recall": 0.5185185185185185,
        "f1-score": 0.5185185185185185,
        "support": 27.0
    },
    "accuracy": 0.5977011494252874,
    "macro avg": {
        "precision": 0.6222092628342628,
        "recall": 0.6208092833092833,
        "f1-score": 0.6197089947089948,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5867505436470953,
        "recall": 0.5977011494252874,
        "f1-score": 0.5902207626345558,
        "support": 87.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.5790
- **Accuracy:** 0.5862
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.4090909090909091,
        "recall": 0.45,
        "f1-score": 0.42857142857142855,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.625,
        "recall": 0.7575757575757576,
        "f1-score": 0.684931506849315,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6111111111111112,
        "recall": 0.4074074074074074,
        "f1-score": 0.4888888888888889,
        "support": 27.0
    },
    "accuracy": 0.5862068965517241,
    "macro avg": {
        "precision": 0.6255862193362194,
        "recall": 0.6180315055315055,
        "f1-score": 0.6148836703631224,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5897335423197492,
        "recall": 0.5862068965517241,
        "f1-score": 0.5790134287063904,
        "support": 87.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.5659
- **Accuracy:** 0.5747
- **Best Parameters:** {'classifier__max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.46153846153846156,
        "recall": 0.3,
        "f1-score": 0.36363636363636365,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6153846153846154,
        "recall": 0.7272727272727273,
        "f1-score": 0.6666666666666666,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.4827586206896552,
        "recall": 0.5185185185185185,
        "f1-score": 0.5,
        "support": 27.0
    },
    "accuracy": 0.5747126436781609,
    "macro avg": {
        "precision": 0.6399204244031831,
        "recall": 0.6007335257335257,
        "f1-score": 0.6133449883449883,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5698039574377268,
        "recall": 0.5747126436781609,
        "f1-score": 0.5659111003938591,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.5630
- **Accuracy:** 0.5632
- **Best Parameters:** {'classifier__n_neighbors': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6666666666666666,
        "recall": 0.8571428571428571,
        "f1-score": 0.75,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.391304347826087,
        "recall": 0.45,
        "f1-score": 0.4186046511627907,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.65625,
        "recall": 0.6363636363636364,
        "f1-score": 0.6461538461538462,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5652173913043478,
        "recall": 0.48148148148148145,
        "f1-score": 0.52,
        "support": 27.0
    },
    "accuracy": 0.5632183908045977,
    "macro avg": {
        "precision": 0.5698596014492754,
        "recall": 0.6062469937469938,
        "f1-score": 0.5836896243291593,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5679295768782275,
        "recall": 0.5632183908045977,
        "f1-score": 0.5630479304176177,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.5326
- **Accuracy:** 0.5517
- **Best Parameters:** {'classifier__max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6,
        "recall": 0.8571428571428571,
        "f1-score": 0.7058823529411765,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.625,
        "recall": 0.25,
        "f1-score": 0.35714285714285715,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5227272727272727,
        "recall": 0.696969696969697,
        "f1-score": 0.5974025974025974,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.56,
        "recall": 0.5185185185185185,
        "f1-score": 0.5384615384615384,
        "support": 27.0
    },
    "accuracy": 0.5517241379310345,
    "macro avg": {
        "precision": 0.5769318181818182,
        "recall": 0.5806577681577682,
        "f1-score": 0.5497223364870424,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5640229885057472,
        "recall": 0.5517241379310345,
        "f1-score": 0.5326066766229038,
        "support": 87.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.4242
- **Accuracy:** 0.4483
- **Best Parameters:** {'classifier__n_neighbors': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.4,
        "recall": 0.8571428571428571,
        "f1-score": 0.5454545454545454,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.4,
        "recall": 0.4,
        "f1-score": 0.4,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5128205128205128,
        "recall": 0.6060606060606061,
        "f1-score": 0.5555555555555556,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.38461538461538464,
        "recall": 0.18518518518518517,
        "f1-score": 0.25,
        "support": 27.0
    },
    "accuracy": 0.4482758620689655,
    "macro avg": {
        "precision": 0.42435897435897435,
        "recall": 0.512097162097162,
        "f1-score": 0.4377525252525253,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.4380194518125552,
        "recall": 0.4482758620689655,
        "f1-score": 0.4241553465691397,
        "support": 87.0
    }
}
```

## GloVe_SVM_Enhanced

- **Weighted F1 Score:** 0.6159
- **Accuracy:** 0.6322
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6,
        "recall": 0.3,
        "f1-score": 0.4,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.625,
        "recall": 0.6060606060606061,
        "f1-score": 0.6153846153846154,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5897435897435898,
        "recall": 0.8518518518518519,
        "f1-score": 0.696969696969697,
        "support": 27.0
    },
    "accuracy": 0.632183908045977,
    "macro avg": {
        "precision": 0.7036858974358975,
        "recall": 0.6537638287638288,
        "f1-score": 0.658857808857809,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6384836427939876,
        "recall": 0.632183908045977,
        "f1-score": 0.615947271119685,
        "support": 87.0
    }
}
```

## GloVe_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.5661
- **Accuracy:** 0.5747
- **Best Parameters:** {'C': 1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5454545454545454,
        "recall": 0.3,
        "f1-score": 0.3870967741935484,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5897435897435898,
        "recall": 0.696969696969697,
        "f1-score": 0.6388888888888888,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.4838709677419355,
        "recall": 0.5555555555555556,
        "f1-score": 0.5172413793103449,
        "support": 27.0
    },
    "accuracy": 0.5747126436781609,
    "macro avg": {
        "precision": 0.6547672757350177,
        "recall": 0.6024170274170274,
        "f1-score": 0.6165759913674262,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5797143160880647,
        "recall": 0.5747126436781609,
        "f1-score": 0.5661186726450813,
        "support": 87.0
    }
}
```

## GloVe_KNN_Enhanced

- **Weighted F1 Score:** 0.5317
- **Accuracy:** 0.5172
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.30303030303030304,
        "recall": 0.5,
        "f1-score": 0.37735849056603776,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5714285714285714,
        "recall": 0.48484848484848486,
        "f1-score": 0.5245901639344263,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.65,
        "recall": 0.48148148148148145,
        "f1-score": 0.5531914893617021,
        "support": 27.0
    },
    "accuracy": 0.5172413793103449,
    "macro avg": {
        "precision": 0.6311147186147186,
        "recall": 0.5808682058682059,
        "f1-score": 0.5945542667347724,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5685948151465393,
        "recall": 0.5172413793103449,
        "f1-score": 0.5316822286834626,
        "support": 87.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.5118
- **Accuracy:** 0.5172
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.75,
        "recall": 0.8571428571428571,
        "f1-score": 0.8,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.3939393939393939,
        "recall": 0.65,
        "f1-score": 0.49056603773584906,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.53125,
        "recall": 0.5151515151515151,
        "f1-score": 0.5230769230769231,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6428571428571429,
        "recall": 0.3333333333333333,
        "f1-score": 0.43902439024390244,
        "support": 27.0
    },
    "accuracy": 0.5172413793103449,
    "macro avg": {
        "precision": 0.5795116341991342,
        "recall": 0.5889069264069264,
        "f1-score": 0.5631668377641686,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5519216176543763,
        "recall": 0.5172413793103449,
        "f1-score": 0.5117990546303541,
        "support": 87.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.4403
- **Accuracy:** 0.4483
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6666666666666666,
        "recall": 0.8571428571428571,
        "f1-score": 0.75,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.3333333333333333,
        "recall": 0.65,
        "f1-score": 0.4406779661016949,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5,
        "recall": 0.3333333333333333,
        "f1-score": 0.4,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5294117647058824,
        "recall": 0.3333333333333333,
        "f1-score": 0.4090909090909091,
        "support": 27.0
    },
    "accuracy": 0.4482758620689655,
    "macro avg": {
        "precision": 0.5073529411764706,
        "recall": 0.5434523809523809,
        "f1-score": 0.49994221879815104,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.48422357448726616,
        "recall": 0.4482758620689655,
        "f1-score": 0.44033349272975225,
        "support": 87.0
    }
}
```

## GloVe_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.4093
- **Accuracy:** 0.4023
- **Best Parameters:** {'max_depth': 10}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.3,
        "recall": 0.45,
        "f1-score": 0.36,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.44,
        "recall": 0.3333333333333333,
        "f1-score": 0.3793103448275862,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.39285714285714285,
        "recall": 0.4074074074074074,
        "f1-score": 0.4,
        "support": 27.0
    },
    "accuracy": 0.40229885057471265,
    "macro avg": {
        "precision": 0.5332142857142858,
        "recall": 0.440542328042328,
        "f1-score": 0.4666457680250784,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.43824302134646964,
        "recall": 0.40229885057471265,
        "f1-score": 0.4092890858645911,
        "support": 87.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.4049
- **Accuracy:** 0.4368
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.25,
        "recall": 0.05,
        "f1-score": 0.08333333333333333,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.45454545454545453,
        "recall": 0.6060606060606061,
        "f1-score": 0.5194805194805194,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.37142857142857144,
        "recall": 0.48148148148148145,
        "f1-score": 0.41935483870967744,
        "support": 27.0
    },
    "accuracy": 0.4367816091954023,
    "macro avg": {
        "precision": 0.5189935064935065,
        "recall": 0.4272426647426647,
        "f1-score": 0.4373603546990644,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.425615763546798,
        "recall": 0.4367816091954023,
        "f1-score": 0.4048622246620022,
        "support": 87.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.3845
- **Accuracy:** 0.4713
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4626865671641791,
        "recall": 0.9393939393939394,
        "f1-score": 0.62,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.42857142857142855,
        "recall": 0.2222222222222222,
        "f1-score": 0.2926829268292683,
        "support": 27.0
    },
    "accuracy": 0.47126436781609193,
    "macro avg": {
        "precision": 0.4728144989339019,
        "recall": 0.43326118326118324,
        "f1-score": 0.4099889135254989,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.38896649756145374,
        "recall": 0.47126436781609193,
        "f1-score": 0.38452124270459004,
        "support": 87.0
    }
}
```

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.3845
- **Accuracy:** 0.4713
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4626865671641791,
        "recall": 0.9393939393939394,
        "f1-score": 0.62,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.42857142857142855,
        "recall": 0.2222222222222222,
        "f1-score": 0.2926829268292683,
        "support": 27.0
    },
    "accuracy": 0.47126436781609193,
    "macro avg": {
        "precision": 0.4728144989339019,
        "recall": 0.43326118326118324,
        "f1-score": 0.4099889135254989,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.38896649756145374,
        "recall": 0.47126436781609193,
        "f1-score": 0.38452124270459004,
        "support": 87.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.3730
- **Accuracy:** 0.3678
- **Best Parameters:** {'max_depth': 10}
```json
{
    "NA_CATEGORY": {
        "precision": 0.75,
        "recall": 0.42857142857142855,
        "f1-score": 0.5454545454545454,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.2692307692307692,
        "recall": 0.35,
        "f1-score": 0.30434782608695654,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4230769230769231,
        "recall": 0.3333333333333333,
        "f1-score": 0.3728813559322034,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.3548387096774194,
        "recall": 0.4074074074074074,
        "f1-score": 0.3793103448275862,
        "support": 27.0
    },
    "accuracy": 0.367816091954023,
    "macro avg": {
        "precision": 0.4492866004962779,
        "recall": 0.3798280423280423,
        "f1-score": 0.4004985180753229,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.3928367702005077,
        "recall": 0.367816091954023,
        "f1-score": 0.37300692409228153,
        "support": 87.0
    }
}
```

## Word2Vec_SVM_Enhanced

- **Weighted F1 Score:** 0.3664
- **Accuracy:** 0.4598
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4305555555555556,
        "recall": 0.9393939393939394,
        "f1-score": 0.5904761904761905,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5,
        "recall": 0.18518518518518517,
        "f1-score": 0.2702702702702703,
        "support": 27.0
    },
    "accuracy": 0.45977011494252873,
    "macro avg": {
        "precision": 0.4826388888888889,
        "recall": 0.424001924001924,
        "f1-score": 0.39700479700479696,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.39894636015325674,
        "recall": 0.45977011494252873,
        "f1-score": 0.3663669042979388,
        "support": 87.0
    }
}
```

## FastText_SVM_Enhanced

- **Weighted F1 Score:** 0.3664
- **Accuracy:** 0.4598
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5714285714285714,
        "f1-score": 0.7272727272727273,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4305555555555556,
        "recall": 0.9393939393939394,
        "f1-score": 0.5904761904761905,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5,
        "recall": 0.18518518518518517,
        "f1-score": 0.2702702702702703,
        "support": 27.0
    },
    "accuracy": 0.45977011494252873,
    "macro avg": {
        "precision": 0.4826388888888889,
        "recall": 0.424001924001924,
        "f1-score": 0.39700479700479696,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.39894636015325674,
        "recall": 0.45977011494252873,
        "f1-score": 0.3663669042979388,
        "support": 87.0
    }
}
```

