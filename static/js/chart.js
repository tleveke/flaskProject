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
            labels.push(formatDate(new Date(element['date'])));
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

    minDate = new Date( moment(minDate, 'YYYY-MM-DD').format('MM-DD-YYYY' ));
    maxDate = new Date( moment(maxDate, 'YYYY-MM-DD').format('MM-DD-YYYY' ));

    let labelsDate = [];
    let tabTable = [];
    let datasets;
    let compteur = 0;
    labels.map(x => {
        let datex = new Date(moment(x, 'DD-MM-YYYY').format('MM-DD-YYYY'));
        if (datex >= minDate && datex <= maxDate) {labelsDate.push(x);tabTable.push(true)}
        else { tabTable.push(false) }
    });

    let ctx = document.getElementById(type).getContext('2d');

    let data = {
       labels: labelsDate,
       datasets: []
    };

    switch (type) {
        case 'vitesse':
            datasets = vitesse
            typeAvg =arrAvg(datasets.data)
            break;
        case 'distance':
            datasets = distance
            typeAvg =arrAvg(datasets.data)
            break;
        case 'nbPanneau':
            datasets = nbPanneau
            typeAvg =arrAvg(datasets.data)
            break;
    }
    let dataofsets = {data:[], label:datasets.label,fill:datasets.fill,borderColor:datasets.borderColor};
    tabTable.map(x => {
        if (x === true) {
            dataofsets.data.push(datasets.data[compteur]);
        }
        compteur++;
    });

    data.datasets.push(dataofsets);

    // Chart declaration:
    new Chart(ctx, {
        type: 'line',
        data: data,
        options: options
    });



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
function formatDate(date) {
    let d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2)
        month = '0' + month;
    if (day.length < 2)
        day = '0' + day;

    return [day, month, year].join('-');
}
const arrAvg = arr => (arr.reduce((a,b) => a + b, 0) / arr.length).toFixed(2)