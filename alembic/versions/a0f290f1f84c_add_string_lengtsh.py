"""Add string lengtsh

Revision ID: a0f290f1f84c
Revises: 317e55321763
Create Date: 2024-05-31 23:17:54.525301

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'a0f290f1f84c'
down_revision: Union[str, None] = '317e55321763'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contracts', sa.Column('contract_number', sa.String(length=50), nullable=False))
    op.alter_column('workers', 'middlename',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('workers', 'middlename',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.drop_column('contracts', 'contract_number')
    # ### end Alembic commands ###