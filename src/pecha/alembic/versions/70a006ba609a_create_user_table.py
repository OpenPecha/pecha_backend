"""create user table

Revision ID: 70a006ba609a
Revises: 
Create Date: 2024-07-20 13:29:22.118998

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from _datetime import datetime
import _datetime

# revision identifiers, used by Alembic.
revision: str = '70a006ba609a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('username', sa.String(150), unique=True),
        sa.Column('email', sa.String(255), unique=True, index=True, nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('is_admin', sa.Boolean, default=False),
        sa.Column('is_active', sa.Boolean, default=False),
        sa.Column('date_joined', sa.DateTime, default=datetime.now(_datetime.UTC)),
        sa.Column('last_login', sa.DateTime, default=None)
    )


def downgrade() -> None:
    # Drop the users table
    op.drop_table('users')
