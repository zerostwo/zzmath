"""Increased string length

Revision ID: 81144126dd3b
Revises: eacfe2102d74
Create Date: 2020-11-30 15:36:09.235078

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '81144126dd3b'
down_revision = 'eacfe2102d74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('changeLog', 'test')
    op.alter_column('feedback', 'contact_details',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=1000),
               existing_nullable=True)
    op.alter_column('feedback', 'description',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=1000),
               existing_nullable=True)
    op.alter_column('feedback', 'is_resolved',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=1000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('feedback', 'is_resolved',
               existing_type=sa.String(length=1000),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=True)
    op.alter_column('feedback', 'description',
               existing_type=sa.String(length=1000),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('feedback', 'contact_details',
               existing_type=sa.String(length=1000),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=True)
    op.add_column('changeLog', sa.Column('test', mysql.VARCHAR(length=16), nullable=True))
    # ### end Alembic commands ###