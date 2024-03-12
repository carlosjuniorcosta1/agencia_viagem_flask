"""empty message

Revision ID: 66de897a8b03
Revises: 38c7ea6c17e1
Create Date: 2024-03-11 20:32:41.572185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66de897a8b03'
down_revision = '38c7ea6c17e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('packages_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('meal', sa.Enum('breakfast', 'lunch', 'dinner', 'all_inclusive', name='mealtype'), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('packages_table', schema=None) as batch_op:
        batch_op.drop_column('meal')

    # ### end Alembic commands ###
