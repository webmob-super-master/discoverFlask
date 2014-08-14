"""empty message

Revision ID: 1244708a9a85
Revises: None
Create Date: 2014-08-13 21:16:54.220687

"""

# revision identifiers, used by Alembic.
revision = '1244708a9a85'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'posts', sa.Column('author_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'posts', 'author_id')
    op.drop_table('users')
    ### end Alembic commands ###
