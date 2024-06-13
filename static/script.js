document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.querySelector('[data-collapse-toggle="mobile-menu"]');
    const menu = document.querySelector('#mobile-menu');
    // Ensure the mobile menu is hidden initially
    menu.style.display = 'none';
    toggleButton.addEventListener('click', () => {
        if (menu.style.display === 'none') {
            menu.style.display = 'block';
        } else {
            menu.style.display = 'none';
        }
    });
});

document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById("myForm").addEventListener("submit", function (e) {
       e.preventDefault() // Cancel the default action
       var myForm = document.getElementById('myForm');
       var url = document.getElementById('url').value;
       myForm.action = '/disable/' + url;
       fetch('/shortenurl/' + url, {
             method: 'POST',
          })
          .then(resp => resp.text()) // or, resp.json(), etc.
          .then(data => {
             document.getElementById("response").innerHTML = data;
          })
          .catch(error => {
             console.error(error);
          });
    });
 });