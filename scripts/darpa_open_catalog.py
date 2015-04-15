#!/usr/bin/python
import getpass
import re
import datetime
#import change_timeline as timeline

def html_head():
  return """
  <!DOCTYPE html>
  <html lang='en'>
  <head>
  <meta charset="utf-8">
  <title>DARPA - Open Catalog</title>

  <link rel='stylesheet' href="css/nv.d3.css" rel="stylesheet" type="text/css">
  <link rel='stylesheet' href='css/style_v2.css' type='text/css'/>
  <link rel='stylesheet' href='css/banner_style.css' type='text/css'/>
  <link rel='stylesheet' href='css/header_footer.css' type='text/css'/>
  <link rel='stylesheet' href='css/list_style.css' type='text/css'/>
  <link rel='stylesheet' href='css/flick/jquery-ui-1.10.4.custom.css' type='text/css'/>
  <script language="javascript" type="text/javascript" src="jquery-1.11.1.min.js"></script>
  <script language="javascript" type='text/javascript' src="jquery-ui.js"></script>
  <script language="javascript" type='text/javascript' src="jstorage.js"></script>
  <script language="javascript" type='text/javascript' src="utils.js"></script>
  <script language="javascript" type='text/javascript' src="spin.js"></script>
  <script language="javascript" type='text/javascript' src='jquery.tablesorter.min.js'></script>
  <script language="javascript" type='text/javascript' src="list.min.js"></script>
 <!--
  <script language="javascript" type='text/javascript' src="d3.v3.js"></script>
  <script language="javascript" type='text/javascript' src="nv.d3.js"></script>
  <script language="javascript" type='text/javascript' src="tooltip.js"></script>
  <script language="javascript" type='text/javascript' src="nv.utils.js"></script>
  <script language="javascript" type='text/javascript' src="legend.js"></script>
  <script language="javascript" type='text/javascript' src="axis.js"></script>
  <script language="javascript" type='text/javascript' src="distribution.js"></script>
 -->
  </head>
  <body>
"""

def catalog_page_header(office_link):
  header = "<header class='darpa-header'><div class='darpa-header-images'><a href='http://www.darpa.mil/'><img class='darpa-logo' src='darpa-transparent-v2.png'></a><a href='index.html' class='programlink'><img src='Open-Catalog-Single-Big.png'></a></div>"
  header += "<div class='darpa-header-text no-space'>"
  if (office_link != ""):
    header += "<span><font color='white'> / </font>%s</span>" % office_link
  header += "</div><div class='catalog_search_outer'><div class='catalog_search_inner'><input id='header_search' type='search'></input><button id='header_button'>Search</button></div></div></header>"
  return header

def get_current_user():
  return getpass.getuser()

def catalog_splash_content():
  date = datetime.datetime.now()
  formatted_date = date.strftime("%B") + " " + date.strftime("%d") + ", " + date.strftime("%Y")
  splash = """
<div width='98%'><p>Welcome to the DARPA Open Catalog, which contains a curated list of DARPA-sponsored software and peer-reviewed publications. DARPA sponsors fundamental and applied research in a variety of areas that may lead to experimental results and reusable technology designed to benefit multiple government domains.</p>
<p>The DARPA Open Catalog organizes publicly releasable material from DARPA programs. DARPA has an open strategy to help increase the impact of government investments.</p>
<p>DARPA is interested in building communities around government-funded research. DARPA plans to continue to make available information generated by DARPA programs, including software, publications, data, and experimental results.</p></div>"""
  #<div id='splash_desc'><p>The table below lists the programs currently participating in the catalog. The graph to the right displays the latest changes to the program data.</p>
  splash += """<div id=''><p>The table on this page lists the programs currently participating in the catalog.</p>
<p>Program Manager:<br>
Mr. Wade Shen<br>
<a href='mailto:wade.shen@darpa.mil'>wade.shen@darpa.mil</a></p>
<p>Report a problem: <a href="mailto:opencatalog@darpa.mil">opencatalog@darpa.mil</a></p>
<p>Last updated: """
  splash += formatted_date + "</p></div>"
  #splash += "<div id='timeline_splash'>" + timeline.timeline_html() + "</div>"
  #splash += timeline.timeline_script()
  return splash

def splash_table_header():
  return """
<div style = 'width:100%; float:left;'><h2>Current Catalog Programs:</h2></div>
<table id='splash' class='tablesorter'>
<thead>
<tr>
    <th>DARPA Program</th>
    <th>Office</th>
    <th>Description</th>
</tr>
</thead>
<tbody>
"""

def splash_table_footer():
  return """
</tbody>
</table>
<br>
"""

