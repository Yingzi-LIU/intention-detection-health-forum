# Experiment Results Summary

**Labels:** fonction_phatique, partage_experience, recherche_information

## TF-IDF_SVM

- **Weighted F1 Score:** 0.8163
- **Accuracy:** 0.8261
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5833333333333334,
        "f1-score": 0.7368421052631579,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8552631578947368,
        "recall": 0.9420289855072463,
        "f1-score": 0.896551724137931,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.4444444444444444,
        "recall": 0.36363636363636365,
        "f1-score": 0.4,
        "support": 11.0
    },
    "accuracy": 0.8260869565217391,
    "macro avg": {
        "precision": 0.766569200779727,
        "recall": 0.6296662274923145,
        "f1-score": 0.6777979431336963,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8250222476481058,
        "recall": 0.8260869565217391,
        "f1-score": 0.8163497198769037,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_SVM

- **Weighted F1 Score:** 0.8051
- **Accuracy:** 0.8261
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.875,
        "recall": 0.5833333333333334,
        "f1-score": 0.7,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8354430379746836,
        "recall": 0.9565217391304348,
        "f1-score": 0.8918918918918919,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.6,
        "recall": 0.2727272727272727,
        "f1-score": 0.375,
        "support": 11.0
    },
    "accuracy": 0.8260869565217391,
    "macro avg": {
        "precision": 0.7701476793248946,
        "recall": 0.6041941150636803,
        "f1-score": 0.6556306306306307,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8124518436984038,
        "recall": 0.8260869565217391,
        "f1-score": 0.805060223266745,
        "support": 92.0
    }
}
```

## Bert_KNN

- **Weighted F1 Score:** 0.7995
- **Accuracy:** 0.8370
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.8181818181818182,
        "recall": 0.75,
        "f1-score": 0.782608695652174,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8481012658227848,
        "recall": 0.9710144927536232,
        "f1-score": 0.9054054054054054,
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
        "precision": 0.7220943613348677,
        "recall": 0.6039745278875713,
        "f1-score": 0.6139534183012444,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8025779256516736,
        "recall": 0.8369565217391305,
        "f1-score": 0.7995280979685517,
        "support": 92.0
    }
}
```

## BoW_SVM

- **Weighted F1 Score:** 0.7982
- **Accuracy:** 0.8370
- **Best Parameters:** {'C': 1, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.6666666666666666,
        "f1-score": 0.8,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8292682926829268,
        "recall": 0.9855072463768116,
        "f1-score": 0.9006622516556292,
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
        "precision": 0.7764227642276422,
        "recall": 0.5810276679841897,
        "f1-score": 0.6181694685005943,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8121686108165429,
        "recall": 0.8369565217391305,
        "f1-score": 0.7982391636581099,
        "support": 92.0
    }
}
```

## TF-IDF_KNN

- **Weighted F1 Score:** 0.7928
- **Accuracy:** 0.8152
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.625,
        "recall": 0.8333333333333334,
        "f1-score": 0.7142857142857143,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.863013698630137,
        "recall": 0.9130434782608695,
        "f1-score": 0.8873239436619719,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.6666666666666666,
        "recall": 0.18181818181818182,
        "f1-score": 0.2857142857142857,
        "support": 11.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.7182267884322678,
        "recall": 0.6427316644707949,
        "f1-score": 0.6291079812206574,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8084921580305737,
        "recall": 0.8152173913043478,
        "f1-score": 0.7928221502930627,
        "support": 92.0
    }
}
```

## TF-IDF_LogisticRegression

