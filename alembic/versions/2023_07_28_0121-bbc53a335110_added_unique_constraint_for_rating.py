"""added unique constraint for rating

Revision ID: bbc53a335110
Revises: 161fdf1bc640
Create Date: 2023-07-28 01:21:14.581643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbc53a335110'
down_revision = '161fdf1bc640'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'ratings', ['book_id', 'user_name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'ratings', type_='unique')
    # ### end Alembic commands ###