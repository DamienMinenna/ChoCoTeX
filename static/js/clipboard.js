function copyImage(url){
    var img=document.createElement('img');
    img.src=url;
    document.body.appendChild(img);
    var r = document.createRange();
    r.setStartBefore(img);
    r.setEndAfter(img);
    r.selectNode(img);
    var sel = window.getSelection();
    sel.addRange(r);
    document.execCommand('Copy');
}

var copyPDF = document.querySelector('.js-copy-PDF');

copyPDF.addEventListener('click', function(event) {
  copyImage('static/img/GroTeX.pdf')
});
