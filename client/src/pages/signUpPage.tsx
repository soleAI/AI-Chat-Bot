import {
  Box,
  Button,
  Container,
  Divider,
  FormLabel,
  TextField,
  Typography
} from '@mui/material'
import React from 'react'
import logo from '../assets/SoleAI_Logo.png'

const ContainerStyle: Object = {
  width: 1,
  height: '98vh',
  display: 'flex',
  flexDirection: {xs: 'column', sm: 'column', md: 'row', lg: 'row'},
  alignItems: 'center'
}
const ImageStyle: Object = {
  width: {xs: 1 / 4, sm: 1 / 4, md: 1, lg: 1},
  visibility: {xs: 'hidden', sm: 'hidden', md: 'visible', lg: 'visible'}
}
const SignUpPage: React.FC = () => {
  return (
    <Container sx={ContainerStyle}>
      <Box sx={ImageStyle}>
        <img src={logo} style={{width: '70%', margin: '15%'}} />
      </Box>
      <Box width="100%">
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            gap: 3,
            mx: {xs: 2, sm: 15, md: 10, lg: 6}
          }}
        >
          <Typography variant="h4" component="h2">
            Create your account
          </Typography>
          <FormLabel>Full Name</FormLabel>
          <TextField
            id="email"
            type="text"
            size="small"
            variant="outlined"
            placeholder="enter your name"
            required
          />
          <FormLabel>Email</FormLabel>
          <TextField
            id="email"
            type="email"
            size="small"
            variant="outlined"
            placeholder="enter your email"
            required
          />
          <FormLabel>Password</FormLabel>
          <TextField
            id="password"
            type="password"
            size="small"
            variant="outlined"
            placeholder="create password"
            required
          />
          <Button id="login-btn" variant="contained" sx={{width: 1}}>
            Sign up
          </Button>
          <Divider sx={{width: '100%'}}>OR</Divider>
          <Button id="google-signIn-btn" variant="contained" sx={{width: 1}}>
            Sign-up with Google
          </Button>
        </Box>
      </Box>
    </Container>
  )
}

export default SignUpPage