- **Weighted F1 Score:** 0.7925
- **Accuracy:** 0.8370
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5833333333333334,
        "f1-score": 0.7368421052631579,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8214285714285714,
        "recall": 1.0,
        "f1-score": 0.9019607843137255,
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
        "precision": 0.9404761904761904,
        "recall": 0.5580808080808081,
        "f1-score": 0.6018231854145167,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8660714285714285,
        "recall": 0.8369565217391305,
        "f1-score": 0.7925079642841117,
        "support": 92.0
    }
}
```

## Bert_LogisticRegression

- **Weighted F1 Score:** 0.7914
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 0.7272727272727273,
        "recall": 0.6666666666666666,
        "f1-score": 0.6956521739130435,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8513513513513513,
        "recall": 0.9130434782608695,
        "f1-score": 0.8811188811188811,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.42857142857142855,
        "recall": 0.2727272727272727,
        "f1-score": 0.3333333333333333,
        "support": 11.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.6690651690651691,
        "recall": 0.6174791392182696,
        "f1-score": 0.6367014627884193,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7846174096174096,
        "recall": 0.8043478260869565,
        "f1-score": 0.7914314733785434,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN

- **Weighted F1 Score:** 0.7889
- **Accuracy:** 0.8152
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 0.6666666666666666,
        "recall": 0.6666666666666666,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8441558441558441,
        "recall": 0.9420289855072463,
        "f1-score": 0.8904109589041096,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.6666666666666666,
        "recall": 0.18181818181818182,
        "f1-score": 0.2857142857142857,
        "support": 11.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.7258297258297257,
        "recall": 0.5968379446640316,
        "f1-score": 0.6142639704283539,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7997835497835497,
        "recall": 0.8152173913043478,
        "f1-score": 0.7889262316004424,
        "support": 92.0
    }
}
```

## TF-IDF_MultinomialNB

- **Weighted F1 Score:** 0.7887
- **Accuracy:** 0.8261
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5833333333333334,
        "f1-score": 0.7368421052631579,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8292682926829268,
        "recall": 0.9855072463768116,
        "f1-score": 0.9006622516556292,
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
        "precision": 0.7208672086720868,
        "recall": 0.5532498902064119,
        "f1-score": 0.5934538332586433,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.792241074584659,
        "recall": 0.8260869565217391,
        "f1-score": 0.7886872739002705,
        "support": 92.0
    }
}
```

## BoW_LogisticRegression

- **Weighted F1 Score:** 0.7856
- **Accuracy:** 0.8261
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5833333333333334,
        "f1-score": 0.7368421052631579,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8192771084337349,
        "recall": 0.9855072463768116,
        "f1-score": 0.8947368421052632,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "accuracy": 0.8260869565217391,
    "macro avg": {
        "precision": 0.7730923694779116,
        "recall": 0.5532498902064119,
        "f1-score": 0.5951417004048584,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.8046752226296491,
        "recall": 0.8260869565217391,
        "f1-score": 0.7855571202253124,
        "support": 92.0
    }
}
```

## Word2Vec_KNN

- **Weighted F1 Score:** 0.7801
- **Accuracy:** 0.8043
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "fonction_phatique": {
        "precision": 0.7777777777777778,
        "recall": 0.5833333333333334,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8333333333333334,
        "recall": 0.9420289855072463,
        "f1-score": 0.8843537414965986,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.4,
        "recall": 0.18181818181818182,
        "f1-score": 0.25,
        "support": 11.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.6703703703703704,
        "recall": 0.5690601668862538,
        "f1-score": 0.6003401360544217,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7742753623188406,
        "recall": 0.8043478260869565,
        "f1-score": 0.7801131322094055,
        "support": 92.0
    }
}
```

## BoW_MultinomialNB

- **Weighted F1 Score:** 0.7751
- **Accuracy:** 0.8152
- **Best Parameters:** {'alpha': 1.0}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5,
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
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.7175368139223561,
        "recall": 0.5254721124286341,
        "f1-score": 0.5680868838763575,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.784747686397765,
        "recall": 0.8152173913043478,
        "f1-score": 0.7750898986596926,
        "support": 92.0
    }
}
```

## FastText_KNN

