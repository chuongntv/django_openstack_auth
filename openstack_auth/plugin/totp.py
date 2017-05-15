# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging

from keystoneauth1.identity import v3 as v3_auth

from openstack_auth import utils
from openstack_auth.plugin import base

LOG = logging.getLogger(__name__)

__all__ = ['TotpPlugin']


class TotpPlugin(base.BasePlugin):
    """Authenticate against keystone given a username and passcode.

    This is the login mechanism. Given a username and password inputted
    from a login form returns a v3 keystone TOTP plugin for
    authentication.
    """

    def get_plugin(self, auth_url=None, username=None, password=None, passcode=None,
                   user_domain_name=None, **kwargs):
        if not all((auth_url, username, password)):
            return None

        LOG.debug('Attempting to authenticate with totp for %s', username)

        return v3_auth.TOTP(auth_url=auth_url,
                            username=username,
                            password=password,
                            passcode=passcode,
                            user_domain_name=user_domain_name,
                            unscoped=True)
