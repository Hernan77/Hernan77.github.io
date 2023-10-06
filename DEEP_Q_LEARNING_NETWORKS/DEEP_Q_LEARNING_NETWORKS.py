#!/usr/bin/env python
# coding: utf-8

# # DEEP Q LEARNING NETWORKS
# 
# ref: Deep Q Learning Networks (LiveLessons): https://www.youtube.com/watch?v=OYhFoMySoVs

# In[1]:


#pip install gym==0.7.4
#pip install pyglet==1.5.27


# The main idea of a **Markov Decision Process** is that we have some agent, in our case a deep reinforcement learning algorithm, that takes some **action** in an **environment**. The environment provides the agent two kinds of information as feedback. The first kind is the **state**, which porvides information about the environment. The second kind is the **reward** that we try to maximize.
# 
# <center><img src="IMAGES/Fig_1.png" width="600"></center><br/><br/>
# 
# We can define this idea formally from the following set of terms. The trademark of any **Markov Decision Process** is that we assume that the current state of the environment at any given time step is representative of all the time steps that have came before 
# 
# <left><img src="IMAGES/Fig_2.png" width="400"></left><br/><br/>
# 
# The **discount factor** is a hyperparameter that we set ourselves. This is how much our agent discounts future reward. When our agent is considering any given action taken in the environment, the agent is going to take the action that maximizes its reward. The further it tries to predict a future reward, the less likely that reward is. The expected reward in the next time step is valued more highly than the expected reward in two or three time steps. 
# 
# Given any set of states, our goal is to create a **policy (pi)** that maps our states to our actions. So, given some states we want to have this overall polciy of what action we should be taking on those states. The policy function is what we are trying to learn with our deep reinformenet learning algorithm. 
# 
# <center><img src="IMAGES/Fig_3.png" width="80"></center><br/><br/>
# 
# Our objective is to find the **optimal polity (pi*)** that maximizes the expected cumulative reward.
# 
# <center><img src="IMAGES/Fig_4.png" width="400"></center><br/><br/>
# 
# The **value function** is the expected cumulative reward from being at a particular state of the environment. We are taking the state and the policy that we are making in that state.
# 
# <center><img src="IMAGES/Fig_5.png" width="250"></center><br/><br/>
# 
# The **Q-value function** is one step more complex. The Q-value function considers both the state, and a given action. It tells us what is the maximum expected reward form the situation of being in a particular state and taking a particular action, and then following our policy afterwards. 
# 
# <center><img src="IMAGES/Fig_6.png" width="350"></center><br/><br/>
# 
# The Q<sup>*</sup> is the **optimal Q-value function** given a particular state and taking a particular action. This is the most expect reward that we could get given a particular state, taking a particular action, and following the optimal policy form that point onward. 
# 
# <center><img src="IMAGES/Fig_7.png" width="250"></center><br/><br/>
# 
# We are going to try to approximate Q<sup>*</sup> by using **Deep Q-Learning Network (DQN)**. DQN is a partciular type of Deep Reinforment Learning Agent. We add the **theta** term to our Q function. Theta represents all the weights in this kind of function that we are using to approximate Q<sup>*</sup>. So we have a Q with a particular state and a particular action. With the set of weights (represented by theta) we can estimate what the maximum expected reward can be. Theta can be any kind of function, for example a linear regression model. However what makes DQN a Deep Reinforment learning method is that theta is a **deep neural network (NN)**. This means that you build some architecture with tensorflow or keras, to have a set of weights and biases. In our case we will use dense layers to approximate the equation above.

# # Cartpole DQN
# 
# Deep Q-Learning Network with Keras and OpenAIGym, based on [Keon Kim's code](https://github.com/keon/deep-q-learning/blob/master/dqn.py).

# ## Import dependencies

# In[2]:


