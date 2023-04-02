from ...models import db, Complaint

def add_complaint(user_id, complaint, origin):
    complaint = Complaint(
        user_id=user_id,
        origin=origin,
        body=complaint
    )
    db.session.add(complaint)
    db.session.commit()
    return "success"

def resolve_complaint(complaint_id):
    complaint = Complaint.query.filter_by(id=complaint_id).first()
    if complaint:
        complaint.resolved = True
        db.session.commit()
        return "success"
    else:
        return "complaint not found"

def remove_complaint(complaint_id):
    complaint = Complaint.query.filter_by(id=complaint_id).first()
    if complaint:
        db.session.delete(complaint)
        db.session.commit()
        return "success"
    else:
        return "complaint not found"
