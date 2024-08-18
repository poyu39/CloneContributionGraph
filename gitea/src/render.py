import drawsvg as draw
from datetime import datetime
from config import CONFIG, WORKDIR

class Render:
    def __init__(self):
        self.image = draw.Drawing(55 * 10, 7 * 10)
        self.now_date = datetime.now().date()
        self.heatmap = []
        for i in range(0, 54):
            self.heatmap.append([0, 0, 0, 0, 0, 0, 0])
    
    def gen_heatmap(self, contributions_list):
        for contribution in contributions_list:
            contribution_date = datetime.fromtimestamp(contribution['timestamp']).date()
            offset = self.now_date - contribution_date
            x = 53 - (offset.days + (5 - self.now_date.weekday())) // 7
            y = contribution_date.weekday() + 1 if contribution_date.weekday() != 6 else 0
            self.heatmap[x][y] += contribution['contributions']
        return self.heatmap
    
    def render(self):
        for x in range(0, 54):
            for y in range(0 ,7):
                if x == 53 and (y - 1) > self.now_date.weekday():
                    continue
                contribution = self.heatmap[x][y]
                offset_x = x * 10
                offset_y = y * 10
                title = self._title(offset_x, offset_y, contribution)
                self.image.append(title)
                # # self.image.append(draw.Text(str(contribution), x=offset_x + 5, y=offset_y + 5, font_size=10, fill='white'))
        self.image.save_svg(f"{WORKDIR}\\storage\\{CONFIG['user']}.svg")
    
    def _title(self, x, y, contribution):
        _title_level_color = {
            0: '#52576799',
            1: '#516939',
            2: '#6c8c4c',
            3: '#87ab63',
            4: '#9fbc82',
            5: '#b7cda1'
        }
        contribution_level = 0
        if contribution > 0:
            contribution_level = int((contribution - 1) / 5) + 1
            if contribution_level > 5:
                contribution_level = 5
        element = draw.Rectangle(x, y, 10, 10, fill=_title_level_color[contribution_level])
        return element

if __name__ == '__main__':
    render = Render()