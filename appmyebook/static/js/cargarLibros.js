
function getLanguagePrefix() {
    const path = window.location.pathname.split('/');
    return path[1]; // El prefijo del idioma es el segundo segmento de la URL
}

document.addEventListener('DOMContentLoaded', function() {
    const languagePrefix = getLanguagePrefix();
    cargarLibros(languagePrefix);

});

function cargarLibros(languagePrefix) {
    const url = `/${languagePrefix}/libros/`;
    fetch(url, {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(libros => {
        const contenedorLibros = document.getElementById('contenedorLibros');
        contenedorLibros.innerHTML = '';
        libros.forEach(libro => {
            contenedorLibros.innerHTML += `
                <li>
                    <div class="libro-item">
                        <a href="/libro/${libro.id}/">
                            <img src="${libro.imagen_url}" alt="${libro.titulo}" />
                        </a>
                        <p></p>
                        <a href="/libro/${libro.id}/">${libro.titulo}</a>
                    </div>
                </li>`;
        });
    })
    .catch(error => console.error('Error:', error));
}
