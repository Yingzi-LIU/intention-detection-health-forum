# Experiment Results Summary

**Labels:** NA_CATEGORY, diagnostique, symptome, traitement

## BoW_MultinomialNB

- **Weighted F1 Score:** 0.6348
- **Accuracy:** 0.6437
- **Best Parameters:** {'alpha': 1.0}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.7142857142857143,
        "f1-score": 0.8333333333333334,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6153846153846154,
        "recall": 0.4,
        "f1-score": 0.48484848484848486,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6829268292682927,
        "recall": 0.8484848484848485,
        "f1-score": 0.7567567567567568,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5357142857142857,
        "recall": 0.5555555555555556,
        "f1-score": 0.5454545454545454,
        "support": 27.0
    },
    "accuracy": 0.6436781609195402,
    "macro avg": {
        "precision": 0.7085064325917985,
        "recall": 0.6295815295815297,
        "f1-score": 0.6550982800982802,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.647224866526801,
        "recall": 0.6436781609195402,
        "f1-score": 0.6348338934545832,
        "support": 87.0
    }
}
```

## TF-IDF_LogisticRegression

- **Weighted F1 Score:** 0.6318
- **Accuracy:** 0.6322
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5882352941176471,
        "recall": 0.5,
        "f1-score": 0.5405405405405406,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.696969696969697,
        "recall": 0.696969696969697,
        "f1-score": 0.696969696969697,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5333333333333333,
        "recall": 0.5925925925925926,
        "f1-score": 0.5614035087719298,
        "support": 27.0
    },
    "accuracy": 0.632183908045977,
    "macro avg": {
        "precision": 0.6689202953908836,
        "recall": 0.6616762866762866,
        "f1-score": 0.664014150856256,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6340770791075051,
        "recall": 0.632183908045977,
        "f1-score": 0.6318242016971599,
        "support": 87.0
    }
}
```

## BoW_SVM

- **Weighted F1 Score:** 0.6293
- **Accuracy:** 0.6322
- **Best Parameters:** {'C': 1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.8333333333333334,
        "recall": 0.5,
        "f1-score": 0.625,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5813953488372093,
        "recall": 0.7575757575757576,
        "f1-score": 0.6578947368421053,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.56,
        "recall": 0.5185185185185185,
        "f1-score": 0.5384615384615384,
        "support": 27.0
    },
    "accuracy": 0.632183908045977,
    "macro avg": {
        "precision": 0.7079678848283499,
        "recall": 0.6583092833092833,
        "f1-score": 0.6696247831116252,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6548587721643055,
        "recall": 0.632183908045977,
        "f1-score": 0.6292987109684025,
        "support": 87.0
    }
}
```

## TF-IDF_SVM

- **Weighted F1 Score:** 0.6218
- **Accuracy:** 0.6207
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5238095238095238,
        "recall": 0.55,
        "f1-score": 0.5365853658536586,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6774193548387096,
        "recall": 0.6363636363636364,
        "f1-score": 0.65625,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5714285714285714,
        "recall": 0.5925925925925926,
        "f1-score": 0.5818181818181818,
        "support": 27.0
    },
    "accuracy": 0.6206896551724138,
    "macro avg": {
        "precision": 0.6574500768049154,
        "recall": 0.6590247715247715,
        "f1-score": 0.6579491012036744,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6236735702809117,
        "recall": 0.6206896551724138,
        "f1-score": 0.6218051520248745,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_LogisticRegression

- **Weighted F1 Score:** 0.6182
- **Accuracy:** 0.6207
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
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
        "recall": 0.45,
        "f1-score": 0.5142857142857142,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.631578947368421,
        "recall": 0.7272727272727273,
        "f1-score": 0.676056338028169,
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
        "precision": 0.6918233082706766,
        "recall": 0.647492784992785,
        "f1-score": 0.664718380211338,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6242113905453288,
        "recall": 0.6206896551724138,
        "f1-score": 0.6182113175799431,
        "support": 87.0
    }
}
```

## BoW_LogisticRegression

