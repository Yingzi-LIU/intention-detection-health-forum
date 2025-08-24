# Experiment Results Summary

**Labels:** non, oui

## TF-IDF_ngram_DecisionTree

- **Weighted F1 Score:** 0.7833
- **Accuracy:** 0.8043
- **Best Parameters:** {'max_depth': 10}
```json
{
    "non": {
        "precision": 0.8395061728395061,
        "recall": 0.9315068493150684,
        "f1-score": 0.8831168831168831,
        "support": 73.0
    },
    "oui": {
        "precision": 0.5454545454545454,
        "recall": 0.3157894736842105,
        "f1-score": 0.4,
        "support": 19.0
    },
    "accuracy": 0.8043478260869565,
    "macro avg": {
        "precision": 0.6924803591470258,
        "recall": 0.6236481614996394,
        "f1-score": 0.6415584415584416,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7787781193578295,
        "recall": 0.8043478260869565,
        "f1-score": 0.7833427442123093,
        "support": 92.0
    }
}
```

## TF-IDF_DecisionTree

- **Weighted F1 Score:** 0.7593
- **Accuracy:** 0.7826
- **Best Parameters:** {'max_depth': 10}
```json
{
    "non": {
        "precision": 0.8271604938271605,
        "recall": 0.9178082191780822,
        "f1-score": 0.8701298701298701,
        "support": 73.0
    },
    "oui": {
        "precision": 0.45454545454545453,
        "recall": 0.2631578947368421,
        "f1-score": 0.3333333333333333,
        "support": 19.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.6408529741863075,
        "recall": 0.5904830569574622,
        "f1-score": 0.6017316017316017,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7502073878885472,
        "recall": 0.782608695652174,
        "f1-score": 0.759269715791455,
        "support": 92.0
    }
}
```

## Bert_LogisticRegression

- **Weighted F1 Score:** 0.7500
- **Accuracy:** 0.7609
- **Best Parameters:** {'C': 1, 'solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.8311688311688312,
        "recall": 0.8767123287671232,
        "f1-score": 0.8533333333333334,
        "support": 73.0
    },
    "oui": {
        "precision": 0.4,
        "recall": 0.3157894736842105,
        "f1-score": 0.35294117647058826,
        "support": 19.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.6155844155844157,
        "recall": 0.5962509012256669,
        "f1-score": 0.6031372549019608,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7421230942970074,
        "recall": 0.7608695652173914,
        "f1-score": 0.7499914748508099,
        "support": 92.0
    }
}
```

## BoW_LogisticRegression

- **Weighted F1 Score:** 0.7482
- **Accuracy:** 0.7935
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.813953488372093,
        "recall": 0.958904109589041,
        "f1-score": 0.8805031446540881,
        "support": 73.0
    },
    "oui": {
        "precision": 0.5,
        "recall": 0.15789473684210525,
        "f1-score": 0.24,
        "support": 19.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.6569767441860466,
        "recall": 0.5583994232155731,
        "f1-score": 0.560251572327044,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7491152679474216,
        "recall": 0.7934782608695652,
        "f1-score": 0.7482253213016135,
        "support": 92.0
    }
}
```

## BoW_MultinomialNB

- **Weighted F1 Score:** 0.7482
- **Accuracy:** 0.7935
- **Best Parameters:** {'alpha': 1.0}
```json
{
    "non": {
        "precision": 0.813953488372093,
        "recall": 0.958904109589041,
        "f1-score": 0.8805031446540881,
        "support": 73.0
    },
    "oui": {
        "precision": 0.5,
        "recall": 0.15789473684210525,
        "f1-score": 0.24,
        "support": 19.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.6569767441860466,
        "recall": 0.5583994232155731,
        "f1-score": 0.560251572327044,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7491152679474216,
        "recall": 0.7934782608695652,
        "f1-score": 0.7482253213016135,
        "support": 92.0
    }
}
```

## TF-IDF_LogisticRegression

