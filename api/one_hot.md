Signature: tf.one_hot(indices, depth, on_value=None, off_value=None, axis=None, dtype=None, name=None)

Returns a one-hot tensor.

Examples
=========

Suppose that

```python
  indices = [0, 2, -1, 1]
  depth = 3
  on_value = 5.0
  off_value = 0.0
  axis = -1
```

Then output is `[4 x 3]`:

```python
  output =
  [5.0 0.0 0.0]  // one_hot(0)
  [0.0 0.0 5.0]  // one_hot(2)
  [0.0 0.0 0.0]  // one_hot(-1)
  [0.0 5.0 0.0]  // one_hot(1)
```

Suppose that

```python
  indices = [[0, 2], [1, -1]]
  depth = 3
  on_value = 1.0
  off_value = 0.0
  axis = -1
```

Then output is `[2 x 2 x 3]`:

```python
  output =
  [
    [1.0, 0.0, 0.0]  // one_hot(0)
    [0.0, 0.0, 1.0]  // one_hot(2)
  ][
    [0.0, 1.0, 0.0]  // one_hot(1)
    [0.0, 0.0, 0.0]  // one_hot(-1)
  ]
```

Using default values for `on_value` and `off_value`:

```python
  indices = [0, 1, 2]
  depth = 3
```

The output will be

```python
  output =
  [[1., 0., 0.],
   [0., 1., 0.],
   [0., 0., 1.]]
```
