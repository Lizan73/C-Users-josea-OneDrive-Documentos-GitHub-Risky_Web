document.addEventListener('DOMContentLoaded', function() {
    // Manejar el botón "Modificar"
    const updateButtons = document.querySelectorAll('.update-button');
    updateButtons.forEach(button => {
        button.addEventListener('click', function() {
            const item = JSON.parse(button.dataset.item);
            document.getElementById('id').value = item.id;
            document.getElementById('name').value = item.name;
            document.getElementById('description').value = item.description || '';
            document.getElementById('ingredients').value = item.ingredients || '';
            document.getElementById('image').value = item.image || '';
            document.getElementById('category').value = item.category;
            document.getElementById('price').value = item.price;
            document.getElementById('add-button').style.display = 'none';
            document.getElementById('confirm-update-button').style.display = 'inline-block';
            document.getElementById('cancel-update-button').style.display = 'inline-block';
        });
    });

    // Manejar la confirmación del botón "Eliminar"
    const deleteForms = document.querySelectorAll('.delete-form');
    deleteForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!confirm('Are you sure you want to delete this item?')) {
                event.preventDefault();
            }
        });
    });
    
    

function cancelUpdate() {
    document.getElementById('id').value = '';
    document.getElementById('name').value = '';
    document.getElementById('description').value = '';
    document.getElementById('ingredients').value = '';
    document.getElementById('image').value = '';
    document.getElementById('category').value = 'Beverage';
    document.getElementById('price').value = '';
    document.getElementById('add-button').style.display = 'inline-block';
    document.getElementById('confirm-update-button').style.display = 'none';
    document.getElementById('cancel-update-button').style.display = 'none';
}

function toggleFields() {
    const category = document.getElementById('category').value;
    const descriptionField = document.getElementById('description');
    const ingredientsField = document.getElementById('ingredients');
    const imageField = document.getElementById('image');

    if (category === 'Beverage') {
        descriptionField.value = '';
        descriptionField.required = false;
        ingredientsField.value = '';
        ingredientsField.required = false;
        imageField.value = '';
        imageField.required = false;
    } else {
        descriptionField.required = true;
        ingredientsField.required = true;
        imageFiseld.required = true;
    }
}

function confirmDelete() {
    return confirm('Are you sure you want to delete this item?');
}
})