- **Weighted F1 Score:** 0.7720
- **Accuracy:** 0.8152
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5,
        "f1-score": 0.6666666666666666,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8095238095238095,
        "recall": 0.9855072463768116,
        "f1-score": 0.8888888888888888,
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
        "precision": 0.7698412698412698,
        "recall": 0.5254721124286341,
        "f1-score": 0.5698005698005697,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.797360248447205,
        "recall": 0.8152173913043478,
        "f1-score": 0.7720178372352285,
        "support": 92.0
    }
}
```

## Bert_SVM

- **Weighted F1 Score:** 0.7698
- **Accuracy:** 0.7717
- **Best Parameters:** {'C': 1, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.6153846153846154,
        "recall": 0.6666666666666666,
        "f1-score": 0.64,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8695652173913043,
        "recall": 0.8695652173913043,
        "f1-score": 0.8695652173913043,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.3,
        "recall": 0.2727272727272727,
        "f1-score": 0.2857142857142857,
        "support": 11.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.5949832775919732,
        "recall": 0.6029863855950812,
        "f1-score": 0.5984265010351967,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7683110367892977,
        "recall": 0.7717391304347826,
        "f1-score": 0.7698136645962733,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_LogisticRegression

- **Weighted F1 Score:** 0.7682
- **Accuracy:** 0.8261
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.5833333333333334,
        "f1-score": 0.7368421052631579,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8117647058823529,
        "recall": 1.0,
        "f1-score": 0.8961038961038961,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.8260869565217391,
        "recall": 0.9382716049382716,
        "f1-score": 0.8786127167630058,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.9058823529411765,
        "recall": 0.7916666666666667,
        "f1-score": 0.816473000683527,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8396514161220044,
        "recall": 0.9382716049382716,
        "f1-score": 0.8725095567200831,
        "support": 81.0
    }
}
```

## FastText_DecisionTree

