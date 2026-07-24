from auto_response.src.environment import SecurityEnvironment
from auto_response.src.agent import ResponseAgent


def train(episodes: int = 500) -> ResponseAgent:
    env = SecurityEnvironment()
    agent = ResponseAgent(n_states=len(env.STATES), n_actions=len(env.ACTIONS))

    for ep in range(episodes):
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = agent.act(state, training=True)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state)
            state = next_state
            total_reward += reward

        if (ep + 1) % 100 == 0:
            print(f"Episode {ep+1}/{episodes}, Total Reward: {total_reward:.1f}")

    policy = agent.get_policy(env.STATES)
    print("\nLearned Policy:")
    for state, action in policy.items():
        print(f"  {state} -> {action}")

    return agent


if __name__ == "__main__":
    train()
