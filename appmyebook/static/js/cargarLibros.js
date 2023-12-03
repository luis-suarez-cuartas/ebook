document.addEventListener('DOMContentLoaded', function() {
    cargarLibros();
});

function cargarLibros() {
    fetch('/libros/', {
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
