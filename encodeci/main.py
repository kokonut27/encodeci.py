import random
import os

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z']

class encode:
  def __init__(self, string):
    self.string = str(string).lower()

  def encode(self):
    return self.string

encode("hiyo").encode()