# You can refer to "Q2.py" to complete this scripts

#import libraries
import numpy as np
from MyCifarNet import MyPyTorchMLP
import torch

## You can set logging_on=True to see some training logging information
## set logging_on=False, will not print such information and make the command window more clean.
## Also, you will only see the information you need to answer the question.
logging_on = False


validation_set_for_each_layer = []
epoch = 10
batch_size = 4
maxpool=(2, 2)
activation_type = "Relu"
layer_nums = [2, 3]
hidden_units = [
    [(6, 5), (16, 5)],
    [(32, 3), (64, 3), (128, 3)]
]

store_model = []
for layer_num, hidden_unit in zip(layer_nums, hidden_units):
    trainer = MyPyTorchMLP(epoch=epoch, batch_size=batch_size, hidden_layer_num=layer_num, hidden_unit_num_list=hidden_unit, maxpool=maxpool, activation_function=activation_type, logging_on=logging_on)
    trainer.train()

    validation_set_for_each_layer.append(trainer.best_validation_accuracy())
    store_model.append(trainer)

print("####################################################################################################")
for idx in range(len(validation_set_for_each_layer)):
    print("For the number of hidden layer {}, with hidden unit {}, the best validation accuracy is {}".
          format(layer_nums[idx], hidden_units[idx], validation_set_for_each_layer[idx]))

best_validation_idx = np.argmax(validation_set_for_each_layer)
best_test_accuracy = store_model[best_validation_idx].evaluation("test")
print("##################################################")
print("The accuracy of test set is {}".format(best_test_accuracy))
print("The corresponding hyper-parameter is hidden layer {}, with hidden unit {}".
          format(layer_nums[best_validation_idx], hidden_units[best_validation_idx]))
print("##################################################")

