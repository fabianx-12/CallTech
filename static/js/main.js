// CallTech - JavaScript Principal
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    // Inicializar componentes
    initializeAnimations();
    initializeSearch();
    initializeCategoryFilters();
    initializeContactCards();
    initializeModals();
    initializeForms();
    initializeNotifications();
    initializeTheme();
}

// Animaciones y efectos visuales
function initializeAnimations() {
    // Animación de entrada para elementos
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observar elementos que necesitan animación
    document.querySelectorAll('.contact-card, .card, .form-group').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // Efecto ripple en botones
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', createRipple);
    });
}

function createRipple(event) {
    const button = event.currentTarget;
    const ripple = document.createElement('span');
    const rect = button.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;

    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    ripple.classList.add('ripple');

    button.appendChild(ripple);

    setTimeout(() => {
        ripple.remove();
    }, 600);
}

// Búsqueda en tiempo real
function initializeSearch() {
    const searchInput = document.getElementById('searchInput');
    if (!searchInput) return;

    let searchTimeout;
    
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            performSearch(this.value);
        }, 300);
    });

    // Limpiar búsqueda
    const clearButton = document.getElementById('clearSearch');
    if (clearButton) {
        clearButton.addEventListener('click', function() {
            searchInput.value = '';
            performSearch('');
        });
    }
}

function performSearch(query) {
    const contactCards = document.querySelectorAll('.contact-card');
    const noResults = document.getElementById('noResults');
    let visibleCount = 0;

    contactCards.forEach(card => {
        const name = card.querySelector('.contact-name')?.textContent.toLowerCase() || '';
        const phone = card.querySelector('.contact-phone')?.textContent.toLowerCase() || '';
        const email = card.querySelector('.contact-email')?.textContent.toLowerCase() || '';
        const company = card.querySelector('.contact-company')?.textContent.toLowerCase() || '';

        const matches = name.includes(query.toLowerCase()) ||
                       phone.includes(query.toLowerCase()) ||
                       email.includes(query.toLowerCase()) ||
                       company.includes(query.toLowerCase());

        if (matches) {
            card.style.display = 'block';
            card.style.animation = 'fadeIn 0.5s ease';
            visibleCount++;
        } else {
            card.style.display = 'none';
        }
    });

    // Mostrar mensaje si no hay resultados
    if (noResults) {
        noResults.style.display = visibleCount === 0 ? 'block' : 'none';
    }

    // Actualizar contador de resultados
    updateResultsCounter(visibleCount);
}

function updateResultsCounter(count) {
    const counter = document.getElementById('resultsCounter');
    if (counter) {
        counter.textContent = `${count} contacto${count !== 1 ? 's' : ''} encontrado${count !== 1 ? 's' : ''}`;
    }
}

// Filtros de categoría
function initializeCategoryFilters() {
    const categoryChips = document.querySelectorAll('.category-chip');
    
    categoryChips.forEach(chip => {
        chip.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remover clase active de todos los chips
            categoryChips.forEach(c => c.classList.remove('active'));
            
            // Agregar clase active al chip seleccionado
            this.classList.add('active');
            
            // Aplicar filtro
            const categoryId = this.dataset.categoryId;
            filterByCategory(categoryId);
            
            // Animación del chip
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });
}

function filterByCategory(categoryId) {
    const contactCards = document.querySelectorAll('.contact-card');
    let visibleCount = 0;

    contactCards.forEach(card => {
        const cardCategoryId = card.dataset.categoryId;
        
        if (!categoryId || categoryId === 'all' || cardCategoryId === categoryId) {
            card.style.display = 'block';
            card.style.animation = 'scaleIn 0.5s ease';
            visibleCount++;
        } else {
            card.style.display = 'none';
        }
    });

    updateResultsCounter(visibleCount);
}

