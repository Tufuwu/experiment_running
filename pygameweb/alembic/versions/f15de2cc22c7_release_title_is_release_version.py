"""release.title is release.version

Revision ID: f15de2cc22c7
Revises: 0b16e0992d44
Create Date: 2017-02-11 19:02:22.356034

"""

# revision identifiers, used by Alembic.
revision = 'f15de2cc22c7'
down_revision = '0b16e0992d44'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('alter table release rename column title to version')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('alter table release rename column version to title')
    # ### end Alembic commands ###
