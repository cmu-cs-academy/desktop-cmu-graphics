# Each link should point to a wheel for this version of the module
# This script should be run from the pygame_loader folder

import subprocess

# Links come from the pypi "download files" page for pygame-ce

links = {
    'pygame_mac_315': 'fill me in',
    'pygame_mac_arm_315': 'fill me in',
    'pygame_win_32_315': 'fill me in',
    'pygame_win_64_315': 'fill me in',
}

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
