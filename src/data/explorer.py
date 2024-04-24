from .init import curs, conn
from model.explorer import Explorer


curs.execute(
    """create table if not exists explorer(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text,
                country text,
                description text)"""
)


def row_to_model(row: tuple) -> Explorer:
    print(f"{row=}")
    (name, description, country) = row
    return Explorer(name=row[0], country=row[1], description=row[2])


def model_to_dict(explorer: Explorer) -> dict:
    return explorer.model_dump() if explorer else None


def get_one(name: str) -> Explorer:
    qry = "select * from explorer where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    return row_to_model(curs.fetchone())


def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


def create(explorer: Explorer) -> Explorer:
    print(f"{curs=}  {conn=}")
    print(f"DATA {explorer=}")
    qry = """insert into explorer (name, country, description)
             values (:name, :country, :description)"""
    print(f"{qry=}")
    params = model_to_dict(explorer)
    print(f"{params=}")
    data_insert = curs.execute(qry, params)
    print(f"{data_insert=}")
    conn.commit()
    result = get_one(explorer.name)
    print(f"{result=}")
    return result


def modify(name: str, explorer: Explorer) -> Explorer:
    qry = """update explorer
             set country=:country,
             name=:name,
             description=:description
             where name=:name_orig"""
    params = model_to_dict(explorer)
    params["name_orig"] = explorer.name
    _ = curs.execute(qry, params)
    explorer2 = get_one(explorer.name)
    return explorer2


def delete(explorer: Explorer) -> bool:
    qry = "delete from explorer where name = :name"
    params = {"name": explorer.name}
    res = curs.execute(qry, params)
    return bool(res)
