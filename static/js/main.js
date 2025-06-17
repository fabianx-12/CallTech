// Cambio de tema mejorado
const themeToggle = document.getElementById('themeToggle');
const themeIcon = document.getElementById('themeIcon');
const html = document.documentElement;

// Cargar tema guardado
const savedTheme = localStorage.getItem('theme') || 'light';
html.setAttribute('data-theme', savedTheme);

// Función para actualizar el icono del tema
function updateThemeIcon(theme) {
    if (theme === 'dark') {
        themeIcon.textContent = '☀️';
        themeToggle.title = 'Cambiar a modo claro';
    } else {
        themeIcon.textContent = '🌙';
        themeToggle.title = 'Cambiar a modo oscuro';
    }
}

// Establecer icono inicial
if (themeToggle && themeIcon) {
    updateThemeIcon(savedTheme);
    
    // Event listener para cambio de tema
    themeToggle.addEventListener('click', () => {
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        // Agregar animación de transición
        html.style.transition = 'all 0.3s ease';
        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        
        // Actualizar icono
        updateThemeIcon(newTheme);
        
        // Remover transición después de la animación
        setTimeout(() => {
            html.style.transition = '';
        }, 300);
    });
}

// Función de búsqueda
function initializeSearch() {
    const searchInput = document.getElementById('searchInput');
    const contactCards = document.querySelectorAll('.contact-card');
    
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            
            contactCards.forEach(card => {
                const name = card.querySelector('.contact-name')?.textContent.toLowerCase() || '';
                const phone = card.querySelector('.contact-info')?.textContent.toLowerCase() || '';
                const email = card.querySelector('.contact-info:nth-of-type(2)')?.textContent.toLowerCase() || '';
                
                if (name.includes(searchTerm) || phone.includes(searchTerm) || email.includes(searchTerm)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }
}

// Función para filtros de categoría
function initializeCategoryFilters() {
    const categoryChips = document.querySelectorAll('.category-chip');
    const contactCards = document.querySelectorAll('.contact-card');
    
    categoryChips.forEach(chip => {
        chip.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remover clase active de todos los chips
            categoryChips.forEach(c => c.classList.remove('active'));
            
            // Agregar clase active al chip clickeado
            this.classList.add('active');
            
            const category = this.textContent.trim().toLowerCase();
            
            contactCards.forEach(card => {
                const cardCategory = card.querySelector('.contact-category')?.textContent.toLowerCase() || '';
                
                if (category === 'todos' || cardCategory.includes(category)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    initializeSearch();
    initializeCategoryFilters();
});
