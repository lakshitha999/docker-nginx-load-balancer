
import { useState } from 'react'
import './App.css'

function App() {
  const [isLogin, setIsLogin] = useState(false)
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState('')
  const [loading, setLoading] = useState(false)

  async function handleSubmit(e) {
    e.preventDefault()
    setMessage('')
    setLoading(true)

    const endpoint = isLogin ? '/api/login' : '/api/register'

    const userData = isLogin
      ? { email, password }
      : { name, email, password }

    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
      })

      const result = await response.json()

      setMessage(result.message || result.error)

      if (response.ok && isLogin) {
        setName('')
        setEmail('')
        setPassword('')
      }

    } catch (error) {
      setMessage('Unable to connect to the server.')
    } finally {
      setLoading(false)
    }
  }

  function switchForm() {
    setIsLogin(!isLogin)
    setName('')
    setEmail('')
    setPassword('')
    setMessage('')
  }

  return (
    <div className="app-container">
      <div className="form-card">

        <div className="card-icon">🛡️</div>

        <h1>{isLogin ? 'Welcome Back!' : 'Create Account'}</h1>

        <p className="subtitle">
          {isLogin ? 'Login to continue' : 'Register to get started'}
        </p>

        <form onSubmit={handleSubmit}>

          {!isLogin && (
            <input
              type="text"
              placeholder="Full Name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />
          )}

          <input
            type="email"
            placeholder="Email Address"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            minLength="6"
            required
          />

          <button type="submit" disabled={loading}>
            {loading
              ? 'Please wait...'
              : isLogin ? 'Login →' : 'Register →'}
          </button>

        </form>

        {message && (
          <p className="message">{message}</p>
        )}

        <p className="switch-text">
          {isLogin
            ? "Don't have an account?"
            : 'Already have an account?'}

          <span onClick={switchForm}>
            {isLogin ? ' Register' : ' Login'}
          </span>
        </p>

      </div>
    </div>
  )
}

export default App
