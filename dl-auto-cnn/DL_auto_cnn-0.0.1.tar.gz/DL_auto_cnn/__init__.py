from keras.models import *
from keras.layers import *
def create_model():
  img_width=int(input('enter image width'))
  img_height=int(input('enter img height'))
  channels=int(input('enter no of color channels'))
  input_shape=(img_width,img_height,channels)
  
  units_dense=int(input('enter units for first dense layer:'))
  last_layer_units_dense=int(input('last layer dense units'))
  activation_last=str(input('activation for last layer:'))
  loss_function=str(input('enter the loss function'))
  opt_to_use=str(input('enter the optimizer to use:'))
  metric_to_use=str(input('metrics for the model:'))
 


  model=Sequential()
  model.add(Conv2D(32,3,input_shape=input_shape,activation='relu'))
  model.add(MaxPooling2D(2))
  model.add(Conv2D(32,3,activation='relu'))
  model.add(MaxPooling2D(2))

  model.add(Conv2D(32,3,activation='relu'))
  model.add(MaxPooling2D(2))
  model.add(Dropout(0.25))

  model.add(Flatten())

  model.add(Dense(units_dense,activation='relu'))
  model.add(Dropout(0.2))
  model.add(Dense(units_dense,activation='relu'))
  model.add(Dense(units_dense,activation='relu'))
  model.add(Dense(last_layer_units_dense,activation=activation_last))

  model.compile(loss=loss_function,optimizer=opt_to_use,metrics=[metric_to_use])
  print(model.summary())
  return model