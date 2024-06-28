let openForm = function () {
    let main_button = document.getElementById('mainButton');
    main_button.className = 'active';
};

let checkBackInput = function (input) {
    input.className = 'active';
};

let checkFrontInput = function (input) {
    if (input.value.length > 0) {
        input.className = 'active';
    } else {
        input.className = '';
    }
};

let updateFront = function (input) {
    let frontText = input.value.trim();
    let frontElement = document.querySelector('.front');
    if (frontText !== '') {
        frontElement.textContent = frontText;
    } else {
        frontElement.textContent = '[Front!]';
    }
}

function updateBack(input) {
    let backText = input.value.trim();
    let backElement = document.querySelector('.back');
    if (backText !== '') {
        backElement.textContent = backText;
    } else {
        backElement.textContent = '[Back!]';
    }
}

let closeForm = function () {
    let main_button = document.getElementById('mainButton');
    main_button.className = '';
    clearError();
    clearInputs();
};

document.addEventListener("keyup", function (e) {
    if (e.key === "Escape" || e.key === "Enter") {
        closeForm();
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.getElementById('add-card-btn').addEventListener('click', function () {
    let front_input = document.getElementById("front");
    let frontText = front_input.value.trim();
    let back_input = document.getElementById("back");
    let backText = back_input.value.trim();
    let errorLabel = document.getElementById("front_error");

    if (frontText === '') {
        errorLabel.textContent = 'front value can\'t be empty';
        errorLabel.style.display = 'block';
    } else {
        const data = {
            front: frontText,
            back: backText,
        };

        const csrftoken = getCookie('csrftoken');

        fetch('/group14/add-new-card/',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify(data),
            })
            .then(response => response.json())
            .then(data => {
                if (!data["error"]) {
                    closeForm()
                } else {
                    errorLabel.textContent = data["error"];
                    errorLabel.style.display = 'block';
                    clearInputs();
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
});

function clearError() {
    let errorLabel = document.getElementById("front_error");
    errorLabel.textContent = '';
    errorLabel.style.display = 'none';
}

function clearInputs() {
    let frontInput = document.getElementById("front");
    let backInput = document.getElementById("back");
    frontInput.value = '';
    backInput.value = '';
    let frontElement = document.querySelector('.front');
    frontElement.textContent = '[Front!]';
    let backElement = document.querySelector('.back');
    backElement.textContent = '[Back!]';
}

document.getElementById('list-cards-btn').addEventListener('click', function () {
    const csrftoken = getCookie('csrftoken');
    fetch('/group14/list-cards/',
        {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
        })
        .then(response => response.json())
        .then(data => {
            let cardsContainer = document.getElementById('cardsContainer');
            cardsContainer.innerHTML = '';  // Clear any existing content

            data.forEach(card => {
                let cardElement = document.createElement('div');
                cardElement.className = 'card-item';
                cardElement.dataset.id = card.id;

                let contentElement = document.createElement('div');
                contentElement.className = 'card-content';
                let frontElement = document.createElement('div');
                frontElement.className = 'Front: ${card.front_value}';
                frontElement.textContent = card.front_value;
                let backElement = document.createElement('div');
                backElement.className = 'Back: ${card.back_value}';
                backElement.textContent = card.back_value;

                contentElement.appendChild(frontElement);
                contentElement.appendChild(backElement);
                cardElement.appendChild(contentElement);

                let actionsElement = document.createElement('div');
                actionsElement.className = 'card-actions';
                // Add edit button
                let editButton = document.createElement('button');
                editButton.className = 'edit-button';
                editButton.textContent = 'Edit';
                editButton.addEventListener('click', () => openEditForm(card));
                cardElement.appendChild(editButton);

                // Add delete button
                let deleteButton = document.createElement('button');
                deleteButton.className = 'delete-button';
                deleteButton.textContent = 'Delete';
                deleteButton.addEventListener('click', () => deleteCard(card.id));
                cardElement.appendChild(deleteButton);
                
                cardElement.appendChild(actionsElement);

                cardsContainer.appendChild(cardElement);
            });
            let modal = document.getElementById('cardsModal');
            modal.style.display = "block";
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

window.onclick = function(event) {
    let modal = document.getElementById('cardsModal');
    let edit_modal = document.getElementById('editCardModal');
    
    if (event.target == cardsModal) {
        cardsModal.style.display = "none";
    }
    if (event.target == editCardModal) {
        closeEditForm();
    }
}

function closeModal() {
    let modal = document.getElementById('cardsModal');
    modal.style.display = "none";
}

let openEditForm = function(card) {
    let editForm = document.getElementById('editCardModal');
    document.getElementById('editCardId').value = card.id;
    document.getElementById('editFront').value = card.front_value;
    document.getElementById('editBack').value = card.back_value;
    document.getElementById('editFrontPreview').textContent = card.front_value;
    document.getElementById('editBackPreview').textContent = card.back_value;
    editForm.style.display = "block";
};

let closeEditForm = function() {
    let editForm = document.getElementById('editCardModal');
    editForm.style.display = 'none'
    clearEditError();
    clearEditInputs();
};

document.getElementById('saveEditBtn').addEventListener('click', function () {
    const csrftoken = getCookie('csrftoken');
    const cardId = document.getElementById('editCardId').value;
    const updatedFront = document.getElementById('editFront').value;
    const updatedBack = document.getElementById('editBack').value;
    let errorLabel = document.getElementById("edit_front_error");

    if (updatedFront === '') {
        errorLabel.textContent = 'Front value can\'t be empty';
        errorLabel.style.display = 'block';
    } else {
        errorLabel.style.display = 'none';
        const data = {
            id: cardId,
            front: updatedFront,
            back: updatedBack,
        };
        fetch(`/group14/edit-card/${cardId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            // Update the card in the modal
            let frontElement = document.querySelector(`.card-item[data-id='${cardId}']`);
            let backElement = document.querySelector(`.card-item[data-id='${cardId}']`);
            
            if (frontElement) {
                //frontElement.textContent = updatedFront;
            } else {
                console.error('Front element not found');
            }

            if (backElement) {
                //backElement.textContent = updatedBack;
            } else {
                console.error('Back element not found');
            }

            // TODO: success message is not shown

            // Show success message
            let successMessage = document.createElement('div');
            successMessage.className = 'success-message';
            successMessage.textContent = 'Card updated successfully!';
            document.querySelector('#editCardModal .modal-content').appendChild(successMessage);
        
            // Remove success message after 2 seconds
            setTimeout(() => {
                successMessage.remove();
            }, 2000);

            closeEditForm();
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});

function clearEditError() {
    let errorLabel = document.getElementById("edit_front_error");
    errorLabel.textContent = '';
    errorLabel.style.display = 'none';
}

function clearEditInputs() {
    document.getElementById("editFront").value = '';
    document.getElementById("editBack").value = '';
}

function deleteCard(cardId) {
    const csrftoken = getCookie('csrftoken');

    fetch(`/group14/delete-card/${cardId}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            let cardElement = document.querySelector(`.card[data-id='${cardId}']`);
            cardElement.remove();
        } else {
            console.error('Error deleting card:', data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function updateEditFront(input) {
    let frontText = input.value.trim();
    let frontElement = document.getElementById('editFrontPreview');
    if (frontText !== '') {
        frontElement.textContent = frontText;
    } else {
        frontElement.textContent = '[Front!]';
    }
}

// TODO: preview is not well located

function updateEditBack(input) {
    let backText = input.value.trim();
    let backElement = document.getElementById('editBackPreview');
    if (backText !== '') {
        backElement.textContent = backText;
    } else {
        backElement.textContent = '[Back!]';
    }
}