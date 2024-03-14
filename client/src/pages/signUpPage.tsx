import {
  Box,
  Button,
  Container,
  Divider,
  FormLabel,
  TextField,
  Typography,Hidden
} from '@mui/material'
import React, { useState } from 'react'
import logo from '../assets/SoleAI_Logo.png'
import { Form } from 'react-router-dom'
import { FormData, FormErrors } from '../interface/user';
const ContainerStyle: Object = {
  width: 1,
  height: '150vh',
  display: 'flex',
  flexDirection: { xs: 'column', sm: 'column', md: 'row', lg: 'row' },
  alignItems: 'center'
}
const ImageStyle: Object = {
  width: { xs: 1 / 4, sm: 1 / 4, md: 1, lg: 1 },
  height: '120vh',
  visibility: { xs: 'hidden', sm: 'hidden', md: 'visible', lg: 'visible' }
}

interface FormDataExt extends FormData {
  name: string;
  confirmPassword: string;
  mobilenumber: string;
}
interface FormErrorExt extends FormErrors {
  name: boolean,
  confirmPassword: boolean,
  mobilenumber: boolean,
}

const SignUpPage: React.FC = () => {
  const [details, setDetails] = useState<FormDataExt>({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
    mobilenumber: "",

  })
  const [error, setErrors] = useState<FormErrorExt>({
    name: false,
    email: false,
    password: false,
    confirmPassword: false,
    mobilenumber: false,

  })
  const changeHandler = (e: Event) => {

    if (e.target != null) {
      const { name, value }: { name: string, value: string } = e.target;
      setDetails({ ...details, [name]: value });
      setErrors({ ...error, [name]: false })
    }
  }
  const validateForm = (e: Event) => {
    e.preventDefault();
    const { name, email, password, confirmPassword, mobilenumber }: FormDataExt = details;
    const newErrors: FormErrorExt = {
      name: false,
      email: false,
      password: false,
      confirmPassword: false,
      mobilenumber: false,
    }
    if (name === "") newErrors.name = true;
    if (email === "") newErrors.email = true;
    if (confirmPassword === "") newErrors.confirmPassword = true;
    if (mobilenumber === "") newErrors.mobilenumber = true;
    if (password === "") newErrors.password = true;
    setErrors(newErrors);

    if (
      details.name &&
      details.email &&
      details.confirmPassword &&
      details.mobilenumber &&
      details.password
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
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            gap: 3,
            mx: { xs: 2, sm: 15, md: 10, lg: 6 }
          }}
        > <Hidden smUp>
        <div style={{ display: "flex", justifyContent: "center" }}>
          <img src={logo} style={{ width: "5rem", height: "5rem" }} alt="Logo" />
        </div>
      </Hidden>
          <Typography variant="h4" component="h2">
            Create your account

          </Typography>
          <FormLabel>Full Name</FormLabel>
          <TextField
            id="Name"
            type="text"
            size="small"
            name="name"
            variant="outlined"
            placeholder="enter your name"
            required
            value={details.name}
            onChange={changeHandler}
            error={error.name}
            helperText={(error.name) && "Please enter your name."}
          />
          <FormLabel>Email</FormLabel>
          <TextField
            id="email"
            type="email"
            size="small"
            name="email"
            variant="outlined"
            placeholder="enter your email"
            required
            value={details.email}
            onChange={changeHandler}
            error={error.email}
            helperText={(error.email) && "Please enter your valid email."}
          />
          <FormLabel>Mobile Number</FormLabel>
          <TextField
            name="mobilenumber"
            id="mobileNumber"
            type={"text"}
            size="small"
            variant="outlined"

            placeholder="enter your mobile number"
            required
            value={details.mobilenumber}
            onChange={changeHandler}
            error={error.mobilenumber}
            helperText={(error.mobilenumber) && "Please enter your mobilenumber."}
          />
          <FormLabel>Password</FormLabel>
          <TextField
            name="password"
            id="password"
            type="password"
            size="small"
            variant="outlined"
            placeholder="create password"
            required
            value={details.password}
            onChange={changeHandler}
            error={error.password}
            helperText={(error.password) && "Password is required"}
          />
          <FormLabel>Confirm Password</FormLabel>
          <TextField
            name="confirmPassword"
            id="confirmPassword"
            type="password"
            size="small"
            variant="outlined"
            placeholder="confirm password"
            required
            value={details.confirmPassword}
            onChange={changeHandler}
            error={error.confirmPassword}
            helperText={(error.confirmPassword && "Please confirm the password")
            }
          />
          {(details.confirmPassword.length > 0 &&
            details.confirmPassword !== details.password) && <p style={{ color: "red", margin: "0px", fontSize: "10px" }}>This does not match with password</p>}

          <Button id="login-btn" variant="contained" sx={{ width: 1 }} onClick={validateForm}>
            Sign up
          </Button>

          <Divider sx={{ width: '100%' }}>OR</Divider>
          <Button id="google-signIn-btn" variant="contained" sx={{ width: 1 }}>
            Sign-up with Google
          </Button>
        </Box>
      </Box>
    </Container >
  )
}

export default SignUpPage
