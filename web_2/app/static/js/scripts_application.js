function setFilter(filterName) {
    var filterButton = document.getElementById('filterBtn');
    filterButton.innerHTML = '<i class="fas fa-filter"></i> ' + filterName;
    var dropdownContent = document.getElementById('dropdownContent');
    dropdownContent.classList.add('hidden');
}

// Открытие/закрытие модального окна с информацией о системе
function toggleSystemInfoModal() {
    var modal = document.getElementById('systemInfoModal');
    modal.classList.toggle('hidden');
}

// Закрытие модального окна с информацией о системе
function closeSystemInfo() {
    var modal = document.getElementById('systemInfoModal');
    modal.classList.add('hidden');
}


// Функция для открытия модального окна добавления новой заявки
function openAddRequestModal() {
    document.getElementById('addRequestModal').style.display = 'block';
}

// Функция для закрытия модального окна добавления новой заявки
function closeAddRequestModal() {
    document.getElementById('addRequestModal').style.display = 'none';
}

// Функция для сохранения данных новой заявки (здесь нужно написать логику сохранения данных)
function saveRequest() {
    // Здесь можно получить значения полей формы и выполнить необходимые действия (например, отправку данных на сервер)
    // После сохранения данных можно закрыть модальное окно
    closeAddRequestModal();
}

function makeEditable(td) {
    let input = document.createElement('input');
    input.type = 'text';
    input.value = td.innerText;
    input.style.width = '100%'; // Чтобы input занял всю ширину ячейки
    input.style.color = 'black'; // Установить черный цвет текста
    td.innerHTML = '';
    td.appendChild(input);
    input.focus();

    input.addEventListener('blur', function() {
        td.innerText = this.value;
        updateDatabase(td.parentElement, td.cellIndex, this.value);
    });

    input.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            this.blur(); // Завершить редактирование при нажатии Enter
        }
    });
}



// Переключение на физические лица
function switchToIndividual() {
    document.querySelector('.tab-btn:nth-child(1)').classList.add('selected');
    document.querySelector('.tab-btn:nth-child(2)').classList.remove('selected');
    // Ваш код для отображения данных физических лиц
}

// Переключение на юридические лица
function switchToLegal() {
    document.querySelector('.tab-btn:nth-child(2)').classList.add('selected');
    document.querySelector('.tab-btn:nth-child(1)').classList.remove('selected');
    // Ваш код для отображения данных юридических лиц
}






document.addEventListener("DOMContentLoaded", function() {
    // Получаем все пункты меню
    var menuItems = document.querySelectorAll('.menu-item');

    // Добавляем обработчик событий для каждого пункта меню
    menuItems.forEach(function(item) {
        item.addEventListener('click', function() {
            // Удаляем класс "active" у всех пунктов меню
            menuItems.forEach(function(menuItem) {
                menuItem.classList.remove('active');
            });

            // Добавляем класс "active" к выбранному пункту меню
            this.classList.add('active');
        });
    });
});