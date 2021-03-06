import tensorflow as tf

# Basic model parameters.
tf.app.flags.DEFINE_string('game', '11arms', """Bandit experiment type to be loaded""")
tf.app.flags.DEFINE_string('best_model_game', '11arms', """Bandit experiment type to be loaded""")
tf.app.flags.DEFINE_string('model_name', '11arms4',
                           """Bandit experiment type to be run""")
tf.app.flags.DEFINE_boolean('resume', True,
                            """Resume training from latest checkpoint""")
tf.app.flags.DEFINE_boolean('train', True,
                            """Whether to train or test""")
tf.app.flags.DEFINE_string('checkpoint_dir', './models',
                           """Directory where to save model checkpoints.""")
tf.app.flags.DEFINE_string('summaries_dir', './summaries',
                           """Directory where to write event logs""")
tf.app.flags.DEFINE_string('frames_dir', './frames',
                           """Directory where to write event gifs""")
tf.app.flags.DEFINE_string('frames_test_dir', './frames_test',
                           """Directory where to write test event gifs""")

tf.app.flags.DEFINE_integer('summary_interval', 20000, """Number of episodes of interval between summary saves""")
tf.app.flags.DEFINE_integer('checkpoint_interval', 20000, """Number of episodes of interval between checkpoint saves""")
tf.app.flags.DEFINE_integer('frames_interval', 20000, """Number of episodes of interval between frames saves""")
tf.app.flags.DEFINE_integer('nb_actions', 11, """Number of actions to take""")
tf.app.flags.DEFINE_float('beta_v', 0.05, """Coefficient of value function loss""")
tf.app.flags.DEFINE_float('lr', 0.001, """LR value used for one test""")
tf.app.flags.DEFINE_float('gamma', 0.8, """Gamma value used for one test""")
tf.app.flags.DEFINE_integer('max_nb_episodes_train', 4000000, """Max number of episodes of training time""")

tf.app.flags.DEFINE_float('gradient_clip_value', 50.0, """gradient_clip_value""")
tf.app.flags.DEFINE_integer('nb_test_episodes', 150, """Test episodes""")
tf.app.flags.DEFINE_integer('nb_trials_episode', 5, """Trials per episode""")
tf.app.flags.DEFINE_boolean('gen_adv', True,
                            """Whether to use generalized advantage estimation""")
tf.app.flags.DEFINE_boolean('meta', True,
                            """Whether to use meta learning""")
tf.app.flags.DEFINE_integer('top', 1, """Take the best n models and test them""")
tf.app.flags.DEFINE_string('results_val_file', './results_val.txt',
                           """File where to write validation results""")
tf.app.flags.DEFINE_string('results_test_file', './results_test.txt',
                           """File where to write test results""")
tf.app.flags.DEFINE_string('results_eval_file', './results_eval.txt',
                           """File where to write eval results""")
