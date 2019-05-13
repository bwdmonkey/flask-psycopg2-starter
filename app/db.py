import psycopg2

import click
from flask import current_app, g
from flask.cli import with_appcontext
from configparser import ConfigParser


cursor = None

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(seed_db_command)


def init_db():
    global cursor
    db = get_db()
    cursor = db.cursor()
    with current_app.open_resource("schema.sql") as f:
        cursor.execute(f.read())
    return cursor.fetchone()[0] # DB Version


@click.command("init-db")
@with_appcontext
def init_db_command():
    """CLI command: Clear the existing data and create new tables."""
    db_version = init_db()
    click.echo("Database initialized. DB version:")
    click.echo("    {0}".format(db_version))

def seed_db():
    global cursor
    db = get_db()
    cursor = db.cursor()
    with current_app.open_resource("seed.sql") as f:
        cursor.execute(f.read())


@click.command("seed-db")
@with_appcontext
def seed_db_command():
    """CLI command: Inserts seed data into the database"""
    seed_db()
    click.echo("Seeded the database.")


def get_config(filename="database.ini", section="postgresql"):
    """Parses and gets database config from file"""
    parser = ConfigParser()
    parser.read(filename)

    db_config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception("Section {0} not found".format(section))

    return db_config


def get_db():
    """Attempt to connect to database and attach to global app"""
    if "db" not in g:
        db_config = get_config()
        g.db = psycopg2.connect(**db_config)

    return g.db


def close_db(e=None):
    """Close database connection"""
    db = g.pop("db", None)
    if db is not None:
        db.close()