- **Weighted F1 Score:** 0.7482
- **Accuracy:** 0.7935
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.813953488372093,
        "recall": 0.958904109589041,
        "f1-score": 0.8805031446540881,
        "support": 73.0
    },
    "oui": {
        "precision": 0.5,
        "recall": 0.15789473684210525,
        "f1-score": 0.24,
        "support": 19.0
    },
    "accuracy": 0.7934782608695652,
    "macro avg": {
        "precision": 0.6569767441860466,
        "recall": 0.5583994232155731,
        "f1-score": 0.560251572327044,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7491152679474216,
        "recall": 0.7934782608695652,
        "f1-score": 0.7482253213016135,
        "support": 92.0
    }
}
```

## Bert_SVM

- **Weighted F1 Score:** 0.7432
- **Accuracy:** 0.7609
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.8227848101265823,
        "recall": 0.8904109589041096,
        "f1-score": 0.8552631578947368,
        "support": 73.0
    },
    "oui": {
        "precision": 0.38461538461538464,
        "recall": 0.2631578947368421,
        "f1-score": 0.3125,
        "support": 19.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.6037000973709835,
        "recall": 0.5767844268204758,
        "f1-score": 0.5838815789473684,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7322932983362264,
        "recall": 0.7608695652173914,
        "f1-score": 0.7431707665903889,
        "support": 92.0
    }
}
```

## BoW_DecisionTree

- **Weighted F1 Score:** 0.7407
- **Accuracy:** 0.7826
- **Best Parameters:** {'max_depth': 10}
```json
{
    "non": {
        "precision": 0.8117647058823529,
        "recall": 0.9452054794520548,
        "f1-score": 0.8734177215189873,
        "support": 73.0
    },
    "oui": {
        "precision": 0.42857142857142855,
        "recall": 0.15789473684210525,
        "f1-score": 0.23076923076923078,
        "support": 19.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.6201680672268908,
        "recall": 0.55155010814708,
        "f1-score": 0.5520934761441091,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7326269638290099,
        "recall": 0.782608695652174,
        "f1-score": 0.7406968375597984,
        "support": 92.0
    }
}
```

## Bert_DecisionTree

- **Weighted F1 Score:** 0.7336
- **Accuracy:** 0.7391
- **Best Parameters:** {'max_depth': None}
```json
{
    "non": {
        "precision": 0.8266666666666667,
        "recall": 0.8493150684931506,
        "f1-score": 0.8378378378378378,
        "support": 73.0
    },
    "oui": {
        "precision": 0.35294117647058826,
        "recall": 0.3157894736842105,
        "f1-score": 0.3333333333333333,
        "support": 19.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.5898039215686275,
        "recall": 0.5825522710886806,
        "f1-score": 0.5855855855855856,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7288320545609548,
        "recall": 0.7391304347826086,
        "f1-score": 0.7336466901684292,
        "support": 92.0
    }
}
```

## Bert_KNN

- **Weighted F1 Score:** 0.7336
- **Accuracy:** 0.7391
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "non": {
        "precision": 0.8266666666666667,
        "recall": 0.8493150684931506,
        "f1-score": 0.8378378378378378,
        "support": 73.0
    },
    "oui": {
        "precision": 0.35294117647058826,
        "recall": 0.3157894736842105,
        "f1-score": 0.3333333333333333,
        "support": 19.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.5898039215686275,
        "recall": 0.5825522710886806,
        "f1-score": 0.5855855855855856,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7288320545609548,
        "recall": 0.7391304347826086,
        "f1-score": 0.7336466901684292,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_LogisticRegression

- **Weighted F1 Score:** 0.7287
- **Accuracy:** 0.7826
- **Best Parameters:** {'C': 10, 'solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.8045977011494253,
        "recall": 0.958904109589041,
        "f1-score": 0.875,
        "support": 73.0
    },
    "oui": {
        "precision": 0.4,
        "recall": 0.10526315789473684,
        "f1-score": 0.16666666666666666,
        "support": 19.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.6022988505747127,
        "recall": 0.5320836337418889,
        "f1-score": 0.5208333333333334,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7210394802598701,
        "recall": 0.782608695652174,
        "f1-score": 0.7287137681159421,
        "support": 92.0
    }
}
```

## FastText_KNN

- **Weighted F1 Score:** 0.7275
- **Accuracy:** 0.7500
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "non": {
        "precision": 0.8125,
        "recall": 0.8904109589041096,
        "f1-score": 0.8496732026143791,
        "support": 73.0
    },
    "oui": {
        "precision": 0.3333333333333333,
        "recall": 0.21052631578947367,
        "f1-score": 0.25806451612903225,
        "support": 19.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.5729166666666666,
        "recall": 0.5504686373467916,
        "f1-score": 0.5538688593717056,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7135416666666666,
        "recall": 0.75,
        "f1-score": 0.7274931477967531,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_KNN

- **Weighted F1 Score:** 0.7258
- **Accuracy:** 0.7609
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "non": {
        "precision": 0.8072289156626506,
        "recall": 0.9178082191780822,
        "f1-score": 0.8589743589743589,
        "support": 73.0
    },
    "oui": {
        "precision": 0.3333333333333333,
        "recall": 0.15789473684210525,
        "f1-score": 0.21428571428571427,
        "support": 19.0
    },
    "accuracy": 0.7608695652173914,
    "macro avg": {
        "precision": 0.570281124497992,
        "recall": 0.5378514780100937,
        "f1-score": 0.5366300366300366,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.70935917583377,
        "recall": 0.7608695652173914,
        "f1-score": 0.7258321388756171,
        "support": 92.0
    }
}
```

