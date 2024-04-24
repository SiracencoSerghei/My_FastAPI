from .init import curs, conn
from model.creature import Creature

curs.execute(
    """CREATE TABLE IF NOT EXISTS creature (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                country TEXT,
                area TEXT,
                aka TEXT)"""
)


def row_to_model(row: tuple) -> Creature:
    (name, description, country, area, aka) = row
    return Creature(
        name=row[0], country=row[1], description=row[2], area=row[3], aka=row[4]
    )


def model_to_dict(creature: Creature) -> dict:
    return creature.dict() if creature else None


def get_one(name: str) -> Creature:
    qry = "select * from creature where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    return row_to_model(curs.fetchone())


def get_all() -> list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


def create(creature: Creature) -> Creature:
    print(f"DATA {creature=}")
    qry = """INSERT INTO creature (name, description, country, area, aka) VALUES
            (:name, :description, :country, :area, :aka)"""
    print(f"{qry=}")
    params = model_to_dict(creature)
    print(f"{params=}")
    data_insert = curs.execute(qry, params)
    print(f"{data_insert=}")
    conn.commit()
    result = get_one(creature.name)
    print(f"{result=}")
    return result


def modify(creature: Creature) -> Creature:
    qry = """update creature
             set country=:country,
                 name=:name,
                 description=:description,
                 area=:area,
                 aka=:aka
             where name=:name_orig"""
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    _ = curs.execute(qry, params)
    return get_one(creature.name)


def delete(creature: Creature) -> bool:
    qry = "delete from creature where name = :name"
    params = {"name": creature.name}
    res = curs.execute(qry, params)
    return bool(res)
