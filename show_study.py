
####################

status_list = {
        'going_out': ['離席中', '離席しています。', 'active'],
        'active'   : ['進捗してる', '進捗してます。 ふふん♪', 'working'],
        'thinking' : ['集中してる', '集中しています。 むふー。', 'working'],
        'space_out': ['ぼんやり', 'ぼんやりしてます。 ぺしょ。', 'thinking'],
        'meeting'  : ['会議', '会議に呼ばれてます。', 'thinking'],
        'sleeping' : ['寝てる', '寝ています💕 もふ。', 'sleeping']
    }

####################

import datetime
import time
import PySimpleGUI as sg
from pypresence import Presence

client_id = "1199013551529013369"
RPC = Presence(client_id)
RPC.connect()

## メモ： https://qiita.com/G-Rape/items/9f14b5f393bc9d88fb49
## メモ： https://zenn.dev/torachi0401/articles/pysimplegui_articles
text_widget = sg.Text('前回の更新日時：')
layout = [
    [text_widget],
    list(map(lambda key: sg.Radio(status_list[key][0], 'status', enable_events=True, key=key), status_list.keys()))
]
window = sg.Window("ねこのすてーたす", layout)
status = ''

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == status:
        # sg.popup('同じ個所を押しました')
        continue

    if event in status_list.keys():
        status = event
        text_widget.update(value='前回の更新日時：' + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        current_status = status_list[event]
        RPC.update(start=time.time(), state=current_status[1], large_image=current_status[2])

window.close()
