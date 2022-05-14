#  Source: https://github.com/adeviney/data-enrichment-project/blob/main/Distributions/Describing%20Distributions.ipynb 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn.preprocessing import StandardScaler
from scipy import stats


def plot_function(df, feature, figsize=(10, 6), kde=True,hist_kws={}):
    """Adapted from Source: https://github.com/adeviney/data-enrichment-project/blob/main/Distributions/Describing%20Distributions.ipynb

    Args:
        df (Frame): _description_
        feature (str): _description_
        figsize (tuple, optional): _description_. Defaults to (10, 6).
        kde (bool, optional): _description_. Defaults to True.
        hist_kws (dict, optional): _description_. Defaults to {}.

    Returns:
        _type_: _description_
        
    example usage:
    """
   
    
    fig = plt.figure(figsize=figsize)
    ax = sns.histplot(x=df[feature],kde=kde, **hist_kws)
    mean = df[feature].mean()
    median = df[feature].median()
    std = df[feature].std()
    
    ax.axvline(mean, color='r', label=f'Mean = {mean:,.2f}')
    ax.axvline(median, color='g', label=f'Median = {median:,.2f}')
    ax.axvline(mean-std, color = 'k', label = f'─1 StDev = {mean-std:,.2f}')
    ax.axvline(mean+std, color = 'k', label = f'+1 StDev = {mean+std:,.2f}')
    ax.axvspan(mean-std,mean+std,color = 'y',zorder = 0)
    ax.set_title(feature);
    ax.legend()
    
    
    # Question Answers
    print('Answers to Questions')
    print('1. Is it Discrete or Continuous?')
    if ((df.dtypes[feature] == 'float') & (df[feature].nunique()/ df[feature].count() > .90)):
        #probably continuous
        print("Continuous")
    else:
        print("Discrete")
    print('\n2. Does it have a skew? If so, which direction (+/-)')
    skew = round(stats.skew(df[feature]),1)
    skew_class = 'Normal; no skew' if skew == 0 else 'Negative Skew' if skew < 0 else 'Positive Skew'
    print(skew_class)
    
    print('\n3. What type of kurtosis does it display? (Mesokurtic, Leptokurtic, Platykurtic)')
    kurt_val = stats.kurtosis(df[feature], fisher = False)
    kurt_class = 'Mesokurtic' if round(kurt_val,1) == 3 else 'Leptokurtic' if kurt_val > 3 else 'Platykurtic'
    print(f'kurtosis = {kurt_val:.2f}, {kurt_class}')
    
    return fig, ax