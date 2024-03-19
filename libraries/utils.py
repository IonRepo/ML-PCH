import numpy             as np
import matplotlib.pyplot as plt
import multiprocessing   as mp
import re

from sklearn.model_selection import learning_curve
from sklearn.preprocessing   import StandardScaler

linewidth    = 0.5
footnotesize = 8


def xy_scaler(X_train, X_test, y_train):
    """Scales the data as z = (x - u) / s. The scalers are fitted with the train sets.

    Args:
        X_train (array-like): Training input samples.
        X_test  (array-like): Testing input samples.
        y_train (array-like): Target values.

    Returns:
        tuple: Tuple containing scaled training inputs, scaled testing inputs,
            scaled target values, and the scaler used for target scaling.
    """
    
    # Defining the standarizers
    X_scaler = StandardScaler()
    y_scaler = StandardScaler()

    # Fitting the scalers with the train sets
    if len(np.shape(X_train)) == 1:
        X_train = X_train.reshape(-1, 1)
    if len(np.shape(X_test)) == 1:
        X_test = X_test.reshape(-1, 1)
    X_scaler.fit(X_train)
    y_scaler.fit(y_train.reshape(-1, 1))

    # Standardizing the sets
    X_train = X_scaler.transform(X_train)
    X_test  = X_scaler.transform(X_test)
    y_train = np.ravel(y_scaler.transform(y_train.reshape(-1, 1)))
    return X_train, X_test, y_train, y_scaler


def y_descaler(y_list, y_scaler):
    """De-scales the data with the given scaler. A list of input data is de-scaled.

    Args:
        y_list (list): List of input data to be de-scaled.
        y_scaler (object): Scaler object used for scaling.

    Returns:
        list: List of de-scaled input data.
    """

    y_list_descaled = []
    for y_item in y_list:
            y_list_descaled.append(np.ravel(y_scaler.inverse_transform(np.array(y_item).reshape(-1, 1))))
    return y_list_descaled


def composition_concentration(structure):
    """Returns a list of strings: components of the formula (left) and their concentrations (right).
    It is indispensable that compounds start with a capital letter.

    Args:
        structure (str): Chemical structure formula.

    Returns:
        list: List containing the components of the formula and their concentrations.
    """

    composition   = []
    concentration = []

    components = re.findall('[A-Z][^A-Z]*', structure)
    for component in components:
        aux = re.split('(\d+)', component)
        composition.append(aux[0])
        if len(aux) > 1: concentration.append(aux[1])
        else:            concentration.append('1')
    return [' '.join(composition), ' '.join(concentration)]


def sign(coord_1, coord_2, coord_3):
    """Determines the orientation of three points (coord_1, coord_2, coord_3).

    Args:
        coord_1 (tuple): Coordinates of the first point.
        coord_2 (tuple): Coordinates of the second point.
        coord_3 (tuple): Coordinates of the third point.

    Returns:
        float: The sign of the orientation.
    """

    return (coord_1[0] - coord_3[0]) * (coord_2[1] - coord_3[1]) - (coord_2[0] - coord_3[0]) * (coord_1[1] - coord_3[1])


class Limits:
    """Class to update and access the limits of each variable.
    """

    upper = None
    lower = None

    def _init_(self):
        self.upper = None
        self.lower = None