#pip install gym==0.7.3
import os; os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' # for creating directories
import random
import gym # to render our environment for our agent to take actions in and receive feedback from.
import numpy as np
from collections import deque # use a special kind of list for the memory of our agent, "deque", 
# which is like a list, but you can add things to the end or front of the list.
from keras.models import Sequential # use a sequential model to build our neural network for the 
# approximation the optimal Q (Q*)
from keras.layers import Dense # we are only going to use dense layers in our network. 
# So the weights will be weights and biases inbetween layers of dense network.
from keras.optimizers import Adam # ...for stochastic gradient descent...
import keras.utils
keras.utils.disable_interactive_logging()


# ### Select processing devices (if you are using a machine with multiple gpu's)
# ...to decide on which devices you want to be running

# In[3]:


# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
# os.environ["CUDA_VISIBLE_DEVICE"] = "" # I just want to run on my cpu's...so, 
# I won't use any cuda devices, or any gpu's.
# os.environ["CUDA_DEVICE_ORDER"] = "1"


# ### Set parameters
# It is a good idea to have as many hyperparameters as possible to the top of the file...

# In[4]:


env = gym.make('CartPole-v1')# define exactly what environment our deep reinforment agent 
# is going to be in. There are some hyperparameters realted to the size of the state 
# and the size of the actions.
state_size = env.observation_space.shape[0]
state_size


# In[5]:


action_size = env.action_space.n
action_size


# In[6]:


batch_size = 32 # Define a batch size for our gradient descent. 
# You can carry this parameter by powers of two.
n_episodes = 1001 # This is the number of games we want our agent to play. 
# The number of games we play provide us with more data for training.
# In each episode we are going to remember some of the things that happened 
# in that episode and we will use that memory to train our deep reinforcement learning agent.
output_dir = 'model_output/cartpole' # ...to store our model output
if not os.path.exists(output_dir): # Creates the direcotry if it doesn't already exsits
    os.makedirs(output_dir)


# ### Define agent

# In[7]:


