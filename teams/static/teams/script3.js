$(document).ready(function(){
    var endpoint = '/blk/api-rest-data/'

    //var customersDjango = parseInt("{{ customers }}") *2
    //console.log(customersDjango)
    var labels = []
    var defaultData = []

    $.ajax({
      method: 'GET',
      url: endpoint,
      success: function(data){
        labels = data.teams
        defaultData = data.two_fgm
        console.log(labels)
        console.log(defaultData)
        //console.log(typeof data)
        

        //chart1
        var ctx = document.getElementById("myChart1").getContext('2d');

        var gradient = ctx.createLinearGradient(0, 0, 0, 330);
        gradient.addColorStop(0, 'green');
        gradient.addColorStop(0.5, 'grey');
        gradient.addColorStop(1, 'red');
        
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: '2FG Made',
                    data: defaultData,
                    backgroundColor: gradient,
                    borderColor: gradient,
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:false
                        }
                    }]
                }
            }
        });





        //chart2
        labels = data.teams
        defaultData = data.two_fgms
        console.log(labels)
        console.log(defaultData)

        var ctx = document.getElementById("myChart2").getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: '2FG Missed',
                    data: defaultData,
                    backgroundColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:false
                        }
                    }]
                }
            }
        });


        //chart3
        labels = data.teams
        defaultData = data.two_prtg
        console.log(labels)
        console.log(defaultData)

        var ctx = document.getElementById("myChart3").getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: '2FG%',
                    data: defaultData,
                    backgroundColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:false
                        }
                    }]
                }
            }
        });

        
        //console.log(data)
        //console.log(data.customers * 100)
      },
      error: function(error_data){
        console.log("error")
        console.log(error_data)
      }
    })

})
