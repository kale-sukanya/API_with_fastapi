"""add last few columns to posts table

Revision ID: 9d05fc22a4c4
Revises: d8cca744c233
Create Date: 2022-04-09 17:38:28.238079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d05fc22a4c4'
down_revision = 'd8cca744c233'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')

    pass
