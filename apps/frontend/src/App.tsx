import { useState } from 'react'
import avatar from '/public/avatar.png';
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://github.com/Qikxiji" target="_blank">
          <img src={avatar} className="logo" alt="Vite logo" />
        </a>
      </div>
      <h1>Nginx/Postgres/Django/React</h1>
      <h2>Qikxiji Docker Compose deploy</h2>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Go to <a href="http://localhost:8000/admin/login/" target="_blank">localhost:8000/admin</a> to see django admin form for Postgres
        </p>
      </div>
      <p className="read-the-docs">
        Click on the avatar see my GitHub!
      </p>
    </>
  )
}

export default App
