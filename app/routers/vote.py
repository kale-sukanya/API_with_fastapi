from fastapi import HTTPException, status, Depends, APIRouter
from .. import models, schemas,database, OAuth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags=["vote"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session= Depends(database.get_db), current_user: int = Depends(OAuth2.get_current_user)):
    POST = db.query(models.Post).filter(models.Vote.user_id == vote.post_id).first()
    if not POST:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id = {vote.post_id} doesnot exist.")


    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if(vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f"user {current_user.id} has already voted on post {vote.post_id}")
        new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id )
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote doesnot exist")
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"messgae":"vote deleted"}
