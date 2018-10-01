import gym

from baselines import deepq
from baselines import logger
from baselines.common.cmd_util import common_arg_parser, parse_unknown_args, make_vec_env
import os


import numpy as np

def callback(lcl, _glb):
    # stop training if reward exceeds 199
    is_solved = lcl['t'] > 100 and sum(lcl['episode_rewards'][-101:-1]) / 100 >= 199
    return is_solved


def main():
    arg_parser = common_arg_parser()
    args, unknown_args = arg_parser.parse_known_args()
    if args.exploration_final_eps is not None:
        exploration_final_eps = args.exploration_final_eps
    else:
        exploration_final_eps = 0.02
    if args.prioritized_replay is not None:
        prioritized_replay=args.prioritized_replay
    else:
        prioritized_replay=False
    if args.prioritized_replay_alpha is not None:
        prioritized_replay_alpha=args.prioritized_replay_alpha
    else:
        prioritized_replay_alpha=0.4
    if args.exploration_fraction is not None:
        exploration_fraction = args.exploration_fraction
    else:
        exploration_fraction = 0.1
    if args.tentative is not None:
        tentative=args.tentative
    else:
        tentative = 1
    env = gym.make("CartPole-v0")

    ''' for final_eps in np.linspace(0.01, 0.2, 19):
        for final_eps_fraction in np.linspace(0.05, 0.2, 15):'''
    #log_dir = os.path.join('./log', str(prioritized_replay)+"_"+str(prioritized_replay_alpha),str(tentative))
    logger.configure('.log', None, 'tttest')
    act = None
    act = deepq.learn(
        env,
        network='mlp',
        lr=1e-3,
        total_timesteps=100000,
        buffer_size=50000,
        exploration_fraction=exploration_fraction,
        exploration_final_eps=exploration_final_eps,
        print_freq=10,
        callback=callback,
        prioritized_replay=prioritized_replay,
        prioritized_replay_alpha=prioritized_replay_alpha,
        gamma=1.0
    )
    # print("Saving model to cartpole_model.pkl")
    # act.save(log_dir+"cartpole_model.pkl")


if __name__ == '__main__':
    main()
