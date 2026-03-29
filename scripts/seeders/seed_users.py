"""
Seed script to populate the database with test users.

All users share the same password: Password123

Usage:
    python -m scripts.seeders.seed_users

Roles seeded:
    - 2 Admin users
    - 4 Supervisor users
    - 6 Student users
"""

import sys
import os

# Ensure the project root is on the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from passlib.context import CryptContext
from api.db.database import get_db_with_ctx_manager, create_database
from api.v1.models.user import User, UserRole

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ──────────────────────────────────────────────
#  Shared password for every seeded user
# ──────────────────────────────────────────────
SEED_PASSWORD = "password123"

USERS = [
    # ── Admins ────────────────────────────────
    {
        "first_name": "Leo",
        "last_name": "Ron",
        "email": "admin@projecthub.com",
        "role": UserRole.ADMIN.value,
        "is_active": True,
    },
    {
        "first_name": "Frank",
        "last_name": "Richkard",
        "email": "admin2@projecthub.com",
        "role": UserRole.ADMIN.value,
        "is_active": True,
    },

    # ── Supervisors ───────────────────────────
    {
        "first_name": "Dr. Ajayi",
        "last_name": "Oluwabukola",
        "email": "ajayioluwabukola@projecthub.com",
        "role": UserRole.SUPERVISOR.value,
        "is_active": True,
    },
    {
        "first_name": "Prof. Ngozi",
        "last_name": "Chisom",
        "email": "ngozichisom@projecthub.com",
        "role": UserRole.SUPERVISOR.value,
        "is_active": True,
    },
    {
        "first_name": "Dr. Seun",
        "last_name": "Ebiesuwa",
        "email": "seunebiesuwa@projecthub.com",
        "role": UserRole.SUPERVISOR.value,
        "is_active": True,
    },
    {
        "first_name": "Dr. Alao",
        "last_name": "Olujimi",
        "email": "alaoolujimi@projecthub.com",
        "role": UserRole.SUPERVISOR.value,
        "is_active": True,
    },
    {
        "first_name": "Dr. Onuiri",
        "last_name": "Ernest",
        "email": "onuiriernest@projecthub.com",
        "role": UserRole.SUPERVISOR.value,
        "is_active": True,
    },

    # ── Students ──────────────────────────────
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@projecthub.com",
        "role": UserRole.STUDENT.value,
        "is_active": True,
    },
    {
        "first_name": "Samuel",
        "last_name": "Akindoju",
        "email": "samuelakindoju@projecthub.com",
        "role": UserRole.STUDENT.value,
        "is_active": True,
    },
    {
        "first_name": "Chidera",
        "last_name": "Eliogu",
        "email": "chideraeliogu@projecthub.com",
        "role": UserRole.STUDENT.value,
        "is_active": True,
    },
    {
        "first_name": "Solomon",
        "last_name": "Chukwuemeka",
        "email": "solomonchukwuemeka@projecthub.com",
        "role": UserRole.STUDENT.value,
        "is_active": True,
    },
    {
        "first_name": "Temi",
        "last_name": "Akin",
        "email": "temiakin4@projecthub.com",
        "role": UserRole.STUDENT.value,
        "is_active": True,
    },
    {
        "first_name": "Emeka",
        "last_name": "Ugo",
        "email": "emekaugo@projecthub.com",
        "role": UserRole.STUDENT.value,
        "is_active": True,
    },
    {
        "first_name": "Alimi",
        "last_name": "Bells",
        "email": "alimibells@projecthub.com",
        "role": UserRole.STUDENT.value,
        "is_active": True,
    },
    {
        "first_name": "Dave",
        "last_name": "Okon",
        "email": "daveokon@projecthub.com",
        "role": UserRole.STUDENT.value,
        "is_active": True,
    },
    {
        "first_name": "Alisha",
        "last_name": "Moma",
        "email": "alishamoma@projecthub.com",
        "role": UserRole.STUDENT.value,
        "is_active": True,
    },
]


def seed_users():
    """Insert seed users into the database, skipping any that already exist."""

    created = 0
    skipped = 0

    with get_db_with_ctx_manager() as db:
        for user_data in USERS:
            existing = User.fetch_one_by_field(db, throw_error=False, email=user_data["email"])
            if existing:
                print(f"  [SKIP] {user_data['email']} (already exists)")
                skipped += 1
                continue

            User.create(
                db=db,
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                email=user_data["email"],
                password=pwd_context.hash(SEED_PASSWORD),
                role=user_data["role"],
                is_active=user_data["is_active"],
            )
            print(f"  [OK]   {user_data['email']} ({user_data['role']})")
            created += 1

    print(f"\nDone — {created} created, {skipped} skipped.")


if __name__ == "__main__":
    print("=" * 50)
    print("  ProjectHub — User Seeder")
    print(f"  Password for all users: {SEED_PASSWORD}")
    print("=" * 50)
    print()

    # Ensure tables exist
    create_database()

    seed_users()

    print()
    print("Login credentials:")
    print("-" * 50)
    print(f"  {'Role':<12} {'Email':<32} Password")
    print("-" * 50)
    print(f"  {'Admin':<12} {'admin@projecthub.com':<32} {SEED_PASSWORD}")
    print(f"  {'Supervisor':<12} {'ajayioluwabukola@projecthub.com':<32} {SEED_PASSWORD}")
    print(f"  {'Student':<12} {'johndoe@projecthub.com':<32} {SEED_PASSWORD}")
    print("-" * 50)
