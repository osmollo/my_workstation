#!/usr/bin/python

import requests
import random
from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: protonvpn_fastest

short_description: return a list with the fastest servers of protonvpn

version_added: "2.5"

description:
    - "return a list with the fastest servers of protonvpn"

options:
    servers:
        description:
            - list of protonvpnservers
        required: true
    tier:
        description:
            - protonvpn user tier
        required: true

author:
    - Oscar Hermosa (osmollo@proton.me)
'''

EXAMPLES = '''
    - uri:
        url: https://api.protonvpn.ch/vpn/logicals
        register: uri_response

    - protonvpn_fastest:
        servers: '{{ uri_response.json["LogicalServers"] }}'
        tier: 0
        register: fastest_response

    - debug: var=fastest_response.fastest
'''

RETURN = '''
fastest:
    description: The fastest protonvpn servers IP
    type: list
    returned: always
'''

def get_server_value(servername, key, servers):
    """Return the value of a key for a given server."""
    value = [server[key] for server in servers if server['Name'] == servername]
    return value[0]

def get_fastest_server(server_pool):
    """Return the fastest server from a list of servers"""

    # Sort servers by "speed" and select top n according to pool_size
    fastest_pool = sorted(
        server_pool, key=lambda server: server["Score"]
    )
    if len(fastest_pool) >= 50:
        pool_size = 4
    else:
        pool_size = 1

    fastest_server = random.choice(fastest_pool[:pool_size])["Name"]
    return fastest_server


def get_fastest(servers=[], tier=0):
    """Return a list of fastest servers for the users Tier."""

    excluded_features = [1, 2]
    server_pool = []
    for server in servers:
        if server["Features"] not in excluded_features and server["Tier"] <= tier and server["Status"] == 1:
            server_pool.append(server)

    fastest_server = get_fastest_server(server_pool)

    subservers = get_server_value(fastest_server, "Servers", servers)
    return [subserver["EntryIP"] for subserver in subservers]


def run_module():
    module_args = dict(
        servers=dict(type='list', required=True),
        tier=dict(type='int', required=True)
    )

    result = dict(
        changed=False,
        fastest=list
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result['fastest'] = get_fastest(servers=module.params["servers"],
                                    tier=module.params["tier"])
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
