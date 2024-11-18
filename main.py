from Cancer_classification import logger
from Cancer_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Cancer_classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME='Data Ingestion Stage'

try:
        logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<< \n\n X==============X")
except Exception as e:
        logger.exception(e)
        raise e    


STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e   