```python
bias = tf.reshape(tf.nn.bias_add(conv, biases), tf.shape(conv))
```