- **Weighted F1 Score:** 0.6144
- **Accuracy:** 0.6207
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
        "precision": 0.6923076923076923,
        "recall": 0.45,
        "f1-score": 0.5454545454545454,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6046511627906976,
        "recall": 0.7878787878787878,
        "f1-score": 0.6842105263157895,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.52,
        "recall": 0.48148148148148145,
        "f1-score": 0.5,
        "support": 27.0
    },
    "accuracy": 0.6206896551724138,
    "macro avg": {
        "precision": 0.7042397137745975,
        "recall": 0.6441257816257816,
        "f1-score": 0.6631854987118145,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6303407151522629,
        "recall": 0.6206896551724138,
        "f1-score": 0.6143629510235682,
        "support": 87.0
    }
}
```

## TF-IDF_MultinomialNB

- **Weighted F1 Score:** 0.6107
- **Accuracy:** 0.6092
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.7142857142857143,
        "f1-score": 0.8333333333333334,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5263157894736842,
        "recall": 0.5,
        "f1-score": 0.5128205128205128,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6857142857142857,
        "recall": 0.7272727272727273,
        "f1-score": 0.7058823529411765,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5,
        "recall": 0.5185185185185185,
        "f1-score": 0.509090909090909,
        "support": 27.0
    },
    "accuracy": 0.6091954022988506,
    "macro avg": {
        "precision": 0.6780075187969925,
        "recall": 0.61501924001924,
        "f1-score": 0.640281777046483,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6167228415867255,
        "recall": 0.6091954022988506,
        "f1-score": 0.6106817906006548,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_SVM

- **Weighted F1 Score:** 0.6100
- **Accuracy:** 0.6092
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5263157894736842,
        "recall": 0.5,
        "f1-score": 0.5128205128205128,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6774193548387096,
        "recall": 0.6363636363636364,
        "f1-score": 0.65625,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5333333333333333,
        "recall": 0.5925925925925926,
        "f1-score": 0.5614035087719298,
        "support": 27.0
    },
    "accuracy": 0.6091954022988506,
    "macro avg": {
        "precision": 0.648552833697146,
        "recall": 0.6465247715247715,
        "f1-score": 0.6469042196838249,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6124270632086334,
        "recall": 0.6091954022988506,
        "f1-score": 0.6100063792327858,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_MultinomialNB

- **Weighted F1 Score:** 0.5948
- **Accuracy:** 0.5977
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.8571428571428571,
        "f1-score": 0.9230769230769231,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5294117647058824,
        "recall": 0.45,
        "f1-score": 0.4864864864864865,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.631578947368421,
        "recall": 0.7272727272727273,
        "f1-score": 0.676056338028169,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5,
        "recall": 0.48148148148148145,
        "f1-score": 0.49056603773584906,
        "support": 27.0
    },
    "accuracy": 0.5977011494252874,
    "macro avg": {
        "precision": 0.6652476780185759,
        "recall": 0.6289742664742665,
        "f1-score": 0.6440464463318569,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5969004661755809,
        "recall": 0.5977011494252874,
        "f1-score": 0.5947863260352378,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_KNN

- **Weighted F1 Score:** 0.5725
- **Accuracy:** 0.5862
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6,
        "recall": 0.8571428571428571,
        "f1-score": 0.7058823529411765,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5555555555555556,
        "recall": 0.5,
        "f1-score": 0.5263157894736842,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.625,
        "recall": 0.7575757575757576,
        "f1-score": 0.684931506849315,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5263157894736842,
        "recall": 0.37037037037037035,
        "f1-score": 0.43478260869565216,
        "support": 27.0
    },
    "accuracy": 0.5862068965517241,
    "macro avg": {
        "precision": 0.5767178362573099,
        "recall": 0.6212722462722462,
        "f1-score": 0.587978064489957,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5763981313436849,
        "recall": 0.5862068965517241,
        "f1-score": 0.5725214071364588,
        "support": 87.0
    }
}
```

## TF-IDF_DecisionTree

