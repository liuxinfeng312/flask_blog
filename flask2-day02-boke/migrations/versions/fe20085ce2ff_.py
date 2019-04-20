"""empty message

Revision ID: fe20085ce2ff
Revises: 98273d070ccc
Create Date: 2019-04-19 21:10:32.396605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe20085ce2ff'
down_revision = '98273d070ccc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('time', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'time')
    # ### end Alembic commands ###