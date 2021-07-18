//function for allowing you to add ingredients to the web form
function add_ingridient(){
    
    let hidden_ingredients = $('#ingredients');
    let ingredients = [];

    let ingr_name = $('#ingredient_name').val();
    let ingr_amount = $('#ingredient_amount').val();
    let ingr_measure = $('#ingredient_measure').val();

    let ingr = { name: ingr_name, amount: ingr_amount, measure: ingr_measure };

    if (hidden_ingredients.val() !== "") {
        ingredients = JSON.parse(hidden_ingredients.val());
    } 

    ingredients.push(ingr);

    display_ingridients(ingredients);
}
 //function for allowing you to remove ingredients to the web form
function remove_ingridient(name){
   
    let hidden_ingredients = $('#ingredients');
    let ingredients = JSON.parse(hidden_ingredients.val());

    let indx = ingredients.findIndex(x => x.name == name);
    if(indx > -1) {

        ingredients.splice(indx, 1);
        display_ingridients(ingredients)
    }
}

//function to display the information on the webpage
function display_ingridients(ingredients){
    let hidden_ingredients = $('#ingredients');

    hidden_ingredients.val(JSON.stringify(ingredients));

    let new_ingridients_string = '<h4 class="container">';
    ingredients.forEach(element => {
       new_ingridients_string += `<div class="row"><div class="col">${element.name}</div><div class="col">${element.amount}</div><div class="col">${element.measure}</div> <div class="col"><button class="btn btn-danger" onclick="remove_ingridient('${element.name}')" >Remove</button></div> </div>`;
    });
    new_ingridients_string += '</h4>';

    $('#current_ingridients').html(new_ingridients_string );

}