$(function() {
					$( "#datepicker" ).datepicker({
						changeMonth: true,
						changeYear: true,
						showOn: "button",
						dateFormat: 'yy-mm-dd',
						showButtonPanel: true,
						altField: '#id_fecha_creacion',
						buttonImageOnly: true,
						buttonImage: "/media/found/css/svgs/fi-calendar.svg",
					});
					$( "#datepicker2" ).datepicker({
						changeMonth: true,
						changeYear: true,
						showOn: "button",
						dateFormat: 'yy-mm-dd',
						showButtonPanel: true,
						buttonImageOnly: true,
						buttonImage: "/media/found/css/svgs/fi-calendar.svg",
						showButtonPanel: true,
						altField: '#id_fecha_inicio',
					});
					$( "#datepicker3" ).datepicker({
						changeMonth: true,
						changeYear: true,
						showOn: "button",
						dateFormat: 'yy-mm-dd',
						showButtonPanel: true,
						buttonImageOnly: true,
						buttonImage: "/media/found/css/svgs/fi-calendar.svg",
						showButtonPanel: true,
						altField: '#id_fecha_fin'
					});
				});