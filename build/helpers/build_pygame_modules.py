# Each link should point to a wheel for this version of the module
# This script should be run from the pygame_loader folder

import subprocess

links = {
    'pygame_mac_311': 'https://files.pythonhosted.org/packages/13/36/97b13be0f1f715b70afa9d13a70c1709959611507de03696d1db2ca60b1b/pygame-2.4.0-cp311-cp311-macosx_10_9_x86_64.whl',
    'pygame_mac_arm_311': 'https://files.pythonhosted.org/packages/4c/53/29ba6c1472b1285d4925e29dda6b7ca8248c12e5702708caedf8b1ac9fb9/pygame-2.4.0-cp311-cp311-macosx_11_0_arm64.whl',
    'pygame_win_32_311': 'https://files.pythonhosted.org/packages/75/ef/8a2f68857149860bd74be79395dfd0c4556f8c6a40f75efc20d783dd3f59/pygame-2.4.0-cp311-cp311-win32.whl',
    'pygame_win_64_311': 'https://files.pythonhosted.org/packages/09/0a/7ba8a50463c289763ab67cde3edf76bfdf9d095b578f9e0782a47ec89c76/pygame-2.4.0-cp311-cp311-win_amd64.whl',
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
    run_command(['mkdir', f'modules/{module_name}'])
    run_command(['mv', 'pygame/pygame', f'modules/{module_name}/pygame'])
    run_command(['rm', '-rf', 'pygame'])
    run_command(['rm', 'pygame.zip'])

for module in links:
    if links[module]:
        make_module(module)
