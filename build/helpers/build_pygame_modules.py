# Each link should point to a wheel for this version of the module
# This script should be run from the pygame_loader folder

import subprocess

links = {
    'pygame_mac_315': 'fill me in',
    'pygame_mac_arm_315': 'fill me in',
    'pygame_win_32_315': 'fill me in',
    'pygame_win_64_315': 'fill me in',
}

# Links come from the pypi "download files" page and look like
# https://files.pythonhosted.org/packages/7e/11/17f7f319ca91824b86557e9303e3b7a71991ef17fd45286bf47d7f0a38e6/pygame-2.6.1-cp313-cp313-win_amd64.whl

def run_command(args):
    print(f'Running command: {" ".join(args)}')
    subprocess.Popen(args).wait()

def make_module(module_name):
    link = links[module_name]
    filename = link.split('/')[-1]

    run_command(['wget', link])
    run_command(['mv', filename, 'pygame.zip'])
    run_command(['mkdir', 'pygame'])
    run_command(['unzip', 'pygame.zip', '-d', 'pygame'])
    run_command(['mkdir', f'modules/{module_name}'])
    run_command(['mv', 'pygame/pygame', f'modules/{module_name}/pygame'])
    run_command(['rm', '-rf', f'modules/{module_name}/pygame/docs'])
    run_command(['rm', '-rf', f'modules/{module_name}/pygame/examples'])
    run_command(['rm', '-rf', f'modules/{module_name}/pygame/tests'])
    run_command(['rm', '-rf', 'pygame'])
    run_command(['rm', 'pygame.zip'])

for module in links:
    if links[module]:
        make_module(module)
