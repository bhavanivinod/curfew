odoo.define("curfew.epass_application_form",function (require) {
	    
		var AbatractAction =    require('web.AbstractAction');
	    var core = require('web.core');
		var Widget = require('web.Widget');
		var rpc = require('web.rpc');
		var Qweb = core.qweb;
		var epass= AbatractAction.extend(Widget.extend,{
			events : {
				'click #insert_all_details' : 'insert_data',
			},

			init:function(parent)
			{
				this._super(parent);
			},
			
			start: function() {
				var self = this;
				
				var mydetail = $(Qweb.render("epass_application"));
				self.$el.empty()
				
				self.$el.append(mydetail)
				rpc.query({
							model: 'curfew.category',
							method: 'get_categoryname'
							
				}).then(function(results){
					// alert(results);
					var category_list=JSON.parse(results);
					var categorylist=document.getElementById("curfew_epass_category");
					for (result in category_list)
					{
						var categoryname=document.createElement('option');
						categoryname.appendChild(document.createTextNode(category_list[result].category_name));
						categoryname.value=category_list[result].category_id;
						categorylist.appendChild(categoryname);
					}
					
							
									 
			});
			
			},
			
			
			insert_data:function(){
				var self = this;
				var curfew_epass_category =  $("#curfew_epass_category").val();
				//var curfew_epass_category = e.options[e.selectedIndex].value;
				var citizen_name = $("#citizen_name").val();
				var citizen_dob = $("#citizen_dob").val();
				var citizen_address = $("#citizen_address").val();
				var district_name = $("#district_name").val();
				var citizen_email = $("#citizen_email").val();
				var citizen_vehicle_no = $("#citizen_vehicle_no").val();
				var citizen_vehicle_type = $("#citizen_vehicle_type").val();
				var from_date = $("#from_date").val();
				var to_date = $("#to_date").val();
				var from_place = $("#from_place").val();
				var to_place = $("#to_place").val();
				if (citizen_name != "") {
					if (citizen_dob != "") {
						if (citizen_address != "") {
							if (district_name != "") {
								if (citizen_email != "") {
									if (citizen_vehicle_no != "") {
										if (citizen_vehicle_type != "") {
											if (from_date != "") {
												if (to_date != "") {
													//this.do_notify(_t("Success"), _t("Successfully added"));
													alert("Successfully added");
												}else{
													document.getElementById("to_date_err").style.visibility = "visible";
													return false;
												}
											}else{
												document.getElementById("from_date_err").style.visibility = "visible";
												return false;
											}
										}else{
											document.getElementById("citizen_vehicle_type_err").style.visibility = "visible";
											return false;
										}
									}else{
										document.getElementById("citizen_vehicle_no_err").style.visibility = "visible";
										return false;
									}
								}else{
									document.getElementById("citizen_email_err").style.visibility = "visible";
									return false;
								}
							} else {
								//this.do_warn(_t("Error"), _t("deceased is invalid."));
								document.getElementById("district_name_err").style.visibility = "visible";
								return false;
							}
						} else {
							//this.do_warn(_t("Error"), _t("Recovered is invalid"));
							document.getElementById("citizen_address_err").style.visibility = "visible";
							return false;
						}
					} else {
						//this.do_warn(_t("Error"), _t("Infected is invalid"));
						document.getElementById("citizen_dob_err").style.visibility = "visible";
						return false;
					}
				} else {
					//this.do_warn(_t("Error"), _t("Invalid Date"));
					document.getElementById("citizen_name_err").style.visibility = "visible";
					return false;
				}

				var dict = {
					'curfew_epass_category':curfew_epass_category,
					'citizen_name' : citizen_name,
					'citizen_dob' : citizen_dob,
					'citizen_address' : citizen_address,
					'district_name' : district_name,
					'citizen_email' : citizen_email,
					'citizen_vehicle_no' : citizen_vehicle_no,
					'citizen_vehicle_type' : citizen_vehicle_type,
					'from_date' : from_date,
					'to_date' : to_date,
					'from_place' : from_place,
					'to_place' : to_place
				};
				// form_values['City']=$("#city").val();
				rpc.query({
					model : 'curfew.epass',
					method : 'create_epass_application',
					args : [ dict ],
				}).then(function(results){
					if(results!=""){
						self.start()

						
						if (results != null){
							
							alert("your application number is : "+results)
						}}});
					}		
									 
			});
			
	  core.action_registry.add('epass_application_form',epass);  
});













		
	
	
	
