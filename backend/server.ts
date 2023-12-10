// Import required modules and libraries
import express from 'express'; // Import the Express framework
import multer from 'multer'; // Import multer for handling file uploads
import { exec } from 'child_process'; // Import exec for running shell commands
import path from 'path'; // Import path for working with file paths
import { v4 as uuidv4 } from 'uuid'; // Import uuidv4 for generating unique filenames

// Create an Express application instance
const app = express();

// Define the port number on which the server will listen
const port = 3000;

// Configure multer for handling file uploads and specify storage settings
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/')
  },
  filename: function (req, file, cb) {
    const fileExt = path.extname(file.originalname);
    cb(null, file.fieldname + '-' + Date.now() + fileExt)
  }
});

const upload = multer({ storage: storage });

// Serve static files from a directory (adjust the path as needed)
app.use(express.static('../frontend/src'));

// Define a route for handling file uploads via POST request
app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    // If no file was uploaded, send a 400 Bad Request response
    res.status(400).send('No file uploaded.');
    return;
  }

  // Construct the file path with the directory and the new filename
  const filePath = path.join(__dirname, '..', 'uploads', req.file.filename);

  // Execute a Python script with the uploaded file as an argument
  exec(`python app/main.py "${filePath}"`, (error, stdout, stderr) => {
    console.log("File path:", filePath);
    if (error) {
      // If an error occurs during execution, log the error and send a 500 Internal Server Error response
      console.error(`exec error: ${error}`);
      res.status(500).send(`Error processing file: ${stderr}`);
      return;
    }

    // Send the plain stdout back to the client as a response
    res.send(stdout);
  });
});

// Start the Express server and listen on the specified port
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
