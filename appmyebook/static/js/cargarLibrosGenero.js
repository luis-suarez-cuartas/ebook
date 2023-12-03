
function getGeneroIdFromUrl() {
    const path = window.location.pathname.split('/');
    return path[2];
}

document.addEventListener('DOMContentLoaded', function() {
    cargarLibrosGenero(getGeneroIdFromUrl());
});

function cargarLibrosGenero(generoId) {
    fetch(`/genero/${generoId}/`, {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        const contenedorLibros = document.getElementById('contenedorLibros');
        const nombreGenero = document.querySelector('.paginaGenero h3');
        const descripcionGenero = document.querySelector('.paginaGenero p');

        // Actualiza los campos de género
        nombreGenero.textContent = data.genero.nombre;
        descripcionGenero.textContent = data.genero.descripcion;

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