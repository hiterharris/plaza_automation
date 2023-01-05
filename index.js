const express = require('express');
const app = express();
const {PythonShell} =require('python-shell');

app.get("/", (req, res, next)=>{
    try {
        res.send("Plaza Automation")
    } catch {
        (error) => next(`Error running script: ${error}`);
    }
});

app.get("/order", (req, res, next)=>{
    try {
        let args = [];
        PythonShell.run('dev.py', { args }, (err, result) => res.status(200).json(result) );
    } catch {
        (error) => next(`Error running script: ${error}`);
    }
});
 
const port=8000;
app.listen(port, ()=>console.log(`Server connected to ${port}`));