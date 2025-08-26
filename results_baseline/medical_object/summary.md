# Experiment Results Summary

**Labels:** NA_CATEGORY, diagnostique, symptome, traitement

## TF-IDF_MultinomialNB

- **Weighted F1 Score:** 0.6751
- **Accuracy:** 0.6739
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.6,
        "f1-score": 0.75,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.5909090909090909,
        "recall": 0.65,
        "f1-score": 0.6190476190476191,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6944444444444444,
        "recall": 0.7575757575757576,
        "f1-score": 0.7246376811594203,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6428571428571429,
        "recall": 0.6206896551724138,
        "f1-score": 0.631578947368421,
        "support": 29.0
    },
    "accuracy": 0.6739130434782609,
    "macro avg": {
        "precision": 0.7320526695526696,
        "recall": 0.6570663531870429,
        "f1-score": 0.6813160618938652,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6888881046489742,
        "recall": 0.6739130434782609,
        "f1-score": 0.6751063623141028,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_MultinomialNB

- **Weighted F1 Score:** 0.6307
- **Accuracy:** 0.6304
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.6,
        "f1-score": 0.75,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.5789473684210527,
        "recall": 0.55,
        "f1-score": 0.5641025641025641,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6578947368421053,
        "recall": 0.7575757575757576,
        "f1-score": 0.704225352112676,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5517241379310345,
        "recall": 0.5517241379310345,
        "f1-score": 0.5517241379310345,
        "support": 29.0
    },
    "accuracy": 0.6304347826086957,
    "macro avg": {
        "precision": 0.697141560798548,
        "recall": 0.614824973876698,
        "f1-score": 0.6425130135365686,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6444508009153319,
        "recall": 0.6304347826086957,
        "f1-score": 0.6306683467583651,
        "support": 92.0
    }
}
```

## Bert_SVM

- **Weighted F1 Score:** 0.6220
- **Accuracy:** 0.6196
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6666666666666666,
        "recall": 0.6,
        "f1-score": 0.631578947368421,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.5,
        "recall": 0.5,
        "f1-score": 0.5,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.7586206896551724,
        "recall": 0.6666666666666666,
        "f1-score": 0.7096774193548387,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5588235294117647,
        "recall": 0.6551724137931034,
        "f1-score": 0.6031746031746031,
        "support": 29.0
    },
    "accuracy": 0.6195652173913043,
    "macro avg": {
        "precision": 0.6210277214334009,
        "recall": 0.6054597701149425,
        "f1-score": 0.6111077424744658,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6294242584590057,
        "recall": 0.6195652173913043,
        "f1-score": 0.6220348674397541,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN

- **Weighted F1 Score:** 0.6085
- **Accuracy:** 0.6087
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6363636363636364,
        "recall": 0.7,
        "f1-score": 0.6666666666666666,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.43478260869565216,
        "recall": 0.5,
        "f1-score": 0.46511627906976744,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6666666666666666,
        "recall": 0.7272727272727273,
        "f1-score": 0.6956521739130435,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6818181818181818,
        "recall": 0.5172413793103449,
        "f1-score": 0.5882352941176471,
        "support": 29.0
    },
    "accuracy": 0.6086956521739131,
    "macro avg": {
        "precision": 0.6049077733860342,
        "recall": 0.611128526645768,
        "f1-score": 0.6039176034417811,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.617739302285616,
        "recall": 0.6086956521739131,
        "f1-score": 0.6085254077891762,
        "support": 92.0
    }
}
```

## BoW_LogisticRegression

