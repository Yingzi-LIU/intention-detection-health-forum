# Experiment Results Summary

**Labels:** negatif, non, positif

## TF-IDF_DecisionTree

- **Weighted F1 Score:** 0.8043
- **Accuracy:** 0.8506
- **Best Parameters:** {'max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.8,
        "recall": 0.36363636363636365,
        "f1-score": 0.5,
        "support": 11.0
    },
    "non": {
        "precision": 0.8536585365853658,
        "recall": 1.0,
        "f1-score": 0.9210526315789473,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8505747126436781,
    "macro avg": {
        "precision": 0.551219512195122,
        "recall": 0.4545454545454546,
        "f1-score": 0.47368421052631576,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7880011213905244,
        "recall": 0.8505747126436781,
        "f1-score": 0.8042952208106473,
        "support": 87.0
    }
}
```

## TF-IDF_SVM

- **Weighted F1 Score:** 0.7857
- **Accuracy:** 0.8276
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.5714285714285714,
        "recall": 0.36363636363636365,
        "f1-score": 0.4444444444444444,
        "support": 11.0
    },
    "non": {
        "precision": 0.85,
        "recall": 0.9714285714285714,
        "f1-score": 0.9066666666666666,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.47380952380952374,
        "recall": 0.44502164502164504,
        "f1-score": 0.4503703703703703,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7561576354679803,
        "recall": 0.8275862068965517,
        "f1-score": 0.7856960408684547,
        "support": 87.0
    }
}
```

## BoW_DecisionTree

- **Weighted F1 Score:** 0.7779
- **Accuracy:** 0.8276
- **Best Parameters:** {'max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.6,
        "recall": 0.2727272727272727,
        "f1-score": 0.375,
        "support": 11.0
    },
    "non": {
        "precision": 0.8414634146341463,
        "recall": 0.9857142857142858,
        "f1-score": 0.9078947368421053,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.48048780487804876,
        "recall": 0.4194805194805195,
        "f1-score": 0.4276315789473684,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.752901597981497,
        "recall": 0.8275862068965517,
        "f1-score": 0.7779038112522686,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.7727
- **Accuracy:** 0.7701
- **Best Parameters:** {'max_depth': 10}
```json
{
    "negatif": {
        "precision": 0.4166666666666667,
        "recall": 0.45454545454545453,
        "f1-score": 0.43478260869565216,
        "support": 11.0
    },
    "non": {
        "precision": 0.8840579710144928,
        "recall": 0.8714285714285714,
        "f1-score": 0.8776978417266187,
        "support": 70.0
    },
    "positif": {
        "precision": 0.16666666666666666,
        "recall": 0.16666666666666666,
        "f1-score": 0.16666666666666666,
        "support": 6.0
    },
    "accuracy": 0.7701149425287356,
    "macro avg": {
        "precision": 0.4891304347826087,
        "recall": 0.49754689754689757,
        "f1-score": 0.49304903902964586,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7754872563718141,
        "recall": 0.7701149425287356,
        "f1-score": 0.7726604323737412,
        "support": 87.0
    }
}
```

## TF-IDF_LogisticRegression

- **Weighted F1 Score:** 0.7693
- **Accuracy:** 0.8161
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.5,
        "recall": 0.2727272727272727,
        "f1-score": 0.35294117647058826,
        "support": 11.0
    },
    "non": {
        "precision": 0.8395061728395061,
        "recall": 0.9714285714285714,
        "f1-score": 0.9006622516556292,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8160919540229885,
    "macro avg": {
        "precision": 0.4465020576131687,
        "recall": 0.41471861471861465,
        "f1-score": 0.4178678093754058,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7386831275720165,
        "recall": 0.8160919540229885,
        "f1-score": 0.7692955236444887,
        "support": 87.0
    }
}
```

## BoW_LogisticRegression

- **Weighted F1 Score:** 0.7673
- **Accuracy:** 0.8161
- **Best Parameters:** {'C': 1, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.6,
        "recall": 0.2727272727272727,
        "f1-score": 0.375,
        "support": 11.0
    },
    "non": {
        "precision": 0.8292682926829268,
        "recall": 0.9714285714285714,
        "f1-score": 0.8947368421052632,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8160919540229885,
    "macro avg": {
        "precision": 0.47642276422764224,
        "recall": 0.41471861471861465,
        "f1-score": 0.42324561403508776,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7430894308943089,
        "recall": 0.8160919540229885,
        "f1-score": 0.7673169993950394,
        "support": 87.0
    }
}
```

