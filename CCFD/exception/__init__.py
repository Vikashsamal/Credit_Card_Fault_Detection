import os
import sys

class CreditcardException(Exception):

    def __int__(self,error_message:Exception, error_detail:sys):
        super().__init__(error_message)
        self.error_message = CreditcardException.error_message_detail(error_message, error_detail=error_detail)
    

    @staticmethod
    def error_message_detail(error:Exception, error_detail:sys)->str:
        """
        error: Exception object raise from module
        error_detail: is sys module contains detail information about system execution information.
        """
        _, _, exc_tb=error_detail.exc_info()
        line_number = exc_tb.tb_frame.f_lineno

        #Extracting file name from exception traceback
        file_name= exc_tb.tb_frame.f_code.co_filename

        #Preparing error message
        error_message = f"Error occurred python script name[{file_name}]" \
              f" line number [{exc_tb.tb_lineno}] error message [{error}]."
        return error_message
    
    def __str__(self):
        return CreditcardException.__name__.__str__()
    