- **Weighted F1 Score:** 0.6079
- **Accuracy:** 0.6087
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6666666666666666,
        "recall": 0.6,
        "f1-score": 0.631578947368421,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.45454545454545453,
        "recall": 0.5,
        "f1-score": 0.47619047619047616,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.7142857142857143,
        "recall": 0.7575757575757576,
        "f1-score": 0.7352941176470589,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5769230769230769,
        "recall": 0.5172413793103449,
        "f1-score": 0.5454545454545454,
        "support": 29.0
    },
    "accuracy": 0.6086956521739131,
    "macro avg": {
        "precision": 0.603105228105228,
        "recall": 0.5937042842215257,
        "f1-score": 0.5971295216651253,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6093453647801474,
        "recall": 0.6086956521739131,
        "f1-score": 0.6078531162829184,
        "support": 92.0
    }
}
```

## Bert_LogisticRegression

- **Weighted F1 Score:** 0.6022
- **Accuracy:** 0.6087
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.7142857142857143,
        "recall": 0.5,
        "f1-score": 0.5882352941176471,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.4375,
        "recall": 0.35,
        "f1-score": 0.3888888888888889,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.696969696969697,
        "recall": 0.696969696969697,
        "f1-score": 0.696969696969697,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5833333333333334,
        "recall": 0.7241379310344828,
        "f1-score": 0.6461538461538462,
        "support": 29.0
    },
    "accuracy": 0.6086956521739131,
    "macro avg": {
        "precision": 0.6080221861471862,
        "recall": 0.5677769070010449,
        "f1-score": 0.5800619315325198,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6066252587991718,
        "recall": 0.6086956521739131,
        "f1-score": 0.6021586114936498,
        "support": 92.0
    }
}
```

## BoW_SVM

- **Weighted F1 Score:** 0.5999
- **Accuracy:** 0.5978
- **Best Parameters:** {'C': 1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6666666666666666,
        "recall": 0.6,
        "f1-score": 0.631578947368421,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.4583333333333333,
        "recall": 0.55,
        "f1-score": 0.5,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6666666666666666,
        "recall": 0.6666666666666666,
        "f1-score": 0.6666666666666666,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6153846153846154,
        "recall": 0.5517241379310345,
        "f1-score": 0.5818181818181818,
        "support": 29.0
    },
    "accuracy": 0.5978260869565217,
    "macro avg": {
        "precision": 0.6017628205128205,
        "recall": 0.5920977011494253,
        "f1-score": 0.5950159489633173,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6052118171683388,
        "recall": 0.5978260869565217,
        "f1-score": 0.5998751820262117,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_LogisticRegression

- **Weighted F1 Score:** 0.5996
- **Accuracy:** 0.5978
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.75,
        "recall": 0.6,
        "f1-score": 0.6666666666666666,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.5263157894736842,
        "recall": 0.5,
        "f1-score": 0.5128205128205128,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6875,
        "recall": 0.6666666666666666,
        "f1-score": 0.676923076923077,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5151515151515151,
        "recall": 0.5862068965517241,
        "f1-score": 0.5483870967741935,
        "support": 29.0
    },
    "accuracy": 0.5978260869565217,
    "macro avg": {
        "precision": 0.6197418261562998,
        "recall": 0.5882183908045977,
        "f1-score": 0.6011993382961125,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6049261927050829,
        "recall": 0.5978260869565217,
        "f1-score": 0.5996170029129356,
        "support": 92.0
    }
}
```

## Bert_DecisionTree

- **Weighted F1 Score:** 0.5977
- **Accuracy:** 0.5978
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.7777777777777778,
        "recall": 0.7,
        "f1-score": 0.7368421052631579,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.5555555555555556,
        "recall": 0.5,
        "f1-score": 0.5263157894736842,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5675675675675675,
        "recall": 0.6363636363636364,
        "f1-score": 0.6,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6071428571428571,
        "recall": 0.5862068965517241,
        "f1-score": 0.5964912280701754,
        "support": 29.0
    },
    "accuracy": 0.5978260869565217,
    "macro avg": {
        "precision": 0.6270109395109396,
        "recall": 0.6056426332288402,
        "f1-score": 0.6149122807017544,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6002800160408855,
        "recall": 0.5978260869565217,
        "f1-score": 0.5977498093058733,
        "support": 92.0
    }
}
```

## TF-IDF_KNN