def software_table_header(columns):
  header = "<table id='sftwr' class='tablesorter'>\n <thead>\n <tr>"
  for column in columns:
    header += "<th>%s</th>" % column
  header += "</tr>\n </thead>\n <tbody  class='list'>"
  return header

def table_footer():
  return """
</tbody>
</table>
"""

def pubs_table_header(columns):

  header = "<table id='pubs' class='tablesorter'>\n <thead>\n <tr>"
  for column in columns:
    header += "<th>%s</th>" % column
  header += "</tr>\n </thead>\n <tbody  class='list'>"
  return header

def data_table_header(columns):

  header = "<table id='data' class='tablesorter'>\n <thead>\n <tr>"
  for column in columns:
    header += "<th>%s</th>" % column
  header += "</tr>\n </thead>\n <tbody  class='list'>"
  return header

def pubs_table_footer():
  return """
</tbody>
</table>
<br>
"""

def project_banner(update_date, new_date, last_update_file, title):
  html = ""
  ribbon_class = ""
  ribbon_div = ""
  change_date = ""
  if new_date != "" and update_date != "":
    if new_date >= update_date:
     change_date = new_date
     ribbon_class = "ribbon-standard ribbon-red"
     ribbon_text = "NEW"
    else:
	  change_date = update_date
	  ribbon_class = "ribbon-standard ribbon-green"
	  ribbon_text = "UPD"
  elif new_date != "" and update_date == "":
    change_date = new_date
    ribbon_class = "ribbon-standard ribbon-red"
    ribbon_text = "NEW"
  elif update_date != "" and new_date == "":
    change_date = update_date
    ribbon_class = "ribbon-standard ribbon-green"
    ribbon_text = "UPD"
  f = open(last_update_file,"r")
  last_build_date = f.read()
  f.close()
  if change_date > last_build_date:
    #Convert timestamp into a date in order to format the date into a string
    change_date = re.sub('-','',change_date)
    formatted_month = datetime.date.strftime(datetime.datetime.strptime(change_date, '%Y%m%d'), "%b");
    formatted_day =  ordinal(int(datetime.date.strftime(datetime.datetime.strptime(change_date, '%Y%m%d'), "%d")))
    formatted_date = formatted_month + " " + formatted_day
    html = "<div class='wrapper'><div class='wrapper-text'>" + title + "</div><div class='ribbon-wrapper'><div class='"  + ribbon_class + "'>" + ribbon_text + " " + formatted_date + "</div></div></div>"
  else:
    html = title
  return html

