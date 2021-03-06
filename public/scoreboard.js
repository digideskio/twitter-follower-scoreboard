window.addEventListener('load', eventWindowLoaded, false);

function eventWindowLoaded() {
    load_scoreboard();
}

function load_scoreboard () {
    $.getJSON("scoreboard.json", function(json_data) {
	    $.each(json_data, function(i, user) {
		    // Lovely regex from http://stackoverflow.com/questions/3883342/add-commas-to-a-number-in-jquery
		    var followers_formatted = user['followers_count'].toString().replace(/\B(?=(?:\d{3})+(?!\d))/g, ',')
		    var table_row = '<tr>'
                                    + '<td>' + (i + 1)  + '</td>' // Rank
			            + '<td><a href="' + 'http://twitter.com/' + user['screen_name'] + '"><img class="avatar" src="' + user['avatar'] + '"/></a></td>' // Avatar
               			    + '<td><a href="' + 'http://twitter.com/' + user['screen_name'] + '">@' + user['screen_name'] + '</a></td>' // Twitter handle
			            + '<td>' + user['display_name'] + '</td>' // Name
			            + '<td>' + followers_formatted + '</td>' // Number of followers
			            + '</tr>';
		    $('#scoreboard tbody').append(table_row);
	    });
    });
    $('#loading').hide();
}