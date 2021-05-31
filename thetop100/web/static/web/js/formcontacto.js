$(function(){
   $("#formcontacto").validate({
      
         rules: {
               nombre: "required",
               email: {
                     required: true,
                     email: true
               },
               password: "required",
               fono: "required"  
               
            }, //rules
         messages: {
            nombre: { 
               required: "No puedes dejar este campo en blanco",
               minlength: 'Caracteres insuficientes'
            },
            email: {
               required: 'Ingresa tu correo electrónico',
               email: 'Formato de correo no válido'
            },
            password: {
               required: 'Ingresa una contraseña',
               minlength: 'Caracteres insuficientes'
            },
            fono:{
               required: 'Ingrese un número de celular',
               minlength: 'Cantidad de digitos insuficiente'
            },
            fecha:{
               required: 'Seleccione una fecha válida',
               min: 'Fecha no corresponde'
            },
            asunto: {
               required: 'No puedes dejar este campo en blanco',
               minlength: 'Caracteres insuficientes'
            },
            mensaje: { 
               required: 'No puedes dejar este campo en blanco',
               minlength: 'Cantidad de dígitos insuficientes'}
         }//se cierran los mensajes
   }); //validación
}); //function

function CambiarMayusculas()
      {
         String.prototype.initCap = function () {
            return this.toLowerCase().replace(/(?:^|\s)[a-z]/g, function (m) {
               return m.toUpperCase();
            });
         };

         a = document.getElementById("nombre");
         a.value = a.value.initCap();
         console.log('funciono!');
      }