"""Added ProductPitch, Edited pickuplines table name

Revision ID: b66aac6e8bec
Revises: 4bff1b47f3c5
Create Date: 2020-09-23 16:01:46.035516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b66aac6e8bec'
down_revision = '4bff1b47f3c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('productpitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post', sa.String(length=255), nullable=True),
    sa.Column('body', sa.String(length=1000), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productpitch')
    # ### end Alembic commands ###
