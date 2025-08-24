# Experiment Results Summary

**Labels:** NA_CATEGORY, negatif, positif

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.7641
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8375,
        "recall": 0.9054054054054054,
        "f1-score": 0.8701298701298701,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.5,
        "recall": 0.36363636363636365,
        "f1-score": 0.42105263157894735,
        "support": 11.0
    },
    "positif": {
        "precision": 0.25,
        "recall": 0.14285714285714285,
        "f1-score": 0.18181818181818182,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.5291666666666667,
        "recall": 0.4706329706329706,
        "f1-score": 0.4910002278423331,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.752445652173913,
        "recall": 0.782608695652174,
        "f1-score": 0.764064310975066,
        "support": 92.0
    }
}
```

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.7606
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__C': 1, 'classifier__kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8395061728395061,
        "recall": 0.918918918918919,
        "f1-score": 0.8774193548387097,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.5,
        "recall": 0.2727272727272727,
        "f1-score": 0.35294117647058826,
        "support": 11.0
    },
    "positif": {
        "precision": 0.2,
        "recall": 0.14285714285714285,
        "f1-score": 0.16666666666666666,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.5131687242798354,
        "recall": 0.44483444483444484,
        "f1-score": 0.4656757326586549,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7502549651100376,
        "recall": 0.782608695652174,
        "f1-score": 0.7606309985424745,
        "support": 92.0
    }
}
```

## BoW_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7534
- **Accuracy:** 0.8043
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8275862068965517,
        "recall": 0.972972972972973,
        "f1-score": 0.8944099378881988,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "positif": {
        "precision": 0.5,
        "recall": 0.14285714285714285,
        "f1-score": 0.2222222222222222,
        "support": 7.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.553639846743295,
        "recall": 0.40224640224640223,
        "f1-score": 0.4198297676558546,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7435657171414293,
        "recall": 0.8043478260869565,
        "f1-score": 0.7534056470729439,
        "support": 92.0
    }
}
```

## TF-IDF_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7345
- **Accuracy:** 0.8043
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8111111111111111,
        "recall": 0.9864864864864865,
        "f1-score": 0.8902439024390244,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.43703703703703706,
        "recall": 0.35913185913185913,
        "f1-score": 0.34803001876172607,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7121980676328503,
        "recall": 0.8043478260869565,
        "f1-score": 0.7344603964434293,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7321
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8181818181818182,
        "recall": 0.972972972972973,
        "f1-score": 0.8888888888888888,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.38383838383838387,
        "recall": 0.3546273546273546,
        "f1-score": 0.3439153439153439,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6979578392621871,
        "recall": 0.7934782608695652,
        "f1-score": 0.7320565907522428,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7292
- **Accuracy:** 0.7717
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8117647058823529,
        "recall": 0.9324324324324325,
        "f1-score": 0.8679245283018868,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "positif": {
        "precision": 0.2,
        "recall": 0.14285714285714285,
        "f1-score": 0.16666666666666666,
        "support": 7.0
    },
    "accuracy": 0.7717391304347826,
    "macro avg": {
        "precision": 0.503921568627451,
        "recall": 0.3887328887328887,
        "f1-score": 0.3961457829382358,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7279411764705882,
        "recall": 0.7717391304347826,
        "f1-score": 0.7291890157968912,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.7277
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8089887640449438,
        "recall": 0.972972972972973,
        "f1-score": 0.8834355828220859,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.3807740324594257,
        "recall": 0.3546273546273546,
        "f1-score": 0.34209757522640954,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6905634261520924,
        "recall": 0.7934782608695652,
        "f1-score": 0.7276702358724232,
        "support": 92.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.7221
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8068181818181818,
        "recall": 0.9594594594594594,
        "f1-score": 0.8765432098765432,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.380050505050505,
        "recall": 0.3501228501228501,
        "f1-score": 0.33980011757789536,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6888175230566534,
        "recall": 0.782608695652174,
        "f1-score": 0.7221263706770954,
        "support": 92.0
    }
}
```

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.7203
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8068181818181818,
        "recall": 0.9594594594594594,
        "f1-score": 0.8765432098765432,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 0.3333333333333333,
        "recall": 0.14285714285714285,
        "f1-score": 0.2,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.380050505050505,
        "recall": 0.3674388674388674,
        "f1-score": 0.35884773662551445,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6743247694334651,
        "recall": 0.782608695652174,
        "f1-score": 0.7202630166398284,
        "support": 92.0
    }
}
```

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7063
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__C': 1, 'classifier__solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8,
        "recall": 0.972972972972973,
        "f1-score": 0.8780487804878049,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.26666666666666666,
        "recall": 0.32432432432432434,
        "f1-score": 0.2926829268292683,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6434782608695653,
        "recall": 0.782608695652174,
        "f1-score": 0.706256627783669,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7063
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8,
        "recall": 0.972972972972973,
        "f1-score": 0.8780487804878049,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.26666666666666666,
        "recall": 0.32432432432432434,
        "f1-score": 0.2926829268292683,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6434782608695653,
        "recall": 0.782608695652174,
        "f1-score": 0.706256627783669,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.6992
- **Accuracy:** 0.7391
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.7976190476190477,
        "recall": 0.9054054054054054,
        "f1-score": 0.8481012658227848,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.376984126984127,
        "recall": 0.3321048321048321,
        "f1-score": 0.3303194695599759,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6814182194616977,
        "recall": 0.7391304347826086,
        "f1-score": 0.6992491548077678,
        "support": 92.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.7591
- **Accuracy:** 0.8152
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8295454545454546,
        "recall": 0.9864864864864865,
        "f1-score": 0.9012345679012346,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.6666666666666666,
        "recall": 0.18181818181818182,
        "f1-score": 0.2857142857142857,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.4987373737373737,
        "recall": 0.3894348894348894,
        "f1-score": 0.39564961787184005,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7469532279314888,
        "recall": 0.8152173913043478,
        "f1-score": 0.7590675561690053,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7401
- **Accuracy:** 0.7826
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8235294117647058,
        "recall": 0.9459459459459459,
        "f1-score": 0.8805031446540881,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.2,
        "recall": 0.09090909090909091,
        "f1-score": 0.125,
        "support": 11.0
    },
    "positif": {
        "precision": 0.5,
        "recall": 0.14285714285714285,
        "f1-score": 0.2222222222222222,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.5078431372549019,
        "recall": 0.3932373932373932,
        "f1-score": 0.40924178895877006,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7243606138107417,
        "recall": 0.782608695652174,
        "f1-score": 0.7400846549995442,
        "support": 92.0
    }
}
```

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7256
- **Accuracy:** 0.7391
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8227848101265823,
        "recall": 0.8783783783783784,
        "f1-score": 0.8496732026143791,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.5,
        "recall": 0.2727272727272727,
        "f1-score": 0.35294117647058826,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.4409282700421941,
        "recall": 0.3837018837018837,
        "f1-score": 0.4008714596949891,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.721587782058338,
        "recall": 0.7391304347826086,
        "f1-score": 0.7256322818982666,
        "support": 92.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.7221
