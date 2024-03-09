import {Card, Button} from '@mui/material'
import React from 'react'
import ControlPointIcon from '@mui/icons-material/ControlPoint'
import {useRef, useState} from 'react'

const ContainerStyle: Object = {
  display: 'flex',
  gap: '20px',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  width: '98vw',
  height: '98vh',
  bgcolor: '#f6f9fc'
}
const WrapperStyle: Object = {
  bgcolor: 'white',
  width: '40%',
  height: '40vh',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  border: '2px dashed gray'
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
    <Card sx={ContainerStyle}>
      <Card
        ref={wrapperRef}
        sx={WrapperStyle}
        onDragEnter={onDragEnter}
        onDragLeave={onDragLeave}
        onDrop={onDropFile}
        onDragOver={onDragHandler}
        onClick={openFileDialog}
      >
        <div
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: '3rem'
          }}
        >
          <h2>Drag and Drop an file or Click to upload</h2>
          <ControlPointIcon sx={{fontSize: '3rem', color: 'gray'}} />
        </div>
        <input
          type="file"
          ref={fileInputRef}
          accept=".doc,.docx,.pdf"
          hidden
          onChange={onFileDrop}
        />
      </Card>
      <div
        style={{
          display: 'flex',
          width: '40%',
          justifyContent: 'space-between',
          alignItems: 'center'
        }}
      >
        <h2 style={{margin: '0px', cursor: 'pointer'}}>
          {file && <a href={URL.createObjectURL(file)}>{file.name}</a>}
        </h2>
        <div
          style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            gap: '5px'
          }}
        >
          <Button variant="contained" onClick={removeHandler}>
            Cancel
          </Button>
          <Button variant="contained" disabled={!file}>
            Continue
          </Button>
        </div>
      </div>
    </Card>
  )
}

export default ResumeUpload
