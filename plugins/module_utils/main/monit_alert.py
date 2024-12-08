from ansible.module_utils.basic import AnsibleModule

from ansible_collections.ansibleguy.opnsense.plugins.module_utils.base.api import \
    Session
from ansible_collections.ansibleguy.opnsense.plugins.module_utils.helper.main import \
    validate_int_fields
from ansible_collections.ansibleguy.opnsense.plugins.module_utils.base.cls import BaseModule
from ansible_collections.ansibleguy.opnsense.plugins.module_utils.helper.validate import \
    is_valid_email


class Alert(BaseModule):
    CMDS = {
        'add': 'addAlert',
        'del': 'delAlert',
        'set': 'setAlert',
        'search': 'get',
        'toggle': 'toggleAlert',
    }
    API_KEY_PATH = 'monit.alert'
    API_MOD = 'monit'
    API_CONT = 'settings'
    API_CONT_REL = 'service'
    FIELDS_CHANGE = ['recipient', 'not_on', 'events', 'format', 'reminder', 'description']
    FIELDS_ALL = ['enabled']
    FIELDS_ALL.extend(FIELDS_CHANGE)
    FIELDS_TRANSLATE = {
        'not_on': 'noton',
    }
    FIELDS_TYPING = {
        'bool': ['enabled', 'not_on'],
        'list': ['events'],
        'int': ['reminder'],
    }
    INT_VALIDATIONS = {
        'reminder': {'min': 0, 'max': 86400},
    }
    EXIST_ATTR = 'alert'

    def __init__(self, module: AnsibleModule, result: dict, session: Session = None):
        BaseModule.__init__(self=self, m=module, r=result, s=session)
        self.alert = {}

    def check(self) -> None:
        if self.p['state'] == 'present':
            validate_int_fields(module=self.m, data=self.p, field_minmax=self.INT_VALIDATIONS)

            if not is_valid_email(self.p['recipient']):
                self.m.fail_json(
                    f"The recipient value '{self.p['recipient']}' is not a "
                    f"valid email address!"
                )

        self._base_check()
