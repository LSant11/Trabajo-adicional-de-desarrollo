const nombre = document.getElementById('nombre');
const email = document.getElementById('email');
const enviar = document.getElementById('enviar');

nombre.addEventListener('input', validarFormulario);
email.addEventListener('input', validarFormulario);

function validarFormulario() {
  if (nombre.value.trim() !== '' && email.value.trim() !== '') {
    enviar.disabled = false;
  } else {
    enviar.disabled = true;
  }
}