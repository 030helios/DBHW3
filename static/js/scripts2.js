$(document).ready(function() {  
    data = {}  
    //covid19
    $.ajax({
		url: '/_regionCovid19Case',
        type: 'GET',
		data: data,
		beforeSend: function(){
            $("table").remove('#regionCovid19Casedata');
		},
		success: function(result){
            var insertText = '<table class="table" id="regionCovid19Casedata"><thead>';
            insertText += '<tr>';
            for (var i=0; i<result.Header.length; i++)
            {
                insertText += '<td>';
                insertText += result.Header[i];
                insertText += '</td>';
            }
            insertText += '</tr></thead>';

            for(var i=0; i<result.Data.length; i++)
            {
                insertText += '<tr>';
                for(var j=0; j<result.Data[i].length; j++)
                {
                    insertText += '<td>';
                    insertText += result.Data[i][j];
                    insertText += '</td>';
                }
                insertText += '</tr>';
            }
            insertText += '</table>';
            
            $('#regionCovid19Case').append(insertText);
		},
		complete: function(){
			
		},
		error: function(result){
			alert("Error.\nMaybe you have closed the app or have a illegal query to database.\nPlease check the status.");
		}		
    })
    $.ajax({
		url: '/_regionCovid19Death',
        type: 'GET',
		data: data,
		beforeSend: function(){
            $("table").remove('#regionCovid19Deathdata');
		},
		success: function(result){
            var insertText = '<table class="table" id="regionCovid19Deathdata"><thead>';
            insertText += '<tr>';
            for (var i=0; i<result.Header.length; i++)
            {
                insertText += '<td>';
                insertText += result.Header[i];
                insertText += '</td>';
            }
            insertText += '</tr></thead>';

            for(var i=0; i<result.Data.length; i++)
            {
                insertText += '<tr>';
                for(var j=0; j<result.Data[i].length; j++)
                {
                    insertText += '<td>';
                    insertText += result.Data[i][j];
                    insertText += '</td>';
                }
                insertText += '</tr>';
            }
            insertText += '</table>';
            
            $('#regionCovid19Death').append(insertText);
		},
		complete: function(){
			
		},
		error: function(result){
			alert("Error.\nMaybe you have closed the app or have a illegal query to database.\nPlease check the status.");
		}		
    })
    //sars
    $.ajax({
		url: '/_regionSARSCase',
        type: 'GET',
		data: data,
		beforeSend: function(){
            $("table").remove('#regionSARSCasedata');
		},
		success: function(result){
            var insertText = '<table class="table" id="regionSARSCasedata"><thead>';
            insertText += '<tr>';
            for (var i=0; i<result.Header.length; i++)
            {
                insertText += '<td>';
                insertText += result.Header[i];
                insertText += '</td>';
            }
            insertText += '</tr></thead>';

            for(var i=0; i<result.Data.length; i++)
            {
                insertText += '<tr>';
                for(var j=0; j<result.Data[i].length; j++)
                {
                    insertText += '<td>';
                    insertText += result.Data[i][j];
                    insertText += '</td>';
                }
                insertText += '</tr>';
            }
            insertText += '</table>';
            
            $('#regionSARSCase').append(insertText);
		},
		complete: function(){
			
		},
		error: function(result){
			alert("Error.\nMaybe you have closed the app or have a illegal query to database.\nPlease check the status.");
		}		
    })
    $.ajax({
		url: '/_regionSARSDeath',
        type: 'GET',
		data: data,
		beforeSend: function(){
            $("table").remove('#regionSARSDeathdata');
		},
		success: function(result){
            var insertText = '<table class="table" id="regionSARSDeathdata"><thead>';
            insertText += '<tr>';
            for (var i=0; i<result.Header.length; i++)
            {
                insertText += '<td>';
                insertText += result.Header[i];
                insertText += '</td>';
            }
            insertText += '</tr></thead>';

            for(var i=0; i<result.Data.length; i++)
            {
                insertText += '<tr>';
                for(var j=0; j<result.Data[i].length; j++)
                {
                    insertText += '<td>';
                    insertText += result.Data[i][j];
                    insertText += '</td>';
                }
                insertText += '</tr>';
            }
            insertText += '</table>';
            
            $('#regionSARSDeath').append(insertText);
		},
		complete: function(){
			
		},
		error: function(result){
			alert("Error.\nMaybe you have closed the app or have a illegal query to database.\nPlease check the status.");
		}		
    })


});  

