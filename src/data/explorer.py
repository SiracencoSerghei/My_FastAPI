from .init import curs, IntegrityError
from model.explorer import Explorer
from errors import Missing, Duplicate

curs.execute(
    """create table if not exists explorer(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text,
                country text,
                description text)"""
)


def row_to_model(row: tuple) -> Explorer:
    name, country, description = row
    result = Explorer(name=name, country=country, description=description)

    return result


def dict_to_model(d: dict) -> Explorer:
    return d


def model_to_dict(explorer: Explorer) -> dict:
    return explorer.dict() if explorer else None


def get_one(name: str) -> Explorer:
    qry = "select * from explorer where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Explorer {name} not found")


def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


def create(explorer: Explorer) -> Explorer:
    if not explorer:
        return None
    qry = """insert into explorer (name, country, description) values
             (:name, :country, :description)"""
    params = model_to_dict(explorer)
    print(f"{qry=}")
    print(f"{params=}")
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg=f"Explorer {explorer.name} already exists")
    return get_one(explorer.name)


def modify(name: str, explorer: Explorer) -> Explorer:
    if not (name and explorer):
        return None
    qry = """update explorer
             set name=:name,
             country=:country,
             description=:description
             where name=:name_orig"""
    params = model_to_dict(explorer)
    params["name_orig"] = explorer.name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(explorer.name)
    else:
        raise Missing(msg=f"Explorer {name} not found")


def delete(name: str):
    if not name:
        return False
    qry = "delete from explorer where name = :name"
    params = {"name": name}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"Explorer {name} not found")