class DQNAgent: # create a python class
    
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        # We are going to play a thousand runs of the game. In each episode we are going to 
        # randomly remember some of the events.
        # We are going to remember some of the states-action pairs, and rewards. 
        # We are going to use those memories and replay them to actually train our model. 
        # The advantge of doing things this way is that it prevents us from trying to go all over the episodes
        # and use every sincle event that ever happened...
        # That would be inefficient, first of all because events that are closer to each other
        # in time are very similar, they are highly correlated. 
        # Close event dont provide much additional information. 
        # It is better to sample from random spots all over the game as opposed to continuous points in the game. 
        # The other thing that it is great about using memory replay to train a model is that 
        # it helps us to create a greater diversity of events that we use to train the model.
        
        self.memory = deque(maxlen=2000) # keep adding pieces on to our list but as soon as we get to 2000 
        # the oldest elements of the 'deque' will start to be removed. 
        # We will take only the last 2000 memories. 
        
        self.gamma = 0.95 # gamma is the discount factor. So this is how much to discount future reward. 
        # When we are trying to estimate future reward, the next time step is easier to guess correctly...
        # than 5 or 10 steps from now. So when we look ahead to estimate how much reward we are goign to 
        # accumulate based on the actions we take we want to weight the upcoming actions more heavily 
        # than the ones that are in the distant future.
        
        self.epsilon = 1.0 # epsilon is the exploration rate for your agent. 
        # There are two kinds of modes that your agent can take action with. 
        # The agent can either try to take the best possible action based on what it has learned 
        # (this is what we call exploitation...of exisitng knowledge)
        # ...or explore. The reason why we might want to explore is because the kind of enviroment 
        # that deep reinforcement learning agent have to explore are very complex and
        # if we are only stocked with exploiting our exisitng best practices we might not 
        # uncover something new that it is helpful.
        # This is particularly important because deep reinforcement learning environments can evolve over time. 
        # Epsilon equal to 1 means that our initial exporation versus exploition rate will be 
        # skewed 100% toward exploration.
        
        self.epsilon_decay = 0.995 # decay epsilon over time. 
        # We slowly shift our agent from exploring at random to exploiting the knowledge 
        # that it has learned over time.
        
        self.epsilon_min = 0.01 # we can set a floor on how low the epsilon can go.
        
        self.learning_rate = 0.001 # Our agent alson has a learning rate. 
        # This is the stochastic gradient decent rate. 
        # It is the step size for our stochastic gradient descent optimizer.
        
        self.model = self._build_model() # This is just private method. 
        # Can only be used by this particular instance of the class.
        
    def _build_model(self):
        # In this method we are going to define our dense neural network for approximating Q*. 
        # This is going to be the usual way we set up a keras model.
        model = Sequential()
        
        # First, layer is going to be dense. 24 neurons. 
        # The four elements of the state are the input to the model. 
        # We will set activation to rectified linear unit.
        model.add(Dense(24, input_dim = self.state_size, activation='relu'))
        # The next layer...
        model.add(Dense(24, activation='relu'))
        # The output layer has as many neurons as possible actions...
        # The activation is linear because we are directly modeling these actions.
        # We dont want some abstract probability. 
        # We want the action estimate to be direct out of this neural network.
        model.add(Dense(self.action_size, activation='linear'))
        # Now we are going to compile the model. 
        # We have use almost always used cross-entropy as our cost function. 
        # It turns out that for this particular configuration of our agent, "MSE" is a good choice
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        # this method is going to return the model.
        return model
        
    def remember(self, state, action, reward, next_state, done):
        # The remember method is really important. 
        # The remember function takes state at the current time step, 
        # takes in the action at the current time stamp,
        # takes in reward at the current time step, and takes in the next state. 
        # It enables us to take, given a state-action pair to model, what is going to happen next, 
        # and know the expected reward we are about to receive. 
        # "Done" is a parameters that lets us know if the episode has ended or not.
        # The only thing this remmember method is going to do is append this information into our memory 'deque'.
        self.memory.append((state, action, reward, next_state, done))
    
    def act(self, state):
        # We are trying to figure out what action to take given a state.
        # We are going to use the epsilon to either explore randomly or 
        # exploit the existing information within the theta weights of our dense network.
        if np.random.rand() <= self.epsilon:
            # ...then we are just going to act randomly...this is the exploration mode
            return random.randrange(self.action_size)
        # Over time as our model trains we epsilon will decay and we will tend toward exploitation. 
        # How do we exploit? In order to exploit the knowledge, we use the theta weights and the 
        # predict method on our model.
        # We pass the state into our agent we want to exploit. 
        # We use the predict method on our deep learning model inside the agent to have a guess 
        # into what the best course of action is to maximize our future reward...
        act_values = self.model.predict(state)
        #...and we return from this method the action that is determined to be the best choice.
        return np.argmax(act_values[0])
    
    def replay(self, batch_size):
        # Create a minibatch that is a random sample from our memory. 
        # We are going to sample some of the memories.
        # The number of memories which we are going to sample is the batch size.
        minibatch = random.sample(self.memory, batch_size)
        # Everyone of our memories has a state, an action, a reward, a next_state, 
        # and whether the episode is done or not.
        for state, action, reward, next_state, done in minibatch:
            # if the episode is ended, that is if we have reached the maximum number of time steps, 
            # we have allowed or if we ended the game by dying...if that happens...we are done.
            # In this case there is no mystery. Our target is equal to the reward...we know how the game ends.
            # We don't need to make predictions about future reward
            target = reward
            if not done:
                # If not done we need to make some estimations about what the discount future reward could be.
                # In that case the target is equal to the reward in our current state 
                # plus the discounted future reward times our estimates of future reward. 
                # The way we estimate our future reward is by using our neural network.
                # Here our neural network based on information about our next state 
                # inpassed into it can predict what the future reward should be.
                target = (reward + self.gamma * np.amax(self.model.predict(next_state)[0]))
            # The next step is to map that maximized future reward to the current reward. 
            # We do that with the theta. First, we estimate our target given the current state 
            # (using the Neural network)...
            target_f = self.model.predict(state)
            # Then we map that target form the current state to the future state with the following line...
            target_f[0][action] = target
            # Then finally, with all of that information altogether we can fit a model to train 
            
            #...so our x's (inputs) into the model are our current state.
            # Our y is the predicted future reward 
            # We do that for a single epoch, because we have only one single moment of information, 
            # one single memory to replay here
            # We don't any verbosity...
            self.model.fit(state, target_f, epochs=1, verbose=0)
            
        # Final thing we to do within our replay method is to decrease our epsilon...
        # if epsilon is greater than our epsilon minimum...
        if self.epsilon > self.epsilon_min:
            # then set our epislon for the next replay to a little bit smaller value 
            # by multiplying into our epsilon decay.
            self.epsilon *= self.epsilon_decay
            
    def load(self, name):
        # We can save information and reload it later...save your model weights
        self.model.load_weights(name)
        
    def save(self, name):
        # We also need a method to save the weights
        self.model.save_weights(name)
        
    # Now that we have our DQN agent, we need to get it inside our environment and train it to perform well


