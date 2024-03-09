import React from 'react'
import {Theme, ThemeProvider, createTheme} from '@mui/material/styles'
import LoginPage from './pages/loginPage'
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import SignUpPage from './pages/signUpPage'
import ResumeUpload from './pages/ResumeUpload'

const App: React.FC = () => {
  const themeLight: Theme = createTheme({
    palette: {
      primary: {
        main: '#2196f3' // or any other color you prefer
      },
      background: {
        default: 'red'
      }
    }
  })
  return (
    <ThemeProvider theme={themeLight}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LoginPage />} />
          <Route path="/signup" element={<SignUpPage />} />
          <Route path="/resumeUpload" element={<ResumeUpload />} />
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  )
}

export default App
