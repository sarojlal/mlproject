import sys
import logging

def error_msg_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename #Getting the filename for error/execption
    error_msg = "Error occured in python script name [{0}], line number [{1}], error message ['{2}']".format(file_name,exc_tb.tb_lineno,str(error)) #Displaying the error message
    return error_msg

#Custom Exection class
class CustomExecption(Exception):
    def __init__(self, error_msg,error_detail: sys):
        super().__init__(error_msg)
        self.error_msg=error_msg_detail(error_msg,error_detail=error_detail)
        
    def __str__(self):
        return self.error_msg
    
#Try exception handling
# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by zero error..")
#         raise CustomExecption(e,sys)