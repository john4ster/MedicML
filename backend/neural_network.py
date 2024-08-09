from torch import nn

# Class definition of the neural network in the pickled model
class NeuralNetwork(nn.Module):
  def __init__(self, input_size, hidden_size, num_classes):
      super(NeuralNetwork, self).__init__()
      self.linear1 = nn.Linear(input_size, hidden_size)
      self.relu1 = nn.ReLU()
      self.linear2 = nn.Linear(hidden_size, hidden_size)
      self.relu2 = nn.ReLU()
      self.linear3 = nn.Linear(hidden_size, num_classes)
  
  def forward(self, x):
      out = self.linear1(x)
      out = self.relu1(out)
      out = self.linear2(out)
      out = self.relu2(out)
      out = self.linear3(out)
      return out