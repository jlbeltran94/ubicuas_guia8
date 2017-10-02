(function($){
  $(function(){

    $('.button-collapse').sideNav();   
    $('.datepicker').pickadate({
      selectMonths: true,
      selectYears: 50,
      max: 1,
      monthsFull: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
      monthsShort: ['Ene', 'Feb', 'Mar', 'Abr', 'Mayo', 'Jun', 'Jul', 'Ago', 'Sept', 'Oct', 'Nov', 'Dic'],
      weekdaysShort: ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sab'],
      weekdaysFull: ['Domingo', 'Lunes', 'Martes', 'Miércole', 'Jueves', 'Viernes', 'Sabado'],
      today: 'Hoy',
      clear: 'Limpiar',
      close: 'Ok',
      format: 'yyyy/mm/dd',
      formatSubmit: 'yyyy_mm_dd',
      labelMonthNext: 'Mes siguiente',
      labelMonthPrev: 'Mes anterior',
      labelMonthSelect: 'Seleccione un mes',
      labelYearSelect: 'Seleccione un año'
    });   
  }); // end of document ready
})(jQuery); // end of jQuery name space