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


