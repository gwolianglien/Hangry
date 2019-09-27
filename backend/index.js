const express = require('express');
const connection = require('./db');

// App & Connections
const app = express();
connection();
app.use(express.json({ extended: false }));

// APIs
// app.use('/api/users', require('./api/users'));

const PORT = process.env.port || 3000;

// Entry
app.listen(
    PORT, 
    () => {
        console.log(`Server live on PORT ${PORT}...`);
    }
);