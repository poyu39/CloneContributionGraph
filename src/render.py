import drawsvg as draw
from datetime import datetime, timedelta
from config import CONFIG

class Render:
    def __init__(self):
        self.image = draw.Drawing(52 * 20, 7 * 20, origin='center')
        self.now_date = datetime.now().date()
        self.now_week = self.now_date.weekday()
        self.now_week_index = 53
        self.now_date_index = self.now_week
        self.heatmap = []
        for i in range(54):
            self.heatmap.append([0] * 7)

    def gen_heatmap(self, contributions):
        for date in contributions:
            offset = self.now_date - date
            x = 53 - int(offset.days / 7)
            y = 7 - offset.days % 7
            self.heatmap[x][y] = contributions[date]
        return self.heatmap
    
    def render(self):
        padding = 3
        for x in range(0, 54):
            for y in range(0 ,7):
                if x == 53 and y > self.now_week:
                    continue
                contribution = self.heatmap[x][y]
                offset_x = x * 10 + padding
                offset_y = y * 10 + padding
                title = self.title(offset_x, offset_y, contribution)
                self.image.append(title)
        self.image.save_svg(f"{CONFIG['user']}.svg")
    
    def xy2datetime(self, x, y):
        x_offset = self.now_date_index - x
        y_offset = self.now_week_index - y
        date = self.now_date - timedelta(days=x_offset, weeks=y_offset)
        return date
    
    def title(self, x, y, contribution):
        _title_level_color = {
            0: '#000000',
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