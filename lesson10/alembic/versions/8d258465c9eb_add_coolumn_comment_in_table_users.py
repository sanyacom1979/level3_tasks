"""Add coolumn comment in table users

Revision ID: 8d258465c9eb
Revises: 
Create Date: 2023-03-06 19:36:01.139722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d258465c9eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('s')
    op.drop_constraint('payments_user_id_fkey', 'payments', type_='foreignkey')
    op.create_foreign_key(None, 'payments', 'users', ['user_id'], ['id'])
    op.add_column('users', sa.Column('comment', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'comment')
    op.drop_constraint(None, 'payments', type_='foreignkey')
    op.create_foreign_key('payments_user_id_fkey', 'payments', 'users', ['user_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_table('s',
    sa.Column('sid', sa.CHAR(length=4), autoincrement=False, nullable=False),
    sa.Column('name', sa.CHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('city', sa.CHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('rating', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('sid', name='s_pkey')
    )
    # ### end Alembic commands ###
