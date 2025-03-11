
var Person = {};

var keyChange = {
    gender: "Gender",
    fname: "First name",
    mname: "Middle name",
    lname: "Last name",
    birthday_date: "Birthday date",
    personal_code: "Personal code",
    education: "Level of education",
    phone: "Phone number", 
    email: "Email address", 
    address: "Physical address",
    martial_status: "Martial status",
    professional_pos: "Professional position",
    work_exp: "Work experiance",
    field_of_work: "Field of work"
};

function isValNum(value) {
    return !isNaN(parseFloat(value));
}

function normalPersonString(Person){
    var persStr = "";
    for(var key in Person){
        if (keyChange.hasOwnProperty(key)){persStr += keyChange[key] + " <br>";}
        else {persStr += String(key) + " <br>";}
    }
    return persStr;
}

function normalPersonAnswers(Person){
    var persStr = "";
    for(var key in Person){
        persStr += Person[key] + " <br>";
    }
    return persStr;
}


document.addEventListener('DOMContentLoaded', () => {

    document.getElementById('duomenu-anketa').addEventListener('submit', function (event) {
        event.preventDefault();
    
        var elements = this.elements;
    
        for (var i = 0 ; i < elements.length ; i++){
            var element = elements[i];
            if (element.type === 'radio' && element.name === 'gender' && element.checked) {
                Person[element.name] = element.value;
            } else if (element.type !== 'submit' && element.type !== 'radio') {
                Person[element.name] = element.value;
            }
        }
        console.log(Person);
        document.querySelector('#results').innerHTML = JSON.stringify(Person);
    });

    document.getElementById('bshowinfo').addEventListener('click', () => {
        document.querySelector('#info').innerHTML = normalPersonString(Person);
        document.querySelector('#results').innerHTML = normalPersonAnswers(Person);
    });
});