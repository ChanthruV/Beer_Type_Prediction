def print_class_perf(y_preds, y_actuals, set_name=None, average='binary'):
    """Print the Accuracy and F1 score for the provided data

    Parameters
    ----------
    y_preds : Numpy Array
        Predicted target
    y_actuals : Numpy Array
        Actual target
    set_name : str
        Name of the set to be printed
    average : str
        Parameter  for F1-score averaging
    Returns
    -------
    """
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score

    print(f"Accuracy {set_name}: {accuracy_score(y_actuals, y_preds)}")



