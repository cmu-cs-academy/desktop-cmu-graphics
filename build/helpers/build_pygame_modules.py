# Each link should point to a wheel for this version of the module
# This script should be run from the pygame_loader folder

import subprocess

links = {
    'pygame_mac_312': 'https://files.pythonhosted.org/packages/48/05/5fc3ee405cee85308f1dd5c0fb7bd0835256969a22b18a55698ffaf498ac/pygame-2.5.2-cp312-cp312-macosx_10_9_x86_64.whl',
    'pygame_mac_arm_312': 'https://files.pythonhosted.org/packages/4c/0b/90b489ae7fc363020d6d18d3e4522b6021f4e0e84fbdd28c1d468c8a8e31/pygame-2.5.2-cp312-cp312-macosx_11_0_arm64.whl',
    'pygame_win_32_312': 'https://files.pythonhosted.org/packages/05/28/5ca545423d6bb55f7ba9d09904c963ced15178f072551629a46b5499d105/pygame-2.5.2-cp312-cp312-win32.whl',
    'pygame_win_64_312': 'https://files.pythonhosted.org/packages/66/57/1311ff5bbd64093795f64c66910bbc12b7c5d83ca95766cce7ba501ff7e7/pygame-2.5.2-cp312-cp312-win_amd64.whl',
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
