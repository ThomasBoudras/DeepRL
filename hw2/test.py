import numpy as np
gamma = 2

def test_rewards_1(rewards) :
    discounted_return = 0
    for t in range(len(rewards)):
        discounted_return += (gamma**t)*rewards[t]
    return [discounted_return]*len(rewards) 

def test_rewards_2(rewards):
    T = len(rewards)
    gamma_list = gamma ** np.array(list(range(T)))
    discounted_sum = np.array(rewards) @ gamma_list
    discounted_rewards = list([discounted_sum])*T
    return discounted_rewards

rewards = [1,2,3,1,2,2,2]
print(test_rewards_1(rewards))
print(test_rewards_2(rewards))
