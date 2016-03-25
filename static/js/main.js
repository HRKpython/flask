var $table = $('#table');
    $(function () {
        $('#toolbar').find('select').change(function () {
            $table.bootstrapTable('refreshOptions', {
                exportDataType: $(this).val()
            });
            console.log("steven");
        });
    })

var $table1 = $('#table1');
    $(function () {
        $('#toolbar1').find('select').change(function () {
            $table1.bootstrapTable('refreshOptions', {
                exportDataType: $(this).val()
            });
        });
    })

$(function () {
                $('#datetimepicker1').datetimepicker();
            });
$(function () {
                $('#datetimepicker2').datetimepicker();
            });

(function ($) {
  $(document).ready(function(){
    
    $(function () {
        $(window).scroll(function () {
            // set distance user needs to scroll before we fadeIn navbar
            if ($(this).scrollTop() < 100) {
                $('.navbar').fadeIn();
           } else {
                $('.navbar').fadeOut();
            }
        });

    
    });

});
  }(jQuery));