$("#regionMaxCaseMonbtn").bind("click", function(){
	const form = document.forms["regionMC"];
	const region = form.elements.region.value;
	var data = {
		Region: region
    }
	$.ajax({
		url: '/_regionMaxCaseMon',
        type: 'GET',
		data: data,
		beforeSend: function(){
            $("table").remove('#regionMaxCaseMondata');
            $("#regionMaxCaseMonbtn").attr({ disabled: "disabled" });
		},
		success: function(result){
            var insertText = '<table class="table" id="regionMaxCaseMondata"><thead>';
            insertText += '<tr>';
            for (var i=0; i<result.Header.length; i++)
            {
                insertText += '<td>';
                insertText += result.Header[i];
                insertText += '</td>';
            }
            insertText += '</tr></thead>';

            for(var i=0; i<result.Data.length; i++)
            {
                insertText += '<tr>';
                for(var j=0; j<result.Data[i].length; j++)
                {
                    insertText += '<td>';
                    insertText += result.Data[i][j];
                    insertText += '</td>';
                }
                insertText += '</tr>';
            }
            insertText += '</table>';
            
            $('#regionMaxCaseMon').append(insertText);
		},
		complete: function(){
			$("#regionMaxCaseMonbtn").removeAttr("disabled");
		},
		error: function(result){
			alert("Error.\nMaybe you have closed the app or have a illegal query to database.\nPlease check the status.");
		}
		
	})
	
})

$("#regionMaxDeathMonbtn").bind("click", function(){
	const form = document.forms["regionMD"];
	const region = form.elements.region.value;
	var data = {
		Region: region
	}
	$.ajax({
		url: '/_regionMaxDeathMon',
        type: 'GET',
		data: data,
		beforeSend: function(){
            $("table").remove('#regionMaxDeathMondata');
            $("#regionMaxDeathMonbtn").attr({ disabled: "disabled" });
		},
		success: function(result){
            var insertText = '<table class="table" id="regionMaxDeathMondata"><thead>';
            insertText += '<tr>';
            for (var i=0; i<result.Header.length; i++)
            {
                insertText += '<td>';
                insertText += result.Header[i];
                insertText += '</td>';
            }
            insertText += '</tr></thead>';

            for(var i=0; i<result.Data.length; i++)
            {
                insertText += '<tr>';
                for(var j=0; j<result.Data[i].length; j++)
                {
                    insertText += '<td>';
                    insertText += result.Data[i][j];
                    insertText += '</td>';
                }
                insertText += '</tr>';
            }
            insertText += '</table>';
            
            $('#regionMaxDeathMon').append(insertText);
		},
		complete: function(){
			$("#regionMaxDeathMonbtn").removeAttr("disabled");
		},
		error: function(result){
			alert("Error.\nMaybe you have closed the app or have a illegal query to database.\nPlease check the status.");
		}
		
	})
	
})

