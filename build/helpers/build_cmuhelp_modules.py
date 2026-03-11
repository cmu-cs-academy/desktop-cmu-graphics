# Each link should point to a wheel for this version of the module
# This script should be run from the cmu_graphics_helpers_loader folder

import subprocess

# Links come from the pypi "download files" page for cmu_graphics_helpers-ce

links = {
    'cmu_graphics_helpers_mac': 'fill me in',
    'cmu_graphics_helpers_mac_arm': 'fill me in',
    'cmu_graphics_helpers_win_64': 'fill me in',
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
