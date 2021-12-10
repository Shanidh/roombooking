console.log('wegfs')
    // $(document).ready(function() {
    //     $("#signupform").validate({
    //         rules: {
    //             username: {
    //                 required: true,
    //                 minlength: 5
    //             },
    //             email: {
    //                 required: true,
    //                 email: true
    //             },
    //             password: {
    //                 required: true,
    //                 minlength: 8
    //             },
    //             confirmpassword: {
    //                 required: true,
    //                 minlength: 8,
    //                 equalTo: "#password"
    //             }
    //         },
    //         messages: {
    //             username: {
    //                 required: "Please Enter a User Name",
    //                 minlength: "Your username must consist of at least 5 characters"
    //             },
    //             password: {
    //                 required: "Please provide a password",
    //                 minlength: "Your password must be at least 8 characters long"
    //             },
    //             confirmpassword: {
    //                 required: "Please provide a password",
    //                 minlength: "Your password must be at least 8 characters long",
    //                 equalTo: "Please enter the same password"
    //             }
    //         }
    //     })

// })

// function valid() {
//     username = document.getElementById('username')
//     email = document.getElementById('email')
//     dob = document.getElementById('dob')
//     phone = document.getElementById('phone')
//     password = document.getElementById('password')
//     confirmpassword = document.getElementById('confirmpassword')
//     gen1 = document.getElementById('male')
//     gen2 = document.getElementById('female')
//     if (username.value = "") {
//         document.getElementById('nerror').innerHTML = "*fill this field"
//         username.focus()
//         return false
//     }
//     if (email.value = "") {
//         document.getElementById('eerror').innerHTML = "*fill this field"
//         email.focus()
//         return false
//     }
//     if (dob.value = "") {
//         document.getElementById('doberror').innerHTML = "*fill this field"
//         dob.focus()
//         return false
//     }
//     if (password.value == "") {
//         document.getElementById('perror').innerHTML = "*fill this field"
//         return false
//     } else if (password.value.length <= 8) {
//         document.getElementById('perror1').innerHTML = "*atleast 8 characters"
//         return false
//     }
//     if (confirmpassword.value == "") {
//         document.getElementById('p2error').innerHTML = "*fill this field"
//         return false
//     } else if (confirmpassword.value.length <= 8) {
//         document.getElementById('p2error1').innerHTML = "*atleast 8 characters"
//         return false
//     }
//     if ((gen1.checked == "") && (gen2.checked == "")) {
//         document.getElementById('generror').innerHTML = "*fill this field"
//         return false
//     } else {
//         return true
//     }
// }