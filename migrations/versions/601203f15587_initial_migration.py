"""Initial migration.

Revision ID: 601203f15587
Revises: 
Create Date: 2021-05-29 15:19:30.834299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '601203f15587'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('car_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('hashed_password', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('ref_car_type', sa.Integer(), nullable=False),
    sa.Column('ref_brand', sa.Integer(), nullable=False),
    sa.Column('ref_location', sa.Integer(), nullable=False),
    sa.Column('num_of_passangers', sa.Integer(), nullable=True),
    sa.Column('price_per_day', sa.Numeric(), nullable=True),
    sa.Column('air_conditioning', sa.Boolean(), nullable=True),
    sa.Column('automatic_transmission', sa.Boolean(), nullable=True),
    sa.Column('doors_4', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['ref_brand'], ['brands.id'], ),
    sa.ForeignKeyConstraint(['ref_car_type'], ['car_types.id'], ),
    sa.ForeignKeyConstraint(['ref_location'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contracts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pick_up_date', sa.DateTime(), nullable=False),
    sa.Column('drop_off_date', sa.DateTime(), nullable=False),
    sa.Column('total_price', sa.Numeric(), nullable=False),
    sa.Column('ref_car', sa.Integer(), nullable=False),
    sa.Column('ref_user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ref_car'], ['cars.id'], ),
    sa.ForeignKeyConstraint(['ref_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contracts')
    op.drop_table('cars')
    op.drop_table('users')
    op.drop_table('locations')
    op.drop_table('car_types')
    op.drop_table('brands')
    # ### end Alembic commands ###