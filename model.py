import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

# ================================
# 1. LOAD DATA
# ================================
df = pd.read_csv('C:/Users/rishi_1rsw9tn/OneDrive/Documents/cricket-performance-predictor/data/cricket_players.csv')
print("✅ Data loaded!")
print(df.shape)

# ================================
# 2. CREATE TARGET VARIABLE
# ================================
def categorize_performance(avg):
    if avg >= 40:
        return 'Elite'
    elif avg >= 32:
        return 'Good'
    else:
        return 'Average'

df['performance'] = df['avg'].apply(categorize_performance)
print("\n✅ Performance categories created!")
print(df[['player', 'avg', 'performance']])

# ================================
# 3. PREPARE FEATURES
# ================================
features = ['matches', 'innings', 'runs', 'strike_rate', 
            'hundreds', 'fifties', 'highest_score', 'fours', 
            'sixes', 'not_outs']

X = df[features]
y = df['performance']

le = LabelEncoder()
y_encoded = le.fit_transform(y)
print("\n✅ Features prepared!")
print("Classes:", le.classes_)

# ================================
# 4. TRAIN TEST SPLIT
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)
print(f"\n✅ Train size: {len(X_train)}, Test size: {len(X_test)}")

# ================================
# 5. TRAIN RANDOM FOREST
# ================================
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
model.fit(X_train, y_train)
print("\n✅ Model trained!")

# ================================
# 6. EVALUATE MODEL
# ================================
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n🎯 Model Accuracy: {accuracy * 100:.1f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred,
      labels=np.unique(y_pred),
      target_names=le.classes_[np.unique(y_pred)]))

# ================================
# 7. FEATURE IMPORTANCE CHART
# ================================
importance_df = pd.DataFrame({
    'feature': features,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

plt.figure(figsize=(10, 6))
colors = sns.color_palette("husl", len(features))
plt.bar(importance_df['feature'], 
        importance_df['importance'], 
        color=colors)
plt.xticks(rotation=45, ha='right')
plt.title('🏏 Feature Importance - Random Forest', 
          fontsize=14, fontweight='bold')
plt.xlabel('Feature', fontsize=12)
plt.ylabel('Importance Score', fontsize=12)
plt.tight_layout()
plt.savefig('data/feature_importance.png', dpi=150)
plt.show()
print("✅ Feature importance chart saved!")

# ================================
# 8. CONFUSION MATRIX
# ================================
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=le.classes_,
            yticklabels=le.classes_)
plt.title('🎯 Confusion Matrix', fontsize=14, fontweight='bold')
plt.ylabel('Actual', fontsize=12)
plt.xlabel('Predicted', fontsize=12)
plt.tight_layout()
plt.savefig('data/confusion_matrix.png', dpi=150)
plt.show()
print("✅ Confusion matrix saved!")

# ================================
# 9. SAVE THE MODEL
# ================================
os.makedirs('data', exist_ok=True)
with open('data/cricket_model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('data/label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

print("\n✅ Model saved as cricket_model.pkl!")
print("\n🎉 Stage 3 Complete! Model is ready!")