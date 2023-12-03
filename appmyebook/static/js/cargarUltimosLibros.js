document.addEventListener('DOMContentLoaded', function() {
    cargarUltimosLibros();
});

function cargarUltimosLibros() {
    fetch('/', { method: 'GET', headers: { 'X-Requested-With': 'XMLHttpRequest' } })
        .then(response => response.json())
        .then(data => {
            const librosRecientes = document.querySelector('.librosRecientes');
            librosRecientes.innerHTML = `<h3>Últimos Libros Añadidos</h3>`; // Limpia el contenedor y agrega el título
            data.ultimos_libros.forEach(libro => {
                // Crear un nuevo div para cada libro y agregar la clase librosRecientesLista
                const libroDiv = document.createElement('div');
                libroDiv.classList.add('librosRecientesLista');
                libroDiv.innerHTML = `
                    <a href="/libro/${libro.id}/"><img src="${libro.imagen_url}" alt="${libro.titulo}" /></a>
                    <p></p>
                    <a href="/libro/${libro.id}/">${libro.titulo}</a>
                `;
                librosRecientes.appendChild(libroDiv);
            });
        })
        .catch(error => console.error('Error:', error));
}
