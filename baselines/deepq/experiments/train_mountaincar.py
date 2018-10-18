import gym

from baselines import deepq
from baselines.common import models
from baselines import logger
from baselines.common.cmd_util import common_arg_parser, parse_unknown_args, make_vec_env
import os

def main():
    arg_parser = common_arg_parser()
    args, unknown_args = arg_parser.parse_known_args()
    if args.exploration_final_eps is not None:
        exploration_final_eps = args.exploration_final_eps
    else:
        exploration_final_eps = 0.02
    if args.exploration_fraction is not None:
        exploration_fraction = args.exploration_fraction
    else:
        exploration_fraction = 0.1
    if args.tentative is not None:
        tentative = args.tentative
    else:
        tentative = 1
    if args.param_noise is not None:
        param_noise = args.param_noise
    else:
        param_noise = False

    log_dir = os.path.join('./log', 'mountaincar',
                           str(exploration_final_eps),
                           str(exploration_fraction),
                           str(param_noise),
                           str(tentative))

    logger.configure(log_dir, None)

    env = gym.make("MountainCar-v0")
    # Enabling layer_norm here is import for parameter space noise!
    act = deepq.learn(
        env,
        network=models.mlp(num_hidden=64, num_layers=1),
        lr=1e-3,
        total_timesteps=1000000,
        buffer_size=50000,
        exploration_fraction=exploration_fraction,
        exploration_final_eps=exploration_final_eps,
        learning_starts=10000,
        print_freq=10,
        param_noise=param_noise
    )
    print("Saving model to mountaincar_model.pkl")
    act.save("mountaincar_model.pkl")


if __name__ == '__main__':
    main()
