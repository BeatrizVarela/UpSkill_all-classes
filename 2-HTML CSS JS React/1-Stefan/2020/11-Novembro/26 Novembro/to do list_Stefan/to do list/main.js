var idCount;

//Elements
var todoInput = document.querySelector(".todo-input");
var todoButton = document.querySelector(".todo-insert");
var todoList = document.querySelector(".todo-list");
var filterDropdown = document.querySelector(".filter-todo");

//Event Listeners
todoButton.addEventListener("click", addTodo);
todoList.addEventListener("click", deleteCheck);
filterDropdown.addEventListener("change", filterTodo);

//Functions
function addTodo(event) {
  event.preventDefault();

  let todoValue = todoInput.value;
  let todoCompleteValue = false;

  let todoJson = {
    value: todoValue,
    complete: todoCompleteValue,
    id: `todo-${idCount}`,
  };

  buildItemWithViewHolder(todoJson);

  todoInput.value = "";

  save(todoJson);
  idCount++;
}

function deleteCheck(event) {
  // obter o botao da lista que foi pressionado
  var pressedBtn = event.target;

  if (pressedBtn.classList[0] == "trash-button") {
    const parent = pressedBtn.parentElement;
    parent.classList.add("fall");
    parent.addEventListener("transitionend", function () {
      parent.remove();
      removeItemWithId(parent.id);
    });
  }

  if (pressedBtn.classList[0] == "check-button") {
    const parent = pressedBtn.parentElement;
    parent.classList.toggle("complete");
    updateTodoWithId(parent.id);
  }
}

function filterTodo(event) {
  const todos = todoList.querySelectorAll(".todo");
  todos.forEach(function (todo) {
    switch (event.target.value) {
      case "all":
        todo.style.display = "flex";
        break;
      case "completed":
        if (todo.classList.contains("complete")) {
          todo.style.display = "flex";
        } else {
          todo.style.display = "none";
        }
        break;
      case "uncompleted":
        if (!todo.classList.contains("complete")) {
          todo.style.display = "flex";
        } else {
          todo.style.display = "none";
        }
        break;
    }
  });
}

function updateTodoWithId(id) {
  // 1. obter o elemento do localstorage com o id
  let todoItems = JSON.parse(localStorage.getItem("todo"));
  const item = todoItems.filter(function (todoItem) {
    return todoItem.id == id;
  })[0];
  console.log(item);
  // 2. alterar o valor do elmento encontrado
  item.complete = !item.complete;
  // 3. guardar alterações
  localStorage.setItem("todo", JSON.stringify(todoItems));
}

function removeItemWithId(id) {
  // 1. Buscar lista de elementos
  let todoItems = JSON.parse(localStorage.getItem("todo"));
  // 2. remover elemento com id
  todoItems = todoItems.filter(function (todoItem) {
    return todoItem.id != id;
  });
  // 3. guardar alterações
  localStorage.setItem("todo", JSON.stringify(todoItems));
}

function loadItems() {
  if (localStorage.getItem("todo") != null) {
    let todoItems = JSON.parse(localStorage.getItem("todo"));
    // todoItems.map(function (todoItem) {
    //   buildItemWithViewHolder(todoItem);
    // });
    todoItems.map(buildItemWithViewHolder);
  }
}

function buildItemWithViewHolder(viewHolder) {
  const div = document.createElement("div");
  /*var class_todo = document.createAttribute("class");
  divClass.value = "todo";                Outra forma de adicionar uma class 
  div.setAttribute(divClass);*/
  div.classList.add("todo");
  div.id = viewHolder.id;
  if (viewHolder.complete) div.classList.add("complete");
  // criar o elemento da lista <li>
  const todoItem = document.createElement("li");
  todoItem.classList.add("todo-item");
  todoItem.innerHTML = viewHolder.value;
  div.appendChild(todoItem);
  // Criar o botao de checkmark
  const checkBtn = document.createElement("button");
  checkBtn.classList.add("check-button");
  checkBtn.innerHTML = '<i class="far fa-check-square"></i>';
  div.appendChild(checkBtn);
  // Criar o butao trash
  const trashBtn = document.createElement("button");
  trashBtn.classList.add("trash-button");
  trashBtn.innerHTML = '<i class="fas fa-trash-alt"></i>';
  div.appendChild(trashBtn);
  //adicionar o div ao ficheiro
  todoList.appendChild(div);
}

function save(todo) {
  let todoItems;
  if (localStorage.getItem("todo") == null) {
    todoItems = [];
  } else {
    todoItems = JSON.parse(localStorage.getItem("todo"));
  }
  // adicionar elementos ao fim da lista
  todoItems.push(todo);
  localStorage.setItem("todo", JSON.stringify(todoItems));
}

window.onpageshow = function () {
  if (localStorage.getItem("idCount") === null) {
    idCount = 0;
  } else {
    idCount = JSON.parse(localStorage.getItem("idCount"));
  }
  loadItems();
};

window.onpagehide = function () {
  localStorage.setItem("idCount", JSON.stringify(idCount));
};
