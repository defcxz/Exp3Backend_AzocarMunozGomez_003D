function validar() {
	var user = document.getElementById("user");
	var email = document.getElementById("email");
	var pass1 = document.getElementById("pass1");
	var pass2 = document.getElementById("pass2");
	var nombre = document.getElementById("nombre")
	var sexo = document.getElementsByName("sexo");
	var seleccionado = false;
	var region = document.getElementById("region").selectedIndex;
	var elementoCHECK = document.getElementById("terminos");
    

	if(user.value.length == 0)
	{
      alert("Debe ingresar el Usuario");
    	user.focus();
    	return false;
	}
	if(email.value.length == 0)
	{
		alert("Por favor, ingrese su Email");
		email.focus();
		return false;
	}
	if(pass1.value.length < 8)
	{
		alert("Debe ingresar una contraseña de más de 8 caracteres");
		pass1.focus();
		return false;
	}
	else if(pass1.value != pass2.value)
	{
		alert("Las contraseñas no coinciden");
		pass2.focus();
		return false;
	}
	
	if(nombre.value.length == 0)
	{
      alert("Debes ingresar Tu Nombre y Apellido");
    	nombre.focus();
    	return false;
	}


	for(var i = 0; i<sexo.length; i++)
	{
		if(sexo[i].checked)
		{
			seleccionado = true;
		}
	}
	if(!seleccionado)
	{
		alert("Debes indicar el sexo");
		return false;
	}
	if(region == 0 || region == null)
	{
		alert("Por favor, seleccione una region");
		return false;
	}
    

	if(!elementoCHECK.checked)
	{
		alert("Debe aceptar los términos y condiciones");
		return false;
	}
  else
  {
    alert("Datos de formulario enviados exitosamente.");
    document.getElementById("myForm").reset();
	  return false;
	}
}

