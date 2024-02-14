function changeLanguage(language) {
    document.getElementById("language_input").value = language;
    document.getElementById("language_form").submit();
}

function openList(button) {
    let isOpened = button.parentNode.querySelector('.dropdown-content--show') !== null;

    document.querySelectorAll('.dropdown-content').forEach(function (content) {
        content.classList.remove('dropdown-content--show');
    });

    button.parentNode.querySelectorAll('.dropdown-content').forEach(function (child) {
        if (!child.classList.contains("dropdown-content--show")) {
            if (!isOpened) {
                child.classList.add("dropdown-content--show");

                child.addEventListener('mouseleave', function () {
                    if (!button.matches(':hover')) {
                        child.classList.remove('dropdown-content--show');
                    }
                });
            }
        }
    });

    button.addEventListener('mouseenter', function () {
        isOpened = true;
    });

    button.addEventListener('mouseleave', function () {
        isOpened = false;
    });
}

function closeAllLists() {
    document.querySelectorAll('.dropdown-content').forEach(function (content) {
        content.classList.remove('dropdown-content--show');
    });
}

document.querySelector('.main_content_layout').addEventListener('click', function (event) {
    closeAllLists_menuPress(event);
});

function closeAllLists_menuPress(event) {
    if (event.target.classList.contains('main_content_layout')) {
        document.querySelectorAll('.dropdown-content').forEach(function (content) {
            content.classList.remove('dropdown-content--show');
        });
    }
}

function changeButtonText(link) {
    let button = link.closest('.dropdown').querySelector('.dropbtn');
    button.textContent  = link.textContent;
    closeAllLists();
}

function updateList(current_el, update_block_id) {
    let current_el_hidden_input = current_el.closest('.setting_option_block').querySelector('.hidden_selector');
    current_el_hidden_input.value = current_el.id;
    console.log(current_el.id)
    changeButtonText(current_el);

    let update_teachers_list_button = document.querySelector("#teachers_select").lastElementChild.querySelector('.dropbtn');
    update_teachers_list_button.innerHTML = "----"
    let teachers_block_list = document.querySelector("#teachers_select").lastElementChild.querySelector('.dropdown-content');
    while (teachers_block_list.firstChild) {
        teachers_block_list.removeChild(teachers_block_list.firstChild);
    }

    let update_departments_list_button = document.querySelector("#departments_select").lastElementChild.querySelector('.dropbtn');
    update_departments_list_button.innerHTML = "----"
    let update_subjects_list_button = document.querySelector("#subjects_select").lastElementChild.querySelector('.dropbtn');
    update_subjects_list_button.innerHTML = "----"
    let subjects_block_list = document.querySelector("#subjects_select").lastElementChild.querySelector('.dropdown-content');
    while (subjects_block_list.firstChild) {
        subjects_block_list.removeChild(subjects_block_list.firstChild);
    }
    newParagraph = document.createElement('a');
    newParagraph.textContent = 'First select Department';
    subjects_block_list.appendChild(newParagraph);


    let update_block_list = document.querySelector("#" + update_block_id + "_select").lastElementChild.querySelector('.dropdown-content');

    while (update_block_list.firstChild) {
        update_block_list.removeChild(update_block_list.firstChild);
    }

    let xhr = new XMLHttpRequest();
    let url = `/api/v1.0/siut/get_${update_block_id}/?${current_el_hidden_input.name}=${current_el_hidden_input.value}`;
    xhr.open("GET", url, true);

    xhr.onreadystatechange = async function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            console.log(json);
            if (json.answer !== "") {
                for (let i of json) {
                    const newEl = document.createElement("a");
                    newEl.text = i.name;
                    newEl.id = i.pk;
                    newEl.addEventListener("click", () => {
                        updateSubjects(newEl);
                    });
                    update_block_list.appendChild(newEl);
                }
            }
        }
    };

    xhr.send();
}


