import {
  Box,
  Button,
  Container,
  Divider,
  FormLabel,
  TextField,
  Typography,
  Hidden
} from '@mui/material'
import React from 'react'
import { useState } from 'react'
import logo from '../assets/SoleAI_Logo.png'
import { FormData, FormErrors } from '../interface/user';
const ContainerStyle: Object = {
  width: 1,
  height: '96vh',
  display: 'flex',
  flexDirection: { xs: 'column', sm: 'column', md: 'row', lg: 'row' },
  alignItems: 'center'
}
const ImageStyle: Object = {
  width: { xs: 1 / 4, sm: 1 / 4, md: 1, lg: 1 },
  visibility: { xs: 'hidden', sm: 'hidden', md: 'visible', lg: 'visible' }
}
const LoginFormStyle: Object = {
  display: 'flex',
  flexDirection: 'column',
  gap: 3,
  mx: { xs: 2, sm: 15, md: 10, lg: 6 }
}

const LoginPage: React.FC = () => {
  const [details, setDetails] = useState<FormData>({
    email: "",
    password: "",
  })
  const [errors, setErrors] = useState<FormErrors>({
    email: false,
    password: false

  })
  function isValidEmail(email: string) {
    const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return regex.test(email);
  }
  const changeHandler = (e: Event) => {

    if (e.target != null) {
      const { name, value }: { name: string, value: string } = e.target;
      setDetails({ ...details, [name]: value });
      setErrors({ ...errors, [name]: false })
    }
  }
  const validateForm = (e: Event) => {
    e.preventDefault();
    const { email, password }: { email: string, password: string } = details;
    const newErrors: FormErrors = { email: false, password: false }


    if (email === "") newErrors.email = true;
    if (!newErrors.email && !isValidEmail(email)) newErrors.email = true;
    if (!password) newErrors.password = true;
    setErrors(newErrors);
    if (!newErrors.email && details.email && details.password
    ) {
      console.log(details);
    } else {
      return;
    }


  }
  return (
    <Container sx={ContainerStyle}>
      <Box sx={ImageStyle}>
        <img src={logo} style={{ width: '70%', margin: '15%' }} />
      </Box>
      <Box width="100%">
        <Box sx={LoginFormStyle}>
          <Hidden smUp>
            <div style={{ display: "flex", justifyContent: "center" }}>
              <img src={logo} style={{ width: "5rem", height: "5rem" }} alt="Logo" />
            </div>
          </Hidden>
          <Typography variant="h4" component="h2">
            Welcome Back...
          </Typography>
          <FormLabel>Email</FormLabel>
          <TextField
            name="email"
            id="email"
            type="email"
            size="small"
            variant="outlined"
            placeholder="enter your email"
            onChange={changeHandler}
            required
            value={details.email}
            error={errors.email}
            helperText={(errors.email) && "Please enter  email/mobile."}
          />
          <FormLabel>Password</FormLabel>
          <TextField

            id="password"
            type="password"
            size="small"
            variant="outlined"
            placeholder="password"
            required
            onChange={changeHandler}
            value={details.password}
            name="password"
            error={errors.password}
            helperText={errors.password && "Please enter password."}

          />
          <Button id="login-btn" variant="contained" sx={{ width: 1 }} onClick={validateForm}>
            Login
          </Button>
          <Divider sx={{ width: '100%' }}>OR</Divider>
          <Button id="google-signIn-btn" variant="contained" sx={{ width: 1 }}>
            Sign-in with Google
          </Button>
        </Box>
      </Box>
    </Container >
  )
}

export default LoginPage
