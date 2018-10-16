import gym

from baselines import deepq
from baselines import logger
from baselines.common import models
from baselines.common.cmd_util import common_arg_parser, parse_unknown_args, make_vec_env
import os



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
        prioritized_replay_alpha=0.6
    if args.prioritized_replay_beta0 is not None:
        prioritized_replay_beta0=args.prioritized_replay_beta0
    else:
        prioritized_replay_beta0=0.4
    if args.prioritized_replay_beta_iters is not None:
        prioritized_replay_beta_iters=args.prioritized_replay_beta_iters
    else:
        prioritized_replay_beta_iters=None
    if args.prioritized_replay_eps is not None:
        prioritized_replay_eps=args.prioritized_replay_eps
    else:
        prioritized_replay_eps=1e-6
    if args.exploration_fraction is not None:
        exploration_fraction = args.exploration_fraction
    else:
        exploration_fraction = 0.1
    if args.tentative is not None:
        tentative=args.tentative
    else:
        tentative = 1
    if args.experiment is not None:
        experiment=args.experiment
    else:
        experiment=0

    env = gym.make("MountainCar-v0")
    log_dir = os.path.join('./log_car/'+str(experiment), str(prioritized_replay)+"_"+str(prioritized_replay_alpha)+"_"+str(prioritized_replay_beta0)+"_"+str(prioritized_replay_beta_iters)+"_"+str(prioritized_replay_eps))
    logger.configure(log_dir, None, str(tentative))

    # Enabling layer_norm here is import for parameter space noise!
    act = deepq.learn(
        env,
        network=models.mlp(num_hidden=64, num_layers=1),
        lr=1e-3,
        prioritized_replay=prioritized_replay,
        prioritized_replay_alpha=prioritized_replay_alpha,
        prioritized_replay_beta0=prioritized_replay_beta0,
        prioritized_replay_beta_iters=prioritized_replay_beta_iters,
        prioritized_replay_eps=prioritized_replay_eps,
        total_timesteps=100000,
        buffer_size=50000,
        exploration_fraction=0.1,
        exploration_final_eps=0.1,
        print_freq=10,
        param_noise=False
    )
    #print("Saving model to mountaincar_model.pkl")
    #act.save("mountaincar_model.pkl")


if __name__ == '__main__':
    main()
