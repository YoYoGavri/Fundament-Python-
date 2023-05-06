import difflib

# Error handler class
class Error(Exception):
  def __init__(self):
    self.open_bold = '\x1B[1m'
    self.close_bold = '\x1B[0m'
    self.open_italic = '\x1B[3m'
    self.close_italic = '\x1B[0m'

  def attribute_error(self, error_msg, value, attempted):
      suggested_functions = [func for func in dir(value) if not func.startswith('__') and callable(getattr(value, func))]
      closest_match = difflib.get_close_matches(attempted, suggested_functions, n=1)
      if closest_match:
          print(f"AttributeError: {error_msg}. Did you mean '{closest_match[0]}'?")
      else:
          print(f"AttributeError: {error_msg}")

class CreateError(Error):
  def no_variable(self, variable):
    print(f'CREATE ERROR: NO VARIABLE {self.open_bold}{self.open_italic}{variable}{self.close_bold}{self.close_italic} EXISTS.')
    

  def quote_mismatch(self, body):
    print(f"CREATE ERROR: QUOTE MISMATCH ON {self.open_bold}{self.open_italic}{body}{self.close_bold}{self.close_italic}.")

  # Add variations for diff data types (pass in type as well)
  def invalid_variable_name(self, body, errorType):
    if errorType == "Starts With Number":
      print(f"INVALID VARIABLE NAME: VARIABLE CANNOT START WITH A NUMBER {self.open_bold}{self.open_italic}{body[-1][0]}{self.close_bold}{self.close_italic}{body[-1][1:]}.")
    if errorType == "Reserved Word":
      print(f"INVALID VARIABLE NAME: VARIABLE NAME IS A RESERVED WORD {self.open_bold}{self.open_italic}{body[-1]}{self.close_bold}{self.close_italic}.")

      
  def missing_keyword(self, body, errorType):
    if errorType == "Missing \"to\"":
      print(f"MISSING KEYWORD: MUST INCLUDE {self.open_bold}{self.open_italic}TO{self.close_bold}{self.close_italic}.")


  # def index_error(self, body):

  # def attrubte_error(self, body): # For when getattr fails, try to somehow bring in the suggested keyword