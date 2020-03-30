import numpy as np
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

#TODO add documentation 

def vectorize_string(s):
    unique=sorted((set(s)))
    idx2char=np.array(unique)
    char2num={u:i for i, u in enumerate(unique)}
    new=[]
    for char in range(len(s)):
        new.append(char2num[s[char]])
    new=np.array(new)
    return new, idx2char

def get_batch(vectorized_string,seq_length,batch_size):
    n=vectorized_string.shape[0]-1
    idx=np.random.choice(n-seq_length,batch_size)
    inputs=[]
    outputs=[]
    for i in idx:
        input_batch=np.array(vectorized_string[i:(i+seq_length)])
        output_batch=np.array(vectorized_string[i+1:((i+seq_length)+1)])
        inputs.append(input_batch)
        outputs.append(output_batch)
    x_batch = np.reshape(inputs, [batch_size, seq_length])
    y_batch = np.reshape(outputs, [batch_size, seq_length])
    try: 
        correct=(batch_size,seq_length)
        assert(x_batch.shape==correct)
    except (AssertionError) as e:
        logger.error("{}".format(type(e)))
        raise
    return x_batch, y_batch