const express = require('express');     //Require lib express

//Constants
const PORT = 8080;
const HOST = '0.0.0.0';

//App 
const app = express();
app.get('/', (req, res) => {
res.send('Hello Huy Ngo \n')
});

// Use lib (express), after that Listen PORT 8080 and call res.send('Hello World  \n');
app.listen(PORT, HOST);
console.log('Running on http://${HOST}:${PORT}');