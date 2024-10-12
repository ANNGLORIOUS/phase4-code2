import csv
from models import db, Episode, Guest, Appearance
from app import app

def seed_database():
    with app.app_context():
        
        db.session.query(Appearance).delete()
        db.session.query(Guest).delete()
        db.session.query(Episode).delete()
        db.session.commit()  
       
        with open('seed.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                
                episode_date = row['Show']
                episode_number = int(episode_date.replace('/', '')) 
                episode = Episode.query.filter_by(date=episode_date).first()
                
                if not episode:
                    episode = Episode(date=episode_date, number=episode_number)
                    db.session.add(episode)
                    db.session.commit()

               
                guest_name = row['Raw_Guest_List']
                occupation = row['GoogleKnowlege_Occupation']
                guest = Guest.query.filter_by(name=guest_name).first()
                
                if not guest:
                    guest = Guest(name=guest_name, occupation=occupation)
                    db.session.add(guest)
                    db.session.commit()

               
                appearance = Appearance(
                    rating=3, 
                    episode_id=episode.id,
                    guest_id=guest.id
                )
                db.session.add(appearance)
                db.session.commit()

        print("Database seeded successfully.")

if __name__ == '__main__':
    seed_database()