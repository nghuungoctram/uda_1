from alembic import op
import sqlalchemy as sql


def addNewItem():
    op.add_column('artist', sql.Column(
        'website', sql.String(length=120), nullable=True))


def delete():
    op.drop_column('artist', 'website')
