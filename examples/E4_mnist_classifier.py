"""
Example 4: MNIST Classifier
Train a network to recognize handwritten digits (0-9)
"""

import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

print("=" * 50)
print("EXAMPLE 4: MNIST Digit Classifier")
print("=" * 50)

# 1. Load and prepare data
print("\n1. Loading MNIST dataset...")
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print(f"   Training samples: {x_train.shape[0]}")
print(f"   Test samples: {x_test.shape[0]}")
print(f"   Image shape: {x_train.shape[1:]}")

# Normalize pixel values to 0-1
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

# Flatten images from 28x28 to 784
x_train_flat = x_train.reshape(-1, 28 * 28)
x_test_flat = x_test.reshape(-1, 28 * 28)
print(f"   ✓ Data prepared and normalized")

# 2. Build model
print("\n2. Building model...")
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
])
print("   ✓ Model created")

# 3. Compile
print("\n3. Compiling model...")
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 4. Train
print("\n4. Training model (this may take a minute)...")
history = model.fit(
    x_train_flat, y_train,
    batch_size=128,
    epochs=10,
    verbose=1,
    validation_split=0.1
)

# 5. Evaluate
print("\n5. Evaluating on test data...")
test_loss, test_accuracy = model.evaluate(x_test_flat, y_test, verbose=0)
print(f"   Test accuracy: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")

# 6. Make predictions
print("\n6. Making predictions...")
predictions = model.predict(x_test_flat[:5], verbose=0)
for i in range(5):
    pred_class = tf.argmax(predictions[i]).numpy()
    confidence = tf.reduce_max(predictions[i]).numpy()
    print(f"   Sample {i}: Predicted {pred_class} (confidence: {confidence:.2%})")

print("\n" + "=" * 50)
print("✓ Example complete!")
print("=" * 50)