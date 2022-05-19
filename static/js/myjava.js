$("#btn_consultar").on('click', function(){
    $.ajax({
        type: 'get',
        url : "/api/apidate",
        data: $("#form_fecha").serialize(),
        success: function(data){
            console.log(data);
            var fechas =[];var datos =[];var color =[];
            var fechas_dolar =[];var datos_dolar =[];var color_dolar =[];
            var fechas_tiie =[];var datos_tiie =[];var color_tiie =[];

            $("#tb_resultados tr").remove(); $("#tb_resultados_dolar tr").remove(); $("#tb_resultados_tiie tr").remove(); 

            if (data =="Error" || data =="Error en fechas"){
                MensajeError();
                $('#myChart').remove();
                $('#myChart11').remove(); // this is my <canvas> element
                $('#contenedor').append('<canvas id="myChart11"><canvas>');
                $("#udis_promedio").text("");$("#udis_max").text("");$("#udis_min").text("");
                $("#dolar_promedio").text("");$("#dolar_max").text("");$("#dolar_min").text("");
                $("#tiie_promedio").text("");$("#tiie_max").text("");$("#tiie_min").text("");
                
            }else{
                $("#udis_promedio").text(data.promedio);$("#udis_max").text(data.max_value);$("#udis_min").text(data.min_value);
                $("#dolar_promedio").text(data.promedio_dolar);$("#dolar_max").text(data.max_value_dolar);$("#dolar_min").text(data.min_value_dolar);
                $("#tiie_promedio").text(data.promedio_tiie);$("#tiie_max").text(data.max_value_tiie);$("#tiie_min").text(data.min_value_tiie);
                for(var i in data.list){
                    $('#tb_resultados').parent().append('<tr><td id="fecha">' + data.list[i].fecha + '</td><td>' + data.list[i].dato + '</td></tr>');
                    color.push(Colores());fechas.push(data.list[i].fecha);datos.push(data.list[i].dato);
                }
                for(var j in data.list_dolar){
                    $('#tb_resultados_dolar').parent().append('<tr><td>' + data.list_dolar[j].fecha + '</td><td>' + data.list_dolar[j].dato + '</td></tr>');
                    color_dolar.push(Colores());fechas_dolar.push(data.list_dolar[j].fecha);datos_dolar.push(data.list_dolar[j].dato);
                }
                for(var k in data.list_tiie){
                    $('#tb_resultados_tiie').parent().append('<tr><td>' + data.list_tiie[k].fecha + '</td><td>' + data.list_tiie[k].dato + '</td></tr>');
                    color_tiie.push(Colores());fechas_tiie.push(data.list_tiie[k].fecha);datos_tiie.push(data.list_tiie[k].dato);
                }
                $('#myChart').remove();$('#myChart11').remove(); $('#contenedor').append('<canvas id="myChart11"><canvas>');
                $('#myChartDolar').remove();$('#myChart22').remove(); $('#contenedorDolar').append('<canvas id="myChart22"><canvas>');
                $('#myChartTiie').remove();$('#myChart33').remove(); $('#contenedorTiie').append('<canvas id="myChart33"><canvas>');

                var ctxUDIS = document.getElementById('myChart11').getContext('2d');
                var ctxDOLAR = document.getElementById('myChart22').getContext('2d');
                var ctxTIIE = document.getElementById('myChart33').getContext('2d');

                var mychartUDIS = new Chart(ctxUDIS,{
                  type:'bar',
                  data:{
                    labels: fechas,
                    datasets:[{
                      label:'UDIS',
                      data: datos,
                      backgroundColor: color,
                      borderWidth:1,
          
                    }]
                  },
                   options:{
                    responsive: true,
                    title: {
                      display: false,
                      position: "top",
                      fontSize: 18,
                      fontColor: "#111"
                    },
                    legend: {
                      display: false,
                      position: "bottom",
                      labels: {
                        fontColor: "#333",
                        fontSize: 16,
                      }
                    },
                    scales: {
                        y: {
                            suggestedMin: .5,
                            suggestedMax: 1
                        }
                    }
                  }
                });
                var mychartDOLAR = new Chart(ctxDOLAR,{
                    type:'bar',
                    data:{
                      labels: fechas_dolar,
                      datasets:[{
                        label:'DOLAR',
                        data: datos_dolar,
                        backgroundColor: color_dolar,
                        borderWidth:1,
            
                      }]
                    },
                     options:{
                      responsive: true,
                      title: {
                        display: false,
                        position: "top",
                        fontSize: 18,
                        fontColor: "#111"
                      },
                      legend: {
                        display: false,
                        position: "bottom",
                        labels: {
                          fontColor: "#333",
                          fontSize: 16,
                        }
                      },
                      scales: {
                          y: {
                              suggestedMin: .5,
                              suggestedMax: 1
                          }
                      }
                    }
                });
                var mychartTIIE = new Chart(ctxTIIE,{
                    type:'bar',
                    data:{
                      labels: fechas_tiie,
                      datasets:[{
                        label:'TIIE',
                        data: datos_tiie,
                        backgroundColor: color_tiie,
                        borderWidth:1,
            
                      }]
                    },
                     options:{
                      responsive: true,
                      title: {
                        display: false,
                        position: "top",
                        fontSize: 18,
                        fontColor: "#111"
                      },
                      legend: {
                        display: false,
                        position: "bottom",
                        labels: {
                          fontColor: "#333",
                          fontSize: 16,
                        }
                      },
                      scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                      }
                    }
                });
            }


        }
    });

});
function Colores() {
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() * 255);
    var b = Math.floor(Math.random() * 255);
    return "rgb(" + r + "," + g + "," + b + ",0.5)";
}

function MensajeError() {
    $.confirm({
        icon: 'fa fa-close',
        columnClass: 'col-md-3',
        title: '¡ERROR!',
        content: 'Error en rangos de fechas',
        type: 'red',
        typeAnimated: true,
        buttons: {
            tryAgain: {
                text: 'Cerrar',
                btnClass: 'btn-red',
                action: function () { },
            },
        }
    });
}