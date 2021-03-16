# ML-Model-Deployment


Built ML model to predict whether a person can purchase car or not using predictors such as age, estimated salary, gender.

Used statsmodels library to build logistic regression.

To upload the model on server, used pickle library. Pickle library is used for serialization and un serialization of python oject to byte objects and byte objects to python objects respectively.

Flask framework  creat framework.

On server, we have 4 fields for userid, gender, age, estimated salary features to add.
once we fill all the required details, we can submit the buttons and can see on webpage whether a given person with aboove details can purchase a car or not.