- **Weighted F1 Score:** 0.5959
- **Accuracy:** 0.5978
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.6,
        "recall": 0.6,
        "f1-score": 0.6,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.43478260869565216,
        "recall": 0.5,
        "f1-score": 0.46511627906976744,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.625,
        "recall": 0.7575757575757576,
        "f1-score": 0.684931506849315,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.7368421052631579,
        "recall": 0.4827586206896552,
        "f1-score": 0.5833333333333334,
        "support": 29.0
    },
    "accuracy": 0.5978260869565217,
    "macro avg": {
        "precision": 0.5991561784897025,
        "recall": 0.5850835945663532,
        "f1-score": 0.583345279813104,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.616185578549398,
        "recall": 0.5978260869565217,
        "f1-score": 0.5958883910227111,
        "support": 92.0
    }
}
```

## BoW_MultinomialNB

- **Weighted F1 Score:** 0.5912
- **Accuracy:** 0.5978
- **Best Parameters:** {'alpha': 1.0}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.4,
        "f1-score": 0.5714285714285714,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.5263157894736842,
        "recall": 0.5,
        "f1-score": 0.5128205128205128,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6190476190476191,
        "recall": 0.7878787878787878,
        "f1-score": 0.6933333333333334,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5555555555555556,
        "recall": 0.5172413793103449,
        "f1-score": 0.5357142857142857,
        "support": 29.0
    },
    "accuracy": 0.5978260869565217,
    "macro avg": {
        "precision": 0.6752297410192147,
        "recall": 0.5512800417972832,
        "f1-score": 0.5783241758241758,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6202825905343069,
        "recall": 0.5978260869565217,
        "f1-score": 0.5911566332218506,
        "support": 92.0
    }
}
```

## TF-IDF_SVM

- **Weighted F1 Score:** 0.5843
- **Accuracy:** 0.5761
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.75,
        "recall": 0.6,
        "f1-score": 0.6666666666666666,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.42857142857142855,
        "recall": 0.6,
        "f1-score": 0.5,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.76,
        "recall": 0.5757575757575758,
        "f1-score": 0.6551724137931034,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.5161290322580645,
        "recall": 0.5517241379310345,
        "f1-score": 0.5333333333333333,
        "support": 29.0
    },
    "accuracy": 0.5760869565217391,
    "macro avg": {
        "precision": 0.6136751152073733,
        "recall": 0.5818704284221525,
        "f1-score": 0.5887931034482758,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6099909837707874,
        "recall": 0.5760869565217391,
        "f1-score": 0.5842828585707146,
        "support": 92.0
    }
}
```

## TF-IDF_LogisticRegression

- **Weighted F1 Score:** 0.5809
- **Accuracy:** 0.5761
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8571428571428571,
        "recall": 0.6,
        "f1-score": 0.7058823529411765,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.47619047619047616,
        "recall": 0.5,
        "f1-score": 0.4878048780487805,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.6774193548387096,
        "recall": 0.6363636363636364,
        "f1-score": 0.65625,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.48484848484848486,
        "recall": 0.5517241379310345,
        "f1-score": 0.5161290322580645,
        "support": 29.0
    },
    "accuracy": 0.5760869565217391,
    "macro avg": {
        "precision": 0.623900293255132,
        "recall": 0.5720219435736678,
        "f1-score": 0.5915165658120054,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5925074224513215,
        "recall": 0.5760869565217391,
        "f1-score": 0.5808577502812092,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_SVM

- **Weighted F1 Score:** 0.5803
- **Accuracy:** 0.5761
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.75,
        "recall": 0.6,
        "f1-score": 0.6666666666666666,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.47619047619047616,
        "recall": 0.5,
        "f1-score": 0.4878048780487805,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.7,
        "recall": 0.6363636363636364,
        "f1-score": 0.6666666666666666,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.48484848484848486,
        "recall": 0.5517241379310345,
        "f1-score": 0.5161290322580645,
        "support": 29.0
    },
    "accuracy": 0.5760869565217391,
    "macro avg": {
        "precision": 0.6027597402597402,
        "recall": 0.5720219435736678,
        "f1-score": 0.5843168109100445,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.588961038961039,
        "recall": 0.5760869565217391,
        "f1-score": 0.5803315887296321,
        "support": 92.0
    }
}
```

## Word2Vec_KNN

