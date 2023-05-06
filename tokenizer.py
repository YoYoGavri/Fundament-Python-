from interpreter import Interpreter
from error import Error, CreateError
from variables import Variables

error_class = Error()
create_error = CreateError()

import ast

interpreter = Interpreter()
newVar = Variables()

printTokens = False

# Literals - Any basic datatype's value (strings, numbers, etc)
# Operators - Any symbol that tells the computer to perform some type of operation (+, -, /, x, etc)
# Variables - Any symbol meant to represent a piece of data
# Reserved Words - Any words that cannot be used by the user as a variable name
# Data Types - Strings, Numbers, etc


class Tokenizer:
  # https://www.scaler.com/topics/python/literals-in-python/
  def __init__(self, body):
    self.keyword = str(body[0]).lower()
    self.body = body[1:]
    ##
    self.operators = ['+', '-', '*', '/', '^', '<', '>', '<=', '>=', 'to', 'from']
    self.variables = newVar.variables.keys()
    self.reserved_words = [func for func in dir(interpreter) if callable(getattr(interpreter, func)) and not func.startswith("__")]
    self.data_types = ['String', 'Number', 'Boolean', 'None', 'List', 'Set', 'Dictionary', 'Tuple']

    self.body_operators = []
    self.body_variables = []
    self.body_reserved_words = []
    self.body_data_types = []
    self.body_literals = []
    
  def line_tokenizer(self):
    try:
      attr = getattr(interpreter, self.keyword)
      if attr:
        cmd = getattr(interpreter, self.keyword)
        cmd(self.body, newVar)
    except AttributeError as e:
      error_class.attribute_error(e, interpreter, self.keyword)

    self.body_reserved_words.append(self.keyword)
    for word in self.body:
      if word in self.reserved_words:
        self.body_reserved_words.append(word)
      elif word in self.operators:
        self.body_operators.append(word)
      elif word in self.variables:
        self.body_variables.append(word)
      else:
        self.body_literals.append(word)

    if printTokens:
      for value in self.body_literals:
        try:
          value_type = ast.literal_eval(value)
          if type(value_type) == float or type(value_type) == int or type(value_type) == complex:
            value_type = 'Number'
          elif type(value_type) == str:
            value_type = 'String'
          elif type(value_type) == list or type(value_type) == range:
            value_type = 'List'
          elif type(value_type) == tuple:
            value_type = 'Tuple'
          elif type(value_type) == dict:
            value_type = 'Dictionary'
          elif type(value_type) == set or type(value_type) == frozenset:
            value_type = 'Set'
          elif type(value_type) == bool:
            value_type = 'Boolean'
          elif type(value_type) == None:
            value_type = 'None'
          
            
            
          self.body_data_types.append((value_type, value))
        except (ValueError, SyntaxError):
          self.body_data_types.append((type(value), value))       

      print('---------------[Tokenizer]---------------')
      print(f'Reserved Words: {self.body_reserved_words}')
      print(f'Operators: {self.body_operators}')
      print(f'Data Types: {self.body_data_types}')
      print(f'Variables: {self.body_variables}')
      print(f'Literals: {self.body_literals}')
      print('-----------------------------------------')