import csv
from models import db, Episode, Guest, Appearance
from app import app

def seed_database():
    with app.app_context():
        # Clear existing data
        db.session.query(Appearance).delete()
        db.session.query(Guest).delete()
        db.session.query(Episode).delete()
        db.session.commit()  # Ensure clearing data is committed

        # Open and read the CSV file
        with open('seed.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # Create or get the episode
                episode_date = row['Show']
                episode_number = int(episode_date.replace('/', ''))  # Assuming number from date
                episode = Episode.query.filter_by(date=episode_date).first()
                
                if not episode:
                    episode = Episode(date=episode_date, number=episode_number)
                    db.session.add(episode)
                    db.session.commit()

                # Create or get the guest
                guest_name = row['Raw_Guest_List']
                occupation = row['GoogleKnowlege_Occupation']
                guest = Guest.query.filter_by(name=guest_name).first()
                
                if not guest:
                    guest = Guest(name=guest_name, occupation=occupation)
                    db.session.add(guest)
                    db.session.commit()

                # Create an appearance (Assigning a random rating for now)
                appearance = Appearance(
                    rating=3,  # You can adjust this logic to randomly assign ratings
                    episode_id=episode.id,
                    guest_id=guest.id
                )
                db.session.add(appearance)
                db.session.commit()

        print("Database seeded successfully.")

if __name__ == '__main__':
    seed_database()