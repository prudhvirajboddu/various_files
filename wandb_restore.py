import wandb

from wandb.tensorflow import WandbHook
wandb.init(project="catsvsdogs", sync_tensorboard=True)



model=wandb.restore('model.h5')
	
weights_file=wandb.restore('weights.h5')

my_pred_model.load_weights(weights_file.name)
