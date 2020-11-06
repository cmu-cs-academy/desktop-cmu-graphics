# Each link should point to a wheel for this version of the module
# This script should be run from the pygame_loader folder

import subprocess

links = {
    'pygame_mac_36': '',
    'pygame_mac_36': '',
    'pygame_mac_37': '',
    'pygame_mac_38': '',
    'pygame_mac_39': '',
    'pygame_win_32_35': '',
    'pygame_win_32_36': '',
    'pygame_win_32_37': '',
    'pygame_win_32_38': '',
    'pygame_win_32_39': '',
    'pygame_win_64_35': '',
    'pygame_win_64_36': '',
    'pygame_win_64_37': '',
    'pygame_win_64_38': '',
    'pygame_win_64_39': '',
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
    make_module(module)
