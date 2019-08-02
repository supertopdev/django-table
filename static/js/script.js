// $(document).ready(function(){
//     $(".delete").click(function() {
//         var id = $(this).attr('id');
//         $.ajax({
//             url: "{% url 'delete' %}",
//             data: "{ 'id' : id }",
//             beforeSend: function(xhr) {
//                 xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
//             },
//             success: function(response){
//                 if (response['success'] == 'success') {
//                     location.reload(true);
//                 }
//             }
//         });
//     });
// });


// function require(bootstrapSlider) {
//             return undefined;
//         }
//
// var mySlider = $("input.slider").slider();
//
// // Call a method on the slider
// var value = mySlider.slider('getValue');
//
// mySlider
//     .slider = function (value1, number) {
//
// }
// // For non-getter methods, you can chain together commands
// mySlider
//     .slider('setValue', 5);

$("#btn-advanced-criterias").click(function (e) {
    if($('input[id="fancy-checkbox-info"]').prop("checked") == true){
        if ($('input[id="fancy-checkbox-warning"]').prop("checked") == true){
            $(".form-group").attr('id');
            console.log("hahaha");
            $("#controls-residential-sale").show();
            $("#controls-residential-rent").hide();
            $("#controls-commercial-sale").hide();
            $("#controls-commercial-rent").hide();
        }
        else {

            console.log("huhuhu");
            $(".form-group").attr('id');
            $("#controls-residential-sale").hide();
            $("#controls-residential-rent").show();
            $("#controls-commercial-sale").hide();
            $("#controls-commercial-rent").hide();
        }
    }
    else {
        if ($('input[id="fancy-checkbox-warning"]').prop("checked") == true){
            $(".form-group").attr('id');
            console.log("hahaha");
            $("#controls-residential-sale").hide();
            $("#controls-residential-rent").hide();
            $("#controls-commercial-sale").show();
            $("#controls-commercial-rent").hide();
        }
        else {

            console.log("huhuhu");
            $(".form-group").attr('id');
            $("#controls-residential-sale").hide();
            $("#controls-residential-rent").hide();
            $("#controls-commercial-sale").hide();
            $("#controls-commercial-rent").show();
        }
    }
    //
    // $(".form-group").attr('id');
    // console.log("hahaha");
    // $("#controls-residential-sale").show();
});

//
// $(document).ready(function(){
//     $('input[id="fancy-checkbox-success"]').click(function(){
//         if($(this).prop("checked") == true){
//             alert("Checkbox is checked.");
//         }
//         else if($(this).prop("checked") == false){
//             alert("Checkbox is unchecked.");
//         }
//     });
// });




