function validate(event){
    console.log("validation started!");
    
    const form = document.forms[0];
    let name = form["name"].value;
    let dob = form["dob"].value;

    console.log(name + ", " + dob)

    if (name == "") {
        // alert("Please enter the name");
        document.getElementById("name_validation").style.display = "block";
        event.preventDefault();
    }
    else {
        document.getElementById("name_validation").style.display = "none";
    }
    if (dob == "") {
        document.getElementById("dob_validation").style.display = "block";
        event.preventDefault();
    }
    else {
        document.getElementById("dob_validation").style.display = "none";
    }

}