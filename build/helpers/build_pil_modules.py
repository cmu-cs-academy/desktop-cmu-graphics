# This script should be run from the pil_image_loader folder

import subprocess

# Each link should point to a wheel for this version of the module
# Note: Make sure you're not using the `-t` version of these builds.
# Our guess is that these are for free-threaded Python builds, but if you're
# not using a free-threaded build, the `-t` binaries don't work.
links = {
    'pil_mac_313': 'https://files.pythonhosted.org/packages/b3/31/9ca79cafdce364fd5c980cd3416c20ce1bebd235b470d262f9d24d810184/pillow-11.1.0-cp313-cp313-macosx_10_13_x86_64.whl',
    'pil_mac_arm_313': 'https://files.pythonhosted.org/packages/ac/0f/ff07ad45a1f172a497aa393b13a9d81a32e1477ef0e869d030e3c1532521/pillow-11.1.0-cp313-cp313-macosx_11_0_arm64.whl',
    'pil_win_32_313': 'https://files.pythonhosted.org/packages/33/48/19c2cbe7403870fbe8b7737d19eb013f46299cdfe4501573367f6396c775/pillow-11.1.0-cp313-cp313-win32.whl',
    'pil_win_64_313': 'https://files.pythonhosted.org/packages/3b/ad/285c556747d34c399f332ba7c1a595ba245796ef3e22eae190f5364bb62b/pillow-11.1.0-cp313-cp313-win_amd64.whl',
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
