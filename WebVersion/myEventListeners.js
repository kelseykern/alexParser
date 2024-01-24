document.addEventListener("DOMContentLoaded", function(event) { 
    
    let filterbody = document.getElementById("FilterBodyArea");
    let new_filter_body = '';

    for (var i = 0; i < filters.length; i++) {
        let filter = filters[i];
        new_filter_body += '<input type="checkbox" id="filter'+i+'" name="filter'+i+'" value="filter'+i+'"></input><label for="filter'+i+'">';

        for(var j = 0; j < filter.length; j++){
            if(j > 0)new_filter_body += " AND ";

            let keyword_array = filter[j];

            new_filter_body += " (";
            for(var k = 0; k < keyword_array.length; k++){
                if(k > 0) new_filter_body += " OR ";
                let keyword = keyword_array[k];
                new_filter_body += keyword;
            }
            new_filter_body += ")";
        }

        new_filter_body += '</label><br></br>';
    }


    filterbody.innerHTML = new_filter_body;

  });