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
    "micro avg": {
        "precision": 0.8505747126436781,
        "recall": 0.9135802469135802,
        "f1-score": 0.8809523809523809,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.826829268292683,
        "recall": 0.6818181818181819,
        "f1-score": 0.7105263157894737,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8463715748268594,
        "recall": 0.9135802469135802,
        "f1-score": 0.8638726445743989,
        "support": 81.0
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
    "micro avg": {
        "precision": 0.8275862068965517,
        "recall": 0.8888888888888888,
        "f1-score": 0.8571428571428571,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.7107142857142856,
        "recall": 0.6675324675324675,
        "f1-score": 0.6755555555555555,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8121693121693122,
        "recall": 0.8888888888888888,
        "f1-score": 0.8438957475994513,
        "support": 81.0
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
    "micro avg": {
        "precision": 0.8275862068965517,
        "recall": 0.8888888888888888,
        "f1-score": 0.8571428571428571,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.7207317073170731,
        "recall": 0.6292207792207792,
        "f1-score": 0.6414473684210527,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8086720867208672,
        "recall": 0.8888888888888888,
        "f1-score": 0.8355263157894737,
        "support": 81.0
    }
}
```

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.7701
- **Accuracy:** 0.7701
- **Best Parameters:** {'max_depth': 10}
```json
{
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.45454545454545453,
        "f1-score": 0.38461538461538464,
        "support": 11.0
    },
    "non": {
        "precision": 0.8840579710144928,
        "recall": 0.8714285714285714,
        "f1-score": 0.8776978417266187,
        "support": 70.0
    },
    "positif": {
        "precision": 0.3333333333333333,
        "recall": 0.16666666666666666,
        "f1-score": 0.2222222222222222,
        "support": 6.0
    },
    "accuracy": 0.7701149425287356,
    "macro avg": {
        "precision": 0.5169082125603864,
        "recall": 0.49754689754689757,
        "f1-score": 0.4948451495214085,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.7764451107779443,
        "recall": 0.7701149425287356,
        "f1-score": 0.7701488676432858,
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
    "micro avg": {
        "precision": 0.8160919540229885,
        "recall": 0.8765432098765432,
        "f1-score": 0.8452380952380952,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.6697530864197531,
        "recall": 0.622077922077922,
        "f1-score": 0.6268017140631087,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7934003962810547,
        "recall": 0.8765432098765432,
        "f1-score": 0.8262803772477841,
        "support": 81.0
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
    "micro avg": {
        "precision": 0.8160919540229885,
        "recall": 0.8765432098765432,
        "f1-score": 0.8452380952380952,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.7146341463414634,
        "recall": 0.622077922077922,
        "f1-score": 0.6348684210526316,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7981330924420355,
        "recall": 0.8765432098765432,
        "f1-score": 0.8241552956465238,
        "support": 81.0
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
    "micro avg": {
        "precision": 0.8275862068965517,
        "recall": 0.8888888888888888,
        "f1-score": 0.8571428571428571,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.9117647058823529,
        "recall": 0.5909090909090909,
        "f1-score": 0.6054590570719602,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8474945533769063,
        "recall": 0.8888888888888888,
        "f1-score": 0.8223508868670159,
        "support": 81.0
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
    "micro avg": {
        "precision": 0.8275862068965517,
        "recall": 0.8888888888888888,
        "f1-score": 0.8571428571428571,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.9117647058823529,
        "recall": 0.5909090909090909,
        "f1-score": 0.6054590570719602,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8474945533769063,
        "recall": 0.8888888888888888,
        "f1-score": 0.8223508868670159,
        "support": 81.0
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
    "micro avg": {
        "precision": 0.7931034482758621,
        "recall": 0.8518518518518519,
        "f1-score": 0.8214285714285714,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.6388888888888888,
        "recall": 0.6461038961038961,
        "f1-score": 0.6391891891891892,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7805212620027435,
        "recall": 0.8518518518518519,
        "f1-score": 0.8134134134134134,
        "support": 81.0
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
    "micro avg": {
        "precision": 0.7931034482758621,
        "recall": 0.8518518518518519,
        "f1-score": 0.8214285714285714,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.5802469135802469,
        "recall": 0.5694805194805195,
        "f1-score": 0.5613556680950526,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7600975461057765,
        "recall": 0.8518518518518519,
        "f1-score": 0.7988572912608752,
        "support": 81.0
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
    "micro avg": {
        "precision": 0.8160919540229885,
        "recall": 0.8765432098765432,
        "f1-score": 0.8452380952380952,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.9069767441860466,
        "recall": 0.5454545454545454,
        "f1-score": 0.532051282051282,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.8392190640252657,
        "recall": 0.8765432098765432,
        "f1-score": 0.7981956315289649,
        "support": 81.0
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
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 0.8641975308641975,
        "f1-score": 0.8333333333333334,
        "support": 81.0
    },
    "macro avg": {
        "precision": 0.4069767441860465,
        "recall": 0.5,
        "f1-score": 0.44871794871794873,
        "support": 81.0
    },
    "weighted avg": {
        "precision": 0.7034165948894631,
        "recall": 0.8641975308641975,
        "f1-score": 0.7755618866729979,
        "support": 81.0
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
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "macro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "weighted avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
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
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "macro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "weighted avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
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
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "macro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "weighted avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
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
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "macro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "weighted avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
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
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "macro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "weighted avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
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
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "macro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "weighted avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
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
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "macro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "weighted avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
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
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "micro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "macro avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
    },
    "weighted avg": {
        "precision": 0.8045977011494253,
        "recall": 1.0,
        "f1-score": 0.89171974522293,
        "support": 70.0
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
        "precision": 0.2222222222222222,
        "recall": 0.18181818181818182,
        "f1-score": 0.2,
        "support": 11.0
    },
    "non": {
        "precision": 0.8194444444444444,
        "recall": 0.8428571428571429,
        "f1-score": 0.8309859154929577,
        "support": 70.0
    },
    "positif": {
        "precision": 0.16666666666666666,
        "recall": 0.16666666666666666,
        "f1-score": 0.16666666666666666,
        "support": 6.0
    },
    "accuracy": 0.7126436781609196,
    "macro avg": {
        "precision": 0.40277777777777773,
        "recall": 0.39711399711399714,
        "f1-score": 0.3992175273865415,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6989144316730523,
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

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.6804
- **Accuracy:** 0.7241
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
        "precision": 0.7974683544303798,
        "recall": 0.9,
        "f1-score": 0.8456375838926175,
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
        "precision": 0.2658227848101266,
        "recall": 0.3,
        "f1-score": 0.28187919463087246,
        "support": 87.0
    },
    "weighted avg": {
        "precision": 0.6416412047140987,
        "recall": 0.7241379310344828,
        "f1-score": 0.6803980560055543,
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

