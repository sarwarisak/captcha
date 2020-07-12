#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastai.vision import *


# In[2]:


def crack(fname):
    decoding_dict={0: '-',
     1: 'A',
     2: 'F',
     3: 'M',
     4: 'P',
     5: 'S',
     6: 'X',
     7: 'a',
     8: 'b',
     9: 'c',
     10: 'd',
     11: 'e',
     12: 'f',
     13: 'g',
     14: 'h',
     15: 'i',
     16: 'j',
     17: 'k',
     18: 'l',
     19: 'm',
     20: 'n',
     21: 'o',
     22: 'p',
     23: 'q',
     24: 'r',
     25: 's',
     26: 't',
     27: 'u',
     28: 'v',
     29: 'w',
     30: 'x',
     31: 'y',
     32: 'z'}

    code_dimension = 33
    captcha_dimension = 7
    def decode(onehot):
        onehot = onehot.reshape(code_dimension, captcha_dimension)
        idx = np.argmax(onehot, axis=0)
        return [decoding_dict[i.item()] for i in idx]

    path=Path('ml_files')

    learn2=load_learner(path,"1_export.pkl")



    img = open_image('static/'+fname)
    #img

    defaults.device = torch.device('cpu')
    pred_class,pred_idx,outputs = learn2.predict(img)

    ll=decode(pred_idx)
    st=""
    for i in ll:
        st=st+i
    return(st)


# In[ ]:




