from sqlalchemy import Date
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import app

db = SQLAlchemy(app)
app.app_context().push()
migrate = Migrate(app, db, compare_type=True)


class MarketingMetrics(db.Model):
    __tablename__ = 'marketing_metrics'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(Date)
    end_date = db.Column(Date)
    clicks = db.Column(db.Integer)
    impressions = db.Column(db.Integer)
    cost = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'start_date': self.start_date.isoformat(),  
            'end_date': self.end_date.isoformat(),
            'clicks': self.clicks,
            'impressions': self.impressions,
            'cost': self.cost,
        }

def get_db_data(session, start_date, end_date):
    return session.query(MarketingMetrics).filter(
        MarketingMetrics.start_date.between(start_date, end_date),
        MarketingMetrics.end_date.between(start_date, end_date)
    ).all()