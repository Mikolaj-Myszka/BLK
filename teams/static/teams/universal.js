$(document).ready(function(){
    var endpoint = {{ endpoint2 }}
    console.log(endpoint)
    //var customersDjango = parseInt("{{ customers }}") *2
    //console.log(customersDjango)
    var labels = []
    var defaultData = []
    var fLen, i
    var cats = []
    var reverse_gradient_flag = []
    //var chartName = "myChart"
    

    $.ajax({
      method: 'GET',
      url: endpoint,
      success: function(data){
        labels = data.teams
        defaultData = data.lol
        fLen = defaultData.length
        cats = data.lol2
        reverse_gradient_flag = data.reverse_gradient_flag
        console.log(labels)
        console.log(defaultData)
        console.log('fLen', fLen)
        //console.log(typeof data)

        for (i = 0; i < fLen; i++) {
            //chart1
            //chartName += i+1;
            var ctx = document.getElementById("myChart"+(i+1)).getContext('2d');

            var gradient = ctx.createLinearGradient(0, 0, 0, 330);
            if (reverse_gradient_flag[i] == 0) {
                gradient.addColorStop(0, 'green');
                gradient.addColorStop(1, 'red');
            } else {
                gradient.addColorStop(1, 'green');
                gradient.addColorStop(0, 'red');
            }
            gradient.addColorStop(0.5, 'grey');
            
            
            var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: "Europe",
                        type: "line",
                        borderColor: "#8e5ea2",
                        //data: [20,20,20,20],
                        fill: false
                    },{
                        label: cats[i],
                        data: defaultData[i],
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
        }
        

        

        
        //console.log(data)
        //console.log(data.customers * 100)
      },
      error: function(error_data){
        console.log("error")
        console.log(error_data)
      }
    })

})
