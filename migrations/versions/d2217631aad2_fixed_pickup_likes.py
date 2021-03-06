"""fixed pickup likes

Revision ID: d2217631aad2
Revises: 4e597f3259d9
Create Date: 2020-09-27 15:51:36.230658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2217631aad2'
down_revision = '4e597f3259d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('promolikes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('promotion_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['promotion_id'], ['promotion.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('promolikes')
    # ### end Alembic commands ###
