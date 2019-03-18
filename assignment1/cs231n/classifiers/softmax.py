import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]
  num_class = W.shape[1]

  for i in range(num_train):
    f = X[i].dot(W)
    f -= np.max(f)

    loss += -np.log(np.exp(f[y[i]]) / np.sum(np.exp(f)))

    for j in range(num_class):
      score = np.exp(f[j]) / np.sum(np.exp(f))

      if j == y[i]:
        dW[:, j] += (score - 1) * X[i]
      else:
        dW[:, j] += score * X[i]

  loss /= num_train
  loss += reg * np.sum(W * W)

  dW /= num_train
  dW += 2 * reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]

  f = X.dot(W)
  f -= np.max(f)
  f = np.exp(f)
  f_sum = np.sum(f, axis = 1)

  loss = -np.sum(np.log(f[range(num_train), y] / f_sum)) / num_train
  loss += reg * np.sum(W * W)

  d = f / f_sum.reshape(num_train, 1)
  d[range(num_train), y] = -(f_sum - f[range(num_train), y]) / f_sum

  dW = np.dot(X.T, d)
  dW /= num_train
  dW += 2 * reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW
