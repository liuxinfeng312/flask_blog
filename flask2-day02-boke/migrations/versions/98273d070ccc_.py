"""empty message

Revision ID: 98273d070ccc
Revises: a0e9829f2d96
Create Date: 2019-04-19 19:40:20.011739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98273d070ccc'
down_revision = 'a0e9829f2d96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('backuser',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('backuser')
    # ### end Alembic commands ###
