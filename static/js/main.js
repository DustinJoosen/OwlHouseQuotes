$(document).ready(function(){
    $("#source_person").on("change", function(){
        if($(this).val() == "Other"){
            document.getElementById("specific_source").style.display = "block";
        }
        else{
            document.getElementById("specific_source").style.display = "none";
        }
    })
})