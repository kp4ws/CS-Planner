from api.core.database import SessionLocal
from categories.models import Category
from datetime import datetime, timezone

# TODO: Is it better to change this to a SQL script?

def seed_data():
    seed_categories()

def seed_categories():
    db = SessionLocal()

    categories = [
        Category(title="Backpack", created_at=datetime.now(timezone.utc)),
        Category(title="Shelter", created_at=datetime.now(timezone.utc)),
        Category(title="Sleep System", created_at=datetime.now(timezone.utc)),
        Category(title="Sleep Pad", created_at=datetime.now(timezone.utc)),
        Category(title="Water Filter", created_at=datetime.now(timezone.utc)),
        Category(title="Cooking System", created_at=datetime.now(timezone.utc)),
        Category(title="Food", created_at=datetime.now(timezone.utc)),
        Category(title="Layers / Clothing", created_at=datetime.now(timezone.utc)),
        Category(title="Rain Gear", created_at=datetime.now(timezone.utc)),
        Category(title="Navigation", created_at=datetime.now(timezone.utc)),
        Category(title="First Aid", created_at=datetime.now(timezone.utc)),
        Category(title="Fire Starting", created_at=datetime.now(timezone.utc)),
        Category(title="Lighting", created_at=datetime.now(timezone.utc)),
        Category(title="Hygiene", created_at=datetime.now(timezone.utc)),
        Category(title="Other", created_at=datetime.now(timezone.utc)),
    ]

    db.add_all(categories)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_data()