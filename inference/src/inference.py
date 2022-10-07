from concurrent import futures

import numpy as np

import grpc
import cv2

import tensorflow as tf
from tensorflow.keras import models

import inference_pb2
import inference_pb2_grpc


class InferenceService(inference_pb2_grpc.inferenceServicer):
    def _read_img(self, path):
    
        img = cv2.imread(path)
        img_array = np.asarray(img)
        img2 = img_array.astype(float) 
        img2 = (np.maximum(img2,0) / img2.max()) * 255.0
        img2 = np.uint8(img2)
    
        return img2

    def predict(self, request, context):
        # load the image from disk
        path = request.path
 
        arreglo = self._read_img(path=path)
        
        
        batch_array_img = self.preprocess(arreglo)
    
        ## UPLOAD MODEL  ##################################
        modelo = self.model()
        
        prediction = np.argmax(modelo.predict(batch_array_img))
    
        flt_percent = np.max(modelo.predict(batch_array_img))*100
        str_dataresult = ''
        if prediction == 0:
            str_dataresult = 'bacteriana'
        if prediction == 1:
            str_dataresult = 'normal'
        if prediction == 2:
            str_dataresult = 'viral'
        
       
        response_message = inference_pb2.datapred(percent = flt_percent, dataresult = str_dataresult)
        return response_message
    
    def preprocess(self, array):
        array = cv2.resize(array , (512 , 512))
        array = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4,4))
        array = clahe.apply(array)
        array = array/255
        array = np.expand_dims(array,axis=-1)
        array = np.expand_dims(array,axis=0)
        return array
        
    def model(self):
        model_cnn = tf.keras.models.load_model('WilhemNet_86.h5')
        return model_cnn

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inference_pb2_grpc.add_inferenceServicer_to_server(InferenceService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
