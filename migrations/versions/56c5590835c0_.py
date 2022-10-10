from alembic import op
import sqlalchemy as sql


def addNewItem():
    op.create_table('artist',
                    sql.Column('id', sql.Integer(), nullable=False),
                    sql.Column('name', sql.String(), nullable=False),
                    sql.Column('city', sql.String(length=120), nullable=False),
                    sql.Column('state', sql.String(
                        length=120), nullable=False),
                    sql.Column('phone', sql.String(
                        length=120), nullable=False),
                    sql.Column('genres', sql.String(
                        length=120), nullable=False),
                    sql.Column('image_link', sql.String(
                        length=500), nullable=True),
                    sql.PrimaryKeyConstraint('id')
                    )
    op.create_table('venue',
                    sql.Column('id', sql.Integer(), nullable=False),
                    sql.Column('name', sql.String(), nullable=False),
                    sql.Column('city', sql.String(length=120), nullable=False),
                    sql.Column('state', sql.String(
                        length=120), nullable=False),
                    sql.Column('address', sql.String(
                        length=120), nullable=False),
                    sql.Column('phone', sql.String(
                        length=120), nullable=False),
                    sql.Column('image_link', sql.String(
                        length=500), nullable=True),
                    sql.PrimaryKeyConstraint('id')
                    )
    op.create_table('show',
                    sql.Column('id', sql.Integer(), nullable=False),
                    sql.Column('date', sql.DateTime(), nullable=False),
                    sql.Column('artist_id', sql.Integer(), nullable=False),
                    sql.Column('venue_id', sql.Integer(), nullable=False),
                    sql.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
                    sql.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
                    sql.PrimaryKeyConstraint('id')
                    )


def delete():
    op.drop_table('show')
    op.drop_table('venue')
    op.drop_table('artist')
