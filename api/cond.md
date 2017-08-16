Example:

```python
  x = tf.constant(2)
  y = tf.constant(5)
  def f1(): return tf.multiply(x, 17)
  def f2(): return tf.add(y, 23)
  r = tf.cond(tf.less(x, y), f1, f2)
  # r is set to f1().
  # Operations in f2 (e.g., tf.add) are not executed.
```

```python
learning_rate = tf.cond(
            global_step < hparams.start_decay_step,
            lambda: tf.constant(hparams.learning_rate),
            lambda: tf.train.exponential_decay(
                hparams.learning_rate,
                (global_step - hparams.start_decay_step),
                hparams.decay_steps,
                hparams.decay_factor,
                staircase=True),
            name="learning_rate")
```
