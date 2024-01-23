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
    [sg.Radio('進捗してる', 'status', enable_events=True, key='active'),
     sg.Radio('ぼんやり', 'status', enable_events=True, key='space_out'),
     sg.Radio('寝てる', 'status', enable_events=True, key='sleeping')]
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

    if event in ['active', 'space_out', 'sleeping']:
        status = event
        text_widget.update(value='前回の更新日時：' + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

    if event == 'active':
        RPC.update(start=time.time(),state="進捗してる♪",large_image="active")
    elif event == 'space_out':
        RPC.update(start=time.time(),state="ぼんやりしてます。",large_image="yukatayu")
    elif event == 'sleeping':
        RPC.update(start=time.time(),state="寝ています💕",large_image="sleeping")

window.close()
