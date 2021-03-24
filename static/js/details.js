

var typeChart = document.currentScript.getAttribute('typeChart');
console.log("typeChart")
console.log(typeChart)

axios.get('http://10.44.17.198:5000/api/voiture/all_' + typeChart)
    .then(response => {
            data = []
            for (let i = 0; i <= 50 && i < response.data.length; i++) {
                data.push(response.data[i])
            }
            setupChart(data).then(status => {
                if (status[0]) {
                    chartDate(document.getElementsByTagName('canvas')[0].id, data[0].date,data[data.length-1].date) ;
                   // chartGenéral();
                }
            });

    })
    .catch(error => console.error(error));
