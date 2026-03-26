"""
Example 2: Understanding Tensors
Deep dive into tensor shapes, dtypes, and operations
"""

import tensorflow as tf
import numpy as np

print("=" * 50)
print("EXAMPLE 2: Tensor Basics")
print("=" * 50)

# 1. Creating tensors from different sources
print("\n1. Creating Tensors:")

# From Python lists
tensor_from_list = tf.constant([[1, 2], [3, 4], [5, 6]])
print(f"   From list:\n{tensor_from_list}")

# From NumPy arrays
np_array = np.array([1, 2, 3, 4, 5])
tensor_from_numpy = tf.constant(np_array)
print(f"\n   From NumPy: {tensor_from_numpy}")

# Special tensors
zeros = tf.zeros((2, 3))
ones = tf.ones((2, 3))
print(f"\n   Zeros (2x3):\n{zeros}")
print(f"   Ones (2x3):\n{ones}")

# 2. Tensor properties
print("\n2. Tensor Properties:")
sample_tensor = tf.constant([[1.5, 2.5], [3.5, 4.5], [5.5, 6.5]])
print(f"   Shape: {sample_tensor.shape}")
print(f"   Data type: {sample_tensor.dtype}")
print(f"   Number of dimensions: {len(sample_tensor.shape)}")
print(f"   Total elements: {tf.size(sample_tensor).numpy()}")

# 3. Reshaping tensors
print("\n3. Reshaping Tensors:")
original = tf.constant([1, 2, 3, 4, 5, 6])
print(f"   Original shape: {original.shape} → {original}")

reshaped_2x3 = tf.reshape(original, (2, 3))
print(f"   Reshaped to (2,3):\n{reshaped_2x3}")

reshaped_3x2 = tf.reshape(original, (3, 2))
print(f"   Reshaped to (3,2):\n{reshaped_3x2}")

# 4. Data type conversion
print("\n4. Data Type Conversion:")
int_tensor = tf.constant([1, 2, 3])
print(f"   Original (int32): {int_tensor} dtype: {int_tensor.dtype}")

float_tensor = tf.cast(int_tensor, tf.float32)
print(f"   Cast to float32: {float_tensor} dtype: {float_tensor.dtype}")

print("\n" + "=" * 50)
print("✓ Example complete!")
print("=" * 50)