# Experiment Results Summary

**Labels:** nan, negatif, positif

## BoW_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7063
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__C': 1, 'classifier__solver': 'liblinear'}
```json
{
    "0": {
        "precision": 0.8,
        "recall": 0.972972972972973,
        "f1-score": 0.8780487804878049,
        "support": 74.0
    },
    "1": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "2": {
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

## BoW_SVM_Enhanced

- **Weighted F1 Score:** 0.7606
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.8395061728395061,
        "recall": 0.918918918918919,
        "f1-score": 0.8774193548387097,
        "support": 74.0
    },
    "1": {
        "precision": 0.5,
        "recall": 0.2727272727272727,
        "f1-score": 0.35294117647058826,
        "support": 11.0
    },
    "2": {
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
    "0": {
        "precision": 0.8275862068965517,
        "recall": 0.972972972972973,
        "f1-score": 0.8944099378881988,
        "support": 74.0
    },
    "1": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "2": {
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

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.7275
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "0": {
        "precision": 0.8089887640449438,
        "recall": 0.972972972972973,
        "f1-score": 0.8834355828220859,
        "support": 74.0
    },
    "1": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "2": {
        "precision": 0.5,
        "recall": 0.14285714285714285,
        "f1-score": 0.2222222222222222,
        "support": 7.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.4363295880149813,
        "recall": 0.37194337194337196,
        "f1-score": 0.368552601681436,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.688751831949194,
        "recall": 0.7934782608695652,
        "f1-score": 0.7274977030911948,
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
    "0": {
        "precision": 0.8111111111111111,
        "recall": 0.9864864864864865,
        "f1-score": 0.8902439024390244,
        "support": 74.0
    },
    "1": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "2": {
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

## TF-IDF_SVM_Enhanced

- **Weighted F1 Score:** 0.7641
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.8375,
        "recall": 0.9054054054054054,
        "f1-score": 0.8701298701298701,
        "support": 74.0
    },
    "1": {
        "precision": 0.5,
        "recall": 0.36363636363636365,
        "f1-score": 0.42105263157894735,
        "support": 11.0
    },
    "2": {
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

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7221
- **Accuracy:** 0.7609
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "0": {
        "precision": 0.8095238095238095,
        "recall": 0.918918918918919,
        "f1-score": 0.8607594936708861,
        "support": 74.0
    },
    "1": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "2": {
        "precision": 0.2,
        "recall": 0.14285714285714285,
        "f1-score": 0.16666666666666666,
        "support": 7.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.4476190476190476,
        "recall": 0.38422838422838423,
        "f1-score": 0.39009443439823194,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7062111801242237,
        "recall": 0.7608695652173914,
        "f1-score": 0.7221119322797915,
        "support": 92.0
    }
}
```

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.7277
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__n_neighbors': 5}
```json
{
    "0": {
        "precision": 0.8089887640449438,
        "recall": 0.972972972972973,
        "f1-score": 0.8834355828220859,
        "support": 74.0
    },
    "1": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "2": {
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

## TF-IDF_ngram_LogisticRegression_Enhanced

- **Weighted F1 Score:** 0.7063
- **Accuracy:** 0.7826
- **Best Parameters:** {'classifier__C': 10, 'classifier__solver': 'liblinear'}
```json
{
    "0": {
        "precision": 0.8,
        "recall": 0.972972972972973,
        "f1-score": 0.8780487804878049,
        "support": 74.0
    },
    "1": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "2": {
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

## TF-IDF_ngram_SVM_Enhanced

- **Weighted F1 Score:** 0.7277
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
```json
{
    "0": {
        "precision": 0.8089887640449438,
        "recall": 0.972972972972973,
        "f1-score": 0.8834355828220859,
        "support": 74.0
    },
    "1": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "2": {
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

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7321
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "0": {
        "precision": 0.8181818181818182,
        "recall": 0.972972972972973,
        "f1-score": 0.8888888888888888,
        "support": 74.0
    },
    "1": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "2": {
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

## TF-IDF_ngram_KNN_Enhanced

- **Weighted F1 Score:** 0.7029
- **Accuracy:** 0.7500
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "0": {
        "precision": 0.8,
        "recall": 0.918918918918919,
        "f1-score": 0.8553459119496856,
        "support": 74.0
    },
    "1": {
        "precision": 0.2,
        "recall": 0.09090909090909091,
        "f1-score": 0.125,
        "support": 11.0
    },
    "2": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.3333333333333333,
        "recall": 0.3366093366093366,
        "f1-score": 0.32678197064989517,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6673913043478261,
        "recall": 0.75,
        "f1-score": 0.7029412770030079,
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
    "0": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "1": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "2": {
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
    "0": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "1": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "2": {
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

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.6841
- **Accuracy:** 0.7065
- **Best Parameters:** {'max_depth': 5}
```json
{
    "0": {
        "precision": 0.7974683544303798,
        "recall": 0.8513513513513513,
        "f1-score": 0.8235294117647058,
        "support": 74.0
    },
    "1": {
        "precision": 0.18181818181818182,
        "recall": 0.18181818181818182,
        "f1-score": 0.18181818181818182,
        "support": 11.0
    },
    "2": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.7065217391304348,
    "macro avg": {
        "precision": 0.3264288454161872,
        "recall": 0.3443898443898444,
        "f1-score": 0.33511586452762926,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6631810676940012,
        "recall": 0.7065217391304348,
        "f1-score": 0.6841432225063938,
        "support": 92.0
    }
}
```

## Word2Vec_KNN_Enhanced

- **Weighted F1 Score:** 0.6552
- **Accuracy:** 0.6739
- **Best Parameters:** {'n_neighbors': 5}
```json
{
    "0": {
        "precision": 0.782051282051282,
        "recall": 0.8243243243243243,
        "f1-score": 0.8026315789473685,
        "support": 74.0
    },
    "1": {
        "precision": 0.07142857142857142,
        "recall": 0.09090909090909091,
        "f1-score": 0.08,
        "support": 11.0
    },
    "2": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.6739130434782609,
    "macro avg": {
        "precision": 0.2844932844932845,
        "recall": 0.3050778050778051,
        "f1-score": 0.2942105263157895,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6375816212772734,
        "recall": 0.6739130434782609,
        "f1-score": 0.6551601830663616,
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
    "0": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "1": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "2": {
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
    "0": {
        "precision": 0.8043478260869565,
        "recall": 1.0,
        "f1-score": 0.891566265060241,
        "support": 74.0
    },
    "1": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "2": {
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

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7112
- **Accuracy:** 0.7283
- **Best Parameters:** {'max_depth': 5}
```json
{
    "0": {
        "precision": 0.810126582278481,
        "recall": 0.8648648648648649,
        "f1-score": 0.8366013071895425,
        "support": 74.0
    },
    "1": {
        "precision": 0.2857142857142857,
        "recall": 0.18181818181818182,
        "f1-score": 0.2222222222222222,
        "support": 11.0
    },
    "2": {
        "precision": 0.16666666666666666,
        "recall": 0.14285714285714285,
        "f1-score": 0.15384615384615385,
        "support": 7.0
    },
    "accuracy": 0.7282608695652174,
    "macro avg": {
        "precision": 0.4208358448864778,
        "recall": 0.3965133965133965,
        "f1-score": 0.4042232277526396,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6984662054144719,
        "recall": 0.7282608695652174,
        "f1-score": 0.7111941766673225,
        "support": 92.0
    }
}
```

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.7221
- **Accuracy:** 0.7826
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "0": {
        "precision": 0.8068181818181818,
        "recall": 0.9594594594594594,
        "f1-score": 0.8765432098765432,
        "support": 74.0
    },
    "1": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "2": {
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

