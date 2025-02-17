#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (C) 2024, AnsibleGuy <guy@ansibleguy.net>
# GNU General Public License v3.0+ (see https://www.gnu.org/licenses/gpl-3.0.txt)

# see: https://docs.opnsense.org/development/api/core/routing.html

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.ansibleguy.opnsense.plugins.module_utils.base.handler import \
    module_dependency_error, MODULE_EXCEPTIONS

try:
    from ansible_collections.ansibleguy.opnsense.plugins.module_utils.helper.wrapper import module_wrapper
    from ansible_collections.ansibleguy.opnsense.plugins.module_utils.defaults.main import \
        OPN_MOD_ARGS, STATE_MOD_ARG, RELOAD_MOD_ARG
    from ansible_collections.ansibleguy.opnsense.plugins.module_utils.main.gateway import Gw

except MODULE_EXCEPTIONS:
    module_dependency_error()


# DOCUMENTATION = 'https://opnsense.ansibleguy.net/modules/routing.html'
# EXAMPLES = 'https://opnsense.ansibleguy.net/modules/routing.html'


def run_module():
    module_args = dict(
        name=dict(
            type='str', required=False,
            description='Gateway Name'
        ),
        interface=dict(
            type='str', required=False, aliases=['int', 'if'],
            description='Interface for Gateway'
        ),
        gateway=dict(
            type='str', required=False, aliases=['gw', 'ip'],
            description='Gateway IP'
        ),
        default_gw=dict(
            type='bool', required=False, aliases=['default', 'internet', 'inet'],
            description='This will select the above gateway as a default gateway candidate.',
            default=False
        ),
        far_gw=dict(
            type='bool', required=False, aliases=['far'],
            description='This will allow the gateway to exist outside of the interface subnet.',
            default=False
        ),
        monitor_disable=dict(
            type='bool', required=False,
            description='This will consider this gateway as always being "up".',
            default=True
        ),
        monitor_noroute=dict(
            type='bool', required=False,
            description='Do not create a dedicated host route for this monitor.',
            default=False
        ),
        monitor=dict(
            type='str', required=False,
            description='Enter an alternative address here to be used to monitor the link. '
                        'This is used for the quality RRD graphs as well as the load balancer entries. '
                        'Use this if the gateway does not respond to ICMP echo requests (pings).'
        ),
        force_down=dict(
            type='bool', required=False, aliases=['down'],
            description='This will force this gateway to be considered "down".',
            default=False
        ),
        priority=dict(
            type='int', required=False, aliases=['prio'],
            description='Choose a value between 1 and 255. Influences sort order when selecting a (default) gateway, '
                        'lower means more important. Default is 255.',
            default=255
        ),
        weight=dict(
            type='int', required=False,
            description='Weight for this gateway when used in a gateway group. '
                        'Specificed as an integer number between 1 and 5. Default equals 1.',
            default=1
        ),
        latency_low=dict(
            type='int', required=False,
            description='Low threshold for latency in milliseconds. Default is 200.',
            default=200
        ),
        latency_high=dict(
            type='int', required=False,
            description='High threshold for latency in milliseconds. Default is 500.',
            default=500
        ),
        loss_low=dict(
            type='int', required=False,
            description='Low threshold for packet loss in %. Default is 10.',
            default=10
        ),
        loss_high=dict(
            type='int', required=False,
            description='High thresholds for packet loss in %. Default is 20.',
            default=20
        ),
        interval=dict(
            type='int', required=False,
            description='How often that an ICMP probe will be sent in seconds. Default is 1.',
            default=1
        ),
        time_period=dict(
            type='int', required=False,
            description='The time period over which results are averaged. Default is 60.',
            default=60
        ),
        loss_interval=dict(
            type='int', required=False,
            description='Time interval before packets are treated as lost. '
                        'Default is 4 (four times the probe interval).',
            default=4
        ),
        data_length=dict(
            type='int', required=False,
            description='Specify the number of data bytes to be sent. Default is 0.',
            default=0
        ),
        description=dict(type='str', required=False, aliases=['desc']),
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

    module_wrapper(Gw(module=module, result=result))
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
