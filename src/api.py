import requests
import json
from datetime import datetime
from config import CONFIG

class GiteaAPI:
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def get_contribution(self, user):
        url = f'{self.url}/api/v1/users/{user}/heatmap'
        headers = {
            'Authorization': f'token {self.token}'
        }
        response = requests.get(url, headers=headers)
        dict_response = json.loads(response.text)
        return dict_response
    
    def contributions_merge(self, contributions):
        '''
            Merge contributions by date
        '''
        merged = {}
        for contribution in contributions:
            date = datetime.fromtimestamp(contribution['timestamp']).date()
            if date in merged:
                merged[date] += contribution['contributions']
            else:
                merged[date] = contribution['contributions']
        return merged


if __name__ == '__main__':
    api = GiteaAPI(CONFIG['url'], CONFIG['token'])
    contributions = api.get_contribution(CONFIG['user'])
    contributions_merged = api.contributions_merge(contributions)
    print(contributions_merged)