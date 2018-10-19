# Game using AI

I decided to make a one-agent/player pong and use deep reinforcement
learning to train it to play without actually telling it all the rules.

## Deep Reinforcement Learning

### Basics

Given **data**, choose **action** to maximize expected long-term **reward**

Every reinforcement learning problem is about an interaction between
an environment and an agent in that environment.

At each step : 

**Agent**:
+ executes action
+ receives observation from environment
+ receives reward

**Environment**
+ receives action
+ emits observation (new state)
+ emits reward

We can quantize these interactions into episodes, where each episode starts
at an initial state and the agent takes some action following which it gets
some reward, which then leads to a new state. 

So in each episode we have S(i) as starting state, A(i) as action 
preformed, R(i) as reward received, and S(i+1) as the next starting
state and so on.

What we need here is a transition function: Which can be modelled using a
markov chain.

> P(S(t+1), R(t) | S(t), A(t))

We want to find a policy(S) = p(A|S) which maximises sum of all rewards
in an episode, i.e.

    R(0) + R(1) + ... + R(t)

Note : Sometimes we focus only on short-term rewards so we can change the
objective to : 

    R(0) + g.R(1) + ... + g^t.R(t)

Since we are working in a stochastic environment we change the objective to 

    E[ R(0) + g.R(1) + ... + g^t.R(t) ]







