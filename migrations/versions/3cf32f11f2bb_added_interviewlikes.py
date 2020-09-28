"""added interviewlikes

Revision ID: 3cf32f11f2bb
Revises: 9ad99c73ff0e
Create Date: 2020-09-27 12:23:13.358544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cf32f11f2bb'
down_revision = '9ad99c73ff0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interviewlikes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('interview_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['interview_id'], ['interview.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('post_like')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_like',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('interview_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['interview_id'], ['interview.id'], name='post_like_interview_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='post_like_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='post_like_pkey')
    )
    op.drop_table('interviewlikes')
    # ### end Alembic commands ###