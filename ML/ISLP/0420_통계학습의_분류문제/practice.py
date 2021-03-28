import pandas as pd
import numpy as np


df = pd.read_csv("./data/Smarket.csv", index_col=[0])


train_n = int(np.ceil(len(df) * 0.8))
df_range = np.arange(len(df))

train_index = np.random.choice(df_range, train_n, replace=False)
test_index = df_range[np.isin(df_range, train_index, invert=True)]

train_df = df.iloc[train_index, :]
test_df = df.iloc[test_index, :]

X_train = train_df[["Volume", "Today"]].to_numpy()
norm_X_train = (X_train - np.min(X_train, axis=0)) / (np.max(X_train, axis=0) - np.min(X_train, axis=0))

Y_train = train_df["Direction"].to_numpy()
Y_train = np.where(Y_train == "Up", 1, 0)

X_test = test_df[["Volume", "Today"]].to_numpy()
norm_X_test = (X_test - np.min(X_test, axis=0)) / (np.max(X_test, axis=0) - np.min(X_test, axis=0))
Y_test = test_df["Direction"].to_numpy()
Y_test = np.where(Y_test == "Up", 1, 0)

print(norm_X_test.shape)
print(norm_X_test[0].shape)
print(norm_X_test[1:].shape)

squ = np.square(norm_X_test[1:] - norm_X_test[0])
distance = np.sqrt(squ[:, 0] + squ[:, 1])
print(distance[np.argsort(distance)[::-1][:5]])