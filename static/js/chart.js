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
let nbDemarrageData = [];
let nbArretData = [];
let nbDetecSuccessData = [];
let nbDetecErrorData = [];
let arrayTemperature = [];
let arrayHygrometrie = [];
let arrayLuminosite = [];

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
let nbDemarrage = {
        label:'nbDemarrage',
        borderColor : "#89fd13",
        fill:false
};
let nbArret = {
        label:'nbArret',
        borderColor : "#89fd13",
        fill:false
};
let nbDetecSuccess = {
        label:'nbDetecSuccess',
        borderColor : "#89fd13",
        fill:false
};
let nbDetecError = {
        label:'nbDetecError',
        borderColor : "#89fd13",
        fill:false
};

let graphTemperature = {
        label:'temperature',
        borderColor : "#89fd13",
        fill:false
};

let graphHygrometrie = {
        label:'hygrometrie',
        borderColor : "#491ddd",
        fill:false
};

let graphLuminosite = {
        label:'luminosite',
        borderColor : "#1ff5d1",
        fill:false
};

async function setupChart(status){

        status.forEach(element => {
            labels.push(element['date'].substring(0,16));
            vitesseData.push(element['vitesse']);
            distanceData.push(element['distance']);
            nbPanneauData.push(element['nbPanneau']);
            nbDemarrageData.push(element['nbDemarrage']);
            nbArretData.push(element['nbArret']);
            nbDetecSuccessData.push(element['nbDetecSuccess']);
            nbDetecErrorData.push(element['nbDetecError']);
            arrayTemperature.push(element['temperature']);
            arrayHygrometrie.push(element['hygrometrie']);
            arrayLuminosite.push(element['luminosite']);
        });

        vitesse.data = vitesseData;
        distance.data = distanceData;
        nbPanneau.data = nbPanneauData;
        nbDemarrage.data = nbDemarrageData;
        nbArret.data = nbArretData;
        nbDetecSuccess.data = nbDetecSuccessData;
        nbDetecError.data = nbDetecErrorData;
        graphTemperature.data = arrayTemperature;
        graphHygrometrie.data = arrayHygrometrie;
        graphLuminosite.data = arrayLuminosite;






        return [true,labels[0],labels[labels.length-1]];
    }

function chartDate(type, minDate, maxDate) {

    minDate = new Date( moment(minDate, 'YYYY-MM-DD HH:mm').format('MM-DD-YYYY HH:mm' ));
    maxDate = new Date( moment(maxDate, 'YYYY-MM-DD HH:mm').format('MM-DD-YYYY HH:mm' ));

    let tabTable = [];
    let datasets;
    let compteur = 0;

    let ctx = document.getElementById(type).getContext('2d');

    let data = {
       labels: labels,
       datasets: []
    };
    switch (type) {
        case 'vitesse':
            datasets = vitesse
            break;
        case 'distance':
            datasets = distance
            break;
        case 'nbPanneau':
            datasets = nbPanneau
            break;
        case 'nbDemarrage':
            datasets = nbDemarrage
            break;
        case 'nbArret':
            datasets = nbArret
            break;
        case 'nbDetecSuccess':
            datasets = nbDetecSuccess
            break;
        case 'nbDetecError':
            datasets = nbDetecError
            break;
        case 'temperature':
            datasets = graphTemperature
            break;
        case 'hygrometrie':
            datasets = graphHygrometrie
            break;
        case 'luminosite':
            datasets = graphLuminosite
            break;
    }


    data.datasets.push(datasets);

    // Chart declaration:
    new Chart(ctx, {
        type: 'line',
        data: data,
        options: options
    });


    typeAvg = arrAvg(datasets.data)
    document.getElementById('moyenne').innerText = typeAvg.toString();




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