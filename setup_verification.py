"""
Verification script - Run this to confirm TensorFlow is properly installed
"""
import sys

def verify_installation():
    print(" Verifying TensorFlow Installation...\n")
    
    # Check Python version
    print(f"✓ Python version: {sys.version}")
    if sys.version_info < (3, 8):
        print(" Python 3.8+ required")
        return False
    
    # Check TensorFlow
    try:
        import tensorflow as tf
        print(f" TensorFlow version: {tf.__version__}")
    except ImportError:
        print(" TensorFlow not installed")
        return False
    
    # Check NumPy
    try:
        import numpy as np
        print(f"✓ NumPy version: {np.__version__}")
    except ImportError:
        print(" NumPy not installed")
        return False
    
    # Check Matplotlib
    try:
        import matplotlib
        print(f" Matplotlib version: {matplotlib.__version__}")
    except ImportError:
        print(" Matplotlib not installed")
        return False
    
    # Test basic TensorFlow operation
    print("\n Testing basic operation...")
    try:
        tensor = tf.constant([1, 2, 3])
        result = tf.reduce_sum(tensor)
        print(f" Basic operation works: sum([1,2,3]) = {result.numpy()}")
    except Exception as e:
        print(f" Error: {e}")
        return False
    
    print("\n All checks passed! Ready to learn TensorFlow ")
    return True

if __name__ == "__main__":
    verify_installation()