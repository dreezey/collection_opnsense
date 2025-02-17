#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (C) 2024, AnsibleGuy <guy@ansibleguy.net>
# GNU General Public License v3.0+ (see https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.ansibleguy.opnsense.plugins.module_utils.base.handler import \
    module_dependency_error, MODULE_EXCEPTIONS

try:
    from ansible_collections.ansibleguy.opnsense.plugins.module_utils.helper.wrapper import module_wrapper
    from ansible_collections.ansibleguy.opnsense.plugins.module_utils.defaults.main import \
        OPN_MOD_ARGS, STATE_ONLY_MOD_ARG, RELOAD_MOD_ARG_DEF_FALSE
    from ansible_collections.ansibleguy.opnsense.plugins.module_utils.main.nginx_upstream_server import UpstreamServer

except MODULE_EXCEPTIONS:
    module_dependency_error()


# DOCUMENTATION = 'https://opnsense.ansibleguy.net/modules/nginx.html'
# EXAMPLES = 'https://opnsense.ansibleguy.net/modules/nginx.html'


def run_module():
    module_args = dict(
        description=dict(type='str', alias=['name'], required=True, aliases=['name']),
        server=dict(type='str', required=False),
        port=dict(type='int', required=False),
        priority=dict(type='int', required=False),
        max_conns=dict(type='int', required=False),
        max_fails=dict(type='int', required=False),
        fail_timeout=dict(type='int', required=False),
        no_use=dict(
            type='str', required=False, choices=['', 'down', 'backup'], default='',
        ),
        **RELOAD_MOD_ARG_DEF_FALSE,
        **STATE_ONLY_MOD_ARG,
        **OPN_MOD_ARGS,
    )

    result = dict(
        changed=False,
        diff={
            'before': {},
            'after': {},
        }
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )


    module_wrapper(UpstreamServer(module=module, result=result))
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
