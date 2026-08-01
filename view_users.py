from database import SessionLocal
from models import User


def main():
    db = SessionLocal()

    try:
        users = db.query(User).all()

        if not users:
            print("No users found in the database.")
            return

        print("\nRegistered Students")
        print("-" * 60)

        for user in users:
            print(
                f"ID: {user.id} | "
                f"Name: {user.full_name} | "
                f"Username: {user.username} | "
                f"Email: {user.email}"
            )

        print("-" * 60)
        print(f"Total students: {len(users)}")

    finally:
        db.close()


if __name__ == "__main__":
    main()
