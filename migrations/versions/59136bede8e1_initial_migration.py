"""Initial migration.

Revision ID: 59136bede8e1
Revises: 
Create Date: 2024-07-10 17:20:46.305080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59136bede8e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('competitor',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('business_name', sa.String(length=100), nullable=False),
    sa.Column('business_type', sa.String(length=50), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('website_traffic', sa.Integer(), nullable=False),
    sa.Column('top_performing_pages', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('competitor')
    # ### end Alembic commands ###
