from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareCallBack, Training
from deepClassifier import logger

STAGE_NAME = "Prepare Callback Stage"

def main():
    config = ConfigurationManager()
    prepare_call_back_config = config.get_prepare_call_back_config()
    prepare_call_back = PrepareCallBack(config=prepare_call_back_config)
    callback_list = prepare_call_back.get_tb_ckpt_callbacks()

    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train(
        callback_list = callback_list
    )

if __name__ == '__main__':
    try:
        logger.info(f"**"*40)
        logger.info(f">>>>>> Stage [{STAGE_NAME}] started <<<<<<<")
        main()
        logger.info(f">>>>>> Stage [{STAGE_NAME}] Completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e