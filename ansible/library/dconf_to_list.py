#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: dconf_to_list

short_description: Parse the file obtained with 'dconf dump /' and returns a list with all elements

version_added: "2.5"

description:
    - "Show status, scheduler, datanodes and more info of deployed frameworks in Marathon"

options:
    dconf_file:
        description:
            - path to file with dconf dump
        required: true
    paths_to_restore:
        description:
            - the module only returns elemets if the path is in this list
        required: false

author:
    - Oscar Hermosa (ohermosa@gmail.com)
'''

EXAMPLES = '''
# Get key and values from all paths of dconf dump
- name: "Get all paths"
  dconf_to_list:
    dconf_file: "/home/ohermosa/Dropbox/datio/gnome_dconf"

# Get Keys and values from several paths of dconf dump
- name: "Get interesting paths of dconf"
  dconf_to_list:
    dconf_file: "/home/ohermosa/Dropbox/datio/gnome_dconf"
    paths_to_restore:
      - com/gexperts/Tilix
      - org/gtk/settings/file-chooser
      - apps/update-manager
'''

RETURN = '''
message:
    description: The output message that the sample module generates
    type: list
    returned: always

    [
        {
            "key": "/system/proxy/autoconfig-url",
            "value": "'http://bbvapac.igrupobbva/accelerated_pac_base.pac'"
        },
        {
            "key": "/system/proxy/mode",
            "value": "'auto'"
        },
        {
            "key": "/org/gnome/settings-daemon/peripherals/keyboard/numlock-state",
            "value": "'on'"
        }
    ]
'''


def read_file(dconf_file):
    with open(dconf_file, "r") as f:
        return f.readlines()


def from_dconf_to_list(dconf_file, paths_to_restore):
    output = []
    lines = read_file(dconf_file)
    path = ""
    for line in lines:
        # Quitamos el '\n' del final de cada elemento de la lista
        line = line.replace('\n', '')
        if line.startswith('['):
            path = '/' + line[1:-1]
        elif '=' in line:
            if path in paths_to_restore or len(paths_to_restore) == 0:
                item = {
                    "key": path + '/' + line.split('=')[0],
                    "value": line.split('=')[1]
                }
                output.append(item)
        elif line == '':
            path = ""
    return output


def run_module():
    module_args = dict(
        paths_to_restore=dict(type='list'),
        dconf_file=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        message=list()
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        no_log=True
    )

    dconf_file = module.params["dconf_file"]

    if "paths_to_restore" in module.params.keys():
        paths_to_restore = module.params["paths_to_restore"]
        # En el fichero dconf, las rutas no empiezan por '/' asi que si algun elemento de la lista
        # empieza por '/' lo quitamos
        # (luego tenemos que comprobar si la ruta del fichero estar en esta lista)
        for item in paths_to_restore:
            if item.startswith('/'):
                item = item[1:]
    else:
        paths_to_restore = []

    output = from_dconf_to_list(dconf_file, paths_to_restore)
    result['message'] = output
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
