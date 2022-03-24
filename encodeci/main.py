import random
import os

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z']

class encode:
  """
  Holds the `encode` class. Encrypts the string using commmon ciphers or made up encrytions - the common ciphers being Atbash and Caesar ciphers.
  """
  def __init__(self, string):
    self.string = str(string).lower()
    self.length = len(self.string)
    self.new_string = ""

  def encode(self, type_code=None, movement=None):
    if type_code == None:
      type_code = random.choice(['caesar', 'atbash']) # atbash and caesar being most common to encrypt with.

      if type_code == 'caesar':
        for x in range(self.length):
          char = self.string[x]
          self.new_string += chr((ord(char) + int(movement) - 97) % 26 + 97)
      elif type_code == 'atbash':
        pass
    elif movement == None:
      raise Exception("'movement' args is required!")
    elif type(movement)!= int:
      raise Exception("'movement' args must be an integer!")
    elif type_code == 'caesar':
      for x in range(self.length):
        char = self.string[x]
        self.new_string += chr((ord(char) + int(movement) - 97) % 26 + 97)
    elif type_code == 'atbash':
      for x in range(self.length):
        char = self.string[x]
        self.new_string += chr((ord(char) + int(movement) - 25) % 26 + 25)
    
    return self.new_string

print(encode("hiyo").encode('atbash', 3))