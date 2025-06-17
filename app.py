from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from models import db, Contact, Category, UserProfile, SharedLink, init_default_categories
from utils import generate_qr_code, check_duplicate_contact, merge_contacts, format_phone_number, validate_email
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'calltech-secret-key-2024')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///calltech.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

def create_tables():
    """Crear tablas y datos iniciales"""
    with app.app_context():
        db.create_all()
        init_default_categories()
        
        # Crear perfil de usuario por defecto si no existe
        if not UserProfile.query.first():
            default_profile = UserProfile(
                name="Mi Perfil CallTech",
                phone="",
                email="",
                company="",
                bio="Comparte tu información de contacto fácilmente"
            )
            db.session.add(default_profile)
            db.session.commit()

# Llamar a create_tables al inicializar la app
create_tables()

# Rutas principales
@app.route('/')
def index():
    """Página principal con lista de contactos"""
    category_id = request.args.get('category', type=int)
    search = request.args.get('search', '')
    
    # Construir query base
    query = Contact.query
    
    # Filtrar por categoría si se especifica
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    # Filtrar por búsqueda si se especifica
    if search:
        query = query.filter(
            db.or_(
                Contact.name.contains(search),
                Contact.phone.contains(search),
                Contact.email.contains(search),
                Contact.company.contains(search)
            )
        )
    
    contacts = query.order_by(Contact.name).all()
    categories = Category.query.all()
    
    # Estadísticas por categoría
    category_stats = {}
    for category in categories:
        category_stats[category.id] = Contact.query.filter_by(category_id=category.id).count()
    
    return render_template('index.html', 
                         contacts=contacts, 
                         categories=categories,
                         category_stats=category_stats,
                         selected_category=category_id,
                         search_term=search)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    """Agregar nuevo contacto"""
    if request.method == 'POST':
        # Obtener datos del formulario
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        company = request.form.get('company')
        notes = request.form.get('notes')
        category_id = request.form.get('category_id', type=int)
        
        # Validaciones
        if not name:
            flash('El nombre es requerido', 'error')
            return redirect(url_for('add_contact'))
            
        if not category_id:
            flash('La categoría es requerida', 'error')
            return redirect(url_for('add_contact'))
        
        if email and not validate_email(email):
            flash('El formato del email no es válido', 'error')
            return redirect(url_for('add_contact'))
        
        # Crear contacto temporal para verificar duplicados
        temp_contact = Contact(name=name, phone=phone, email=email)
        existing_contacts = Contact.query.all()
        duplicates = check_duplicate_contact(temp_contact, existing_contacts)
        
        if duplicates:
            # Si hay duplicados, mostrar advertencia
            duplicate_info = []
            for dup_type, dup_contact in duplicates:
                duplicate_info.append({
                    'type': dup_type,
                    'contact': dup_contact.to_dict()
                })
            
            return render_template('add_contact.html', 
                                 categories=Category.query.all(),
                                 duplicates=duplicate_info,
                                 form_data=request.form)
        
        # Si no hay duplicados, crear el contacto
        contact = Contact(
            name=name,
            phone=phone,
            email=email,
            company=company,
            notes=notes,
            category_id=category_id
        )
        
        db.session.add(contact)
        db.session.commit()
        
        flash('Contacto agregado exitosamente', 'success')
        return redirect(url_for('index'))
    
    categories = Category.query.all()
    return render_template('add_contact.html', categories=categories)

