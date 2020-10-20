from torch import nn
from arkab.lightning.config import LightningConfig
import pytorch_lightning as pl


class LightningTrainer:
    def __init__(self, model: nn.Module, config: LightningConfig) -> None:
        """
        Provide a full model for lightning training process
        """
        self.trainer = pl.Trainer(gpus=config.gpus, min_epoches=config.min_epoch, max_epoches=config.max_epoch)