import numpy as np
import pickle
loaded_model=pickle.load(open('c:/Users/HP/Downloads/trained_model.sav','rb'))
input_data=(1,189,60,23,846,30.1,0.398,59)
#changing to numpy array
input_array_data=np.asarray(input_data)
#reshape the array that we are using only 1 datapoint not 768 values
input_data_reshaped=input_array_data.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==0):
  print('the person is not diabetic')
else:
  print('the person is diabetic')