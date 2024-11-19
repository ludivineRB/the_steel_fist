from sqlmodel import SQLModel, create_engine
import models

#creation of the Engine
sqlite_file_name = "steel_fist.db"
sqlite_url=f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)