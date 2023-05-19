# Each link should point to a wheel for this version of the module
# This script should be run from the pygame_loader folder

import subprocess

links = {
    'pil_mac_311': 'https://files.pythonhosted.org/packages/78/a8/3c2d737d856eb9cd8c18e78f6fe0ed08a2805bded74cbb0455584859023b/Pillow-9.5.0-cp311-cp311-macosx_10_10_x86_64.whl',
    'pil_mac_arm_311': 'https://files.pythonhosted.org/packages/a9/15/310cde63cb15a091de889ded26281924cf9cfa5c000b36b06bd0c7f50261/Pillow-9.5.0-cp311-cp311-macosx_11_0_arm64.whl',
    'pil_win_32_311': 'https://files.pythonhosted.org/packages/46/a0/e410f655300932308e70e883dd60c0c51e6f74bed138641ea9193e64fd7c/Pillow-9.5.0-cp311-cp311-win32.whl',
    'pil_win_64_311': 'https://files.pythonhosted.org/packages/0c/02/7729c8aecbc525b560c7eb283ffa34c6f5a6d0ed6d1339570c65a3e63088/Pillow-9.5.0-cp311-cp311-win_amd64.whl',
}

def run_command(args):
    subprocess.Popen(args).wait()

def make_module(module_name):
    link = links[module_name]
    filename = link.split('/')[-1]

    run_command(['wget', link])
    run_command(['mv', filename, 'PIL.zip'])
    run_command(['mkdir', 'PIL'])
    run_command(['unzip', 'PIL.zip', '-d', 'PIL'])
    run_command(['mkdir', f'modules/{module_name}'])
    run_command(['mv', 'PIL/PIL', f'modules/{module_name}/PIL'])
    run_command(['rm', '-rf', 'PIL'])
    run_command(['rm', 'PIL.zip'])

for module in links:
    if links[module]:
        make_module(module)