## BoW_SVM

- **Weighted F1 Score:** 0.7656
- **Accuracy:** 0.8276
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 1.0,
        "recall": 0.18181818181818182,
        "f1-score": 0.3076923076923077,
        "support": 11.0
    },
    "non": {
        "precision": 0.8235294117647058,
        "recall": 1.0,
        "f1-score": 0.9032258064516129,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.6078431372549019,
        "recall": 0.393939393939394,
        "f1-score": 0.40363937138130684,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7890466531440161,
        "recall": 0.8275862068965517,
        "f1-score": 0.7656370326003251,
        "support": 87.0
    }
}
```

## BoW_MultinomialNB

- **Weighted F1 Score:** 0.7656
- **Accuracy:** 0.8276
- **Best Parameters:** {'alpha': 1.0}
```json
{
    "negatif": {
        "precision": 1.0,
        "recall": 0.18181818181818182,
        "f1-score": 0.3076923076923077,
        "support": 11.0
    },
    "non": {
        "precision": 0.8235294117647058,
        "recall": 1.0,
        "f1-score": 0.9032258064516129,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8275862068965517,
    "macro avg": {
        "precision": 0.6078431372549019,
        "recall": 0.393939393939394,
        "f1-score": 0.40363937138130684,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7890466531440161,
        "recall": 0.8275862068965517,
        "f1-score": 0.7656370326003251,
        "support": 87.0
    }
}
```

## TF-IDF_KNN

- **Weighted F1 Score:** 0.7573
- **Accuracy:** 0.7931
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "negatif": {
        "precision": 0.4444444444444444,
        "recall": 0.36363636363636365,
        "f1-score": 0.4,
        "support": 11.0
    },
    "non": {
        "precision": 0.8333333333333334,
        "recall": 0.9285714285714286,
        "f1-score": 0.8783783783783784,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.7931034482758621,
    "macro avg": {
        "precision": 0.4259259259259259,
        "recall": 0.4307359307359307,
        "f1-score": 0.42612612612612616,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7266922094508301,
        "recall": 0.7931034482758621,
        "f1-score": 0.7573159366262815,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_KNN

- **Weighted F1 Score:** 0.7438
- **Accuracy:** 0.7931
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.18181818181818182,
        "f1-score": 0.23529411764705882,
        "support": 11.0
    },
    "non": {
        "precision": 0.8271604938271605,
        "recall": 0.9571428571428572,
        "f1-score": 0.8874172185430463,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.7931034482758621,
    "macro avg": {
        "precision": 0.3868312757201646,
        "recall": 0.37965367965367963,
        "f1-score": 0.37423711206336835,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7076770256846885,
        "recall": 0.7931034482758621,
        "f1-score": 0.7437636849670217,
        "support": 87.0
    }
}
```

## TF-IDF_MultinomialNB

- **Weighted F1 Score:** 0.7431
- **Accuracy:** 0.8161
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "negatif": {
        "precision": 1.0,
        "recall": 0.09090909090909091,
        "f1-score": 0.16666666666666666,
        "support": 11.0
    },
    "non": {
        "precision": 0.813953488372093,
        "recall": 1.0,
        "f1-score": 0.8974358974358975,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8160919540229885,
    "macro avg": {
        "precision": 0.6046511627906977,
        "recall": 0.3636363636363636,
        "f1-score": 0.3547008547008547,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.781341887195937,
        "recall": 0.8160919540229885,
        "f1-score": 0.7431476569407605,
        "support": 87.0
    }
}
```

## GloVe_LogisticRegression

- **Weighted F1 Score:** 0.7326
- **Accuracy:** 0.7701
- **Best Parameters:** {'C': 1, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.25,
        "recall": 0.09090909090909091,
        "f1-score": 0.13333333333333333,
        "support": 11.0
    },
    "non": {
        "precision": 0.8227848101265823,
        "recall": 0.9285714285714286,
        "f1-score": 0.87248322147651,
        "support": 70.0
    },
    "positif": {
        "precision": 0.25,
        "recall": 0.16666666666666666,
        "f1-score": 0.2,
        "support": 6.0
    },
    "accuracy": 0.7701149425287356,
    "macro avg": {
        "precision": 0.4409282700421941,
        "recall": 0.3953823953823954,
        "f1-score": 0.40193885160328113,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7108613414811582,
        "recall": 0.7701149425287356,
        "f1-score": 0.7326493352876134,
        "support": 87.0
    }
}
```

## Word2Vec_KNN

- **Weighted F1 Score:** 0.7301
- **Accuracy:** 0.7701
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "negatif": {
        "precision": 0.2857142857142857,
        "recall": 0.18181818181818182,
        "f1-score": 0.2222222222222222,
        "support": 11.0
    },
    "non": {
        "precision": 0.8227848101265823,
        "recall": 0.9285714285714286,
        "f1-score": 0.87248322147651,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.7701149425287356,
    "macro avg": {
        "precision": 0.3694996986136227,
        "recall": 0.37012987012987014,
        "f1-score": 0.3649018145662441,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6981355615139989,
        "recall": 0.7701149425287356,
        "f1-score": 0.730095056871266,
        "support": 87.0
    }
}
```

## BoW_KNN

- **Weighted F1 Score:** 0.7221
- **Accuracy:** 0.8046
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.813953488372093,
        "recall": 1.0,
        "f1-score": 0.8974358974358975,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.2713178294573643,
        "recall": 0.3333333333333333,
        "f1-score": 0.29914529914529914,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6549051055867415,
        "recall": 0.8045977011494253,
        "f1-score": 0.7220748600058945,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_LogisticRegression

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.2681992337164751,
        "recall": 0.3333333333333333,
        "f1-score": 0.29723991507430997,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.64737746069494,
        "recall": 0.8045977011494253,
        "f1-score": 0.7174756570759206,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_SVM

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.2681992337164751,
        "recall": 0.3333333333333333,
        "f1-score": 0.29723991507430997,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.64737746069494,
        "recall": 0.8045977011494253,
        "f1-score": 0.7174756570759206,
        "support": 87.0
    }
}
```

## TF-IDF_ngram_MultinomialNB

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'alpha': 0.5}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.2681992337164751,
        "recall": 0.3333333333333333,
        "f1-score": 0.29723991507430997,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.64737746069494,
        "recall": 0.8045977011494253,
        "f1-score": 0.7174756570759206,
        "support": 87.0
    }
}
```

## Word2Vec_LogisticRegression

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.2681992337164751,
        "recall": 0.3333333333333333,
        "f1-score": 0.29723991507430997,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.64737746069494,
        "recall": 0.8045977011494253,
        "f1-score": 0.7174756570759206,
        "support": 87.0
    }
}
```