## TF-IDF_SVM

- **Weighted F1 Score:** 0.7198
- **Accuracy:** 0.7391
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.810126582278481,
        "recall": 0.8767123287671232,
        "f1-score": 0.8421052631578947,
        "support": 73.0
    },
    "oui": {
        "precision": 0.3076923076923077,
        "recall": 0.21052631578947367,
        "f1-score": 0.25,
        "support": 19.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.5589094449853944,
        "recall": 0.5436193222782985,
        "f1-score": 0.5460526315789473,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.706362982092206,
        "recall": 0.7391304347826086,
        "f1-score": 0.7198226544622426,
        "support": 92.0
    }
}
```

## TF-IDF_KNN

- **Weighted F1 Score:** 0.7185
- **Accuracy:** 0.7500
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "non": {
        "precision": 0.8048780487804879,
        "recall": 0.9041095890410958,
        "f1-score": 0.8516129032258064,
        "support": 73.0
    },
    "oui": {
        "precision": 0.3,
        "recall": 0.15789473684210525,
        "f1-score": 0.20689655172413793,
        "support": 19.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.552439024390244,
        "recall": 0.5310021629416005,
        "f1-score": 0.5292547274749722,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.7006097560975609,
        "recall": 0.75,
        "f1-score": 0.7184649610678532,
        "support": 92.0
    }
}
```

## BoW_SVM

- **Weighted F1 Score:** 0.7111
- **Accuracy:** 0.7391
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.8024691358024691,
        "recall": 0.8904109589041096,
        "f1-score": 0.8441558441558441,
        "support": 73.0
    },
    "oui": {
        "precision": 0.2727272727272727,
        "recall": 0.15789473684210525,
        "f1-score": 0.2,
        "support": 19.0
    },
    "accuracy": 0.7391304347826086,
    "macro avg": {
        "precision": 0.5375982042648709,
        "recall": 0.5241528478731075,
        "f1-score": 0.522077922077922,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6930659249499829,
        "recall": 0.7391304347826086,
        "f1-score": 0.7111236589497459,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_SVM

- **Weighted F1 Score:** 0.7038
- **Accuracy:** 0.7283
- **Best Parameters:** {'C': 10, 'kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.8,
        "recall": 0.8767123287671232,
        "f1-score": 0.8366013071895425,
        "support": 73.0
    },
    "oui": {
        "precision": 0.25,
        "recall": 0.15789473684210525,
        "f1-score": 0.1935483870967742,
        "support": 19.0
    },
    "accuracy": 0.7282608695652174,
    "macro avg": {
        "precision": 0.525,
        "recall": 0.5173035328046143,
        "f1-score": 0.5150748471431583,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6864130434782609,
        "recall": 0.7282608695652174,
        "f1-score": 0.7037968997790796,
        "support": 92.0
    }
}
```

## TF-IDF_ngram_MultinomialNB

- **Weighted F1 Score:** 0.7021
- **Accuracy:** 0.7935
- **Best Parameters:** {'alpha': 0.5}
```json
{
    "non": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "micro avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "macro avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "weighted avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    }
}
```

## Word2Vec_LogisticRegression

- **Weighted F1 Score:** 0.7021
- **Accuracy:** 0.7935
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "micro avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "macro avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "weighted avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    }
}
```

## Word2Vec_SVM

