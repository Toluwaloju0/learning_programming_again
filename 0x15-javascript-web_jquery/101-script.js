document.addEventListener('DOMContentLoaded', () => {
  // Add item
  document.querySelector('div#add_item').addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    document.querySelector('ul.my_list').appendChild(newItem);
  });

  // Remove last item
  document.querySelector('div#remove_item').addEventListener('click', () => {
    const list = document.querySelector('ul.my_list');
    if (list.lastElementChild) {
      list.removeChild(list.lastElementChild);
    }
  });

  // Clear entire list
  document.querySelector('div#clear_list').addEventListener('click', () => {
    const list = document.querySelector('ul.my_list');
    list.innerHTML = '';
  });
});
