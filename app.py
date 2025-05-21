import requests
import FreeSimpleGUI as sg

sg.theme('DarkGray15')


layout_fixo = [
    [sg.Text('Ache a letra de sua música!', size=(40, 1), justification='center')],
    [sg.Text('Coloque Sua Banda!', size=(40, 1), justification='center')],
    [sg.Input(key='banda', size=(40, 1))],
    [sg.Text('Coloque Sua Música!', size=(40, 1), justification='center')],
    [sg.Input(key='musica', size=(40, 1))],
    [sg.Push(), sg.Button('Buscar'), sg.Button('Sair'), sg.Push()]
]


layout_letra = [
    [sg.Multiline('', key='-OUTPUT-', size=(50, 10), disabled=True, autoscroll=True)]
]


layout = layout_fixo + layout_letra

window = sg.Window('Letra de Música', layout, finalize=True, element_justification='c')

while True:
    evento, valores = window.read()
    
    if evento == sg.WIN_CLOSED:
        break
        
    if evento == 'Buscar':
        if not valores['banda'] or not valores['musica']:
            window['-OUTPUT-'].update('Preencha todos os campos!')
            continue
        try:
            banda = valores['banda']
            musica = valores['musica']
            url = f'https://api.lyrics.ovh/v1/{banda}/{musica}'
            response = requests.get(url)
            lyrics = response.json()['lyrics']
            window['-OUTPUT-'].update(lyrics)
        except Exception as e:
            window['-OUTPUT-'].update(f'Erro ao buscar letra: {str(e)}')
    if evento == 'Sair':
        break

window.close()