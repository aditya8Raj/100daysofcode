import { useState } from "react";
import "../css/todo.css";
import { useRef } from "react";
import { useEffect } from "react";
import TodoItems from "./TodoItems";

let count = 0;
const Todo = () => {
  const [todos, setTodos] = useState([]);
  const inputRef = useRef(null);

  const addTodos = () => {
    setTodos([
      ...todos,
      { no: count++, text: inputRef.current.value, display: "" },
    ]);
    inputRef.current.vallue = "";
    localStorage.setItem("todos_count", count);
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      addTodos();
    }
  };

  useEffect(() => {
    setTodos(JSON.parse(localStorage.getItem("todos")));
    count = localStorage.getItem("todos_count");
  }, []);

  useEffect(() => {
    setTimeout(() => {
      console.log(todos);
      localStorage.setItem("todos", JSON.stringify(todos));
    }, 100);
  }, [todos]);

  return (
    <>
      <div className="todo">
        <div className="todo-header">To-Do List</div>
        <div className="todo-add">
          <input
            ref={inputRef}
            type="text"
            placeholder="Add Your Task"
            className="todo-input"
            onKeyDown={handleKeyDown}
          />
          <div
            onClick={() => {
              addTodos();
            }}
            className="todo-add-btn"
          >
            ADD
          </div>
        </div>
        <div className="todo-list">
          {todos.map((item, index) => {
            return (
              <TodoItems
                key={index}
                setTodos={setTodos}
                no={item.no}
                display={item.display}
                text={item.text}
              />
            );
          })}
        </div>
      </div>
    </>
  );
};

export default Todo;