def catalog_program_script():
  return """

<script type='text/javascript'>
var swList = ssftList = pubList = spubList = dataList = sdtList = "";

$(document).ready(function()
    {

	   $('#header_button').click(function(){
			$.jStorage.set("searchTerm", $('#header_search').val());
			window.location = 'catalog_search.html';
	   });

		$("#header_search").keyup(function(event){
			if(event.keyCode == 13)
				$('#header_button').click();
		});

	   $('#sftwr').tablesorter({
		// sort on the first column and second column, order asc
        	sortList: [[0,0],[1,0]]
    	});
        $('#pubs').tablesorter({
        	sortList: [[0,0],[1,0]]
    	});
        $('#data').tablesorter({
        	sortList: [[0,0],[1,0]]
    	});
        $('#splash').tablesorter({
		// sort on the first column, order asc
        	sortList: [[0,0]]
    	});

		//get the list of tabs and the number of tabs
		var tabList = $('#tabs >ul >li');
		var tabCount = $('#tabs >ul >li').size();

		//create table tabs
		$(function() {
			$( "#tabs" ).tabs
			var param_tab = decodeURIComponent(getUrlParams("tab"));
			var param_term = decodeURIComponent(getUrlParams("term"));

			if(param_tab && !param_term){
				//console.log("tab");
				if (param_tab == "tabs0")
					$("#tabs").tabs({active: 0});  //software tab
				else if (param_tab == "tabs1")
					$("#tabs").tabs({active: 1});  //publications tab
				else if (param_tab == "tabs2")
					$("#tabs").tabs({active: 2});  //data tab
			}
			else if(param_tab && param_term){
				//console.log("tab and term");
				if (param_tab == "tabs0")
					swSearch(param_term);
				else if (param_tab == "tabs1")
					pubSearch(param_term);
				else if (param_tab == "tabs2")
					dataSearch(param_term);
			}
			else{
				//console.log("no params");
				if($("#tabs0"))
					$("#tabs").tabs({active: 0}); //software tab
				else if($("#tabs1"))
					$("#tabs").tabs({active: 1}); //publications tab
				else
					$("#tabs").tabs({active: 2}); //data tab
			}

		});

		//configure table search and clear button for software, publications, and data table
		for (var i=0; i<tabCount; i++){

			var tabName = tabList[i].textContent.toLowerCase(); //name of tab

			if(tabName == "software"){
				var tabTable = $('#tabs0 table'); //table within this tab
				var tabHeaders = getTableHeaders(tabTable);

				var sw_options = {
				  valueNames: tabHeaders
				};

				swList = new List(tabName, sw_options);

				$("#clear0").click(function() {
					var currId = this.id.match(/\d+/g);
					$("#search" + currId[0]).val("");
					swList.search();
				});
			}

			if(tabName == "publications"){
				var tabTable = $('#tabs1 table'); //table within this tab
				var tabHeaders = getTableHeaders(tabTable);

				var pub_options = {
				  valueNames: tabHeaders
				};

				pubList = new List(tabName, pub_options);

				$("#clear1").click(function() {
					var currId = this.id.match(/\d+/g);
					$("#search" + currId[0]).val("");
					pubList.search();
				});

			}

			if(tabName == "data"){
				var tabTable = $('#tabs2 table'); //table within this tab
				var tabHeaders = getTableHeaders(tabTable);

				var data_options = {
				  valueNames: tabHeaders
				};

				dataList = new List(tabName, data_options);

				$("#clear2").click(function() {
					var currId = this.id.match(/\d+/g);
					$("#search" + currId[0]).val("");
					dataList.search();
				});

			}
			if(tabName == "search"){

				var table_clone = $('#tabs table').clone();
				for (var k=0; k<table_clone.length; k++){
					var searchHeaders = getTableHeaders(table_clone[k]);
					var search_options = {
						  valueNames: searchHeaders
					};

					if (table_clone[k].id == "sftwr"){
						$("#softwareSearch #sftwrTable").append(table_clone[k]);
						//tables are hidden initially
						$("#softwareSearch #sftwrTable").hide();
						ssftList = new List("softwareSearch", search_options);
					}
					else if (table_clone[k].id == "pubs"){

						$("#publicationsSearch #pubTable").append(table_clone[k]);
						$("#publicationsSearch #pubTable").hide();
						spubList = new List("publicationsSearch", search_options);
					}
					else{
						$("#dataSearch #dataTable").append(table_clone[k]);
						$("#dataSearch #dataTable").hide();
						sdtList = new List("dataSearch", search_options);
					}


				}

				$("#clear300").click(function() {
					var currId = this.id.match(/\d+/g);
					$("#search" + currId[0]).val("");
					if (ssftList != "")
						ssftList.search();
					if (spubList != "")
						spubList.search();
					if (sdtList != "")
						sdtList.search();
					//when search is cleared tables need to be hidden
					$("#softwareSearch #sftwrTable").hide();
					$("#publicationsSearch #pubTable").hide();
					$("#dataSearch #dataTable").hide();

				});

			}
		}
    }
);

function jump(h){
    var url = location.href;
    location.href = "#"+h;
        history.replaceState(null,null,url)
}

function swSearch(link){
	var search_text = "";
	if(link.hash)
		search_text = link.hash.replace("#", "");
	else
		search_text = link;
	$('#tabs').tabs({active: 0}); //publications tab
	var search_box = $("#search0");
	search_box.val(search_text);

	setTimeout(function(){
		$('html, body').animate({
			scrollTop: $("#tabs").offset().top
		}, 0);
		search_box.focus();
		search_box.select();
		swList.search(search_text);

	},300);
}

function pubSearch(link){
	var search_text = "";
	if(link.hash)
		search_text = link.hash.replace("#", "");
	else
		search_text = link;
	$('#tabs').tabs({active: 1}); //publications tab
	var search_box = $("#search1");
	search_box.val(search_text);

	setTimeout(function(){
		$('html, body').animate({
			scrollTop: $("#tabs").offset().top
		}, 0);
		search_box.focus();
		search_box.select();
		pubList.search(search_text);
	},300);
}

function dataSearch(link){
	var search_text = "";
	if(link.hash)
		search_text = link.hash.replace("#", "");
	else
		search_text = link;
	$('#tabs').tabs({active: 2}); //publications tab
	var search_box = $("#search2");
	search_box.val(search_text);

	setTimeout(function(){
		$('html, body').animate({
			scrollTop: $("#tabs").offset().top
		}, 0);
		search_box.focus();
		search_box.select();
		dataList.search(search_text);
	},300);
}
function allSearch(this_search){
	if(this_search.value != "" && this_search.value.length >= 3){
		var value = this_search.value;
		//TODO: Implement Stop Words
		ssftList.search(value);

		//hide table if there are no rows that match the search term
		if ($("#softwareSearch #sftwrTable tbody").children().length != 0)
			$("#softwareSearch #sftwrTable").show();
		else
			$("#softwareSearch #sftwrTable").hide();

		if(spubList != ""){
			var value = this_search.value;
			spubList.search(value);

			if ($("#publicationsSearch #pubTable tbody").children().length != 0)
				$("#publicationsSearch #pubTable").show();
			else
				$("#publicationsSearch #pubTable").hide();
		}

		if(sdtList != ""){
			var value = this_search.value;
			sdtList.search(value);

			if ($("#dataSearch #dataTable tbody").children().length != 0)
				$("#dataSearch #dataTable").show();
			else
				$("#dataSearch #dataTable").hide();
		}

	}
	else{
		//if search_term is empty or not 3 chars in length, make sure the tables are hidden
		$("#publicationsSearch #pubTable").hide();
		$("#softwareSearch #sftwrTable").hide();
		$("#dataSearch #dataTable").hide();
	}
}

function getTableHeaders(table){
	var this_table;

	if(table[0])
		this_table = table[0];
	else
		this_table = table;

	var headerRow = this_table.tHead.rows[0].cells; //header row of table
	var tableHeaders = [];

	for (var j=0; j<headerRow.length; j++)
		tableHeaders.push(headerRow[j].textContent.toLowerCase());

	return tableHeaders;
}

function licenseInfo(short_nm, long_nm, link, description, event){

	var x=event.clientX;
	var y=event.clientY;

	$( "#dialog" ).removeClass("ribbon-dialog");
	$(".ui-dialog").removeClass("ribbon-dialog vertical-green vertical-red");
	$(".ui-dialog-titlebar").removeClass("ribbon-dialog-text");

	if(short_nm != ""){
		$( "#dialog" ).empty().dialog({
		position: [x , y - 20],
		title: short_nm
		});

		if(description != "")
			$("#dialog").html("<a href='" + link + "'>" + long_nm + "</a>: " + description);
		else
			$("#dialog").html("<a href='" + link + "'>" + long_nm + "</a>");

		$(".ui-dialog").mouseleave( function () {
			 $( "#dialog" ).dialog( "close" );
		  });
	}
}

function dateInfo(ribbon, event){
	if(ribbon !="")
	{
		var date_id = document.getElementById(ribbon).firstChild.id;
		var str_pattern = /(\d{4})(\d{2})(\d{2})/;
		var date = date_id.replace(str_pattern,"$2-$3-$1"); //full date string

		var ribbon_type = document.getElementById(ribbon).firstChild.getAttribute("name");
		var x=event.clientX;
		var y=event.clientY;
		var text = "";
		var background = "";

		if(ribbon_type == "NEW"){
			text = "CREATED";
			$(".ui-dialog").removeClass('vertical-green');
			background = "vertical-red";
		}
		else{
			text = ribbon_type;
			$(".ui-dialog").removeClass('vertical-red');
			background = "vertical-green";
		}

		$( "#dialog" ).empty().dialog({
		position: [x , y - 20],
		title: text + ": " + date,
		});

		$( "#dialog" ).addClass("ribbon-dialog");
		$(".ui-dialog").addClass(background + " ribbon-dialog");
		$(".ui-dialog-titlebar").addClass("ribbon-dialog-text");



		$(".ui-dialog").mouseleave( function () {
			 $( "#dialog" ).dialog( "close" );
		});
	}
}
</script>
"""

def catalog_page_footer():
  return """
<footer>
<div class='footer-style'>
<hr>
<p><a href='http://www.darpa.mil/FOIA.aspx'>FOIA</a> | <a href='http://www.darpa.mil/Privacy_Security_Notice.aspx'>Privacy and Security</a> |
<a href='http://www.darpa.mil/NoFearAct.aspx'>No Fear Act</a> | <a href='http://www.darpa.mil/External_Link.aspx?url=http://dodcio.defense.gov/DoDSection508/Std_Stmt.aspx'>Accessibility/Section 508</a></p>
</div>
</footer>
</div>
</body>
</html>
"""

def write_file(html, file):
  page_file = file
  print "Writing to %s" % page_file
  outfile = open(page_file, 'w')
  outfile.write(html)

def valid_email(email, program):
  if re.match(r"^(([a-zA-Z0-9\-?\.?]+)@(([a-zA-Z0-9\-_]+\.)+)([a-z]{2,3}))+$", email)!=None:
    return email
  else:
    raise ValueError( "%s is an invalid email address.  Please fix this in %s files and restart the build." % (email, program))

def ordinal(n):
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
       return  str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")
