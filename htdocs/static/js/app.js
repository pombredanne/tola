


//App specific JavaScript

//Pop-over field values for info fields

var elem = '<a id="close-popover" data-toggle="clickover" class="btn btn-small" onclick="$(&quot;#info1&quot;).popover(&quot;hide&quot;);">close</a>';
var elem2 = '<a id="close-popover" data-toggle="clickover" class="btn btn-small" onclick="$(&quot;#info2&quot;).popover(&quot;hide&quot;);">close</a>';
var elem3 = '<a id="close-popover" data-toggle="clickover" class="btn btn-small" onclick="$(&quot;#info3&quot;).popover(&quot;hide&quot;);">close</a>';
var elem4 = '<a id="close-popover" data-toggle="clickover" class="btn btn-small" onclick="$(&quot;#info4&quot;).popover(&quot;hide&quot;);">close</a>';
var elem5 = '<a id="close-popover" data-toggle="clickover" class="btn btn-small" onclick="$(&quot;#info5&quot;).popover(&quot;hide&quot;);">close</a>';


//custom jquery to trigger dat picker, info pop-over and print category text
$(document).ready(function() {
    $('.datepicker').datepicker();
    $('#info1').popover({animation:true, content:elem, html: true, container: "body", title: "Please estimate the replacement, repair or insurance value of the stolen or damaged item"});
    $('#info2').popover({animation:true, content:elem2, html: true, container: "body", title: "Description of what impact means"});
    $('#info3').popover({animation:true, content:elem3, html: true, container: "body", title: "Upload photos of the incident"});
    $('#info4').popover({animation:true, content:elem4, html: true, container: "body", title: "Upload a map of the incident site"});
    $('#info5').popover({animation:true, content:elem5, html: true, container: "body", title: "Upload any additional documentation you might have in a zip or archive file (receipts, documents etc.)"});

    //Populate the incident primary category into the HELP text
    var selected = $(':selected', this);
    $("#hint_id_incident_primary").text("Category: " + selected.closest('optgroup').attr('label'));

    $('#id_incident_primary').change(function() {
        var selected = $(':selected', this);
        $("#hint_id_incident_primary").text("Category: " + selected.closest('optgroup').attr('label'));
    });

    //Populate the hidden impact field based on intent
    var $impact_value
    var radiovalue = $("input:radio[name ='intent']:checked").val();

    //check the current value
    if (radiovalue == 1){
        $impact_value = "1"
    }else if(radiovalue == 2){
        $impact_value = "2"
    }else{
        $impact_value = "3"
    }

    //set current value
    $("#id_impact_hidden").val($impact_value);


    //if the intent field changed update the impact
     $('input[type=radio][name=intent]').change(function() {
        if (this.value == 1){
            $impact_value = "1"
        }else if(this.value == 2){
            $impact_value = "2"
        }else{
            $impact_value = "3"
        }
        $("#id_impact_hidden").val($intent_value);
    });


});


$('input[type="file"]').each(function() {
    var $file = $(this), $form = $file.closest('.upload-form');
    $file.ajaxSubmitInput({
        url: '/incident/add/', //URL where you want to post the form
        beforeSubmit: function($input) {
            //manipulate the form before posting
        },
        onComplete: function($input, iframeContent, options) {
            if (iframeContent) {
                $input.closest('form')[0].reset();
                if (!iframeContent) {
                    return;
                }
                var iframeJSON;
                try {
                    iframeJSON = $.parseJSON(iframeContent);
                    //use the response data
                } catch(err) {
                    console.log(err)
                }
            }
        }
    });
});
