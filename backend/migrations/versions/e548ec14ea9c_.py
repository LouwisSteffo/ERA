"""empty message

Revision ID: e548ec14ea9c
Revises: 3799c4b15972
Create Date: 2024-02-07 15:40:16.762194

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e548ec14ea9c'
down_revision = '3799c4b15972'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pengguna', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nama_pengguna', sa.String(length=100), nullable=False))
        batch_op.drop_column('nama_pelanggan')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pengguna', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nama_pelanggan', mysql.VARCHAR(length=100), nullable=False))
        batch_op.drop_column('nama_pengguna')

    # ### end Alembic commands ###