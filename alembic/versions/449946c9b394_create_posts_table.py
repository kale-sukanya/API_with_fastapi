"""create posts table

Revision ID: 449946c9b394
Revises: 
Create Date: 2022-04-09 16:45:23.636263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '449946c9b394'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
    sa.Column('title',sa.String(),nullable=False)
    )
    pass


def downgrade():
    pass
