"""empty message

Revision ID: 439965774946
Revises: 94c0aab76471
Create Date: 2023-03-26 23:44:03.043757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '439965774946'
down_revision = '94c0aab76471'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_posted', sa.DateTime(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('date_posted')

    # ### end Alembic commands ###
