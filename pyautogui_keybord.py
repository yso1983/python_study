import pyautogui

pyautogui.write('hello world!') # 괄호 안의 문자를 타이핑 합니다.
pyautogui.write('hello world!', interval=0.25) # 각 문자를 0.25마다 타이핑합니다. 

#주의사항 pyautogui 는 한글에 대한 적용이 안되어 있어요!!
#한글을 입력하려면, pyperclip 모듈을 통해서 한글을 복사 후 입력할 수 있습니다.

import pyperclip

pyperclip.copy("안녕하세요") # 클립보드에 텍스트를 복사합니다. 
pyautogui.hotkey('ctrl', 'v') # 붙여넣기 (hotkey 설명은 아래에 있습니다.)

pyautogui.press('shift') # shift 키를 누릅니다.
pyautogui.press('ctrl') # ctrl 키를 누릅니다. 

pyautogui.keyDown('ctrl') # ctrl 키를 누른 상태를 유지합니다.
pyautogui.press('c') # c key를 입력합니다. 
pyautogui.keyUp('ctrl') # ctrl 키를 뗍니다. 

pyautogui.press(['left', 'left', 'left']) # 왼쪽 방향키를 세번 입력합니다.
pyautogui.press('left', presses=3) # 왼쪽 방향키를 세번 입력합니다. 
pyautogui.press('enter', presses=3, interval=3) # enter 키를 3초에 한번씩 세번 입력합니다. 