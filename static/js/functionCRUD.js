  //JQUERY
        //AJAX => jAVAsCRIPT Asincrono y XML
        function CRUD (idbco, bank , url){
            var formData ={
                idbco: idbco,
                bank:bank
            };
           //Realizar solicitud AJAX  usando JQuey
           $.ajax({
                    //configurar solicitud POST
                    type:'POST',
                    //Especificar la URL
                    url: url,
                    contentType: 'application/json;charset=UTF-8',
                    //CONVERTIR obj a JSON
                    data: JSON.stringify(formData),

                    success: function (response) {
                        //Ejecucion correcta
                        Swal.fire({
                                  icon: "info",
                                  title: "Mantenimiento",
                                  text: "Operación Realizada!",
                                   willClose :  function () {
                                        window.location.href = '/allBanks';
                                   }
                                });
            },
            //Funcion ejecuta en caso de error
            error: function (error){
                console.error('Error',error);
            }
        });
        }