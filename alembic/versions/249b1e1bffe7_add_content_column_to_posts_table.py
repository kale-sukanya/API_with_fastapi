"""add content column to posts table

Revision ID: 249b1e1bffe7
Revises: 449946c9b394
Create Date: 2022-04-09 17:05:22.966861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '249b1e1bffe7'
down_revision = '449946c9b394'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
