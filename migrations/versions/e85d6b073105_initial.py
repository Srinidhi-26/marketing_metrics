"""initial

Revision ID: e85d6b073105
Revises: 
Create Date: 2024-07-04 01:06:06.063993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e85d6b073105'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('marketing_metrics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('clicks', sa.Integer(), nullable=True),
    sa.Column('impressions', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('marketing_metrics')
    # ### end Alembic commands ###
