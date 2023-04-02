from ...models import db, Bookmark


def add_bookmark(user_id, question_id):
    bookmark = Bookmark(user_id=user_id, question_id=question_id)
    db.session.add(bookmark)
    db.session.commit()
    return "Success"


def remove_bookmark(id):
    bookmark = Bookmark.query.filter_by(id=id).first()
    if bookmark:
        db.session.delete(bookmark)
        db.session.commit()
        return "Success"
    return None
