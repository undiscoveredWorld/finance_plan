"""Added ReportsConfig

Revision ID: f7d9e1f6dfec
Revises: d1bf0fd14ebb
Create Date: 2024-06-20 17:15:48.465654

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7d9e1f6dfec'
down_revision: Union[str, None] = 'd1bf0fd14ebb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'report_configs', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'report_configs', type_='unique')
    # ### end Alembic commands ###
