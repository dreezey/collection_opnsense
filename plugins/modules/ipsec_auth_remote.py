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
        OPN_MOD_ARGS, STATE_MOD_ARG, RELOAD_MOD_ARG
    from ansible_collections.ansibleguy.opnsense.plugins.module_utils.defaults.ipsec_auth import \
        IPSEC_AUTH_MOD_ARGS
    from ansible_collections.ansibleguy.opnsense.plugins.module_utils.main.ipsec_auth_remote import \
        Auth

except MODULE_EXCEPTIONS:
    module_dependency_error()


# DOCUMENTATION = 'https://opnsense.ansibleguy.net/modules/ipsec.html'
# EXAMPLES = 'https://opnsense.ansibleguy.net/modules/ipsec.html'


def run_module():
    module_args = dict(
        **IPSEC_AUTH_MOD_ARGS,
        **RELOAD_MOD_ARG,
        **STATE_MOD_ARG,
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

    module_wrapper(Auth(module=module, result=result))
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
