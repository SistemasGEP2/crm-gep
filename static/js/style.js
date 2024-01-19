var valorPosicion = 0; 

window.addEventListener('scroll', function() {
    var id_header = document.getElementById("id_header");
    var posicionScroll = window.scrollY;

    if (posicionScroll > valorPosicion) {
        id_header.classList.remove('header');
        id_header.classList.add('header-up');
        console.log("Scroll hacia abajo - Posición: " + posicionScroll);
    } else {
        id_header.classList.remove('header-up');
        id_header.classList.add('header');
        console.log("Scroll hacia arriba - Posición: " + posicionScroll);
    }

    valorPosicion = posicionScroll; 
});

function actualizarServ(){
    var actualizar = document.getElementById('iframe1');
    var cerrar = document.getElementById('close1');
    
    actualizar.classList.remove('iframe1');
    actualizar.classList.add('iframeView');
    cerrar.classList.remove('close');
    cerrar.classList.add('closeView');
}
function actualizarServ() {
    var actualizar = document.getElementById('iframe1');
    var cerrar = document.getElementById('close1');
    
    actualizar.classList.remove('iframe1');
    actualizar.classList.add('iframeView');
    cerrar.classList.remove('close');
    cerrar.classList.add('closeView');
}

function cerrarView() {
    var actualizar = document.getElementById('iframe1');
    var cerrar = document.getElementById('close1');

    actualizar.classList.remove('iframeView');
    actualizar.classList.add('iframe1');
    cerrar.classList.remove('closeView');
    cerrar.classList.add('close');
}