## Word2Vec_SVM

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.2681992337164751,
        "recall": 0.3333333333333333,
        "f1-score": 0.29723991507430997,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.64737746069494,
        "recall": 0.8045977011494253,
        "f1-score": 0.7174756570759206,
        "support": 87.0
    }
}
```

## FastText_LogisticRegression

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.2681992337164751,
        "recall": 0.3333333333333333,
        "f1-score": 0.29723991507430997,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.64737746069494,
        "recall": 0.8045977011494253,
        "f1-score": 0.7174756570759206,
        "support": 87.0
    }
}
```

## FastText_SVM

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.2681992337164751,
        "recall": 0.3333333333333333,
        "f1-score": 0.29723991507430997,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.64737746069494,
        "recall": 0.8045977011494253,
        "f1-score": 0.7174756570759206,
        "support": 87.0
    }
}
```

## GloVe_SVM

- **Weighted F1 Score:** 0.7175
- **Accuracy:** 0.8046
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.8045977011494253,
    "macro avg": {
        "precision": 0.2681992337164751,
        "recall": 0.3333333333333333,
        "f1-score": 0.29723991507430997,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.64737746069494,
        "recall": 0.8045977011494253,
        "f1-score": 0.7174756570759206,
        "support": 87.0
    }
}
```

## FastText_DecisionTree

