const form = document.querySelector('form');
const container = document.querySelector('#food')
form.addEventListener('submit',function(e){
    e.preventDefault();
    console.log(e);
    for(let i=0;i<24;i++){
        if(form.elements[i].checked === true){
            const item = document.createElement('li');
            item.append(form.elements[i].name);
            container.append(item);
        }
    }
    document.querySelector('form').reset();
})