document.querySelector('#add_item').addEventListener('click', function () {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newLi);
});
