"""Create phone number for user column

Revision ID: e12d14c0c2e0
Revises: 
Create Date: 2024-07-31 16:46:56.140500

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e12d14c0c2e0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String, nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
