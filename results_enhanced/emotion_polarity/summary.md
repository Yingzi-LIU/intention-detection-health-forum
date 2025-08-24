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
- **Best Parameters:** {'classifier__C': 10, 'classifier__kernel': 'linear'}
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

- **Weighted F1 Score:** 0.7602
- **Accuracy:** 0.8152
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8295454545454546,
        "recall": 0.9864864864864865,
        "f1-score": 0.9012345679012346,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.5,
        "recall": 0.09090909090909091,
        "f1-score": 0.15384615384615385,
        "support": 11.0
    },
    "positif": {
        "precision": 0.5,
        "recall": 0.14285714285714285,
        "f1-score": 0.2222222222222222,
        "support": 7.0
    },
    "accuracy": 0.8152173913043478,
    "macro avg": {
        "precision": 0.6098484848484849,
        "recall": 0.40675090675090675,
        "f1-score": 0.4257676479898702,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7650691699604744,
        "recall": 0.8152173913043478,
        "f1-score": 0.7602089268755935,
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

## TF-IDF_KNN_Enhanced

- **Weighted F1 Score:** 0.7277
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__n_neighbors': 5}
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

## BoW_KNN_Enhanced

- **Weighted F1 Score:** 0.7275
- **Accuracy:** 0.7935
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8089887640449438,
        "recall": 0.972972972972973,
        "f1-score": 0.8834355828220859,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 11.0
    },
    "positif": {
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

## TF-IDF_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7221
- **Accuracy:** 0.7609
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8095238095238095,
        "recall": 0.918918918918919,
        "f1-score": 0.8607594936708861,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "positif": {
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

## TF-IDF_ngram_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7189
- **Accuracy:** 0.7500
- **Best Parameters:** {'classifier__max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8170731707317073,
        "recall": 0.9054054054054054,
        "f1-score": 0.8589743589743589,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.09090909090909091,
        "f1-score": 0.14285714285714285,
        "support": 11.0
    },
    "positif": {
        "precision": 0.14285714285714285,
        "recall": 0.14285714285714285,
        "f1-score": 0.14285714285714285,
        "support": 7.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.4310878823073945,
        "recall": 0.3797238797238797,
        "f1-score": 0.38156288156288154,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7079356663131848,
        "recall": 0.75,
        "f1-score": 0.7188644688644689,
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

- **Weighted F1 Score:** 0.7029
- **Accuracy:** 0.7500
- **Best Parameters:** {'classifier__n_neighbors': 3}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8,
        "recall": 0.918918918918919,
        "f1-score": 0.8553459119496856,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.2,
        "recall": 0.09090909090909091,
        "f1-score": 0.125,
        "support": 11.0
    },
    "positif": {
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

## FastText_KNN_Enhanced

- **Weighted F1 Score:** 0.7221
- **Accuracy:** 0.7826
- **Best Parameters:** {'n_neighbors': 3}
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

## FastText_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.7119
- **Accuracy:** 0.7283
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.810126582278481,
        "recall": 0.8648648648648649,
        "f1-score": 0.8366013071895425,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.3333333333333333,
        "recall": 0.18181818181818182,
        "f1-score": 0.23529411764705882,
        "support": 11.0
    },
    "positif": {
        "precision": 0.14285714285714285,
        "recall": 0.14285714285714285,
        "f1-score": 0.14285714285714285,
        "support": 7.0
    },
    "accuracy": 0.7282608695652174,
    "macro avg": {
        "precision": 0.4287723528229857,
        "recall": 0.3965133965133965,
        "f1-score": 0.40491752256458136,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7023481929921115,
        "recall": 0.7282608695652174,
        "f1-score": 0.7119210002841716,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree_Enhanced

- **Weighted F1 Score:** 0.6985
- **Accuracy:** 0.7283
- **Best Parameters:** {'max_depth': 5}
```json
{
    "NA_CATEGORY": {
        "precision": 0.8024691358024691,
        "recall": 0.8783783783783784,
        "f1-score": 0.8387096774193549,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.2222222222222222,
        "recall": 0.18181818181818182,
        "f1-score": 0.2,
        "support": 11.0
    },
    "positif": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 7.0
    },
    "accuracy": 0.7282608695652174,
    "macro avg": {
        "precision": 0.3415637860082305,
        "recall": 0.3533988533988534,
        "f1-score": 0.34623655913978496,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6720343531937735,
        "recall": 0.7282608695652174,
        "f1-score": 0.6985273492286115,
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
    "NA_CATEGORY": {
        "precision": 0.782051282051282,
        "recall": 0.8243243243243243,
        "f1-score": 0.8026315789473685,
        "support": 74.0
    },
    "negatif": {
        "precision": 0.07142857142857142,
        "recall": 0.09090909090909091,
        "f1-score": 0.08,
        "support": 11.0
    },
    "positif": {
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

