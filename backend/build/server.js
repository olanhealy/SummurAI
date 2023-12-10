"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
// Import required modules and libraries
const express_1 = __importDefault(require("express")); // Import the Express framework
const multer_1 = __importDefault(require("multer")); // Import multer for handling file uploads
const child_process_1 = require("child_process"); // Import exec for running shell commands
const path_1 = __importDefault(require("path")); // Import path for working with file paths
// Create an Express application instance
const app = (0, express_1.default)();
// Define the port number on which the server will listen
const port = 3000;
// Configure multer for handling file uploads and specify storage settings
const storage = multer_1.default.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'uploads/');
    },
    filename: function (req, file, cb) {
        const fileExt = path_1.default.extname(file.originalname);
        cb(null, file.fieldname + '-' + Date.now() + fileExt);
    }
});
const upload = (0, multer_1.default)({ storage: storage });
// Serve static files from a directory (adjust the path as needed)
app.use(express_1.default.static('../frontend/src'));
// Define a route for handling file uploads via POST request
app.post('/upload', upload.single('file'), (req, res) => {
    if (!req.file) {
        // If no file was uploaded, send a 400 Bad Request response
        res.status(400).send('No file uploaded.');
        return;
    }
    // Construct the file path with the directory and the new filename
    const filePath = path_1.default.join(__dirname, '..', 'uploads', req.file.filename);
    // Execute a Python script with the uploaded file as an argument
    (0, child_process_1.exec)(`python app/main.py "${filePath}"`, (error, stdout, stderr) => {
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
