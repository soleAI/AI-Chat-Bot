import { Card, Button, Box, Hidden } from '@mui/material'
import React from 'react'
import CloudUploadOutlinedIcon from '@mui/icons-material/CloudUploadOutlined';
import VisibilityIcon from '@mui/icons-material/Visibility';
import { useRef, useState } from 'react'

const ContainerStyle: Object = {
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  height: '100vh',
  bgcolor: '',
  overFlow: "Hidden"
}
const WrapCardStyle: Object = {
  bgcolor: "#e6e6e6", padding: "1.5rem", width: {
    xs: "90%",
    sm: "80%",
    md: "70%",
    lg: "50%",
    xl: "40%"
  }
}
const HeadingStyle: Object = {
  fontSize: '1.5rem', fontWeight: 'bold', margin: '0px'
}
const HeadingStyle1: Object = {
  fontSize: '.5rem', marginBottom: '1rem'
}
const DropArea: Object = {
  height: "35vh", width: "100%", bgcolor: "white", display: 'flex', justifyContent: 'center', borderRadius: "5px", border: '2px  #C0C2C9 solid', cursor: 'pointer'
}
const DropAreaDiv: Object = {
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  gap: '0.2rem',
}
const DropAreaIcon: Object = {
  fontSize: '7rem', color: 'gray'
}
const FileInfoText: Object = {
  margin: '0px', cursor: 'pointer'
}
const FileInfoTextName: Object = {
  overflowWrap: 'break-word', textAlign: "center", fontSize: '.3rem', width: '100%'
}
const ButtonDiv: Object = {

  display: 'flex',
  flexWrap: 'wrap',
  justifyContent: 'center',
  alignItems: 'center',
  gap: '20px',
  marginTop: "15px"

}
const ReviewIcon: Object = {
  textDecoration: 'none', display: 'flex', justifyContent: "center", alignItems: 'center', padding: '0px 10px'
}
const ResumeUpload: React.FC = () => {
  const [file, setFile] = useState<any>()
  const wrapperRef = useRef<HTMLDivElement>(null)
  const fileInputRef = useRef<HTMLInputElement>(null)

  const onDragEnter = () => wrapperRef.current?.classList.add('dragover')
  const onDragLeave = () => wrapperRef.current?.classList.remove('dragover')
  const onDropFile = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    const files = e.dataTransfer.files

    if (files.length) {
      const firstFile = files[0]
      wrapperRef.current?.classList.remove('dragover')

      setFile(firstFile)
    }
  }

  const onDragHandler = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    wrapperRef.current?.classList.remove('dragover')
  }
  const onFileDrop = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!e.target.files) return
    setFile(e.target.files[0])
  }

  const openFileDialog = () => {
    fileInputRef.current?.click()
  }
  const removeHandler = () => {
    setFile(null)
  }
  return (
    <Box sx={ContainerStyle}>
      <Card sx={WrapCardStyle}>

        <p style={HeadingStyle}>Upload or attach resume </p>
        <p style={HeadingStyle1}>Click to upload or drag and drop </p>

        <Box sx={DropArea}
          ref={wrapperRef}

          onDragEnter={onDragEnter}
          onDragLeave={onDragLeave}
          onDrop={onDropFile}
          onDragOver={onDragHandler}
          onClick={openFileDialog}
        >
          <div
            style={DropAreaDiv}
          ><CloudUploadOutlinedIcon sx={DropAreaIcon} />
            <h3 style={FileInfoText}>
              {file ? <p style={FileInfoTextName}>{file.name}</p> : <p style={{ fontSize: '.5rem' }}>No file Selected</p>}
            </h3>
          </div>

          <input
            type="file"
            ref={fileInputRef}
            accept=".doc,.docx,.pdf"
            hidden
            onChange={onFileDrop}
          />
        </Box>



        <div
          style={ButtonDiv}
        >
          <Button variant="contained" color={"error"} onClick={removeHandler}>
            Cancel
          </Button>
          <Button variant="contained" color={"primary"} disabled={!file}>
            Continue
          </Button>
          {file && <a style={ReviewIcon} href={URL.createObjectURL(file)}><VisibilityIcon sx={{ color: '#8c8e96' }}>
          </VisibilityIcon></a>}
        </div>


      </Card>
    </Box>
  )
}

export default ResumeUpload
