from kaggle_environments import make

from xconnect.eval import get_win_percentages
from xconnect.agents import agent_random, agent_leftmost, onestep_lookahead_agent
from xconnect.utils import save_env_render_html

env = make("connectx", debug=True)

get_win_percentages(agent1=onestep_lookahead_agent, agent2=onestep_lookahead_agent)
