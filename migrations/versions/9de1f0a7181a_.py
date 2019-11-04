"""empty message

Revision ID: 9de1f0a7181a
Revises: 
Create Date: 2019-10-24 22:11:36.386603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9de1f0a7181a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('repo_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('repo',
    sa.Column('repo_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('deep_link', sa.String(length=50), nullable=True),
    sa.Column('related_link', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('repo_id')
    )
    op.create_table('doc',
    sa.Column('doc_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('repo_id', sa.Integer(), nullable=True),
    sa.Column('path', sa.String(length=50), nullable=True),
    sa.Column('format', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['repo_id'], ['repo.repo_id'], ),
    sa.PrimaryKeyConstraint('doc_id')
    )
    op.create_table('note',
    sa.Column('note_id', sa.Integer(), nullable=False),
    sa.Column('repo_id', sa.Integer(), nullable=True),
    sa.Column('meta_data', sa.Text(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['repo_id'], ['repo.repo_id'], ),
    sa.PrimaryKeyConstraint('note_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('note')
    op.drop_table('doc')
    op.drop_table('repo')
    op.drop_table('users')
    # ### end Alembic commands ###
