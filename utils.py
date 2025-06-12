import qrcode
from io import BytesIO
import base64
from difflib import SequenceMatcher
import re

def generate_qr_code(data):
    """
    Genera un código QR y lo devuelve como una imagen base64
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#1a237e", back_color="white")
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def normalize_phone(phone):
    """
    Normaliza un número de teléfono eliminando caracteres no numéricos
    """
    return re.sub(r'\D', '', phone) if phone else ''

def is_similar(str1, str2, threshold=0.85):
    """
    Compara dos strings y determina si son similares basado en un umbral
    """
    if not str1 or not str2:
        return False
    return SequenceMatcher(None, str1.lower(), str2.lower()).ratio() > threshold

def check_duplicate_contact(contact, existing_contacts):
    """
    Verifica si un contacto es potencialmente duplicado
    Retorna una lista de posibles duplicados
    """
    duplicates = []
    normalized_phone = normalize_phone(contact.phone)
    
    for existing in existing_contacts:
        # Verificar número de teléfono
        if normalized_phone and normalize_phone(existing.phone) == normalized_phone:
            duplicates.append(('phone', existing))
            continue
            
        # Verificar email
        if contact.email and contact.email.lower() == existing.email.lower():
            duplicates.append(('email', existing))
            continue
            
        # Verificar nombre similar
        if is_similar(contact.name, existing.name):
            duplicates.append(('name', existing))
            
    return duplicates

def merge_contacts(source, target):
    """
    Combina dos contactos, manteniendo la información más completa
    """
    merged = {
        'name': source.name if len(source.name) > len(target.name) else target.name,
        'phone': source.phone or target.phone,
        'email': source.email or target.email,
        'company': source.company or target.company,
        'notes': f"{source.notes or ''}\n{target.notes or ''}".strip(),
        'category_id': source.category_id
    }
    return merged

def format_phone_number(phone):
    """
    Formatea un número de teléfono para mostrar
    Ejemplo: +1 (234) 567-8900
    """
    if not phone:
        return ""
        
    clean_phone = normalize_phone(phone)
    if len(clean_phone) == 10:  # Número local
        return f"({clean_phone[:3]}) {clean_phone[3:6]}-{clean_phone[6:]}"
    elif len(clean_phone) > 10:  # Número internacional
        return f"+{clean_phone[:-10]} ({clean_phone[-10:-7]}) {clean_phone[-7:-4]}-{clean_phone[-4:]}"
    return phone  # Devolver original si no coincide con formatos conocidos

def validate_email(email):
    """
    Valida el formato de un email
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email)) if email else False

def generate_initials(name):
    """
    Genera las iniciales de un nombre para avatares
    """
    words = name.split()
    if len(words) >= 2:
        return (words[0][0] + words[1][0]).upper()
    return words[0][0].upper() if words else '?'

def get_contact_color(category_color, index):
    """
    Genera una variación del color de la categoría para el contacto
    basado en su índice para evitar colores idénticos
    """
    # Convertir color hex a RGB
    r = int(category_color[1:3], 16)
    g = int(category_color[3:5], 16)
    b = int(category_color[5:7], 16)
    
    # Ajustar el brillo basado en el índice
    factor = 1.0 + (index % 3 - 1) * 0.1
    
    r = min(255, max(0, int(r * factor)))
    g = min(255, max(0, int(g * factor)))
    b = min(255, max(0, int(b * factor)))
    
    return f'#{r:02x}{g:02x}{b:02x}'
