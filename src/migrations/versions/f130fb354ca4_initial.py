"""initial

Revision ID: f130fb354ca4
Revises: a96ed004f5a5
Create Date: 2024-07-07 11:11:23.729510

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f130fb354ca4'
down_revision: Union[str, None] = 'a96ed004f5a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hero', 'surname')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hero', sa.Column('surname', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###