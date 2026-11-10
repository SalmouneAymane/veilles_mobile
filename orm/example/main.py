from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    active: Mapped[bool] = mapped_column(default=True)


def main() -> None:
    engine = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add_all(
            [
                User(name="Aymane", active=True),
                User(name="Inactive user", active=False),
            ]
        )
        session.commit()

        statement = select(User).where(User.active.is_(True)).order_by(User.name)
        print("Active users:")
        for user in session.scalars(statement):
            print(f"- {user.name} (id: {user.id})")


if __name__ == "__main__":
    main()