- **Weighted F1 Score:** 0.4878
- **Accuracy:** 0.4891
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 1.0,
        "recall": 0.5,
        "f1-score": 0.6666666666666666,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.3793103448275862,
        "recall": 0.55,
        "f1-score": 0.4489795918367347,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.46511627906976744,
        "recall": 0.6060606060606061,
        "f1-score": 0.5263157894736842,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.6,
        "recall": 0.3103448275862069,
        "f1-score": 0.4090909090909091,
        "support": 29.0
    },
    "accuracy": 0.4891304347826087,
    "macro avg": {
        "precision": 0.6111066559743384,
        "recall": 0.49160135841170327,
        "f1-score": 0.5127632392669986,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.5471200446288483,
        "recall": 0.4891304347826087,
        "f1-score": 0.4878077817355359,
        "support": 92.0
    }
}
```

## BoW_DecisionTree

- **Weighted F1 Score:** 0.4663
- **Accuracy:** 0.4674
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.625,
        "recall": 0.5,
        "f1-score": 0.5555555555555556,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.4090909090909091,
        "recall": 0.45,
        "f1-score": 0.42857142857142855,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.46153846153846156,
        "recall": 0.5454545454545454,
        "f1-score": 0.5,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.4782608695652174,
        "recall": 0.3793103448275862,
        "f1-score": 0.4230769230769231,
        "support": 29.0
    },
    "accuracy": 0.4673913043478261,
    "macro avg": {
        "precision": 0.49347256004864704,
        "recall": 0.46869122257053286,
        "f1-score": 0.47680097680097683,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.47317557206498606,
        "recall": 0.4673913043478261,
        "f1-score": 0.46626320539364013,
        "support": 92.0
    }
}
```

## Bert_KNN

- **Weighted F1 Score:** 0.4625
- **Accuracy:** 0.4674
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.7,
        "recall": 0.7,
        "f1-score": 0.7,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.41379310344827586,
        "recall": 0.6,
        "f1-score": 0.4897959183673469,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5,
        "recall": 0.45454545454545453,
        "f1-score": 0.47619047619047616,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.391304347826087,
        "recall": 0.3103448275862069,
        "f1-score": 0.34615384615384615,
        "support": 29.0
    },
    "accuracy": 0.4673913043478261,
    "macro avg": {
        "precision": 0.5012743628185907,
        "recall": 0.5162225705329153,
        "f1-score": 0.5030350601779173,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.46873574082523956,
        "recall": 0.4673913043478261,
        "f1-score": 0.462485495870589,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree

- **Weighted F1 Score:** 0.4411
- **Accuracy:** 0.4348
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.5555555555555556,
        "recall": 0.5,
        "f1-score": 0.5263157894736842,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.4090909090909091,
        "recall": 0.45,
        "f1-score": 0.42857142857142855,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5769230769230769,
        "recall": 0.45454545454545453,
        "f1-score": 0.5084745762711864,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.3142857142857143,
        "recall": 0.3793103448275862,
        "f1-score": 0.34375,
        "support": 29.0
    },
    "accuracy": 0.43478260869565216,
    "macro avg": {
        "precision": 0.463963813963814,
        "recall": 0.44596394984326015,
        "f1-score": 0.4517779485790748,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.4553274020665325,
        "recall": 0.43478260869565216,
        "f1-score": 0.44111953785994096,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.4363
- **Accuracy:** 0.4348
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.45454545454545453,
        "recall": 0.5,
        "f1-score": 0.47619047619047616,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.45,
        "recall": 0.45,
        "f1-score": 0.45,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.5483870967741935,
        "recall": 0.5151515151515151,
        "f1-score": 0.53125,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.3,
        "recall": 0.3103448275862069,
        "f1-score": 0.3050847457627119,
        "support": 29.0
    },
    "accuracy": 0.43478260869565216,
    "macro avg": {
        "precision": 0.438233137829912,
        "recall": 0.4438740856844305,
        "f1-score": 0.44063130548829704,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.43850248629351013,
        "recall": 0.43478260869565216,
        "f1-score": 0.4363110042285153,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.3636
- **Accuracy:** 0.3587
- **Best Parameters:** {'max_depth': None}
```json
{
    "NA_CATEGORY": {
        "precision": 0.4444444444444444,
        "recall": 0.4,
        "f1-score": 0.42105263157894735,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.2,
        "recall": 0.25,
        "f1-score": 0.2222222222222222,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.41935483870967744,
        "recall": 0.3939393939393939,
        "f1-score": 0.40625,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.4074074074074074,
        "recall": 0.3793103448275862,
        "f1-score": 0.39285714285714285,
        "support": 29.0
    },
    "accuracy": 0.358695652173913,
    "macro avg": {
        "precision": 0.3678016726403823,
        "recall": 0.35581243469174506,
        "f1-score": 0.3605954991645781,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.3706300971378111,
        "recall": 0.358695652173913,
        "f1-score": 0.36363128155533764,
        "support": 92.0
    }
}
```

## FastText_KNN

- **Weighted F1 Score:** 0.3460
- **Accuracy:** 0.3478
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.375,
        "recall": 0.3,
        "f1-score": 0.3333333333333333,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.25806451612903225,
        "recall": 0.4,
        "f1-score": 0.3137254901960784,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4,
        "recall": 0.42424242424242425,
        "f1-score": 0.4117647058823529,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.3888888888888889,
        "recall": 0.2413793103448276,
        "f1-score": 0.2978723404255319,
        "support": 29.0
    },
    "accuracy": 0.34782608695652173,
    "macro avg": {
        "precision": 0.3554883512544803,
        "recall": 0.341405433646813,
        "f1-score": 0.3391739674593241,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.3629246532647655,
        "recall": 0.34782608695652173,
        "f1-score": 0.3460258293881845,
        "support": 92.0
    }
}
```

## BoW_KNN

- **Weighted F1 Score:** 0.3092
- **Accuracy:** 0.3913
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.3333333333333333,
        "recall": 0.7,
        "f1-score": 0.45161290322580644,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.5,
        "recall": 0.15,
        "f1-score": 0.23076923076923078,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.4098360655737705,
        "recall": 0.7575757575757576,
        "f1-score": 0.5319148936170213,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.25,
        "recall": 0.034482758620689655,
        "f1-score": 0.06060606060606061,
        "support": 29.0
    },
    "accuracy": 0.391304347826087,
    "macro avg": {
        "precision": 0.37329234972677594,
        "recall": 0.4105146290491118,
        "f1-score": 0.3187257720545298,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.37073829888334525,
        "recall": 0.391304347826087,
        "f1-score": 0.30915522711500154,
        "support": 92.0
    }
}
```

