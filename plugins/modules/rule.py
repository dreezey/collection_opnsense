#!/usr/bin/python3

# Copyright: (C) 2022, AnsibleGuy <guy@ansibleguy.net>
# GNU General Public License v3.0+ (see https://www.gnu.org/licenses/gpl-3.0.txt)

# see: https://docs.opnsense.org/development/api/plugins/firewall.html

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.ansibleguy.opnsense.plugins.module_utils.rule_defaults import RULE_MOD_ARGS
from ansible_collections.ansibleguy.opnsense.plugins.module_utils.helper import diff_remove_empty
from ansible_collections.ansibleguy.opnsense.plugins.module_utils.rule_obj import Rule


DOCUMENTATION = 'https://github.com/ansibleguy/collection_opnsense/blob/stable/docs/use_rule.md'
EXAMPLES = 'https://github.com/ansibleguy/collection_opnsense/blob/stable/docs/use_rule.md'


def run_module():
    result = dict(
        changed=False,
        diff={
            'before': {},
            'after': {},
        },
    )

    module = AnsibleModule(
        argument_spec=RULE_MOD_ARGS,
        supports_check_mode=True,
    )

    rule = Rule(module=module, result=result)
    rule.check()
    rule.process()

    rule.s.close()
    result['diff'] = diff_remove_empty(result['diff'])
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
