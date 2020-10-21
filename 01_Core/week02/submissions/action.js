const memberNames = []

// this will start when button is pressed
addMember = () => {
    event.preventDefault();
    let fname = document.getElementById("fname").value;
    let lname = document.getElementById("lname").value;
    let fullName = `${fname} , <div class = "lname"> ${lname} </div>`;

    memberNames.push(fullName);

    memberNames.sort(compare);

    deleteLi();
    displayli();

    document.getElementById("fname").value="";
    document.getElementById("lname").value="";
}

//split name to sort by last name
function compare(a, b)  {
    let splitA = a.split(",");
    let splitB = b.split(",");
    let lastA = splitA[splitA.length - 1];
    let lastB = splitB[splitB.length - 1];

    if (lastA < lastB) return -1;
    if (lastA > lastB) return 1;
    return 0;
}

//display array by adding each name as an li
function displayli () {
    memberNames.forEach((i)=> {
        let li = document.createElement('li');
        document.getElementById("all-members").appendChild(li);
        li.innerHTML += i;
    })
}


//delete old list in html
function deleteLi () {
    var ul = document.getElementById("all-members");
    ul.innerHTML = "";   
}
