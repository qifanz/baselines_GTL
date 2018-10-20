import gym

from baselines import deepq
from baselines import logger
from baselines.common import models
from baselines.common.cmd_util import common_arg_parser, parse_unknown_args, make_vec_env
import os

def main():
    arg_parser = common_arg_parser()
    args, unknown_args = arg_parser.parse_known_args()
    if args.buffer_size is not None:
      buffer_size = args.buffer_size
    else:
      buffer_size=50000
    if args.learning_starts is not None:
      learning_starts = args.learning_starts
    else:
      learning_starts = 1000
    if args.tentative is not None:
      tentative = args.tentative
    else:
      tentative = 1

    log_dir = os.path.join('./log','mountaincar',
        str(learning_starts)+"_"+str(buffer_size), str(tentative))
    logger.configure(log_dir, None)

    env = gym.make("MountainCar-v0")
    # Enabling layer_norm here is import for parameter space noise!
    act = deepq.learn(
        env,
        network=models.mlp(num_hidden=64, num_layers=1),
        lr=1e-3,
        total_timesteps=1000000,
        buffer_size=buffer_size,
        learning_starts = learning_starts,
        exploration_fraction=0.1,
        exploration_final_eps=0.1,
        print_freq=10,
        param_noise=False
    )
   # print("Saving model to mountaincar_model.pkl")
   # act.save("mountaincar_model.pkl")


if __name__ == '__main__':
    main()
