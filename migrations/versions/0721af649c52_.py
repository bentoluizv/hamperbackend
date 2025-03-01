"""empty message

Revision ID: 0721af649c52
Revises: c04ce36db125
Create Date: 2025-02-21 12:44:35.532529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0721af649c52'
down_revision = 'c04ce36db125'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('value',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=6),
               existing_nullable=False)

    with op.batch_alter_table('restaurant', schema=None) as batch_op:
        batch_op.alter_column('classification',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant', schema=None) as batch_op:
        batch_op.alter_column('classification',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('value',
               existing_type=sa.Float(precision=6),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