# In[8]:


# let's define a particular instance of our agent and we pass into it on the two parameters
agent = DQNAgent(state_size, action_size)


# ### Now we can interact with the environment

# In[9]:


# We are going to stat our episode by saying that done = False
done = False
# For each episode in the range of episodes we selected 
for e in range(n_episodes):
    # we are going to take the following actions...
    # but first we need a reset state (in our case a random position)
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    
    # then we are going to iterate over time steps of the game. 
    # So we can set a max number of time steps that our episode can run for.
    # This mean that we keep the cart pole alive 
    # The maximum game time is 500o game time steps
    for time in range(5000): # Truncation: Doesnt matter if I used 5000 because 
        # Episode length is greater than 500 (200 for v0). So score will never be larger than 500 
        # (https://www.gymlibrary.dev/environments/classic_control/cart_pole/)
        env.render() # will dockerize a container enviroment on a cloud service
        # the first step in interacting with our environment is to pass the current state 
        # (we initalize with a random state so our agent can take an initial action).
        # The action is going to be a 0 or 1 (left or right)
        # at the beginning is random guesses, but as it learns from memory 
        # it gets better to approximating the optimal future reward.
        action = agent.act(state)
        # After our agent has taken an action, we can use that action 
        # to pass the enviroment and get the next state and reward form our enviroment
        # and whether the game is done or not.
        next_state, reward, done, _ = env.step(action)
        # next, we find our reward which it is the regard that the enviroment pops out 
        # as long as our game is not done...
        # otherwise it is going to be equal to -10 (we penalize poor actions)
        # our reward is related to the number of steps we get through the game, 
        # but if we die the reward is -10
        reward = reward if not done else -10
        # We simply reshape out next state.
        next_state = np.reshape(next_state, [1, state_size])
        
        # then we use the remember method to remember 
        # the previous time steps, the state, actions, and rewards.
        agent.remember(state, action, reward, next_state, done)
        
        # For the susequent the state..it is what the state was in the previous iteration
        state = next_state
        
        if done:
            print("episode: {}/{}, score: {}, e: {:.2}".format(e, n_episodes, time, agent.epsilon))
            break
        
    # Final step is to actually train our theta. 
    # We need to give the agent a chance to update its theta weights so that it can improve for future itertion.
    # If agent memory is greater than batch_size we resample our memory and replay some experience to train our theta
    if len(agent.memory) > batch_size:
        agent.replay(batch_size)
            
    # Last thing, is that for every 50th episode we save out our model parameters
    if e % 50 == 0:
        agent.save(output_dir + "weights_" + "{:04d}".format(e) + "hdf5")

