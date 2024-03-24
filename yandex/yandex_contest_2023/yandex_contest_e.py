import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import numpy as np


df = pd.read_csv('train.csv')
scalar = StandardScaler()
min_max = MinMaxScaler()
# print(df)
# print(df["target"].unique())
# print(df.corr()["target"].abs().sort_values(ascending=False))

predictors = df.drop("target",axis=1)
target = np.array(df["target"])

predictors = scalar.fit_transform(predictors)
# print(predictors)
# predictors = pd.DataFrame(min_max.fit_transform(predictors), columns=predictors.columns)
# print(predictors)

# print(predictors.shape)
# print(target.shape)


X_train,X_test,Y_train,Y_test = train_test_split(predictors,target,test_size=0.15,random_state=0)
# print(X_train.shape, X_test.shape)
# print(Y_train.shape, Y_test.shape)

# # Logistic regression
# lr = LogisticRegression()
# lr.fit(X_train,Y_train)
# Y_pred_lr = lr.predict(X_test)
# score_lr = round(accuracy_score(Y_pred_lr, Y_test) * 100, 2)
# print("The accuracy score achieved using Logistic Regression is: "+str(score_lr)+" %")


# # Random forest
# max_accuracy = 0
# for x in range(500):
#     rf = RandomForestClassifier(random_state=x)
#     rf.fit(X_train,Y_train)
#     Y_pred_rf = rf.predict(X_test)
#     current_accuracy = round(accuracy_score(Y_pred_rf,Y_test) * 100, 2)
#     if(current_accuracy>max_accuracy):
#         max_accuracy = current_accuracy
#         best_x = x
        
# # print(max_accuracy)

# rf = RandomForestClassifier(random_state=best_x)
# rf.fit(X_train,Y_train)
# Y_pred_rf = rf.predict(X_test)

# score_rf = round(accuracy_score(Y_pred_rf,Y_test) * 100, 2)
# print("The accuracy score achieved using Decision Tree is: " + str(score_rf)+" %")


import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader


class ClassficationDataset(Dataset):
    def __init__(self, data, targets=None) -> None:
        super().__init__()
        self.data = data
        self.targets = targets

    def __len__(self):
        return self.data.shape[0]
    
    def __getitem__(self, idx):
        data = torch.tensor(self.data[idx], dtype=torch.float32)
        if self.targets is not None:
            target = torch.tensor(self.targets[idx], dtype=torch.float32)
            return data, target
        else:
            return data

class Classificator(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.layers = nn.Sequential(*[
            nn.Linear(16, 64),
            # nn.Sigmoid(),
            nn.ReLU(),
            nn.Linear(64, 128),
            # nn.Sigmoid(),
            nn.ReLU(),
            nn.Linear(128, 128),
            # nn.Sigmoid(),
            nn.ReLU(),
            nn.Linear(128, 1),
            nn.Sigmoid()
        ])
    
    def forward(self, x):
        return self.layers(x)
    
lr = 0.0001
epochs = 500
b_size = 64
device = (torch.device('cuda') if torch.cuda.is_available()
          else torch.device('cpu'))

train_dset = ClassficationDataset(X_train, targets=Y_train)
test_dset = ClassficationDataset(X_test, targets=Y_test)
train_loader = DataLoader(train_dset, batch_size=b_size, shuffle=True)
test_loader = DataLoader(test_dset, batch_size=b_size)
    
loss_func = nn.BCELoss()
model = Classificator().to(device=device)
optimizer = optim.Adam(
    params=model.parameters(), lr=lr, weight_decay=0.0005)

for e in range(epochs):
    model.train()
    losses = []
    train_accuracies = []
    for x, y in train_loader:
        x = x.to(device=device)
        y = y.to(device=device)[:, None]
        pred = model(x)
        loss = loss_func(pred, y)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        acc = (pred.round() == y).float().mean()
        losses.append(loss.detach().cpu())
        train_accuracies.append(acc.detach().cpu())

    val_accuracies = []
    with torch.no_grad():
        model.eval()
        for x, y in test_loader:
            x = x.to(device=device)
            y = y.to(device=device)
            pred = model(x)
            acc = (pred.round() == y).float().mean()
            val_accuracies.append(acc)

    mean_loss = torch.tensor(losses).mean().item()
    mean_train_acc = torch.tensor(train_accuracies).mean().item()
    mean_val_acc = torch.tensor(val_accuracies).mean().item()
    print(f'Epoch {e}: loss - {mean_loss}, train_acc - {mean_train_acc}, val_acc - {mean_val_acc}')