def plot_learning_curve(estimator, figure_name, X, y, axes=None, ylim=None, cv=None,
                        n_jobs=mp.cpu_count(), dpi=400, scoring=None,
                        train_sizes=np.linspace(0.1, 1.0, 5),):
    """
    Generate 3 plots: the test and training learning curve, the training
    samples vs fit times curve, the fit times vs score curve.

    Parameters
    ----------
    estimator : estimator instance
        An estimator instance implementing `fit` and `predict` methods which
        will be cloned for each validation.

    title : str
        Title for the chart.

    X : array-like of shape (n_samples, n_features)
        Training vector, where ``n_samples`` is the number of samples and
        ``n_features`` is the number of features.

    y : array-like of shape (n_samples) or (n_samples, n_features)
        Target relative to ``X`` for classification or regression;
        None for unsupervised learning.

    axes : array-like of shape (3,), default=None
        Axes to use for plotting the curves.

    ylim : tuple of shape (2,), default=None
        Defines minimum and maximum y-values plotted, e.g. (ymin, ymax).

    cv : int, cross-validation generator or an iterable, default=None
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:

          - None, to use the default 5-fold cross-validation,
          - integer, to specify the number of folds.
          - :term:`CV splitter`,
          - An iterable yielding (train, test) splits as arrays of indices.

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`StratifiedKFold` used. If the estimator is not a classifier
        or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validators that can be used here.

    n_jobs : int or None, default=None
        Number of jobs to run in parallel.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    scoring : str or callable, default=None
        A str (see model evaluation documentation) or
        a scorer callable object / function with signature
        ``scorer(estimator, X, y)``.

    train_sizes : array-like of shape (n_ticks,)
        Relative or absolute numbers of training examples that will be used to
        generate the learning curve. If the ``dtype`` is float, it is regarded
        as a fraction of the maximum size of the training set (that is
        determined by the selected validation method), i.e. it has to be within
        (0, 1]. Otherwise it is interpreted as absolute sizes of the training
        sets. Note that for classification the number of samples usually have
        to be big enough to contain at least one sample from each class.
        (default: np.linspace(0.1, 1.0, 5))
    """

    train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(
        estimator,
        X,
        y,
        scoring=scoring,
        cv=cv,
        n_jobs=n_jobs,
        train_sizes=train_sizes,
        return_times=True,
    )
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores,   axis=1)
    test_scores_mean = np.mean(test_scores,   axis=1)
    test_scores_std = np.std(test_scores,     axis=1)
    fit_times_mean = np.mean(fit_times,       axis=1)
    fit_times_std = np.std(fit_times,         axis=1)

    # Plot learning curve
    
    fig = plt.figure(figsize=(5, 5))
    if ylim is not None:
        plt.ylim(*ylim)

    plt.grid()
    plt.fill_between(
        train_sizes,
        train_scores_mean - train_scores_std,
        train_scores_mean + train_scores_std,
        alpha=0.1,
        color='r',
    )
    plt.fill_between(
        train_sizes,
        test_scores_mean - test_scores_std,
        test_scores_mean + test_scores_std,
        alpha=0.1,
        color='g',
    )
    plt.plot(
        train_sizes, train_scores_mean, 'o-', color='r', label='Training score'
    )
    plt.plot(
        train_sizes, test_scores_mean, 'o-', color='g', label='Cross-validation score'
    )
    plt.xlabel('Training examples', fontsize=footnotesize)
    plt.ylabel('Loss ($\mu\mathregular{m^{-1}}$)',              fontsize=footnotesize)
    plt.tick_params(axis='x', labelsize=footnotesize)
    plt.tick_params(axis='y', labelsize=footnotesize)
    plt.legend(loc='best', fontsize=footnotesize)
    plt.savefig(figure_name, dpi=dpi, bbox_inches='tight')
    plt.show()

    # Plot n_samples vs fit_times
    
    fig = plt.figure(figsize=(5, 5))
    plt.grid()
    plt.plot(train_sizes, fit_times_mean, 'o-')
    plt.fill_between(
        train_sizes,
        fit_times_mean - fit_times_std,
        fit_times_mean + fit_times_std,
        alpha=0.1,
    )
    plt.xlabel('Training examples', fontsize=footnotesize)
    plt.ylabel('Fit times',         fontsize=footnotesize)
    plt.tick_params(axis='x', labelsize=footnotesize)
    plt.tick_params(axis='y', labelsize=footnotesize)
    #plt.legend(loc='best', fontsize=footnotesize)
    #plt.savefig(figure_name, dpi=dpi, bbox_inches='tight')
    plt.show()

    # Plot fit_time vs score
    
    fig = plt.figure(figsize=(5, 5))
    fit_time_argsort = fit_times_mean.argsort()
    fit_time_sorted = fit_times_mean[fit_time_argsort]
    test_scores_mean_sorted = test_scores_mean[fit_time_argsort]
    test_scores_std_sorted = test_scores_std[fit_time_argsort]
    plt.grid()
    plt.plot(fit_time_sorted, test_scores_mean_sorted, 'o-')
    plt.fill_between(
        fit_time_sorted,
        test_scores_mean_sorted - test_scores_std_sorted,
        test_scores_mean_sorted + test_scores_std_sorted,
        alpha=0.1,
    )
    plt.xlabel('Fit times', fontsize=footnotesize)
    plt.ylabel('Loss',      fontsize=footnotesize)
    plt.tick_params(axis='x', labelsize=footnotesize)
    plt.tick_params(axis='y', labelsize=footnotesize)
    #plt.legend(loc='best', fontsize=footnotesize)
    #plt.savefig(figure_name, dpi=dpi, bbox_inches='tight')
    plt.show()
    return train_sizes, train_scores, test_scores