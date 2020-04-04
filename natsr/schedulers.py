from torch.optim.lr_scheduler import ExponentialLR
from torch.optim.optimizer import Optimizer

from natsr import LRSchedulerType


def build_lr_scheduler(config, optimizer: Optimizer):
    lr_schedule_type: str = config['model']['lr_schedule_type']
    if lr_schedule_type == LRSchedulerType.EXPONENTIAL:
        return ExponentialLR(
            optimizer, gamma=config['model']['lr_decay_ratio']
        )
    raise NotImplementedError(
        f'[-] not supported lr_schedule_type {lr_schedule_type}'
    )