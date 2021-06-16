$(document).ready(function () {
    $("#formulario1").validate({
        rules: {
            first_name: {
                required: true,
                minlength: 3

            },
            run: {
                required: true,
                rut: true
            },
            last_name: {
                required: true,
                minlength: 3

            },
            email: {
                required: true,
                email: true
            },
            phone1: {
                required: true
            },
            phone2: {
                required: true,
                equalTo: '#id_phone1'
            },
            birth_day: {
                required: true,
                date: true
            },
            password1: {
                required: true,
                minlength: 7
            },
            password2: {
                required: true,
                equalTo: '#id_password1'
            },
            movie_preference: {
                required: true
            },

            sex: {
                required: true
            }


        }

    });

});