function updateSubjects(current_el) {
    let current_el_hidden_input = current_el.closest('.setting_option_block').querySelector('.hidden_selector');
    current_el_hidden_input.value = current_el.id;
    console.log(current_el.id)
    changeButtonText(current_el);

    let update_teachers_list_button = document.querySelector("#teachers_select").lastElementChild.querySelector('.dropbtn');
    update_teachers_list_button.innerHTML = "----"
    let teachers_block_list = document.querySelector("#teachers_select").lastElementChild.querySelector('.dropdown-content');
    while (teachers_block_list.firstChild) {
        teachers_block_list.removeChild(teachers_block_list.firstChild);
    }

    let update_subjects_list_button = document.querySelector("#subjects_select").lastElementChild.querySelector('.dropbtn');
    update_subjects_list_button.innerHTML = "----"
    let subjects_block_list = document.querySelector("#subjects_select").lastElementChild.querySelector('.dropdown-content');
    while (subjects_block_list.firstChild) {
        subjects_block_list.removeChild(subjects_block_list.firstChild);
    }

    let update_block_list = document.querySelector("#subjects_select").lastElementChild.querySelector('.dropdown-content');

    while (update_block_list.firstChild) {
        update_block_list.removeChild(update_block_list.firstChild);
    }

    let xhr = new XMLHttpRequest();
    let url = `/api/v1.0/siut/get_subjects_by_department_id/?department_id=${current_el_hidden_input.value}`;
    xhr.open("GET", url, true);

    xhr.onreadystatechange = async function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            console.log(json);
            if (json.answer !== "") {
                for (let i of json) {
                    const newEl = document.createElement("a");
                    newEl.text = i.name;
                    newEl.id = i.pk;
                    newEl.addEventListener("click", () => {
                        updateTeachers(newEl);
                    });
                    update_block_list.appendChild(newEl);
                }
            }
        }
    };

    xhr.send();
}

function updateTeachers(current_el) {
    let current_el_hidden_input = current_el.closest('.setting_option_block').querySelector('.hidden_selector');
    current_el_hidden_input.value = current_el.id;
    console.log(current_el.id)
    changeButtonText(current_el);

    let update_teachers_list_button = document.querySelector("#teachers_select").lastElementChild.querySelector('.dropbtn');
    update_teachers_list_button.innerHTML = "----"
    let update_block_list = document.querySelector("#teachers_select").lastElementChild.querySelector('.dropdown-content');
    while (update_block_list.firstChild) {
        update_block_list.removeChild(update_block_list.firstChild);
    }


    let xhr = new XMLHttpRequest();
    let url = `/api/v1.0/siut/get_teachers_by_subject_id/?subject_id=${current_el_hidden_input.value}`;
    xhr.open("GET", url, true);

    xhr.onreadystatechange = async function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            console.log(json);
            if (json.answer !== "") {
                for (let i of json) {
                    const newEl = document.createElement("a");
                    newEl.text = i.name;
                    newEl.id = i.pk;
                    newEl.addEventListener("click", () => {
                        newEl.closest('.setting_option_block').querySelector('.hidden_selector').value = newEl.id;
                        changeButtonText(newEl);
                    });
                    update_block_list.appendChild(newEl);
                }
            }
        }
    };

    xhr.send();
}

function checkUserInfoForm(clicked_btn) {
    const hiddenSelectors = document.querySelectorAll('.hidden_selector--main_info');
    const user_name_field = document.querySelectorAll('.user_name_input');

    for (const hiddenSelector of hiddenSelectors) {
        if (hiddenSelector.value.trim() === '') {
            alert('Please fill in all the required fields.');
            return false;
        }
    }

    for (const inputField of user_name_field) {
        if (inputField.value.trim() === '') {
            alert('Please fill in all the required fields.');
            return false;
        }
    }

    clicked_btn.closest(".submit_button_block").classList.add("all_questions_block--hide");
    return true;
}


function showQuestions() {
    document.querySelector(".all_questions_block").classList.remove("all_questions_block--hide")
}

function isRadioButtonChecked(questionNumber) {
    // Get all radio buttons for the specified question
    var radioButtons = document.getElementsByName('question' + questionNumber);

    // Check if at least one radio button is checked
    for (var i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            return true;
        }
    }

    // If no radio button is checked, return false
    return false;
}

function checkFeedbackForm() {
    for (var i = 1; i <= 6; i++) {  // Start from 1 instead of 0 for question numbers
        if (!isRadioButtonChecked(i)) {
                alert("Please select a response for Question " + i + ".");
            return false;
        }
    }

    return true;
}

function FeedbackResultsSearch(inputElement) {
    var searchText = inputElement.value.toLowerCase();
    var questionBlocks = document.querySelectorAll('.question_block');

    questionBlocks.forEach(function(block) {
        if (!block.classList.contains('organizer_class')) {
            var titleText = block.querySelector('.question_title_block h2').textContent.toLowerCase();
            if (searchText !== '' && !titleText.includes(searchText)) {
                block.classList.add('-hide_block');
            } else {
                block.classList.remove('-hide_block');
            }
        }
    });

    if (searchText === '') {
        questionBlocks.forEach(function(block) {
            if (!block.classList.contains('organizer_class')) {
                block.classList.remove('-hide_block');
            }
        });
    }
}





