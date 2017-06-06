import click

from .tasks import update_logs as _update_logs


@click.group()
def cli():
    pass

@cli.command('update_logs')
@click.option('--contract',
              help='ID of the contracts')
@click.option('--block',
              help='Block number to update logs up to')
@click.option('--uri',
              help='URI of the database (e.g. postgresql://postgres:postgres@localhost:5432/postgres)')
def update_logs(contract, block, uri):
    """
    Update logs 
    """
    contract, from_block, to_block = _update_logs(contract, block, uri)
    block_count = to_block - from_block + 1
    output = "Correctly updated logs for contract [id=%s] at address %s from block %s to %s (total %s blocks)" % \
             (contract.id, contract.address, from_block, to_block, block_count)
    click.echo(click.style(output, fg='green', bold=True))