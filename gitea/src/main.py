from api import GiteaAPI
from render import Render
from config import CONFIG

if __name__ == '__main__':
    api = GiteaAPI(CONFIG['url'], CONFIG['token'])
    contributions_list = api.get_contribution(CONFIG['user'])
    render = Render()
    heatmap = render.gen_heatmap(contributions_list)
    render.render()