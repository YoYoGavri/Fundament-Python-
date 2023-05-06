from variables import Variables
from error import Error, CreateError

newVar = Variables()
error_class = Error()
create_error = CreateError()


class Interpreter:
  def __init__(self):
    self.reserved_words = [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")]
  
  # Miscellaneous Commands
  def display(self, body, instance):
    if body[0] in instance.variables.keys():
      if type(instance.variables[body[0]]) == int or type(instance.variables[body[0]]) == float:
      # if int(instance.variables[body[0]]) == instance.variables[body[0]]:
        print(int(instance.variables[body[0]]))
      else:
        print(instance.variables[body[0]])
    elif body[0].startswith("\"") and body[0].endswith("\""):
      print(f"{body[0]}")
    elif not body[0].startswith("\"") or not body[0].endswith("\""):
      temp = ""
      for i in body:
        temp += i + ' '
      temp = temp[:-1]
      if "\"" not in temp:
        create_error.no_variable(variable=temp)
      else:
        create_error.quote_mismatch(body=temp)
        
        

  def assign(self, body, instance):
    '''
    - Check if TO keyword is present
    - Check if value is valid
    - Check if variable is valid
    '''
    # Check if the "to" keyword is present
    if "to" not in body:
      create_error.missing_keyword(body=body, errorType="Missing \"to\"")
    value_to_store = body[0]
    variable_to_save_to = body[2]
    # Check if the value starts and ends with quotes
    if body[0].startswith("\"") and body[0].endswith("\""):
      # Value is a string, proceed
      print("String Value")
    # Check if the value has only one quote
    elif body[0].count("\"") == 1:
      # Quote error
      print("Missing a quote")
    # Check if the value has zero quotes
    elif body[0].count("\"") == 0:
      # Check if the value is a variable name
      if body[0] in instance.variables.keys():
        print()
        # Value is an existing variable, proceed
      else:
        print()
        # Value has no quotes and is not a variable, eror
    if (body[-1][0].isdigit()):
      create_error.invalid_variable_name(body=body, errorType="Starts With Number")
    if body[-1] in self.reserved_words:
      create_error.invalid_variable_name(body=body, errorType="Reserved Word")
    else:
      ##
      if body[0].startswith("\"") and body[0].endswith("\""):
        instance.add_variable(body[2], body[0])
      elif body[0].count("\"") == 0:
        if body[0].isdigit():
          instance.add_variable(body[2], body[0])
        else:
          create_error.no_variable(variable=body[:-1])
      elif body[0].count("\"") == 1:
        new_temp = body[0].partition('to')[0]
        create_error.quote_mismatch(body=new_temp[:-1])
        

  # Math Commands
  def add(self, body, instance):
    if body[2] in instance.variables.keys():
      newSet = {body[2]:(int(body[0]) + int(instance.variables[body[2]]))}
      instance.variables.update(newSet)
    else:
      create_error.no_variable(variable=body[2])

  def subtract(self, body, instance):
    if body[2] in instance.variables.keys():
      newSet = {body[2]:(int(instance.variables[body[2]]) - int(body[0]))}
      instance.variables.update(newSet)
    else:
      create_error.no_variable(variable=body[0])

  def multiply(self, body, instance):
    if body[0] in instance.variables.keys():
      newSet = {body[0]:(int(body[2]) * int(instance.variables[body[0]]))}
      instance.variables.update(newSet)
    else:
      create_error.no_variable(variable=body[0])

  def divide(self, body, instance):
    if body[0] in instance.variables.keys():
      newSet = {body[0]:(int(instance.variables[body[0]]) / int(body[2]))}
      instance.variables.update(newSet)
    else:
      create_error.no_variable(variable=body[2])