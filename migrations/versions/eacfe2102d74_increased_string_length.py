"""Increased string length


Revision ID: eacfe2102d74
Revises: 57bec17e94c8
Create Date: 2020-11-30 15:31:51.709537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eacfe2102d74'
down_revision = '57bec17e94c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('changeLog', sa.Column('test', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('changeLog', 'test')
    # ### end Alembic commands ###
