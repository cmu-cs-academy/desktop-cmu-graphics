# Each link should point to a wheel for this version of the module
# This script should be run from the cmu_graphics_helpers_loader folder

import subprocess

# Links come from the pypi "download files" page for cmu_graphics_helpers-ce

links = {
    'cmu_graphics_helpers_mac_315': 'https://test-files.pythonhosted.org/packages/34/09/16d6822bfc42cf762f94be830592f6cc13d54823384d5526fbe0cc52ff6d/cmu_graphics_helpers-0.1.2-cp37-abi3-macosx_10_12_x86_64.whl',
    'cmu_graphics_helpers_mac_arm_315': 'https://test-files.pythonhosted.org/packages/02/81/62919ee060b3b23aea27cda49871177272793fa89684a162adb257d1b630/cmu_graphics_helpers-0.1.2-cp37-abi3-macosx_11_0_arm64.whl',
    'cmu_graphics_helpers_win_64_315': 'https://test-files.pythonhosted.org/packages/b0/30/b87cf4286d93f8417643abc8e9a8a5575f4a8358fe865091505fdd49316f/cmu_graphics_helpers-0.1.2-cp37-abi3-win_amd64.whl',
}

def run_command(args):
    print(f'Running command: {" ".join(args)}')
    subprocess.Popen(args).wait()

def make_module(module_name):
    link = links[module_name]
    filename = link.split('/')[-1]

    run_command(['wget', link])
    run_command(['mv', filename, 'cmu_graphics_helpers.zip'])
    run_command(['mkdir', 'cmu_graphics_helpers'])
    run_command(['unzip', 'cmu_graphics_helpers.zip', '-d', 'cmu_graphics_helpers'])
    run_command(['mkdir', f'modules/{module_name}'])
    run_command(['mv', 'cmu_graphics_helpers/cmu_graphics_helpers', f'modules/{module_name}/cmu_graphics_helpers'])
    run_command(['rm', '-rf', f'modules/{module_name}/cmu_graphics_helpers/docs'])
    run_command(['rm', '-rf', f'modules/{module_name}/cmu_graphics_helpers/examples'])
    run_command(['rm', '-rf', f'modules/{module_name}/cmu_graphics_helpers/tests'])
    run_command(['rm', '-rf', 'cmu_graphics_helpers'])
    run_command(['rm', 'cmu_graphics_helpers.zip'])

for module in links:
    if links[module]:
        make_module(module)
