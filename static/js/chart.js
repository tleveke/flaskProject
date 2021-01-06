let options = {
          scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        },
                        scaleLabel: {
                             display: true,
                             labelString: '',
                             fontSize: 20
                          }
                    }]
                }
        };

// Global Options:
Chart.defaults.global.defaultFontColor = 'black';
Chart.defaults.global.defaultFontSize = 16;

let labels = [];
let vitesseData = [];
let distanceData = [];
let nbPanneauData = [];

let vitesse = {
        label:'Vitesse',
        borderColor : "#3e95cd",
        fill:false
};
let distance = {
        label:'Distance',
        borderColor : "#e70606",
        fill:false
};
let nbPanneau = {
        label:'nbPanneau',
        borderColor : "#89fd13",
        fill:false
};

async function setupChart(status){

        status.forEach(element => {
            labels.push(element['date']);
            vitesseData.push(element['vitesse']);
            distanceData.push(element['distance']);
            nbPanneauData.push(element['nbPanneau']);
        });

        vitesse.data = vitesseData;
        distance.data = distanceData;
        nbPanneau.data = nbPanneauData;






        return [true,labels[0],labels[labels.length-1]];
    }

function chart(type) {

        let ctx = document.getElementById(type).getContext('2d');

        let data = {
          labels: labels,
          datasets: []
        };

        let typeAvg = 0;

        switch (type) {
            case 'vitesse':
                data.datasets.push(vitesse)
                typeAvg = arrAvg(vitesse.data)

                break;
            case 'distance':
                data.datasets.push(distance)
                typeAvg= arrAvg(distance.data)
                break;
            case 'nbPanneau':
                data.datasets.push(nbPanneau)
                typeAvg =arrAvg(nbPanneau.data)
                break;
        }
        // Chart declaration:
        new Chart(ctx, {
          type: 'line',
          data: data,
          options: options
        });

        document.getElementById('moyenne').innerText = typeAvg.toString();


}

function chartDate(type, minDate, maxDate) {
    let labelsDate = [];
    labels.map(x => {if (new Date(x) > new Date(minDate) && x < new Date(maxDate)) {labelsDate.push(x)} });

}

function chartGenéral() {
        let ctx = document.getElementById("myChart").getContext('2d');

        var data = {
          labels: labels,
          datasets: [vitesse,distance,nbPanneau]
        };

        // Chart declaration:
        new Chart(ctx, {
          type: 'line',
          data: data,
          options: options
        });
}


const arrAvg = arr => (arr.reduce((a,b) => a + b, 0) / arr.length).toFixed(2)