# Each link should point to a wheel for this version of the module
# This script should be run from the pil_image_loader folder

import subprocess

links = {
    'pil_mac_313': 'https://files.pythonhosted.org/packages/79/30/77f54228401e84d6791354888549b45824ab0ffde659bafa67956303a09f/pillow-11.1.0-cp313-cp313t-macosx_10_13_x86_64.whl',
    'pil_mac_arm_313': 'https://files.pythonhosted.org/packages/ce/b1/56723b74b07dd64c1010fee011951ea9c35a43d8020acd03111f14298225/pillow-11.1.0-cp313-cp313t-macosx_11_0_arm64.whl',
    'pil_win_32_313': 'https://files.pythonhosted.org/packages/e5/fb/a7960e838bc5df57a2ce23183bfd2290d97c33028b96bde332a9057834d3/pillow-11.1.0-cp313-cp313t-win32.whl',
    'pil_win_64_313': 'https://files.pythonhosted.org/packages/d7/6c/6ec83ee2f6f0fda8d4cf89045c6be4b0373ebfc363ba8538f8c999f63fcd/pillow-11.1.0-cp313-cp313t-win_amd64.whl',
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
