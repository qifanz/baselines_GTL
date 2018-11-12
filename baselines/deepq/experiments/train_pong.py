from baselines import deepq
from baselines import bench
from baselines import logger
from baselines.common.atari_wrappers import make_atari


def main():
    logger.configure()
    env = make_atari('BreakoutNoFrameskip-v4')
    env = bench.Monitor(env, logger.get_dir())
    env = deepq.wrap_atari_dqn(env)
    logger.configure('../log/breakout/2', None)

    model = deepq.learn(
        env,
        "conv_only",
        convs=[(32, 8, 4), (64, 4, 2), (64, 3, 1)],
        hiddens=[256],
        dueling=True,
        lr=0.00025,
        target_network_update_freq=10000,
        total_timesteps=int(2e7),
        buffer_size=1000000,
        exploration_fraction=0.1,
        exploration_final_eps=0.01,
        train_freq=4,
        learning_starts=50000,
        gamma=0.99,
        print_freq=10
    )

    #model.save('pong_model.pkl')
    env.close()

if __name__ == '__main__':
    main()
