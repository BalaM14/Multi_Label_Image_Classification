from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareBaseModel
from deepClassifier import logger

STAGE_NAME = "Prepare Base Model Stage"

def main():
    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f"**"*40)
        logger.info(f">>>>>> Stage [{STAGE_NAME}] started <<<<<<<")
        main()
        logger.info(f">>>>>> Stage [{STAGE_NAME}] Completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e