- **Accuracy:** 0.7826
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8068181818181818,
        "recall": 0.9594594594594594,
        "f1-score": 0.8765432098765432,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.380050505050505,
        "recall": 0.3501228501228501,
        "f1-score": 0.33980011757789536,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6888175230566534,
        "recall": 0.782608695652174,
        "f1-score": 0.7221263706770954,
        "support": 92.0
    }
}
```

## Word2Vec_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.26811594202898553,
        "recall": 0.3333333333333333,
        "f1-score": 0.2971887550200803,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6469754253308129,
        "recall": 0.8043478260869565,
        "f1-score": 0.7171293871136721,
        "support": 92.0
    }
}
```

## Word2Vec_SVM_Enhanced

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.26811594202898553,
        "recall": 0.3333333333333333,
        "f1-score": 0.2971887550200803,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6469754253308129,
        "recall": 0.8043478260869565,
        "f1-score": 0.7171293871136721,
        "support": 92.0
    }
}
```

## FastText_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.26811594202898553,
        "recall": 0.3333333333333333,
        "f1-score": 0.2971887550200803,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6469754253308129,
        "recall": 0.8043478260869565,
        "f1-score": 0.7171293871136721,
        "support": 92.0
    }
}
```

## FastText_SVM_Enhanced

- **Weighted F1 Score:** 0.7171
- **Accuracy:** 0.8043
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.26811594202898553,
        "recall": 0.3333333333333333,
        "f1-score": 0.2971887550200803,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6469754253308129,
        "recall": 0.8043478260869565,
        "f1-score": 0.7171293871136721,
        "support": 92.0
    }
}
```

