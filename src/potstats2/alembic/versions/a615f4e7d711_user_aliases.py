"""User aliases

Revision ID: a615f4e7d711
Revises: ef6118072daa
Create Date: 2018-06-30 11:26:43.955280

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a615f4e7d711'
down_revision = 'ef6118072daa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('aliases', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    op.add_column('users', sa.Column('name_timestamp', sa.TIMESTAMP(), nullable=True))
    op.execute("UPDATE users SET aliases = '[]'::jsonb;")
    op.execute("UPDATE users SET name_timestamp = '01-01-1970';")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'name_timestamp')
    op.drop_column('users', 'aliases')
    # ### end Alembic commands ###
