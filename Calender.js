//calender 

const daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
const monthsOfYear = ["January", "Feburary", "March", "April", "May", "June", "July", "August", 
"September", "October", "November", "December"];
const thirtyDayMonths = [4, 6, 9, 11];

// program to check leap year
function checkLeapYear(year) {

    //three conditions to find out the leap year
    if ((0 == year % 4) && (0 != year % 100) || (0 == year % 400)) {
        return true;
    } else {
        return false;
    }
}

function cycleThrough(weekCycle) {
    var counter = 1;
    for(var k = 0; k < weekCycle; k++) {
        if(k === 4) {
        for(var p = 1; p <= 3; p++) {
             console.log(counter + daysOfWeek[p]);
             counter++;
        }
         counter++;
      }else {
        for(var p = 1; p <= 7; p++) {
             console.log(counter + daysOfWeek[p]);
             counter++;
        }
         counter++;
      }
       
    }
}

function betterCycleThrough(numberOfDays) {
    var weekVal = 7, weekCount = 1, output = [];
    for(var i = 1; i <= numberOfDays; i++) {
        
        if(i <= 7) {
        output.push("|");
        output.push(i + " " + daysOfWeek[i-1]);
        if(i === 7) output.push("\n");
        
        }else if(i > 7 && i <= 14) {
        output.push("|");
        output.push(i + " " + daysOfWeek[i - (weekCount * weekVal)-1]);
        if(i === 14) output.push("\n");
        
        }else if(i > 14 && i <= 21) {
        output.push("|");
        output.push(i + " " + daysOfWeek[(i - (2 * 7))-1]);
        if(i === 21) output.push("\n");
        
        }else if(i > 21 && i <= 28) {
        output.push("|");
        output.push(i + " " + daysOfWeek[i - (3 * weekVal)-1]);
        if(i === 28) output.push("\n");
        
        }else {
        output.push("|");
        output.push(i + " " + daysOfWeek[i - (4 * weekVal)-1]);
        
        }
    }
    
    console.log(output.join(" "));
    
}

function printCalender(userInputYear) {
    var isLeapYear = checkLeapYear(userInputYear);
    var feburaryIs29Days = 0, counter = 1;
    var monthVal1 = 30, monthVal2 = 31, monthVal3 = 28;
    if(isLeapYear === true) {
        feburaryIs29Days = 1;
    }
    
    if(feburaryIs29Days === 0) {
        
        for(var i = 0; i < monthsOfYear.length; i++) {
            //console.log("\n");
            console.log(monthsOfYear[i]);
            console.log("--------------------------------------------------------------------------------------------");
            switch(monthsOfYear[i]) {
            case "January":
             betterCycleThrough(31);
            break;   
            case "Feburary":
             betterCycleThrough(28);
            break;
            case "March":
             betterCycleThrough(31);
            break;
            case "April":
             betterCycleThrough(30);
            break;
            case "May":
             betterCycleThrough(31);
            break;
            case "June":
             betterCycleThrough(30);
            break;
            case "July":
             betterCycleThrough(31);
            break;
            case "August":
             betterCycleThrough(31);
            break;
            case "September":
             betterCycleThrough(30);
            break;
            case "October":
             betterCycleThrough(31);
            break;
            case "November":
             betterCycleThrough(30);
            break;
            case "December":
             betterCycleThrough(31);
            break;
            }
        }
    }else {
         for(var i = 0; i < monthsOfYear.length; i++) {
            console.log(monthsOfYear[i]);
            console.log("------------------------------");
            switch(monthsOfYear[i]) {
            case "January":
             betterCycleThrough(31);
            break;   
            case "Feburary":
             betterCycleThrough(29);
            break;
            case "March":
             betterCycleThrough(31);
            break;
            case "April":
             betterCycleThrough(30);
            break;
            case "May":
             betterCycleThrough(31);
            break;
            case "June":
             betterCycleThrough(30);
            break;
            case "July":
             betterCycleThrough(31);
            break;
            case "August":
             betterCycleThrough(31);
            break;
            case "September":
             betterCycleThrough(30);
            break;
            case "October":
             betterCycleThrough(31);
            break;
            case "November":
             betterCycleThrough(30);
            break;
            case "December":
             betterCycleThrough(31);
            break;
            }
        }
    }
    
}

var inputOfYear = 2026;
var isLeapYear = checkLeapYear(inputOfYear);

console.log(printCalender(inputOfYear));





