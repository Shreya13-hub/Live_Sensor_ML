import sys
import os



# through sys we are going to find the file name and error present in line
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # exc_info() is function from sys which gives 3 output(exc_type,exc_value,exc_tb) exc_tb will give you in which line the error is present
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'error occured and file name is [{0}] and line number is [{1}] and error is [{2}].'.format(file_name,exc_tb.tb_lineno,str(error))
    
    return error_message





## to handle the error 
class SensorException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)   ### super function will help you to fetch the parameter from parent class(Exception class) which is unknown
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):              ## __str__ is magic method which is used at object level this fuction will help us to convert error msg in String
        return self.error_message
    
