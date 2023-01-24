function solution(today, terms, privacies) {
    var answer = [];
    var obj = {};
    var todayArr = today.split('.');
    var year = todayArr[0];
    var month = todayArr[1];
    var day = todayArr[2];

    for(var t in terms){
        var tArr = terms[t].split(' ');
        var key = tArr[0];
        obj[key] = tArr[1];
    }

    for(var i=0; i<privacies.length; i++){
        var p = privacies[i];
        var pArr = p.split(' ');
        var key = pArr[1];

        var pDate = pArr[0].split('.');
        var pYear = Number(pDate[0]);
        var pMonth = Number(pDate[1]);
        var pDay = Number(pDate[2]);

        var value = Number(obj[key]);
        
        var plusYear = Math.floor(value / 12);
        var plusMonth = value % 12;
        // console.log(pYear, pMonth, pDay);
        // console.log(plusYear, plusMonth);

        pYear = pYear + plusYear;
        pMonth = pMonth + plusMonth;

        if(pMonth > 12){
            pYear = pYear + 1;
            pMonth = pMonth - 12;
        }
        
        pDay = pDay - 1;
        if(pDay < 1){
            pMonth = pMonth - 1;
            pDay = 28;
        }
        
        // console.log(pYear, pMonth, pDay);
        // console.log();

        if(pYear > year){
            continue;
        }

        if(pYear < year){
            answer[answer.length] = (i+1);
            continue;
        }

        if(pMonth > month){
            continue;
        }

        if(pMonth < month) {
            answer[answer.length] = (i+1);
            continue;
        }
        
        if(pDay < day) {
            answer[answer.length] = (i+1);
            continue;
        }
    }

    return answer;
}

today = '2022.05.19';
terms = [ 'A 6', 'B 12', 'C 3' ];
privacies = [ '2021.05.02 A', '2021.07.01 B', '2022.02.19 C', '2022.02.20 C' ];
console.log(solution(today, terms, privacies));