window.onload = function() {
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();
        // generate a five digit number for the contact_number variable
        this.contact_number.value = Math.random() * 100000 | 0;
        // these IDs from the previous steps
        emailjs.sendForm('service_ddhhgx7', 'template_rcboj0b', this)
            .then(function() {
                console.log('SUCCESS!');
                alert("전송 되었습니다.");
                location.reload();
            }, function(error) {
                console.log('FAILED...', error);
                alert("문의 전송이 실패되었습니다.");
            });
    });
}