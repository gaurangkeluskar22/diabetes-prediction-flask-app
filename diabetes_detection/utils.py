def json2Xtest(data):
    X_test = [
        data.get("Age"),
        data.get("Gender"),
        data.get("Polyuria"),
        data.get("Polydipsia"),
        data.get("SuddenWeightLoss"),
        data.get("Weakness"),
        data.get("Polyphagia"),
        data.get("GenitalThrush"),
        data.get("VisualBlurring"),
        data.get("Itching"),
        data.get("Irritability"),
        data.get("DelayedHealing"),
        data.get("PartialParesis"),
        data.get("MuscleStiffness"),
        data.get("Alopecia"),
        data.get("Obesity"),    
    ]
    X_test = [int(_) for _ in X_test]
    return [X_test]