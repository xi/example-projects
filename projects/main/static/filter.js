var input = document.querySelector('input');
var items = Array.from(document.querySelectorAll('[data-filter]'));

input.addEventListener('input', event => {
    var words = event.target.value.toLowerCase().split(' ');
    items.forEach(item => {
        item.hidden = !words.every(word => item.dataset.filter.includes(word));
    });
});
