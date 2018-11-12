from baselines import deepq
from baselines import bench
from baselines import logger
from baselines.common.cmd_util import common_arg_parser, parse_unknown_args, make_vec_env
import os
from baselines.common.atari_wrappers import make_atari


def main():
    arg_parser = common_arg_parser()
    args, unknown_args = arg_parser.parse_known_args()
    if args.prioritized_replay is not None:
        prioritized_replay=args.prioritized_replay
    else:
        prioritized_replay=False
    if args.prioritized_replay_alpha is not None:
        prioritized_replay_alpha=args.prioritized_replay_alpha
    else:
        prioritized_replay_alpha=0.4
    if args.prioritized_replay_beta0 is not None:
        prioritized_replay_beta0=args.prioritized_replay_beta0
    else:
        prioritized_replay_beta0=0.6
    if args.prioritized_replay_beta_iters is not None:
        prioritized_replay_beta_iters=args.prioritized_replay_beta_iters
    else:
        prioritized_replay_beta_iters=None
    if args.prioritized_replay_eps is not None:
        prioritized_replay_eps=args.prioritized_replay_eps
    else:
        prioritized_replay_eps=1e-6
    if args.tentative is not None:
        tentative=args.tentative
    else:
        tentative = 1
    if args.experiment is not None:
        experiment=args.experiment
    else:
        experiment=0

    logger.configure()
    #env = make_atari('PongNoFrameskip-v4')
    env = make_atari('BreakoutNoFrameskip-v4')
    env = bench.Monitor(env, logger.get_dir())
    env = deepq.wrap_atari_dqn(env)
    log_dir = os.path.join('./log_breakout/'+str(experiment), str(prioritized_replay)+"_"+str(prioritized_replay_alpha)+"_"+str(prioritized_replay_beta0)+"_"+str(prioritized_replay_beta_iters)+"_"+str(prioritized_replay_eps))
    logger.configure(log_dir, None, str(tentative))
    model = deepq.learn(
        env,
        "conv_only",
        convs=[(32, 8, 4), (64, 4, 2), (64, 3, 1)],
        hiddens=[256],
        dueling=True,
        seed = 42,
        lr=1e-4,
	prioritized_replay=True,
        total_timesteps=int(1e7),
        buffer_size=10000,
        exploration_fraction=0.1,
        exploration_final_eps=0.01,
        train_freq=4,
        learning_starts=5000,
        target_network_update_freq=1000,
        gamma=0.99,
        print_freq=10
    )

    #model.save('pong_model.pkl')
    env.close()

if __name__ == '__main__':
    main()