$("#regionSARSMaxCaseMonbtn").bind("click", function(){
	const form = document.forms["regionSARSMC"];
	const region = form.elements.region.value;
	var data = {
		Region: region
    }
	$.ajax({
		url: '/_regionSARSMaxCaseMon',
        type: 'GET',
		data: data,
		beforeSend: function(){
            $("table").remove('#regionSARSMaxCaseMondata');
            $("#regionSARSMaxCaseMonbtn").attr({ disabled: "disabled" });
		},
		success: function(result){
            var insertText = '<table class="table" id="regionSARSMaxCaseMondata"><thead>';
            insertText += '<tr>';
            for (var i=0; i<result.Header.length; i++)
            {
                insertText += '<td>';
                insertText += result.Header[i];
                insertText += '</td>';
            }
            insertText += '</tr></thead>';

            for(var i=0; i<result.Data.length; i++)
            {
                insertText += '<tr>';
                for(var j=0; j<result.Data[i].length; j++)
                {
                    insertText += '<td>';
                    insertText += result.Data[i][j];
                    insertText += '</td>';
                }
                insertText += '</tr>';
            }
            insertText += '</table>';
            
            $('#regionSARSMaxCaseMon').append(insertText);
		},
		complete: function(){
			$("#regionSARSMaxCaseMonbtn").removeAttr("disabled");
		},
		error: function(result){
			alert("Error.\nMaybe you have closed the app or have a illegal query to database.\nPlease check the status.");
		}
		
	})
	
})

$("#regionSARSMaxDeathMonbtn").bind("click", function(){
	const form = document.forms["regionSARSMD"];
	const region = form.elements.region.value;
	var data = {
		Region: region
	}
	$.ajax({
		url: '/_regionSARSMaxDeathMon',
        type: 'GET',
		data: data,
		beforeSend: function(){
            $("table").remove('#regionSARSMaxDeathMondata');
            $("#regionSARSMaxDeathMonbtn").attr({ disabled: "disabled" });
		},
		success: function(result){
            var insertText = '<table class="table" id="regionSARSMaxDeathMondata"><thead>';
            insertText += '<tr>';
            for (var i=0; i<result.Header.length; i++)
            {
                insertText += '<td>';
                insertText += result.Header[i];
                insertText += '</td>';
            }
            insertText += '</tr></thead>';

            for(var i=0; i<result.Data.length; i++)
            {
                insertText += '<tr>';
                for(var j=0; j<result.Data[i].length; j++)
                {
                    insertText += '<td>';
                    insertText += result.Data[i][j];
                    insertText += '</td>';
                }
                insertText += '</tr>';
            }
            insertText += '</table>';
            
            $('#regionSARSMaxDeathMon').append(insertText);
		},
		complete: function(){
			$("#regionSARSMaxDeathMonbtn").removeAttr("disabled");
		},
		error: function(result){
			alert("Error.\nMaybe you have closed the app or have a illegal query to database.\nPlease check the status.");
		}
		
	})
	
})

$("#countryinfobtn").bind("click", function(){
	const form = document.forms["countryInfo"];
	const country = form.elements.region.value;
	var data = {
		Country: country
	}
	$.ajax({
		url: '/_countryinfo',
        type: 'GET',
		data: data,
		beforeSend: function(){
            $("table").remove('#countryinfodata');
            $("#countryinfobtn").attr({ disabled: "disabled" });
		},
		success: function(result){
            var insertText = '<table class="table" id="countryinfodata"><thead>';
            insertText += '<tr>';
            for (var i=0; i<result.Header.length; i++)
            {
                insertText += '<td>';
                insertText += result.Header[i];
                insertText += '</td>';
            }
            insertText += '</tr></thead>';

            for(var i=0; i<result.Data.length; i++)
            {
                insertText += '<tr>';
                for(var j=0; j<result.Data[i].length; j++)
                {
                    insertText += '<td>';
                    insertText += result.Data[i][j];
                    insertText += '</td>';
                }
                insertText += '</tr>';
            }
            insertText += '</table>';
            
            $('#countryinfo').append(insertText);
		},
		complete: function(){
			$("#countryinfobtn").removeAttr("disabled");
		},
		error: function(result){
			alert("Error.\nMaybe you have closed the app or have a illegal query to database.\nPlease check the status.");
		}
		
	})
	
})
