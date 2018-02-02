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