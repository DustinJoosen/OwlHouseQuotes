$(document).ready(function(){
    //when the value of the select box changes, change the specific_source#
    $("#source_person").on("change", function(){
        if($(this).val() == "Other"){
            document.getElementById("specific_source").style.display = "block";
        }
        else{
            document.getElementById("specific_source").style.display = "none";
        }
    })
})