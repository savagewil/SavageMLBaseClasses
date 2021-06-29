import random
import time

from Models.BaseModel import BaseModel
from Simulations.SimulationState import SimulationState


def get_default_seed():
    return int(time.time() * 1E6)


class BaseSimulation:
    def __init__(self, model=None, seed=get_default_seed()):
        self.seed: int = seed
        self.model: BaseModel = model
        self.random = random.Random()
        self.random.seed(self.seed)
        self.state: SimulationState = SimulationState.INITIALIZED

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def set_seed(self, seed=get_default_seed()):
        self.seed = seed

    def get_seed(self):
        return self.seed

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def get_state(self):
        return self.state

    def step(self):
        pass

    def run(self):
        pass

    def reset(self):
        self.random.seed(self.seed)
