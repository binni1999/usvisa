from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys 
from us_visa.pipeline.training_pipeline import TrainPipeline
#logging.info("Welcome to our custom log")

try: 
    obj = TrainPipeline()
    obj.run_pipeline()
    
except  Exception as e: 
    raise USvisaException(e,sys)