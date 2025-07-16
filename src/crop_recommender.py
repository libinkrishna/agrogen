from sklearn.tree import DecisionTreeClassifier

def recommend_crop(data):
    print("Running crop recommendation model...")
    # Encode categorical 'soil_type' to numerical
    data['soil_type_encoded'] = data['soil_type'].astype('category').cat.codes
    X = data[['ph', 'nitrogen', 'phosphorus', 'potassium', 'soil_type_encoded']]
    y = data['yield'].astype('category').cat.codes

    model = DecisionTreeClassifier()
    model.fit(X, y)
    print("Model trained successfully on sample data.")
    return model
