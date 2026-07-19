import gymnasium as gym



class TradingEnvironment(
    gym.Env
):


    def __init__(self):

        self.balance=10000


    def step(self,action):


        reward=0


        if action=="BUY":

            reward=1


        elif action=="SELL":

            reward=-1


        return reward
