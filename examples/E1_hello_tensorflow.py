"""
Example 1: Hello TensorFlow
Learn the basics of creating and manipulating tensors
"""

import tensorflow as tf

print("=" * 50)
print("EXAMPLE 1: Hello TensorFlow")
print("=" * 50)

# 1. Create a constant string tensor
hello = tf.constant("Hello, TensorFlow!")
print(f"\n1. String tensor: {hello}")

# 2. Create numerical tensors (different dimensions)
print("\n2. Numerical Tensors:")

# Scalar (0D) - single value
scalar = tf.constant(5)
print(f"   Scalar: {scalar} (shape: {scalar.shape})")

# Vector (1D) - list of numbers
vector = tf.constant([1, 2, 3, 4, 5])
print(f"   Vector: {vector} (shape: {vector.shape})")

# Matrix (2D) - grid of numbers
matrix = tf.constant([[1, 2, 3], [4, 5, 6]])
print(f"   Matrix:\n{matrix}\n   (shape: {matrix.shape})")

# 3. Perform basic operations
print("\n3. Basic Operations:")
sum_result = tf.reduce_sum(vector)
print(f"   Sum of [1,2,3,4,5] = {sum_result.numpy()}")

mean_result = tf.reduce_mean(tf.cast(vector, tf.float32))
print(f"   Mean of [1,2,3,4,5] = {mean_result.numpy():.2f}")

# 4. Element-wise operations
print("\n4. Element-wise Operations:")
a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])
addition = tf.add(a, b)
multiplication = tf.multiply(a, b)
print(f"   [1,2,3] + [4,5,6] = {addition.numpy()}")
print(f"   [1,2,3] × [4,5,6] = {multiplication.numpy()}")

print("\n" + "=" * 50)
print("✓ Example complete!")
print("=" * 50)