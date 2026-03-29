"""
Seed script to populate the database with departments.

Usage:
    python -m scripts.seeders.seed_departments
    OR
    python scripts/seeders/seed_departments.py

Departments seeded: 5 BUCC departments
"""

import sys
import os

# Ensure the project root is on the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from api.db.database import get_db_with_ctx_manager, create_database
from api.v1.models.department import Department


DEPARTMENTS = [
  {
    "name": "Computer Information Systems",
    "code": "CIS",
    "description": "Study of how computing systems are applied in business environments to manage, process, and support organizational information."
  },
  {
    "name": "Computer Information Technology",
    "code": "CIT",
    "description": "Focus on practical implementation, deployment, and maintenance of computing infrastructure, networks, and systems."
  },
  {
    "name": "Computer Science",
    "code": "CS",
    "description": "Study of computation, algorithms, data structures, and software engineering."
  },
  {
    "name": "Information Technology",
    "code": "IT",
    "description": "Application of computing technologies to manage and process information."
  },
  {
    "name": "Software Engineering",
    "code": "SE",
    "description": "Systematic approach to the design, development, and maintenance of software."
  }
]


def seed_departments():
    """Insert seed departments into the database, skipping any that already exist."""

    created = 0
    skipped = 0

    with get_db_with_ctx_manager() as db:
        for dept_data in DEPARTMENTS:
            # Check by code (unique)
            existing = Department.fetch_one_by_field(
                db, throw_error=False, code=dept_data["code"]
            )
            if existing:
                print(f"  [SKIP] {dept_data['code']} — {dept_data['name']} (already exists)")
                skipped += 1
                continue

            Department.create(
                db=db,
                name=dept_data["name"],
                code=dept_data["code"],
                description=dept_data["description"],
            )
            print(f"  [OK]   {dept_data['code']} — {dept_data['name']}")
            created += 1

    print(f"\nDone — {created} created, {skipped} skipped.")


if __name__ == "__main__":
    print("=" * 50)
    print("  ProjectHub — Department Seeder")
    print("=" * 50)
    print()

    # Ensure tables exist
    create_database()

    seed_departments()
