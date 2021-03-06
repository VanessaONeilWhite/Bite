"""empty message

Revision ID: 8920dbfd8f59
Revises: 6609a1d0e3a6
Create Date: 2022-06-22 14:00:29.026457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8920dbfd8f59'
down_revision = '6609a1d0e3a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_bites',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bite_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bite_id'], ['bite.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'bite_id')
    )
    op.drop_column('user', 'icon')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('icon', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_table('user_bites')
    # ### end Alembic commands ###
