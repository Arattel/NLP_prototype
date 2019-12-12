document.addEventListener('click', async evt =>{
    if(evt.target.matches(".Butt")){
        var text = document.getElementsByClassName("Form")[0].value;
         let config = {
             method:  'POST',
             headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
             },
           body: JSON.stringify({text:text})
         };
         console.log(config);
         const  response = await (await fetch(`http://127.0.0.1:5000/results/`, config)).json();
         const label = response.class;
         document.getElementsByClassName("Cathegory")[0].innerHTML = label;
    }
});