- **Weighted F1 Score:** 0.5644
- **Accuracy:** 0.5747
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.75,
        "recall": 0.8571428571428571,
        "f1-score": 0.8,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5294117647058824,
        "recall": 0.45,
        "f1-score": 0.4864864864864865,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5454545454545454,
        "recall": 0.7272727272727273,
        "f1-score": 0.6233766233766234,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6111111111111112,
        "recall": 0.4074074074074074,
        "f1-score": 0.4888888888888889,
        "support": 27.0
    },
    "accuracy": 0.5747126436781609,
    "macro avg": {
        "precision": 0.6089943553178847,
        "recall": 0.610455747955748,
        "f1-score": 0.5996879996879997,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5786004056795132,
        "recall": 0.5747126436781609,
        "f1-score": 0.5643811298983713,
        "support": 87.0
    }
}
```

## Bert_LogisticRegression

- **Weighted F1 Score:** 0.5541
- **Accuracy:** 0.5517
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8,
        "recall": 0.5714285714285714,
        "f1-score": 0.6666666666666666,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5,
        "recall": 0.55,
        "f1-score": 0.5238095238095238,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6,
        "recall": 0.5454545454545454,
        "f1-score": 0.5714285714285714,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5,
        "recall": 0.5555555555555556,
        "f1-score": 0.5263157894736842,
        "support": 27.0
    },
    "accuracy": 0.5517241379310345,
    "macro avg": {
        "precision": 0.6,
        "recall": 0.555609668109668,
        "f1-score": 0.5720551378446115,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5620689655172414,
        "recall": 0.5517241379310345,
        "f1-score": 0.5541439806412584,
        "support": 87.0
    }
}
```

## TF-IDF_KNN

- **Weighted F1 Score:** 0.5461
- **Accuracy:** 0.5632
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6666666666666666,
        "recall": 0.8571428571428571,
        "f1-score": 0.75,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.45454545454545453,
        "recall": 0.5,
        "f1-score": 0.47619047619047616,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6410256410256411,
        "recall": 0.7575757575757576,
        "f1-score": 0.6944444444444444,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.47058823529411764,
        "recall": 0.2962962962962963,
        "f1-score": 0.36363636363636365,
        "support": 27.0
    },
    "accuracy": 0.5632183908045977,
    "macro avg": {
        "precision": 0.55820649938297,
        "recall": 0.6027537277537277,
        "f1-score": 0.5710678210678211,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5473253363719894,
        "recall": 0.5632183908045977,
        "f1-score": 0.5460765288351496,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.5433
- **Accuracy:** 0.5517
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.8571428571428571,
        "f1-score": 0.8571428571428571,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5714285714285714,
        "recall": 0.4,
        "f1-score": 0.47058823529411764,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5,
        "recall": 0.696969696969697,
        "f1-score": 0.5822784810126582,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.55,
        "recall": 0.4074074074074074,
        "f1-score": 0.46808510638297873,
        "support": 27.0
    },
    "accuracy": 0.5517241379310345,
    "macro avg": {
        "precision": 0.6196428571428572,
        "recall": 0.5903799903799903,
        "f1-score": 0.5945236699581529,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5606732348111659,
        "recall": 0.5517241379310345,
        "f1-score": 0.5432787638119597,
        "support": 87.0
    }
}
```

## Bert_SVM

- **Weighted F1 Score:** 0.5405
- **Accuracy:** 0.5402
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.5714285714285714,
        "recall": 0.5714285714285714,
        "f1-score": 0.5714285714285714,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.48,
        "recall": 0.6,
        "f1-score": 0.5333333333333333,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5862068965517241,
        "recall": 0.5151515151515151,
        "f1-score": 0.5483870967741935,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5384615384615384,
        "recall": 0.5185185185185185,
        "f1-score": 0.5283018867924528,
        "support": 27.0
    },
    "accuracy": 0.5402298850574713,
    "macro avg": {
        "precision": 0.5440242516104584,
        "recall": 0.5512746512746513,
        "f1-score": 0.5453627220821378,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5457849324674532,
        "recall": 0.5402298850574713,
        "f1-score": 0.5405470322254169,
        "support": 87.0
    }
}
```

