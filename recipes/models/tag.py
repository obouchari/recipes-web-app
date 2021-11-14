import uuid
from sqlalchemy.dialects.postgresql import UUID

from recipes.extensions import db


class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(30), nullable=False, unique=True)

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def find(cls, tag_id):
        return cls.query.get_or_404(tag_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
