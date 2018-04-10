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
                    label: "Europe",
                    type: "line",
                    borderColor: "#8e5ea2",
                    data: [20,20,20,20],
                    fill: false
                },{
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

        var gradient = ctx.createLinearGradient(0, 0, 0, 330);
        gradient.addColorStop(0, 'red');
        gradient.addColorStop(0.5, 'grey');
        gradient.addColorStop(1, 'green');
        
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: '2FG Missed',
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


        //chart3
        labels = data.teams
        defaultData = data.two_prtg
        console.log(labels)
        console.log(defaultData)

        var ctx = document.getElementById("myChart3").getContext('2d');

        var gradient = ctx.createLinearGradient(0, 0, 0, 330);
        gradient.addColorStop(0, 'green');
        gradient.addColorStop(0.5, 'grey');
        gradient.addColorStop(1, 'red');
        
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: '2FG%',
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




        //chart4
        labels = data.teams
        defaultData = data.three_fgm
        console.log(labels)
        console.log(defaultData)
        //console.log(typeof data)
        
        var ctx = document.getElementById("myChart4").getContext('2d');

        var gradient = ctx.createLinearGradient(0, 0, 0, 330);
        gradient.addColorStop(0, 'green');
        gradient.addColorStop(0.5, 'grey');
        gradient.addColorStop(1, 'red');
        
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: "Europe",
                    type: "line",
                    borderColor: "#8e5ea2",
                    data: [4,4,4,4],
                    fill: false
                },{
                    label: '3FG Made',
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





        //chart5
        labels = data.teams
        defaultData = data.three_fgms
        console.log(labels)
        console.log(defaultData)

        var ctx = document.getElementById("myChart5").getContext('2d');

        var gradient = ctx.createLinearGradient(0, 0, 0, 330);
        gradient.addColorStop(0, 'red');
        gradient.addColorStop(0.5, 'grey');
        gradient.addColorStop(1, 'green');
        
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: '3FG Missed',
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


        //chart6
        labels = data.teams
        defaultData = data.three_prtg
        console.log(labels)
        console.log(defaultData)

        var ctx = document.getElementById("myChart6").getContext('2d');

        var gradient = ctx.createLinearGradient(0, 0, 0, 330);
        gradient.addColorStop(0, 'green');
        gradient.addColorStop(0.5, 'grey');
        gradient.addColorStop(1, 'red');
        
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: '3FG%',
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

        
        //console.log(data)
        //console.log(data.customers * 100)
      },
      error: function(error_data){
        console.log("error")
        console.log(error_data)
      }
    })

})
