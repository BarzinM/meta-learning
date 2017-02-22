from multiprocessing import Queue
import tensorflow as tf
from network import GACNetwork
import numpy as np
from predictor import Predictor
from trainer import Trainer
from Agent import Agent
import flags
FLAGS = tf.app.flags.FLAGS

class Server:
    def __init__(self, nb_actions):

        self.training_q = Queue(maxsize=FLAGS.max_queue_size)
        self.prediction_q = Queue(maxsize=FLAGS.max_queue_size)

        self.network = GACNetwork(nb_actions)
        self.global_step = self.network.global_step

        self.training_step = 0
        self.frame_counter = 0
        self.agents = []
        self.predictors = []
        self.trainers = []

    def run(self):
        for i in np.arange(FLAGS.nb_trainers):
            self.trainers.append(Trainer(self, i))
            self.trainers[-1].start()
        for i in np.arange(FLAGS.nb_predictors):
            self.predictors.append(Predictor(self, i))
            self.predictors[-1].start()
        for i in np.arange(FLAGS.nb_concurrent):
            self.agents.append(Agent(self, i))
            self.agents[-1].start()

    def train(self, batch_states, batch_rewards, batch_actions, trainer_id):
        self.network.train(batch_states, batch_rewards, batch_actions, trainer_id)
        self.training_step += 1
        self.frame_counter += batch_states.shape[0]
        self.network.increment_global_step()