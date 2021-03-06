"""Display a list of available chassis."""
# :license: MIT, see LICENSE for more details.

import SoftLayer
from SoftLayer.CLI import environment
from SoftLayer.CLI import formatting

import click


@click.command()
@environment.pass_env
def cli(env):
    """Display a list of available chassis."""

    table = formatting.Table(['code', 'chassis'])
    table.align['code'] = 'r'
    table.align['chassis'] = 'l'

    mgr = SoftLayer.HardwareManager(env.client)
    chassis_list = mgr.get_available_dedicated_server_packages()

    for code, name, _ in chassis_list:
        table.add_row([code, name])

    return table
