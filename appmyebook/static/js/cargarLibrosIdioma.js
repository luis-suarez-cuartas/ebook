function getLanguagePrefix() {
    const path = window.location.pathname.split('/');
    return path[1]; // El prefijo del idioma es el segundo segmento de la URL
}

function getIdiomaIdFromUrl() {
    const path = window.location.pathname.split('/');
    return path[3]; // Asumiendo que el ID del idioma está en el cuarto segmento
}

document.addEventListener('DOMContentLoaded', function() {
    const languagePrefix = getLanguagePrefix();
    const idiomaId = getIdiomaIdFromUrl();
    cargarLibrosIdioma(languagePrefix, idiomaId);
});

function cargarLibrosIdioma(languagePrefix, idiomaId) {
    const url = `/${languagePrefix}/idioma/${idiomaId}/`;
    fetch(url, {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        const contenedorLibros = document.getElementById('contenedorLibros');
        const nombreIdioma = document.querySelector('.paginaIdioma h3');
        const descripcionIdioma = document.querySelector('.paginaIdioma p');

        // Actualiza los campos de idioma
        nombreIdioma.textContent = `Libros en ${data.idioma.nombre}`;
        descripcionIdioma.textContent = `Aquí encontrarás una selección de libros en ${data.idioma.nombre}. Explora una variedad de títulos y géneros literarios disponibles en este idioma.`;

        // Actualiza los libros
        contenedorLibros.innerHTML = '';
        data.libros.forEach(libro => {
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
