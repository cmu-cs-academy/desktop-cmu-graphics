# Each link should point to a wheel for this version of the module
# This script should be run from the pygame_loader folder

import subprocess

links = {
    'pygame_mac_36': '',
    'pygame_mac_36': '',
    'pygame_mac_37': '',
    'pygame_mac_38': '',
    'pygame_mac_39': '',
    'pygame_mac_310': 'https://files.pythonhosted.org/packages/7b/42/39f655a232b92936b23fc1c801b8ed8a64cad644ad82616754402ec3d495/pygame-2.0.3-cp310-cp310-macosx_10_9_x86_64.whl',
    'pygame_win_32_35': '',
    'pygame_win_32_36': '',
    'pygame_win_32_37': '',
    'pygame_win_32_38': '',
    'pygame_win_32_39': '',
    'pygame_win_32_310': 'https://files.pythonhosted.org/packages/cf/10/c30f258bd56b4d3c221e735ef1eb050910259fae708ee259e58427a4d9ba/pygame-2.0.3-cp310-cp310-win32.whl',
    'pygame_win_64_35': '',
    'pygame_win_64_36': '',
    'pygame_win_64_37': '',
    'pygame_win_64_38': '',
    'pygame_win_64_39': '',
    'pygame_win_64_310': 'https://files.pythonhosted.org/packages/5e/9b/e91f2ef1a843be0b75a8660037fd0562fb38b41018fc0d08adb204a575b3/pygame-2.0.3-cp310-cp310-win_amd64.whl',
}

def run_command(args):
    subprocess.Popen(args).wait()

def make_module(module_name):
    link = links[module_name]
    filename = link.split('/')[-1]

    run_command(['wget', link])
    run_command(['mv', filename, 'pygame.zip'])
    run_command(['mkdir', 'pygame'])
    run_command(['unzip', 'pygame.zip', '-d', 'pygame'])
    run_command(['mv', 'pygame/pygame', f'modules/{module_name}'])
    run_command(['rm', '-rf', 'pygame'])
    run_command(['rm', 'pygame.zip'])

for module in links:
    if links[module]:
        make_module(module)
