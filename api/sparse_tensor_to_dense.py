st = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

st.indices, st.values, st.dense_shape

(<tf.Tensor 'SparseTensor_4/indices:0' shape=(2, 2) dtype=int64>,
 <tf.Tensor 'SparseTensor_4/values:0' shape=(2,) dtype=int32>,
 <tf.Tensor 'SparseTensor_4/dense_shape:0' shape=(2,) dtype=int64>)
 
 """
represents the dense tensor

[[1, 0, 0, 0]
 [0, 0, 2, 0]
 [0, 0, 0, 0]]
"""
 
 tf.sparse_tensor_to_dense(st)
 <tf.Tensor 'SparseToDense:0' shape=(3, 4) dtype=int32>

tf.sparse_to_dense(st.indices, st.dense_shape, st.values)
<tf.Tensor 'SparseToDense_1:0' shape=(3, 4) dtype=int32>
