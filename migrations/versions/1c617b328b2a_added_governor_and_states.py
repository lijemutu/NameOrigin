"""added governor and states

Revision ID: 1c617b328b2a
Revises: 
Create Date: 2022-02-26 12:04:25.682959

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1c617b328b2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fullnamestb')
    op.drop_table('partialnamestb')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('partialnamestb',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('typeName', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('foundCountry1', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('foundCountry1percent', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('foundCountry2', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('foundCountry2percent', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('foundCountry3', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('foundCountry3percent', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('foundCountry4', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('foundCountry4percent', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('foundCountry5', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('foundCountry5percent', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='partialnamestb_pkey')
    )
    op.create_table('fullnamestb',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('firstName', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('lastName', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('secondLastName', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('foundCountry1', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('foundCountry1percent', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('foundCountry2', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('foundCountry2percent', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('foundCountry3', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('foundCountry3percent', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('foundCountry4', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('foundCountry4percent', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('foundCountry5', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('foundCountry5percent', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='fullnamestb_pkey')
    )
    # ### end Alembic commands ###