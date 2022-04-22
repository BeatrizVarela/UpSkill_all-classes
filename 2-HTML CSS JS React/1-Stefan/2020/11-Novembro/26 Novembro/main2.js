var idCount;

// elements
var todoInput = document.querySelector(".todo-input");
var todoButton = document.querySelector(".todo-btn");
var todoList = document.querySelector(".todo-list");
var filterDropdown = document.querySelector(".filter-todo");

// Event listeners
todoButton.addEventListener("click", addTodo);
todoList.addEventListener("click", deleteCheck);
filterDropdown.addEventListener("change", filterTodo);

// functions
function addTodo(event) {
  event.preventDefault();

  let todoValue = todoInput.value;

  if (!todoValue) {
    return;
  }

  let todoCompleteValue = false;
  idCount++;
  let todoJson = {
    value: todoValue,
    complete: todoCompleteValue,
    id: "todo-${idCount}",
  };
  buildItemWithViewHolder(todoJson);
  save(todoJson);
  todoInput.value = "";
}

function deleteCheck(event) {
  // obter o botao da lista que foi pressionado
  var pressedButton = event.target;

  if (pressedButton.classList[0] == "trash-btn") {
    const parent = pressedButton.parentElement;
    parent.classList.add("fall");
    parent.addEventListener("transitionend", function () {
      parent.remove();
      removeItemWithId(parent.id);
    });
  }

  if (pressedButton.classList[0] == "complete-btn") {
    const parent = pressedButton.parentElement;
    parent.classList.toggle("complete");
    updateTodoWithId(parent.id);
  }
}

function filterTodo(event) {
  // console.log(event.target.querySelector(".todo"));
  const todos = todoList.querySelectorAll(".todo");
  // console.log(event.target.value);
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

function loadItems() {
  if (localStorage.getItem("todo") != null) {
    let todoItems = JSON.parse;
  }
}

function updateTodoWithId(id) {
  // 1. obter o elemento do localstorage com o id
  let todoItems = JSON.parce(localStorage.getItem("todo"));
  const item = todoItems.filter(function (todoItem) {
    return todoItem.id == id;
  })[0];
  console.log(item);
  // 2. alterar o valor do elemento encontrado
  item.complete = !item.complete;
  // 3. guardar alteracoes
  localStorage.setItem("todo", JSON.stringify(todoItems));
}

function removeItemWithId(id) {
  // 1. buscar lista de elementos
  let todoItems = JSON.parse(localStorage.getItem("todo"));
  // 2. remover elemento com id
  todoItems = todoItems.filter(function (todoItem) {
    return todoItem.id != id;
  });
  // 3. guardar alteracoes
  localStorage.setItem("todo", JSON.stringify(todoItems));
}

function loadItems() {
  if (localStorage.getItem("todo") != null) {
    let todoItems = JSON.parse(localStorage.getItem("todo"));
    /*     todoItems.map(function (todoItem) {
                buildItemWithViewHolder(todoItem);
        }); */
    todoItems.map(function (todoItem) {
      buildItemWithViewHolder(todoItem);
    });
  }
}

function buildItemWithViewHolder(viewHolder) {
  const div = document.createElement("div");
  // const divClass = document.createAttribute("class");
  // divClass.value = "todo";
  // div.setAttributeNode(divClass)
  div.id = viewHolder.id;
  if (viewHolder.complete) div.classList.add("complete");
  div.classList.add("todo");

  // criar o elemento da lista li
  const todoItem = document.createElement("li");
  todoItem.classList.add("todo-item");
  todoItem.innerHTML = viewHolder.value;
  div.appendChild(todoItem);

  // criar o botão de check
  const completeBtn = document.createElement("button");
  completeBtn.classList.add("complete-btn");
  completeBtn.innerHTML = '<i class = "fas fa-check"></i>';
  div.appendChild(completeBtn);

  // criar o botão de apagar
  const trashBtn = document.createElement("button");
  trashBtn.classList.add("trash-btn");
  trashBtn.innerHTML = '<i class = "fas fa-trash"></i>';
  div.appendChild(trashBtn);

  // adicionar à lista de to dos
  todoList.appendChild(div);
}

function save(todo) {
  let todosItems;
  if (localStorage.getItem("todo") == null) {
    todosItems = [];
  } else {
    todosItems = JSON.parse(localStorage.getItem("todo"));
  }

  // adicionar elemento no fim da lista
  todosItems.push(todo);
  localStorage.setItem("todo", JSON.stringify(todosItems));
}

window.onpageshow = function () {
  if (localStorage.getItem("idCount") == null) {
    idCount = 0;
  } else {
    idCount = JSON.parse(localStorage.getItem("idCount"));
  }
  loadItems();
};

/*
window.onunload = function () {
  localStorage.setItem = JSON.stringify(idCount);
};
*/

window.onpagehide = function () {
  localStorage.setItem("idCount", JSON.stringify(idCount));
};