// Interacciones de tarjetas de contacto
function initializeContactCards() {
    const contactCards = document.querySelectorAll('.contact-card');
    
    contactCards.forEach(card => {
        // Efecto hover mejorado
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
            this.style.boxShadow = '0 20px 40px rgba(0, 0, 0, 0.15)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        });

        // Click en la tarjeta para ver detalles
        card.addEventListener('click', function(e) {
            if (!e.target.closest('.contact-actions')) {
                const contactId = this.dataset.contactId;
                if (contactId) {
                    window.location.href = `/contact/${contactId}`;
                }
            }
        });
    });
}

// Sistema de modales
function initializeModals() {
    const modalTriggers = document.querySelectorAll('[data-modal]');
    const modals = document.querySelectorAll('.modal-overlay');
    
    modalTriggers.forEach(trigger => {
        trigger.addEventListener('click', function(e) {
            e.preventDefault();
            const modalId = this.dataset.modal;
            openModal(modalId);
        });
    });

    modals.forEach(modal => {
        // Cerrar modal al hacer click en el overlay
        modal.addEventListener('click', function(e) {
            if (e.target === this) {
                closeModal(this.id);
            }
        });

        // Cerrar modal con botón de cerrar
        const closeBtn = modal.querySelector('.modal-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => closeModal(modal.id));
        }
    });

    // Cerrar modal con tecla Escape
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            const activeModal = document.querySelector('.modal-overlay.active');
            if (activeModal) {
                closeModal(activeModal.id);
            }
        }
    });
}

function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
        
        // Enfocar el primer input del modal
        const firstInput = modal.querySelector('input, textarea, select');
        if (firstInput) {
            setTimeout(() => firstInput.focus(), 100);
        }
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }
}

// Validación y mejoras de formularios
function initializeForms() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        // Validación en tiempo real
        const inputs = form.querySelectorAll('input, textarea, select');
        inputs.forEach(input => {
            input.addEventListener('blur', () => validateField(input));
            input.addEventListener('input', () => clearFieldError(input));
        });

        // Prevenir envío si hay errores
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
                showNotification('Por favor, corrige los errores en el formulario', 'error');
            }
        });
    });

    // Verificación de duplicados en tiempo real
    const nameInput = document.getElementById('name');
    const phoneInput = document.getElementById('phone');
    const emailInput = document.getElementById('email');

    if (nameInput && phoneInput && emailInput) {
        let checkTimeout;
        
        [nameInput, phoneInput, emailInput].forEach(input => {
            input.addEventListener('input', function() {
                clearTimeout(checkTimeout);
                checkTimeout = setTimeout(() => {
                    checkForDuplicates();
                }, 500);
            });
        });
    }
}

function validateField(field) {
    const value = field.value.trim();
    const fieldName = field.name;
    let isValid = true;
    let errorMessage = '';

    // Validaciones específicas
    switch (fieldName) {
        case 'name':
            if (!value) {
                isValid = false;
                errorMessage = 'El nombre es requerido';
            }
            break;
        case 'email':
            if (value && !isValidEmail(value)) {
                isValid = false;
                errorMessage = 'El formato del email no es válido';
            }
            break;
        case 'phone':
            if (value && !isValidPhone(value)) {
                isValid = false;
                errorMessage = 'El formato del teléfono no es válido';
            }
            break;
    }

    // Mostrar/ocultar error
    if (!isValid) {
        showFieldError(field, errorMessage);
    } else {
        clearFieldError(field);
    }

    return isValid;
}

function showFieldError(field, message) {
    clearFieldError(field);
    
    field.classList.add('error');
    const errorDiv = document.createElement('div');
    errorDiv.className = 'field-error';
    errorDiv.textContent = message;
    field.parentNode.appendChild(errorDiv);
}

function clearFieldError(field) {
    field.classList.remove('error');
    const existingError = field.parentNode.querySelector('.field-error');
    if (existingError) {
        existingError.remove();
    }
}

