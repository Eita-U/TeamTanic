import numpy as np
import pandas as pd

def load_data():
    test_df = pd.read_csv('titanic/test.csv')
    train_df = pd.read_csv('titanic/train.csv')
    return train_df, test_df

def data_clean(df):
    # Sex: male = 0, female = 1
    df[df['Sex'] == 'male'] = 0
    df[df['Sex'] == 'female'] = 1

    # Age

    # Fare

    # Cabin

    return df

if __name__ == "__main__":
    train_df, test_df = load_data()
    train_df = data_clean(train_df)