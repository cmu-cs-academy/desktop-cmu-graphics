# Each link should point to a wheel for this version of the module
# This script should be run from the pil_image_loader folder

import subprocess

links = {
    'pil_mac_312': 'https://files.pythonhosted.org/packages/37/d5/2c00228ace73a7855a52053a92fdd6cea9b22393fbf3961125c11829dcd2/pillow-10.2.0-cp312-cp312-macosx_10_10_x86_64.whl',
    'pil_mac_arm_312': 'https://files.pythonhosted.org/packages/9d/a0/28756da34d6b58c3c5f6c1d5589e4e8f4e73472b55875524ae9d6e7e98fe/pillow-10.2.0-cp312-cp312-macosx_11_0_arm64.whl',
    'pil_win_32_312': 'https://files.pythonhosted.org/packages/ce/a7/11a539c1e12dfb9d67c35e5d3d99c7a6853face9083e6483360f4d9cd1d8/pillow-10.2.0-cp312-cp312-win32.whl',
    'pil_win_64_312': 'https://files.pythonhosted.org/packages/51/07/7e9266a59bb267b56c1f432f6416653b9a78dda771c57740d064a8aa2a44/pillow-10.2.0-cp312-cp312-win_amd64.whl',
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
