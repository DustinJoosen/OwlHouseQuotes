$(document).ready(function(){
    let source_person_other_value = null;
    let source_person_other = document.getElementById("source_person_other");
    let specific_source = document.getElementById("specific_source");

    //when the value of the select box changes, change the specific_source#
    $("#source_person").on("change", function(){
        if($(this).val() == "Other"){
            specific_source.style.display = "block";
            source_person_other.value = source_person_other_value;
        }
        else{
            specific_source.style.display = "none";

            source_person_other_value = source_person_other.value;
            source_person_other.value = null;
        }
    })
})