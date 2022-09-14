import numpy as np
import tensorflow as tf
from tensorflow.keras import models
import tensorflow as tf
from tensorflow.keras import models
import ModelgradCam
import ModelpreprocessImg


def predict(array): 
    
    batch_array_img = ModelpreprocessImg.preprocess(array)
    
    ## UPLOAD MODEL  ##################################
    modelo = model()

    prediction = np.argmax(modelo.predict(batch_array_img))
    
    Tests = np.max(modelo.predict(batch_array_img))*100
    label = ''
    if prediction == 0:
        label = 'bacteriana'
    if prediction == 1:
        label = 'normal'
    if prediction == 2:
        label = 'viral'
    
    
    
    heatmap = ModelgradCam.grad_cam(array)
    return(label, Tests, heatmap)

## MODEL COMPILATED

def model():
    model_cnn = tf.keras.models.load_model('WilhemNet_86.h5')
    return model_cnn
