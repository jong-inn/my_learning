# You can refer to "MyTorchMLP.py" to complete this scripts

import copy
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision
import torchvision.transforms as transforms


class Net(nn.Module):
    def __init__(self, hidden_layer_num=2, hidden_unit_num_list=[(6, 5), (16, 5)], maxpool=(2, 2), activation_function="Relu"):
        super().__init__()
        
        self.hidden_layer_num = hidden_layer_num
        self.hidden_unit_num_list = hidden_unit_num_list
        self.maxpool = maxpool
        self.activation_function = activation_function

        input_layer = []
        
        for idx in range(hidden_layer_num):
            # for the first hidden layer
            if idx == 0:
                input_layer.append(nn.Conv2d(3, self.hidden_unit_num_list[idx][0], self.hidden_unit_num_list[idx][1]))
            else:
                input_layer.append(nn.Conv2d(self.hidden_unit_num_list[idx-1][0], self.hidden_unit_num_list[idx][0], self.hidden_unit_num_list[idx][1]))
            
            # add an activation function after convolutional layer
            if self.activation_function.lower() == "sigmoid":
                input_layer.append(nn.Sigmoid())
            elif self.activation_function.lower() == "relu":
                input_layer.append(nn.ReLU())
            elif self.activation_function.lower() == "tanh":
                input_layer.append(nn.Tanh())
                
            # add a maxpool function after activation function
            input_layer.append(nn.MaxPool2d(*self.maxpool)) #
        
        # flatten the output
        input_layer.append(nn.Flatten())
        
        # add linear layers
        unit_list = [120, 84, 10]
        for idx in range(3):
            
            if idx == 0:
                start_dimension = 32
                for out_channels, kernel_size in self.hidden_unit_num_list:
                    start_dimension -= (kernel_size-1)
                    start_dimension //= self.maxpool[0]
                start_dimension = out_channels * start_dimension * start_dimension
                
                input_layer.append(nn.Linear(start_dimension, unit_list[idx])) #
            else:
                input_layer.append(nn.Linear(unit_list[idx-1], unit_list[idx])) #
            
            if idx == 2:
                input_layer.append(nn.ReLU())
            else:
                if self.activation_function.lower() == "sigmoid":
                    input_layer.append(nn.Sigmoid())
                elif self.activation_function.lower() == "relu":
                    input_layer.append(nn.ReLU())
                elif self.activation_function.lower() == "tanh":
                    input_layer.append(nn.Tanh())
        
        self.nn_stack = nn.Sequential(*input_layer)

    def forward(self, x):
        y = self.nn_stack(x)
        return y


