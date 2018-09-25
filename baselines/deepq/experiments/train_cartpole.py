import gym

from baselines import deepq
from baselines import logger
from baselines.common.cmd_util import common_arg_parser, parse_unknown_args, make_vec_env


import numpy as np

def callback(lcl, _glb):
    # stop training if reward exceeds 199
    is_solved = lcl['t'] > 100 and sum(lcl['episode_rewards'][-101:-1]) / 100 >= 199
    return is_solved


def main():
    arg_parser = common_arg_parser()
    args, unknown_args = arg_parser.parse_known_args()
    if args.eps is not None:
        final_eps = args.eps
    else:
        final_eps = 0.02
    if args.eps_fraction is not None:
        final_eps_fraction = args.eps_fraction
    else:
        final_eps_fraction = 0.1
    env = gym.make("CartPole-v0")

    ''' for final_eps in np.linspace(0.01, 0.2, 19):
        for final_eps_fraction in np.linspace(0.05, 0.2, 15):'''
    log_dir='./log/'+str(final_eps)+"_"+str(final_eps_fraction)+'/'
    logger.configure(log_dir, None)
    act = None
    act = deepq.learn(
        env,
        network='mlp',
        lr=1e-3,
        total_timesteps=100000,
        buffer_size=50000,
        exploration_fraction=final_eps_fraction,
        exploration_final_eps=final_eps,
        print_freq=10,
        callback=callback,
        gamma=1.0
    )
    print("Saving model to cartpole_model.pkl")
    act.save(log_dir+"cartpole_model.pkl")


if __name__ == '__main__':
    main()
