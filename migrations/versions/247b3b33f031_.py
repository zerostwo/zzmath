"""empty message

Revision ID: 247b3b33f031
Revises: 
Create Date: 2020-03-10 13:48:40.852163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '247b3b33f031'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userModel',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userName', sa.String(length=16), nullable=True),
    sa.Column('userDescription', sa.String(length=128), nullable=True),
    sa.Column('userID', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('userName')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userModel')
    # ### end Alembic commands ###