## Word2Vec_KNN

- **Weighted F1 Score:** 0.5136
- **Accuracy:** 0.5287
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.42857142857142855,
        "f1-score": 0.6,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5,
        "recall": 0.5,
        "f1-score": 0.5,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5434782608695652,
        "recall": 0.7575757575757576,
        "f1-score": 0.6329113924050633,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.4444444444444444,
        "recall": 0.2962962962962963,
        "f1-score": 0.35555555555555557,
        "support": 27.0
    },
    "accuracy": 0.5287356321839081,
    "macro avg": {
        "precision": 0.6219806763285025,
        "recall": 0.4956108706108706,
        "f1-score": 0.5221167369901547,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.539480259870065,
        "recall": 0.5287356321839081,
        "f1-score": 0.5136330568892769,
        "support": 87.0
    }
}
```

## Bert_KNN

- **Weighted F1 Score:** 0.5055
- **Accuracy:** 0.5057
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6,
        "recall": 0.42857142857142855,
        "f1-score": 0.5,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.5217391304347826,
        "recall": 0.6,
        "f1-score": 0.5581395348837209,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5555555555555556,
        "recall": 0.45454545454545453,
        "f1-score": 0.5,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.4375,
        "recall": 0.5185185185185185,
        "f1-score": 0.4745762711864407,
        "support": 27.0
    },
    "accuracy": 0.5057471264367817,
    "macro avg": {
        "precision": 0.5286986714975845,
        "recall": 0.5004088504088504,
        "f1-score": 0.5081789515175404,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5147197234715976,
        "recall": 0.5057471264367817,
        "f1-score": 0.5054752875828542,
        "support": 87.0
    }
}
```

## BoW_DecisionTree

- **Weighted F1 Score:** 0.4966
- **Accuracy:** 0.5057
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.75,
        "recall": 0.8571428571428571,
        "f1-score": 0.8,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.3888888888888889,
        "recall": 0.35,
        "f1-score": 0.3684210526315789,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4883720930232558,
        "recall": 0.6363636363636364,
        "f1-score": 0.5526315789473685,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5555555555555556,
        "recall": 0.37037037037037035,
        "f1-score": 0.4444444444444444,
        "support": 27.0
    },
    "accuracy": 0.5057471264367817,
    "macro avg": {
        "precision": 0.5457041343669251,
        "recall": 0.5534692159692159,
        "f1-score": 0.5413742690058481,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.5074029522706347,
        "recall": 0.5057471264367817,
        "f1-score": 0.4966122202056867,
        "support": 87.0
    }
}
```

## FastText_DecisionTree

- **Weighted F1 Score:** 0.4605
- **Accuracy:** 0.4598
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.5,
        "recall": 0.5714285714285714,
        "f1-score": 0.5333333333333333,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.43478260869565216,
        "recall": 0.5,
        "f1-score": 0.46511627906976744,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5384615384615384,
        "recall": 0.42424242424242425,
        "f1-score": 0.4745762711864407,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.4,
        "recall": 0.4444444444444444,
        "f1-score": 0.42105263157894735,
        "support": 27.0
    },
    "accuracy": 0.45977011494252873,
    "macro avg": {
        "precision": 0.46831103678929764,
        "recall": 0.48502886002886003,
        "f1-score": 0.4735196287921222,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.46856187290969903,
        "recall": 0.45977011494252873,
        "f1-score": 0.4605183553622161,
        "support": 87.0
    }
}
```

## BoW_KNN

