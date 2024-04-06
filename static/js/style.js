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


function abrirporfecha() {
    var fecha = document.getElementById('fecha-input');

    if (fecha.classList.contains('fecha-input-hidden')) {
        fecha.classList.remove('fecha-input-hidden');
        fecha.classList.add('fecha-input');
    } else {
        fecha.classList.remove('fecha-input');
        fecha.classList.add('fecha-input-hidden');
    }
}

function abrirhistorial(){
    var btn = document.getElementById('history-down');

    btn.classList.toggle('view-history')
}

function verhistoryindex(){
    var tbl = document.getElementById('table-history-false')
     
    if(tbl.classList.contains('table-history-false')){
        tbl.classList.remove('table-history-false')
        tbl.classList.add('table-history')

    }else{
        tbl.classList.remove('table-history')
        tbl.classList.add('table-history-false')
    }
}

var alertElement1 = document.getElementById('alert-good');
var alertElement2 = document.getElementById('alert-false');
var alertElement3 = document.getElementById('alertatruecorreo');



setTimeout(function() {
  alertElement1.style.opacity = '0';
  alertElement1.style.display = 'none';
}, 5000);
setTimeout(function() {
    alertElement2.style.opacity = '0';
    alertElement2.style.display = 'none';
  }, 5000);

setTimeout(function(){
    alertElement3.style.opacity = '0';
    alertElement3.style.display = 'none';
}, 5000)
function mostrarbtnsmenu(){
    var boton_contratos = document.getElementById('btnmenu-contratos');
    var boton_reasignacines = document.getElementById('btnmenu-reasignaciones')
    

    
}   
// function mostrarmenu(){
//         document.getElementById("mostrar-menu").addEventListener("click", function () {
//         var menu = document.getElementById("menu");
//         var button = document.getElementById("mostrar-menu");
//         button.classList.toggle("btn-move");

//         if (button.classList.contains("btn-move")) {
//             button.style.animation = "rotate 0.7s linear forwards";
//         } else {
//             button.style.animation = "rotate-back 0.9s linear forwards";
//         }

//         menu.classList.toggle("active");

//         if (menu.classList.contains("active")) {
//             button.classList.add("btn-move");
//         } else {
//             button.classList.remove("btn-move");
//         }
//     })
// };


