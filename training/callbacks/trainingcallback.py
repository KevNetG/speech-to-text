from keras.callbacks import Callback

from training.training import Training, save


class TrainingCallback(Callback):
    def __init__(self, training: Training, save_file_path: str):
        super().__init__()
        self.training = training
        self.save_file_path = save_file_path

    def on_epoch_end(self, epoch, logs=None):
        loss = logs['loss']
        validation_loss = logs['val_loss']

        if len(self.training.validation_loss) == 0 or validation_loss < self.training.validation_loss[-1]:
            self.training.loss.append(loss)
            self.training.validation_loss.append(validation_loss)
            save(self.save_file_path, self.training)