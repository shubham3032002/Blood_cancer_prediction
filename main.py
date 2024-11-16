from Cancer_classification import logger
from Cancer_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME='Data Ingestion Stage'

try:
        logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<< \n\n X==============X")
except Exception as e:
        logger.exception(e)
        raise e       