from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import secrets

db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(7), nullable=False)  # Hex color
    icon = db.Column(db.String(50), nullable=False)
    
    # Relación con contactos
    contacts = db.relationship('Contact', backref='category', lazy=True)
    
    def __repr__(self):
        return f'<Category {self.name}>'

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    company = db.Column(db.String(100), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign key para categoría
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    
    def __repr__(self):
        return f'<Contact {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'company': self.company,
            'notes': self.notes,
            'category': self.category.name if self.category else None,
            'created_date': self.created_date.isoformat()
        }

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    company = db.Column(db.String(100), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    share_code = db.Column(db.String(20), unique=True, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, **kwargs):
        super(UserProfile, self).__init__(**kwargs)
        if not self.share_code:
            self.share_code = self.generate_share_code()
    
    def generate_share_code(self):
        """Genera un código único para compartir"""
        return secrets.token_urlsafe(12)[:12]
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'company': self.company,
            'bio': self.bio,
            'share_code': self.share_code
        }

def init_default_categories():
    """Inicializa las categorías por defecto"""
    default_categories = [
        {'name': 'Familia', 'color': '#e91e63', 'icon': 'heart'},
        {'name': 'Amigos', 'color': '#ff9800', 'icon': 'user-group'},
        {'name': 'Trabajo', 'color': '#2196f3', 'icon': 'briefcase'},
        {'name': 'Compañeros', 'color': '#4caf50', 'icon': 'users'},
        {'name': 'Clientes', 'color': '#9c27b0', 'icon': 'building-office'},
        {'name': 'Otros', 'color': '#607d8b', 'icon': 'ellipsis-horizontal'}
    ]
    
    for cat_data in default_categories:
        if not Category.query.filter_by(name=cat_data['name']).first():
            category = Category(**cat_data)
            db.session.add(category)
    
    db.session.commit()
