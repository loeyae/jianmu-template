from reactivity import ref, computed, watch, watch_effect
from .utils.p import fig, plot_cnt, plot_title
from jianmu import File, beep, open_external, open_path, show_error_box, show_item_in_folder, show_message_box, show_open_dialog, show_save_dialog, trash_item
import pandas as pd
import os
import logging.config

cpath = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath('../')
if not os.path.exists(os.path.join(project_dir, 'log')):
    os.mkdir(os.path.join(project_dir, 'log'), 0o777)
logging.config.fileConfig(os.path.join(project_dir, 'logging.conf'))
logger = logging.getLogger('root')


header_index = ref('jianmu-template')


def handle_header_select(index):
    header_index.value = index


aside_index = ref('1')


def handle_aside_select(index):
    aside_index.value = index


count = ref(0)
# 创建一个响应式变量 name，初始值为 'World'
name = ref('World')
# 创建一个响应式变量 result
result = computed(lambda: {
    'message': f'Hello {name.value}',
    'count': count.value,
})


def add_count():
    count.value += 1
    # print(f'count is {count.value} now')


sentence = ref('他叫汤姆去拿外衣')


def getter():
    return list(sentence.value)


sent_split = computed(getter)


def test_message_box():
    result = show_message_box({'message': 'message', 'type': 'info'})
    print('test_message_box result:', result)


def test_error_box():
    show_error_box('error', 'error message')
    print('test_error_box has been clicked')


def test_beep():
    beep()


def test_save_dialog():
    result = show_save_dialog()
    if result['canceled']:
        return
    file_path: str = result['filePath']
    file_path = file_path if file_path.endswith('.txt') else f'{file_path}.txt'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('Hello World!')


test_file_path = ref('')


def test_open_dialog():
    result = show_open_dialog()
    if result['canceled']:
        return
    test_file_path.value = result['filePaths'][0]
    print(test_file_path.value)


def test_show_item_in_folder():
    if not test_file_path.value:
        show_error_box('错误', 'test_file_path 的值为空')
        return
    show_item_in_folder(test_file_path.value)


def test_open_path():
    if not test_file_path.value:
        show_error_box('错误', 'test_file_path 的值为空')
        return
    open_path(test_file_path.value)


def test_open_external():
    open_external('http://www.bnu.edu.cn')


def test_trash_item():
    if not test_file_path.value:
        show_error_box('错误', 'test_file_path 的值为空')
        return
    trash_item(test_file_path.value)
    show_message_box({'message': f'{test_file_path.value} 已删除'})


file_list = ref([])

file_content_list = ref([])


def file_list_update():
    tmp = []
    for file in file_list.value:
        raw: File = file['raw']
        if raw.type == 'text/plain':
            text = raw.bytes.decode('utf-8')
            tmp.append(text)
        elif raw.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            df = pd.read_excel(raw.bytes)
            tmp.append(df.to_markdown())
    file_content_list.value = tmp


watch(file_list, file_list_update)


def clear_file():
    file_list.value = []