- **Weighted F1 Score:** 0.7659
- **Accuracy:** 0.7609
- **Best Parameters:** {'max_depth': None}
```json
{
    "fonction_phatique": {
        "precision": 0.6428571428571429,
        "recall": 0.75,
        "f1-score": 0.6923076923076923,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8787878787878788,
        "recall": 0.8405797101449275,
        "f1-score": 0.8592592592592593,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.25,
        "recall": 0.2727272727272727,
        "f1-score": 0.2608695652173913,
        "support": 11.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.5905483405483406,
        "recall": 0.6211023276240667,
        "f1-score": 0.604145505594781,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7728331451157537,
        "recall": 0.7608695652173914,
        "f1-score": 0.7659363740649184,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree

- **Weighted F1 Score:** 0.7511
- **Accuracy:** 0.7500
- **Best Parameters:** {'max_depth': None}
```json
{
    "fonction_phatique": {
        "precision": 0.6153846153846154,
        "recall": 0.6666666666666666,
        "f1-score": 0.64,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8529411764705882,
        "recall": 0.8405797101449275,
        "f1-score": 0.8467153284671532,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.2727272727272727,
        "recall": 0.2727272727272727,
        "f1-score": 0.2727272727272727,
        "support": 11.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.5803510215274922,
        "recall": 0.593324549846289,
        "f1-score": 0.5864808670648086,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7525821365335431,
        "recall": 0.75,
        "f1-score": 0.7511234528721041,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.7458
- **Accuracy:** 0.7717
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.5714285714285714,
        "recall": 0.6666666666666666,
        "f1-score": 0.6153846153846154,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.863013698630137,
        "recall": 0.9130434782608695,
        "f1-score": 0.8873239436619719,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.47814742335290283,
        "recall": 0.5265700483091788,
        "f1-score": 0.5009028530155292,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.721794435463286,
        "recall": 0.7717391304347826,
        "f1-score": 0.7457605162749069,
        "support": 92.0
    }
}
```

## BoW_DecisionTree

- **Weighted F1 Score:** 0.7449
- **Accuracy:** 0.8043
- **Best Parameters:** {'max_depth': 10}
```json
{
    "fonction_phatique": {
        "precision": 0.75,
        "recall": 0.5,
        "f1-score": 0.6,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.8095238095238095,
        "recall": 0.9855072463768116,
        "f1-score": 0.8888888888888888,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.8043478260869565,
        "recall": 0.9135802469135802,
        "f1-score": 0.8554913294797688,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.7797619047619048,
        "recall": 0.7427536231884058,
        "f1-score": 0.7444444444444445,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8007054673721341,
        "recall": 0.9135802469135802,
        "f1-score": 0.8460905349794239,
        "support": 81.0
    }
}
```

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.7190
- **Accuracy:** 0.7283
- **Best Parameters:** {'max_depth': 10}
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

## Bert_DecisionTree

- **Weighted F1 Score:** 0.7027
- **Accuracy:** 0.7065
- **Best Parameters:** {'max_depth': 5}
```json
{
    "fonction_phatique": {
        "precision": 0.6666666666666666,
        "recall": 0.5,
        "f1-score": 0.5714285714285714,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.7916666666666666,
        "recall": 0.8260869565217391,
        "f1-score": 0.8085106382978723,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.18181818181818182,
        "recall": 0.18181818181818182,
        "f1-score": 0.18181818181818182,
        "support": 11.0
    },
    "accuracy": 0.7065217391304348,
    "macro avg": {
        "precision": 0.5467171717171717,
        "recall": 0.502635046113307,
        "f1-score": 0.5205857971815419,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7024456521739131,
        "recall": 0.7065217391304348,
        "f1-score": 0.70265627064887,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_MultinomialNB

- **Weighted F1 Score:** 0.6882
- **Accuracy:** 0.7717
- **Best Parameters:** {'alpha': 0.5}
```json
{
    "fonction_phatique": {
        "precision": 1.0,
        "recall": 0.16666666666666666,
        "f1-score": 0.2857142857142857,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.7666666666666667,
        "recall": 1.0,
        "f1-score": 0.8679245283018868,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.7717391304347826,
        "recall": 0.8765432098765432,
        "f1-score": 0.8208092485549133,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.8833333333333333,
        "recall": 0.5833333333333334,
        "f1-score": 0.5768194070080863,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8012345679012346,
        "recall": 0.8765432098765432,
        "f1-score": 0.7816711590296497,
        "support": 81.0
    }
}
```

## BoW_KNN

- **Weighted F1 Score:** 0.6775
- **Accuracy:** 0.6413
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "fonction_phatique": {
        "precision": 0.36,
        "recall": 0.75,
        "f1-score": 0.4864864864864865,
        "support": 12.0
    },
    "partage_experience": {
        "precision": 0.9215686274509803,
        "recall": 0.6811594202898551,
        "f1-score": 0.7833333333333333,
        "support": 69.0
    },
    "recherche_information": {
        "precision": 0.1875,
        "recall": 0.2727272727272727,
        "f1-score": 0.2222222222222222,
        "support": 11.0
    },
    "accuracy": 0.6413043478260869,
    "macro avg": {
        "precision": 0.4896895424836601,
        "recall": 0.5679622310057092,
        "f1-score": 0.4973473473473473,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7605514705882352,
        "recall": 0.6413043478260869,
        "f1-score": 0.6775248074161118,
        "support": 92.0
    }
}
```

## Word2Vec_LogisticRegression

- **Weighted F1 Score:** 0.6429
- **Accuracy:** 0.7500
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "macro avg": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "weighted avg": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    }
}
```

## Word2Vec_SVM

- **Weighted F1 Score:** 0.6429
- **Accuracy:** 0.7500
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "macro avg": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "weighted avg": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    }
}
```

## FastText_LogisticRegression

- **Weighted F1 Score:** 0.6429
- **Accuracy:** 0.7500
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "fonction_phatique": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "macro avg": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "weighted avg": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    }
}
```

## FastText_SVM

- **Weighted F1 Score:** 0.6429
- **Accuracy:** 0.7500
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "fonction_phatique": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "micro avg": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "macro avg": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    },
    "weighted avg": {
        "precision": 0.75,
        "recall": 1.0,
        "f1-score": 0.8571428571428571,
        "support": 69.0
    }
}
```