- **Weighted F1 Score:** 0.7054
- **Accuracy:** 0.7126
- **Best Parameters:** {'max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.18181818181818182,
        "recall": 0.18181818181818182,
        "f1-score": 0.18181818181818182,
        "support": 11.0
    },
    "non": {
        "precision": 0.8194444444444444,
        "recall": 0.8428571428571429,
        "f1-score": 0.8309859154929577,
        "support": 70.0
    },
    "positif": {
        "precision": 0.25,
        "recall": 0.16666666666666666,
        "f1-score": 0.2,
        "support": 6.0
    },
    "accuracy": 0.7126436781609196,
    "macro avg": {
        "precision": 0.4170875420875421,
        "recall": 0.39711399711399714,
        "f1-score": 0.4042680324370465,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6995530012771392,
        "recall": 0.7126436781609196,
        "f1-score": 0.7053909664885867,
        "support": 87.0
    }
}
```

## GloVe_DecisionTree

- **Weighted F1 Score:** 0.7053
- **Accuracy:** 0.7356
- **Best Parameters:** {'max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.25,
        "recall": 0.18181818181818182,
        "f1-score": 0.21052631578947367,
        "support": 11.0
    },
    "non": {
        "precision": 0.8051948051948052,
        "recall": 0.8857142857142857,
        "f1-score": 0.8435374149659864,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.735632183908046,
    "macro avg": {
        "precision": 0.35173160173160173,
        "recall": 0.35584415584415585,
        "f1-score": 0.3513545769184867,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6794670846394985,
        "recall": 0.735632183908046,
        "f1-score": 0.7053265347276237,
        "support": 87.0
    }
}
```

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.6987
- **Accuracy:** 0.7586
- **Best Parameters:** {'max_depth': 5}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8048780487804879,
        "recall": 0.9428571428571428,
        "f1-score": 0.868421052631579,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.7586206896551724,
    "macro avg": {
        "precision": 0.2682926829268293,
        "recall": 0.3142857142857143,
        "f1-score": 0.2894736842105263,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6476030277544155,
        "recall": 0.7586206896551724,
        "f1-score": 0.6987295825771325,
        "support": 87.0
    }
}
```

## GloVe_KNN

- **Weighted F1 Score:** 0.6897
- **Accuracy:** 0.7241
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "non": {
        "precision": 0.8181818181818182,
        "recall": 0.9,
        "f1-score": 0.8571428571428571,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.7241379310344828,
    "macro avg": {
        "precision": 0.27272727272727276,
        "recall": 0.3,
        "f1-score": 0.2857142857142857,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.658307210031348,
        "recall": 0.7241379310344828,
        "f1-score": 0.6896551724137931,
        "support": 87.0
    }
}
```

## FastText_KNN

- **Weighted F1 Score:** 0.6747
- **Accuracy:** 0.6897
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "negatif": {
        "precision": 0.16666666666666666,
        "recall": 0.18181818181818182,
        "f1-score": 0.17391304347826086,
        "support": 11.0
    },
    "non": {
        "precision": 0.7945205479452054,
        "recall": 0.8285714285714286,
        "f1-score": 0.8111888111888111,
        "support": 70.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 6.0
    },
    "accuracy": 0.6896551724137931,
    "macro avg": {
        "precision": 0.32039573820395734,
        "recall": 0.3367965367965368,
        "f1-score": 0.328367284889024,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.66034220332756,
        "recall": 0.6896551724137931,
        "f1-score": 0.674669658177904,
        "support": 87.0
    }
}
```

