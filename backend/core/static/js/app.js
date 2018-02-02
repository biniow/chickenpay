function uuidv4() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}

function generateQRCode() {
    var comment = $("#comment")[0].value,
        price = $("#price")[0].value,
        qrcodeDiv = $("#qrcodeTable");
        qrcodeDiv.empty();
        qrcodeDiv.qrcode({
            render: "table",
            text: comment + ";" + price
        });
}

function exportCode() {

}

function sendRegistrationData() {
    var userName = $('#registration_username')[0].value,
        firstname = $('#registration_firstname')[0].value,
        lastname = $('#registration_lastname')[0].value,
        email = $('#registration_email')[0].value,
        password = $('#registration_password')[0].value,
        json = {
            username: userName,
            first_name: firstname,
            last_name: lastname,
            email: email,
            password: password
        };
    $.ajax
    ({
        type: "POST",
        url: 'http://127.0.0.1:8000/api/user/create/',
        headers: {
            "Access-Control-Allow-Origin":"*"
        },
        async: false,
        dataType: 'json',
        //json object to sent to the authentication url
        data: JSON.stringify(json),
        success: function (response) {
            console.log(response);
        }
    })
}