@app.route('/contact/<int:id>')
def view_contact(id):
    """Ver detalles de un contacto"""
    contact = Contact.query.get_or_404(id)
    return render_template('view_contact.html', contact=contact)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    """Editar contacto existente"""
    contact = Contact.query.get_or_404(id)
    
    if request.method == 'POST':
        # Actualizar datos
        contact.name = request.form.get('name')
        contact.phone = request.form.get('phone')
        contact.email = request.form.get('email')
        contact.company = request.form.get('company')
        contact.notes = request.form.get('notes')
        contact.category_id = request.form.get('category_id', type=int)
        
        # Validaciones
        if not contact.name:
            flash('El nombre es requerido', 'error')
            return redirect(url_for('edit_contact', id=id))
        
        if contact.email and not validate_email(contact.email):
            flash('El formato del email no es válido', 'error')
            return redirect(url_for('edit_contact', id=id))
        
        db.session.commit()
        flash('Contacto actualizado exitosamente', 'success')
        return redirect(url_for('view_contact', id=id))
    
    categories = Category.query.all()
    return render_template('edit_contact.html', contact=contact, categories=categories)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_contact(id):
    """Eliminar contacto"""
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contacto eliminado exitosamente', 'success')
    return redirect(url_for('index'))

# Rutas para perfil personal y compartir
@app.route('/my-profile')
def my_profile():
    """Página del perfil personal"""
    profile = UserProfile.query.first()
    if not profile:
        profile = UserProfile(
            name="Mi Perfil CallTech",
            phone="",
            email="",
            company="",
            bio="Comparte tu información de contacto fácilmente"
        )
        db.session.add(profile)
        db.session.commit()
    
    return render_template('my_profile.html', profile=profile)

@app.route('/update-profile', methods=['POST'])
def update_profile():
    """Actualizar perfil personal"""
    profile = UserProfile.query.first()
    if not profile:
        profile = UserProfile()
        db.session.add(profile)
    
    profile.name = request.form.get('name')
    profile.phone = request.form.get('phone')
    profile.email = request.form.get('email')
    profile.company = request.form.get('company')
    profile.bio = request.form.get('bio')
    
    db.session.commit()
    flash('Perfil actualizado exitosamente', 'success')
    return redirect(url_for('my_profile'))

@app.route('/share-profile')
def share_profile():
    """Página para compartir perfil"""
    profile = UserProfile.query.first()
    if not profile:
        return redirect(url_for('my_profile'))
    
    # Generar URL para compartir
    share_url = url_for('public_profile', code=profile.share_code, _external=True)
    
    # Generar código QR
    qr_code = generate_qr_code(share_url)
    
    return render_template('share_profile.html', 
                         profile=profile, 
                         share_url=share_url,
                         qr_code=qr_code)

@app.route('/profile/<code>')
def public_profile(code):
    """Vista pública del perfil compartido"""
    profile = UserProfile.query.filter_by(share_code=code).first_or_404()
    return render_template('public_profile.html', profile=profile)

# API endpoints para funcionalidad AJAX
@app.route('/api/contacts')
def api_contacts():
    """API para obtener contactos"""
    contacts = Contact.query.all()
    return jsonify([contact.to_dict() for contact in contacts])

@app.route('/api/categories')
def api_categories():
    """API para obtener categorías"""
    categories = Category.query.all()
    return jsonify([{
        'id': cat.id,
        'name': cat.name,
        'color': cat.color,
        'icon': cat.icon
    } for cat in categories])

@app.route('/api/check-duplicate', methods=['POST'])
def api_check_duplicate():
    """API para verificar duplicados"""
    data = request.get_json()
    temp_contact = Contact(
        name=data.get('name', ''),
        phone=data.get('phone', ''),
        email=data.get('email', '')
    )
    
    existing_contacts = Contact.query.all()
    duplicates = check_duplicate_contact(temp_contact, existing_contacts)
    
    return jsonify({
        'has_duplicates': len(duplicates) > 0,
        'duplicates': [{
            'type': dup_type,
            'contact': dup_contact.to_dict()
        } for dup_type, dup_contact in duplicates]
    })

# Filtros de template personalizados
@app.template_filter('format_phone')
def format_phone_filter(phone):
    return format_phone_number(phone)

@app.template_filter('initials')
def initials_filter(name):
    from utils import generate_initials
    return generate_initials(name)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=port)
