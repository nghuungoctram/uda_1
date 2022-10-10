from alembic import op
import sqlalchemy as sql


def addNewItem():
    op.add_column('venue', sql.Column(
        'genres', sql.String(length=300), nullable=False))
    op.add_column('venue', sql.Column(
        'website', sql.String(length=120), nullable=False))


def delete():
    op.drop_column('venue', 'website')
    op.drop_column('venue', 'genres')
