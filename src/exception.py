import sys # This library has the information regarding the exception if occurs, as this module provides function and variables that are used to manipulate different parts of the python runtime environment.
from logger import logging
# Generally this library is present by default and hence is not needed to be mentioned in the requirements.txt file.




def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() 
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in the python script [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)

    )

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) # super is needed as I want to inherit the init from the 'Exception' class.
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self): # Basically what to show when printing
        return self.error_message 

# So bacially whenever you use try/catch then this type of error would be coming 


# Testing

# if __name__ == "__main__":
#     try: 
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by zero error")
#         raise CustomException(e,sys)