- **Weighted F1 Score:** 0.3762
- **Accuracy:** 0.4138
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.2608695652173913,
        "recall": 0.8571428571428571,
        "f1-score": 0.4,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.6,
        "recall": 0.15,
        "f1-score": 0.24,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4782608695652174,
        "recall": 0.6666666666666666,
        "f1-score": 0.5569620253164557,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.38461538461538464,
        "recall": 0.18518518518518517,
        "f1-score": 0.25,
        "support": 27.0
    },
    "accuracy": 0.41379310344827586,
    "macro avg": {
        "precision": 0.4309364548494983,
        "recall": 0.4647486772486772,
        "f1-score": 0.3617405063291139,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.459693230307923,
        "recall": 0.41379310344827586,
        "f1-score": 0.3762039866142878,
        "support": 87.0
    }
}
```

## Bert_DecisionTree

- **Weighted F1 Score:** 0.3526
- **Accuracy:** 0.3793
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.2727272727272727,
        "recall": 0.42857142857142855,
        "f1-score": 0.3333333333333333,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.4666666666666667,
        "recall": 0.35,
        "f1-score": 0.4,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4166666666666667,
        "recall": 0.6060606060606061,
        "f1-score": 0.49382716049382713,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.23076923076923078,
        "recall": 0.1111111111111111,
        "f1-score": 0.15,
        "support": 27.0
    },
    "accuracy": 0.3793103448275862,
    "macro avg": {
        "precision": 0.3467074592074592,
        "recall": 0.3739357864357864,
        "f1-score": 0.3442901234567901,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.3588872813010744,
        "recall": 0.3793103448275862,
        "f1-score": 0.3526394210302256,
        "support": 87.0
    }
}
```

## FastText_KNN

- **Weighted F1 Score:** 0.3457
- **Accuracy:** 0.3448
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.5,
        "recall": 0.5714285714285714,
        "f1-score": 0.5333333333333333,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.25,
        "recall": 0.3,
        "f1-score": 0.2727272727272727,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4166666666666667,
        "recall": 0.30303030303030304,
        "f1-score": 0.3508771929824561,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.3225806451612903,
        "recall": 0.37037037037037035,
        "f1-score": 0.3448275862068966,
        "support": 27.0
    },
    "accuracy": 0.3448275862068966,
    "macro avg": {
        "precision": 0.37231182795698925,
        "recall": 0.3862073112073112,
        "f1-score": 0.37544134631248965,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.35585836114200964,
        "recall": 0.3448275862068966,
        "f1-score": 0.34571460901018447,
        "support": 87.0
    }
}
```

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.3264
- **Accuracy:** 0.3333
- **Best Parameters:** {'max_depth': 10}
```json
{
    "NA_CATEGORY": {
        "precision": 0.3,
        "recall": 0.42857142857142855,
        "f1-score": 0.35294117647058826,
        "support": 7.0
    },
    "diagnostique": {
        "precision": 0.2727272727272727,
        "recall": 0.15,
        "f1-score": 0.1935483870967742,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.40625,
        "recall": 0.3939393939393939,
        "f1-score": 0.4,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.29411764705882354,
        "recall": 0.37037037037037035,
        "f1-score": 0.32786885245901637,
        "support": 27.0
    },
    "accuracy": 0.3333333333333333,
    "macro avg": {
        "precision": 0.3182737299465241,
        "recall": 0.3357202982202982,
        "f1-score": 0.3185896040065947,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.3322065738521114,
        "recall": 0.3333333333333333,
        "f1-score": 0.3263679884324488,
        "support": 87.0
    }
}
```

## Word2Vec_LogisticRegression

- **Weighted F1 Score:** 0.2086
- **Accuracy:** 0.3793
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    },
    "micro avg": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    },
    "macro avg": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    },
    "weighted avg": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    }
}
```

## Word2Vec_SVM

- **Weighted F1 Score:** 0.2086
- **Accuracy:** 0.3793
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    },
    "micro avg": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    },
    "macro avg": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    },
    "weighted avg": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    }
}
```

## FastText_LogisticRegression

- **Weighted F1 Score:** 0.2086
- **Accuracy:** 0.3793
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    },
    "micro avg": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    },
    "macro avg": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    },
    "weighted avg": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    }
}
```

## FastText_SVM

- **Weighted F1 Score:** 0.2086
- **Accuracy:** 0.3793
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    },
    "micro avg": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    },
    "macro avg": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    },
    "weighted avg": {
        "precision": 0.3793103448275862,
        "recall": 1.0,
        "f1-score": 0.55,
        "support": 33.0
    }
}
```

