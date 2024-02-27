from api import GiteaAPI
from render import Render
from config import CONFIG

if __name__ == '__main__':
    api = GiteaAPI(CONFIG['url'], CONFIG['token'])
    contributions = api.get_contribution(CONFIG['user'])
    contributions_merged = api.contributions_merge(contributions)
    render = Render()
    heatmap = render.gen_heatmap(contributions_merged)
    render.render(heatmap)