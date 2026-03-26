"""
Example 3: Building Your First Neural Network
Create and train a simple network
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np

print("=" * 50)
print("EXAMPLE 3: Simple Neural Network")
print("=" * 50)

# 1. Create sample data (synthetic)
print("\n1. Creating sample data...")
np.random.seed(42)
X_train = np.random.randn(100, 4)  # 100 samples, 4 features
y_train = np.random.randint(0, 2, 100)  # Binary labels (0 or 1)
print(f"   Training data shape: {X_train.shape}")
print(f"   Labels shape: {y_train.shape}")

# 2. Build the network
print("\n2. Building neural network...")
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(4,)),
    # Layer 1: 64 neurons, ReLU activation
    
    keras.layers.Dense(32, activation='relu'),
    # Layer 2: 32 neurons, ReLU activation
    
    keras.layers.Dense(1, activation='sigmoid')
    # Layer 3: 1 neuron, Sigmoid for binary classification
])

print("   Model architecture:")
model.summary()

# 3. Compile the model
print("\n3. Compiling model...")
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
print("   ✓ Model compiled")

# 4. Train the model
print("\n4. Training model...")
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=16,
    verbose=0
)
print(f"   Final training accuracy: {history.history['accuracy'][-1]:.4f}")

# 5. Make predictions
print("\n5. Making predictions...")
sample_input = np.random.randn(1, 4)
prediction = model.predict(sample_input, verbose=0)
print(f"   Sample input: {sample_input[0]}")
print(f"   Prediction: {prediction[0][0]:.4f}")
print(f"   Predicted class: {'Class 1' if prediction[0][0] > 0.5 else 'Class 0'}")

print("\n" + "=" * 50)
print("✓ Example complete!")
print("=" * 50)