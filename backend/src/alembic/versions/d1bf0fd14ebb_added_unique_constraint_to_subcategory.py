"""Added unique constraint to subcategory

Revision ID: d1bf0fd14ebb
Revises: d557b7d951d9
Create Date: 2024-06-19 11:36:12.171902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1bf0fd14ebb'
down_revision: Union[str, None] = 'd557b7d951d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'buys', ['id'])
    op.create_unique_constraint(None, 'categories', ['id'])
    op.create_unique_constraint(None, 'subcategories', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subcategories', type_='unique')
    op.drop_constraint(None, 'categories', type_='unique')
    op.drop_constraint(None, 'buys', type_='unique')
    # ### end Alembic commands ###