class MyPyTorchMLP(nn.Module):
    def __init__(self, batch_size=4, lr=0.001, epoch=200, hidden_layer_num=2, hidden_unit_num_list=[(6, 5), (16, 5)], maxpool=(2, 2),
                 activation_function="Relu", check_continue_epoch=10, logging_on=False):
        super().__init__()
        
        assert hidden_layer_num == len(hidden_unit_num_list)
        assert len(maxpool) == 2 and maxpool[0] == maxpool[1]
        
        self.batch_size = batch_size
        self.lr = lr
        self.epoch = epoch
        self.hidden_layer_num = hidden_layer_num
        self.hidden_unit_num_list = hidden_unit_num_list
        self.maxpool = maxpool
        self.activation_function = activation_function
        self.check_continue_epoch = check_continue_epoch
        self.logging_on = logging_on


        # store the accuracy of the validation, which would be used in
        self.valid_accuracy = []

        # obtain the dataset for train, valid, test
        transform = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
            ]
        )

        dataset_train = torchvision.datasets.CIFAR10(
                        root='./data',
                        train=True,
                        download=True,
                        transform=transform
                    )

        dataset_test = torchvision.datasets.CIFAR10(
                        root='./data',
                        train=False,
                        download=True,
                        transform=transform
                    )

        # obtain the dataloader
        self.train_loader = DataLoader(
            dataset=dataset_train,
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=0,
            drop_last=True
        )

        self.test_loader = DataLoader(
            dataset=dataset_test,
            batch_size=self.batch_size,
            shuffle=False,
            num_workers=0,
            drop_last=False
        )

        # the instance of the network
        self.net = Net(hidden_layer_num=self.hidden_layer_num,
                       hidden_unit_num_list=self.hidden_unit_num_list,
                       maxpool=self.maxpool,
                       activation_function=self.activation_function)

        # initialize the best net for evaluating the data in test set
        self.net_best_validation = copy.deepcopy(self.net)

        # define the optimizer
        self.optimizer = optim.SGD(self.net.parameters(), lr=self.lr, momentum=0.9)

        # you will define your forward function
        self.criterion = nn.CrossEntropyLoss()

    def print_msg(self, message: str):
        if self.logging_on:
            print(message)

    def evaluation(self, type="valid"):
        if type == "valid":
            data_loader = self.test_loader
        else:
            data_loader = self.test_loader

        prediction = []
        ground_truth = []

        for i, data in enumerate(data_loader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # do not need to calculate the gradient
            with torch.no_grad():
                if type == "valid":
                    outputs = self.net(inputs)
                else:
                    outputs = self.net_best_validation(inputs)
                prediction_label = torch.max(outputs, 1)[1]
            prediction.append(prediction_label)
            ground_truth.append(labels)

        prediction = torch.cat(prediction, dim=0)
        ground_truth = torch.cat(ground_truth, dim=0)

        accuracy = ((prediction == ground_truth).sum() / ground_truth.shape[0]).item()

        return accuracy


    def stopping_criteria(self, check_continue_epoch=10):
        # You will implement the stopping_criteria
        # you can utilize the self.valid_accuracy
        # ------------------------------------------------------------------------------------------------------------
        # complete your code here
        recent_valid_accuracy = self.valid_accuracy[-check_continue_epoch:]
        # pass the stopping criteria unitl we get 10 valid accuracies
        if len(recent_valid_accuracy) <= 9:
            return False
        # round up
        recent_valid_accuracy = list(map(lambda x: round(x, 3), recent_valid_accuracy))
        
        count = 0
        for idx in range(len(recent_valid_accuracy)-1):
            if recent_valid_accuracy[idx] - recent_valid_accuracy[idx+1] == 0:
                count += 1
        
        if count == len(recent_valid_accuracy) - 1:
            return True
        else:
            return False
        # ------------------------------------------------------------------------------------------------------------

    def best_validation_accuracy(self):
        return max(self.valid_accuracy)


    def train(self):
        for epoch in range(self.epoch):  # loop over the dataset multiple times

            running_loss = 0.0
            for i, data in enumerate(self.train_loader, 0):
                # get the inputs; data is a list of [inputs, labels]
                inputs, labels = data

                # zero the parameter gradients
                self.optimizer.zero_grad()

                # forward + backward + optimize
                outputs = self.net(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()

                # print statistics
                running_loss += loss.item()
                if i % 2000 == 1999:  # print every 10 mini-batches
                    self.print_msg(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
                    running_loss = 0.0

            self.print_msg('Finished Training for Epoch {}'.format(epoch+1))

            # evaluate in validation set
            self.print_msg('Prepare for the evaluation on validation set')
            valid_accuracy = self.evaluation("valid")
            self.valid_accuracy.append(valid_accuracy)
            self.print_msg("The accuracy of validation set on Epoch {} is {}".format(epoch+1, valid_accuracy))

            # check whether it is the current best validation accuracy, if yes, save the net work
            if valid_accuracy == max(self.valid_accuracy):
                self.net_best_validation = copy.deepcopy(self.net)

            # apply stopping_criteria
            # self.stopping_criteria() returns a bool, if True, we will terminate the training procedure
            if self.stopping_criteria(self.check_continue_epoch):
                self.print_msg("Enter the stopping_criteria, the current number of epoch is {}".format(epoch))
                break