function validateForm(form) {
    const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
    let isValid = true;

    inputs.forEach(input => {
        if (!validateField(input)) {
            isValid = false;
        }
    });

    return isValid;
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function isValidPhone(phone) {
    const phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
    const cleanPhone = phone.replace(/[\s\-\(\)]/g, '');
    return phoneRegex.test(cleanPhone);
}

// Verificación de duplicados
async function checkForDuplicates() {
    const nameInput = document.getElementById('name');
    const phoneInput = document.getElementById('phone');
    const emailInput = document.getElementById('email');

    if (!nameInput || !phoneInput || !emailInput) return;

    const data = {
        name: nameInput.value.trim(),
        phone: phoneInput.value.trim(),
        email: emailInput.value.trim()
    };

    if (!data.name && !data.phone && !data.email) return;

    try {
        const response = await fetch('/api/check-duplicate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        
        if (result.has_duplicates) {
            showDuplicateWarning(result.duplicates);
        } else {
            hideDuplicateWarning();
        }
    } catch (error) {
        console.error('Error checking duplicates:', error);
    }
}

function showDuplicateWarning(duplicates) {
    let warningDiv = document.getElementById('duplicateWarning');
    
    if (!warningDiv) {
        warningDiv = document.createElement('div');
        warningDiv.id = 'duplicateWarning';
        warningDiv.className = 'notification warning';
        
        const form = document.querySelector('form');
        if (form) {
            form.insertBefore(warningDiv, form.firstChild);
        }
    }

    const duplicateList = duplicates.map(dup => 
        `<li><strong>${dup.contact.name}</strong> (${dup.type === 'phone' ? 'teléfono' : dup.type === 'email' ? 'email' : 'nombre similar'})</li>`
    ).join('');

    warningDiv.innerHTML = `
        <div class="notification-icon">⚠️</div>
        <div>
            <strong>Posibles contactos duplicados encontrados:</strong>
            <ul style="margin: 0.5rem 0 0 1rem;">${duplicateList}</ul>
        </div>
    `;
}

function hideDuplicateWarning() {
    const warningDiv = document.getElementById('duplicateWarning');
    if (warningDiv) {
        warningDiv.remove();
    }
}

// Sistema de notificaciones
function initializeNotifications() {
    // Auto-ocultar notificaciones después de 5 segundos
    const notifications = document.querySelectorAll('.notification');
    notifications.forEach(notification => {
        setTimeout(() => {
            notification.style.opacity = '0';
            setTimeout(() => notification.remove(), 300);
        }, 5000);
    });
}

function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    
    const icon = type === 'success' ? '✅' : type === 'error' ? '❌' : type === 'warning' ? '⚠️' : 'ℹ️';
    
    notification.innerHTML = `
        <div class="notification-icon">${icon}</div>
        <div class="notification-message">${message}</div>
    `;

    // Insertar al inicio del contenedor principal
    const container = document.querySelector('.container');
    if (container) {
        container.insertBefore(notification, container.firstChild);
    }

    // Auto-ocultar después de 5 segundos
    setTimeout(() => {
        notification.style.opacity = '0';
        setTimeout(() => notification.remove(), 300);
    }, 5000);
}

// Tema claro/oscuro
function initializeTheme() {
    const themeToggle = document.getElementById('themeToggle');
    if (!themeToggle) return;

    // Cargar tema guardado
    const savedTheme = localStorage.getItem('calltech-theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeToggle(savedTheme);

    themeToggle.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('calltech-theme', newTheme);
        updateThemeToggle(newTheme);
    });
}

function updateThemeToggle(theme) {
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
        themeToggle.title = theme === 'dark' ? 'Cambiar a tema claro' : 'Cambiar a tema oscuro';
    }
}

// Utilidades para compartir
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('Enlace copiado al portapapeles', 'success');
    }).catch(() => {
        // Fallback para navegadores que no soportan clipboard API
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        showNotification('Enlace copiado al portapapeles', 'success');
    });
}

function shareProfile(url) {
    if (navigator.share) {
        navigator.share({
            title: 'Mi perfil CallTech',
            text: 'Conecta conmigo a través de CallTech',
            url: url
        });
    } else {
        copyToClipboard(url);
    }
}

// Exportar funciones globales
window.CallTech = {
    showNotification,
    copyToClipboard,
    shareProfile,
    openModal,
    closeModal
};
