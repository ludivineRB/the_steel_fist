from init_db import engine  # Import the existing engine
from model import Members, Accesscards #, Coaches, Courses, Registrations  # Import existing models
from sqlmodel import SQLModel, Field, Session, select, create_engine

# # Define a second database URL
NEW_DATABASE_URL = "sqlite:///new_database.db"

# # Create the engine for the new database
new_engine = create_engine(NEW_DATABASE_URL)

# Creation of the Engine for the new database
# sqlite_file_name = "new_database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
# new_engine = create_engine(sqlite_url, echo=True)

# Define the new table model
class NewTable(SQLModel, table=True):
    member_name: str 
    email: str 
    card_id: int
    unique_number: int

# Query and join data from the initial database
with Session(engine) as session:
    statement = (
        select(Members, Accesscards)
        .join(Accesscards, Members.access_card_id == Accesscards.card_id)
    )
    results = session.exec(statement).all()

# Create the new table in the second database
SQLModel.metadata.create_all(new_engine)

# Insert the joined data into the new table in the second database
try:
    with Session(new_engine) as session:
        for row in results:
            Members, Accesscards = row
            new_entry = NewTable(
                member_name=Members.member_name,
                email=Members.email,
                card_id=Members.access_card_id,
                unique_number=Accesscards.unique_number
            )
            session.add(new_entry)
        session.commit()
except Exception as e:
    print(f"An error occurred: {e}")

print("New table created and populated in the second database successfully!")
