import os
 
def func_print_test_var(event, context):
  test_var =os.environ['TEST_VAR']
  print(f'Value in test_Var is {test_var}')