- **Weighted F1 Score:** 0.7021
- **Accuracy:** 0.7935
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "micro avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "macro avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "weighted avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    }
}
```

## FastText_LogisticRegression

- **Weighted F1 Score:** 0.7021
- **Accuracy:** 0.7935
- **Best Parameters:** {'C': 0.1, 'solver': 'liblinear'}
```json
{
    "non": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "micro avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "macro avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "weighted avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    }
}
```

## FastText_SVM

- **Weighted F1 Score:** 0.7021
- **Accuracy:** 0.7935
- **Best Parameters:** {'C': 0.1, 'kernel': 'linear'}
```json
{
    "non": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "micro avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "macro avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    },
    "weighted avg": {
        "precision": 0.7934782608695652,
        "recall": 1.0,
        "f1-score": 0.8848484848484849,
        "support": 73.0
    }
}
```

## BoW_KNN

- **Weighted F1 Score:** 0.6967
- **Accuracy:** 0.7826
- **Best Parameters:** {'n_neighbors': 3}
```json
{
    "non": {
        "precision": 0.7912087912087912,
        "recall": 0.9863013698630136,
        "f1-score": 0.8780487804878049,
        "support": 73.0
    },
    "oui": {
        "precision": 0.0,
        "recall": 0.0,
        "f1-score": 0.0,
        "support": 19.0
    },
    "accuracy": 0.782608695652174,
    "macro avg": {
        "precision": 0.3956043956043956,
        "recall": 0.4931506849315068,
        "f1-score": 0.43902439024390244,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6278069756330626,
        "recall": 0.782608695652174,
        "f1-score": 0.696712619300106,
        "support": 92.0
    }
}
```

## TF-IDF_MultinomialNB

- **Weighted F1 Score:** 0.6952
- **Accuracy:** 0.7500
- **Best Parameters:** {'alpha': 0.1}
```json
{
    "non": {
        "precision": 0.7906976744186046,
        "recall": 0.9315068493150684,
        "f1-score": 0.8553459119496856,
        "support": 73.0
    },
    "oui": {
        "precision": 0.16666666666666666,
        "recall": 0.05263157894736842,
        "f1-score": 0.08,
        "support": 19.0
    },
    "accuracy": 0.75,
    "macro avg": {
        "precision": 0.4786821705426356,
        "recall": 0.4920692141312184,
        "f1-score": 0.46767295597484276,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6618217054263565,
        "recall": 0.75,
        "f1-score": 0.6952201257861637,
        "support": 92.0
    }
}
```

## Word2Vec_DecisionTree

- **Weighted F1 Score:** 0.6801
- **Accuracy:** 0.7065
- **Best Parameters:** {'max_depth': 5}
```json
{
    "non": {
        "precision": 0.7875,
        "recall": 0.863013698630137,
        "f1-score": 0.8235294117647058,
        "support": 73.0
    },
    "oui": {
        "precision": 0.16666666666666666,
        "recall": 0.10526315789473684,
        "f1-score": 0.12903225806451613,
        "support": 19.0
    },
    "accuracy": 0.7065217391304348,
    "macro avg": {
        "precision": 0.4770833333333333,
        "recall": 0.4841384282624369,
        "f1-score": 0.476280834914611,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.659284420289855,
        "recall": 0.7065217391304348,
        "f1-score": 0.6801006517614059,
        "support": 92.0
    }
}
```

## Word2Vec_KNN

- **Weighted F1 Score:** 0.6744
- **Accuracy:** 0.6848
- **Best Parameters:** {'n_neighbors': 7}
```json
{
    "non": {
        "precision": 0.7894736842105263,
        "recall": 0.821917808219178,
        "f1-score": 0.8053691275167785,
        "support": 73.0
    },
    "oui": {
        "precision": 0.1875,
        "recall": 0.15789473684210525,
        "f1-score": 0.17142857142857143,
        "support": 19.0
    },
    "accuracy": 0.6847826086956522,
    "macro avg": {
        "precision": 0.48848684210526316,
        "recall": 0.4899062725306417,
        "f1-score": 0.488398849472675,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6651530320366134,
        "recall": 0.6847826086956522,
        "f1-score": 0.674446621368127,
        "support": 92.0
    }
}
```

## FastText_DecisionTree

- **Weighted F1 Score:** 0.6520
- **Accuracy:** 0.6630
- **Best Parameters:** {'max_depth': None}
```json
{
    "non": {
        "precision": 0.7763157894736842,
        "recall": 0.8082191780821918,
        "f1-score": 0.7919463087248322,
        "support": 73.0
    },
    "oui": {
        "precision": 0.125,
        "recall": 0.10526315789473684,
        "f1-score": 0.11428571428571428,
        "support": 19.0
    },
    "accuracy": 0.6630434782608695,
    "macro avg": {
        "precision": 0.4506578947368421,
        "recall": 0.4567411679884643,
        "f1-score": 0.45311601150527325,
        "support": 92.0
    },
    "weighted avg": {
        "precision": 0.6418049199084668,
        "recall": 0.6630434782608695,
        "f1-score": 0.6519946642211013,
        "support": 92.0
    }
}
```

