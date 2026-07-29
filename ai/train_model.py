import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

import joblib



data = pd.read_csv(
    "fertilizer_dataset.csv"
)



X = data[

[
"soil_ph",
"nitrogen",
"phosphorus",
"potassium",
"moisture",
"rainfall",
"temperature",
"previous_yield"
]

]



y = data[
"recommended_fertilizer"
]




X_train,X_test,y_train,y_test = train_test_split(

X,
y,
test_size=0.2,
random_state=42

)




model = RandomForestClassifier(

n_estimators=100

)




model.fit(

X_train,

y_train

)




prediction = model.predict(X_test)



accuracy = accuracy_score(

y_test,

prediction

)


print(
"Accuracy:",
accuracy
)



joblib.dump(

model,

"fertilizer_model.pkl"

)


print(
"Model Saved"
)