## FastText_DecisionTree

- **Weighted F1 Score:** 0.3049
- **Accuracy:** 0.3043
- **Best Parameters:** {'max_depth': 10}
```json
{
    "NA_CATEGORY": {
        "precision": 0.16666666666666666,
        "recall": 0.1,
        "f1-score": 0.125,
        "support": 10.0
    },
    "diagnostique": {
        "precision": 0.23076923076923078,
        "recall": 0.3,
        "f1-score": 0.2608695652173913,
        "support": 20.0
    },
    "symptome": {
        "precision": 0.44,
        "recall": 0.3333333333333333,
        "f1-score": 0.3793103448275862,
        "support": 33.0
    },
    "traitement": {
        "precision": 0.2857142857142857,
        "recall": 0.3448275862068966,
        "f1-score": 0.3125,
        "support": 29.0
    },
    "accuracy": 0.30434782608695654,
    "macro avg": {
        "precision": 0.28078754578754583,
        "recall": 0.2695402298850575,
        "f1-score": 0.26941997751124436,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.316171364867017,
        "recall": 0.30434782608695654,
        "f1-score": 0.30486013786584965,
        "support": 92.0
    }
}
```

## Word2Vec_LogisticRegression

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "micro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "macro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "weighted avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    }
}
```

## Word2Vec_SVM

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "micro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "macro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "weighted avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    }
}
```

## FastText_LogisticRegression

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "micro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "macro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "weighted avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    }
}
```

## FastText_SVM

- **Weighted F1 Score:** 0.1894
- **Accuracy:** 0.3587
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "micro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "macro avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    },
    "weighted avg": {
        "precision": 0.358695652173913,
        "recall": 1.0,
        "f1-score": 0.528,
        "support": 33.0
    }
}
```

