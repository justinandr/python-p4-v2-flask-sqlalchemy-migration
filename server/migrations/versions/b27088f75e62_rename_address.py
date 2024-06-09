"""rename address

Revision ID: b27088f75e62
Revises: bf6299652d41
Create Date: 2024-06-09 17:49:32.939880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b27088f75e62'
down_revision = 'bf6299652d41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address', new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location', new_column_name='address')
    # ### end Alembic commands ###
